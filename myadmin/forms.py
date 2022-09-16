from django import forms
from myprofile.models import Achievement, LanguageImage
class LanguageInputForm(forms.ModelForm):
    class Meta():
        model = LanguageImage
        fields = ['content']
class AchievementInputForm(forms.ModelForm):
    class Meta():
        model = Achievement
        fields = ['content','date',]