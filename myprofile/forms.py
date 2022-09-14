from django import forms
from myprofile.models import ContactMessage
class ContactMsgForm(forms.ModelForm):
    class Meta():
        model = ContactMessage
        fields = ['user', 'content', ]
