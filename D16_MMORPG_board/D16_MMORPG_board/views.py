from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView


from .models import Advertisement, Category, Reply
from .filters import AdsFilter
from .forms import AdForm, ReplyForm


class AdsListView(ListView):
    model = Advertisement
    queryset = Advertisement.objects.order_by('-ad_date')
    context_object_name = 'ads_list'
    template_name = 'D16_MMORPG_board/index.html'
    paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super(AdsListView, self).get_context_data(**kwargs)
        context['ads'] = Advertisement.objects.all()
        context['cat_list'] = Category.objects.all()
        context['filterset'] = self.filterset
        return context


class AdCategory(ListView):
    model = Advertisement
    queryset = Advertisement.objects.order_by('-ad_date')
    template_name = 'D16_MMORPG_board/category.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super(AdCategory, self).get_context_data(**kwargs)
        context['category_name'] = Category.objects.get(id=self.kwargs['id']).category_name
        context['ads_category'] = Advertisement.objects.filter(ad_category_id=self.kwargs['id'])
        context['cat_list'] = Category.objects.all()
        context['filterset'] = self.filterset
        return context


def reply_accept(request, pk1, pk2):
    filterargs = {'reply_ad_id': pk1, 'reply_author_id': pk2}
    Advertisement.objects.filter(id=pk1).update(ad_status=False)
    Reply.objects.filter(**filterargs).update(reply_status=True)
    instance = Reply.objects.filter(**filterargs).get()
    post_save.send(Reply, instance=instance, created=False, dispatch_uid="reply_update_handler")
    return HttpResponseRedirect(reverse_lazy('ad_detail', args=[pk1]))


def reply_cancel(request, pk1, pk2):
    filterargs = {'reply_ad_id': pk1, 'reply_author_id': pk2}
    Reply.objects.filter(**filterargs).update(reply_status=False)
    instance = Reply.objects.filter(**filterargs).get()
    post_save.send(Reply, instance=instance, created=False, dispatch_uid="reply_update_handler")
    return HttpResponseRedirect(reverse_lazy('ad_detail', args=[pk1]))


class AdDetail(DetailView):
    model = Advertisement
    template_name = 'D16_MMORPG_board/ad.html'
    pk_url_kwarg = 'id'

    def get_context_data(self, **kwargs):
        context = super(AdDetail, self).get_context_data(**kwargs)
        context['cat_list'] = Category.objects.all()
        context['ads_reply'] = Reply.objects.filter(reply_ad_id=self.get_object().id)
        context['filterset'] = self.filterset
        check_reply_args = {'reply_ad_id': self.get_object().id, 'reply_author_id': self.request.user.id}
        context['check_reply'] = Reply.objects.filter(**check_reply_args)
        context['accepted_reply'] = Reply.objects.filter(reply_ad_id=self.get_object().id).filter(reply_status=True).first()

        return context

    def get_success_url(self):
        return reverse_lazy(kwargs={'pk': self.get_object().id})

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def re_accept(self, request):
        Reply.objects.filter(pk=request.pk).update(reply_status=True)
        return reverse_lazy(kwargs={'pk': self.get_object().id})


@method_decorator(login_required, name='dispatch')
class AdCreate(CreateView):
    raise_exception = True
    form_class = AdForm
    model = Advertisement
    template_name = 'D16_MMORPG_board/ad_create.html'

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.ad_author = self.request.user
        ad.save()

        return super().form_valid(form)

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs


@method_decorator(login_required, name='dispatch')
class AdEdit(UpdateView):
    model = Advertisement
    raise_exception = True
    form_class = AdForm
    template_name = 'D16_MMORPG_board/ad_edit.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = AdsFilter(self.request.GET, queryset)
        return self.filterset.qs


@method_decorator(login_required, name='dispatch')
class ReplyAd(CreateView):
    model = Reply
    form_class = ReplyForm
    template_name = 'D16_MMORPG_board/reply.html'

    def form_valid(self, form):
        form.instance.reply_author = self.request.user
        pk = self.kwargs['pk']
        form.instance.reply_ad = Advertisement.objects.get(pk=pk)
        return super(ReplyAd, self).form_valid(form)

    def get_success_url(self):
        messages.success(self.request, "Отклик отправлен!")
        return reverse('ad_detail', kwargs={'id': self.kwargs['pk']})