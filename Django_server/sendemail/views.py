# sendemail/views.py
from django.core.mail import BadHeaderError

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .utils_sendmail import email_form
from web_med_plist.settings import EMAIL_HOST_USER
from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data['message']
            sender_email_1e9usd = EMAIL_HOST_USER
            try:
                email_form(subject, message, sender_email_1e9usd, from_email) 
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success_email')
    return render(request, "email.html", {'form': form})

def successView(request):
    return render(request, 'success_send_email.html', {
        'foo': 'bar',
    })
