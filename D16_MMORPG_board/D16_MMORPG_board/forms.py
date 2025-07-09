from django import forms
from django.core.exceptions import ValidationError


from .models import Advertisement, Reply


class AdForm(forms.ModelForm):
    class Meta:
        model = Advertisement
        fields = [
            'ad_title',
            'ad_text',
            'ad_category',
            'ad_upload',
        ]
        widgets = {
            'ad_title': forms.TextInput(attrs={'class': 'form-control'}),
            'ad_text': forms.Textarea(attrs={'class': 'form-control',
                                             'style': 'resize: vertical; height: 200px; line-height: 1.5rem;'}),
            'ad_category': forms.Select(attrs={'class': 'form-control'}),
            'ad_upload': forms.FileInput()
        }

    def clean(self):
        cleaned_data = super().clean()
        ad_text = cleaned_data.get('ad_text')
        ad_title = cleaned_data.get('ad_title')

        if ad_title == ad_text:
            raise ValidationError({
                "Описание не должно быть идентичным названию."
            })

        return cleaned_data

    def clean_name(self):
        name = self.cleaned_data["ad_title"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы."
            )
        return name


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = [
            'reply_text',
        ]
        widgets = {
            'reply_text': forms.Textarea(attrs={'class': 'form-control',
                                             'style': 'resize: vertical; height: 200px; line-height: 1.5rem; padding-top:'}
                                         ),
        }