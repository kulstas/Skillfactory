from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, TemplateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic import ListView, DateDetailView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.template import RequestContext
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from D16_MMORPG_board.models import Advertisement, Profile

from .forms import SignUpForm, LoginUserForm, CheckCode, ProfileForm, UserForm
from D16_MMORPG_board.models import OneTimeCode


# доработать удаление кода
def get_code(request):
    if request.method == "POST":
        form = CheckCode(request.POST)
        if form.is_valid():
            try:
                code = request.POST['code']
                if OneTimeCode.objects.get(code=code):
                    user = User.objects.get(onetimecode__code=code)
                    user.is_active = True
                    user.save()
            except OneTimeCode.DoesNotExist:
                raise Http404

            return HttpResponseRedirect("/accounts/login/")

    # if a GET (or any other method) we'll create a blank form
    else:
        form = CheckCode()

    return render(request, "accounts/activation.html", {"form": form})


@method_decorator(csrf_protect, name='dispatch')
class CustomSignUp(CreateView):
    model = User
    form_class = SignUpForm
    success_url = '/accounts/activation'
    template_name = 'accounts/signup.html'
    extra_content = 'Регистрация'

    def form_valid(self, form):
        to_return = super().form_valid(form)
        user = form.save(commit=False)
        user.is_active = False
        user.save()

        form.send_activation_email(user)

        return to_return


class CustomLoginView(LoginView):
    form_class = LoginUserForm
    template_name = 'accounts/login.html'
    success_url = reverse_lazy('D16_MMORPG_board:ads')

    def get_success_url(self):
        return reverse_lazy('ads')


@method_decorator(login_required, name='dispatch')
class MyAds(ListView):
    model = Advertisement
    ordering = 'ad_date'
    context_object_name = 'my_ads'
    template_name = 'accounts/my_ads.html'
    paginate_by = 5

    # def get_queryset(self):
    #     return Advertisement.objects.filter(ad_author__username=self.request.user.username)

    def get_context_data(self, **kwargs):
        context = super(MyAds, self).get_context_data(**kwargs)
        context['my_ads'] = Advertisement.objects.filter(ad_author__username=self.request.user)

        return context


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'accounts/profile.html'


class ProfileUpdateView(LoginRequiredMixin, TemplateView):
    user_form = UserForm
    profile_form = ProfileForm
    template_name = 'accounts/profile-update.html'

    def post(self, request):
        post_data = request.POST or None
        file_data = request.FILES or None

        user_form = UserForm(post_data, instance=request.user)
        profile_form = ProfileForm(post_data, file_data, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "Профиль обновлен!")
            return HttpResponseRedirect(reverse_lazy('profile'))

        context = self.get_context_data(
            user_form=user_form,
            profile_form=profile_form
        )

        return self.render_to_response(context)

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)
