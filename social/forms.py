from django import forms
from .models import SocialPost, SocialComment

class SocialPostForm(forms.ModelForm):
    body = forms.CharField(widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '3',
            'placeholder': 'Say Something...'
            }),
        required=True)

    image = forms.FileField(widget=forms.ClearableFileInput(attrs={
            'class': 'relative dark:text-dark-txt dark:bg-dark-second cursor-pointer bg-white rounded-md font-medium text-indigo-600 hover:text-indigo-500 focus-within:outline-none focus-within:ring-2 focus-within:ring-offset-2 focus-within:ring-indigo-500',
        }),
        required=False,
        label='Selecciona varios archivos',
        help_text='Mantén presionada la tecla "Control", o "Command" en un Mac, para seleccionar varios archivos.'
    )

    class Meta:
        model=SocialPost
        fields=['body']

class SocialCommentForm(forms.ModelForm):
    comment = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'shadow-sm focus:ring-indigo-500 focus:border-indigo-500 dark:bg-dark-third dark:border-dark-third dark:text-dark-txt flex max-w-full sm:text-sm border-gray-300 rounded-md',
            'rows': '1',
            'placeholder': 'Comment Something...'
            }),
        required=True
        )

    class Meta:
        model=SocialComment
        fields=['comment']