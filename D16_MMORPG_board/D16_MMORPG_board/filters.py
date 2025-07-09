import django_filters
from django_filters import FilterSet
from django import forms

from .models import Advertisement


class AdsFilter(FilterSet):
    ad_title = django_filters.CharFilter(
        field_name='ad_title',
        lookup_expr='icontains',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Поиск по объявлениям'}),
        label='',
    )

    class Meta:
        model = Advertisement
        fields = []