# sendemail/forms.py
from django import forms
from django.utils.translation import gettext_lazy as _


class ContactForm(forms.Form):
    from_email = forms.EmailField(label=_('from_email'), required=True)
    subject = forms.CharField(label=_('subject'), required=True)
    message = forms.CharField(label=_('message'), widget=forms.Textarea(attrs={"cols":4, "rows":5}), required=True)
