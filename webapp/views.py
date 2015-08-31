from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail, mail_admins
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext, HttpResponseRedirect
from .forms import ContactUsForm


def index(request):
   # return HttpResponse("Hello, world! This is our first view.")
    return render_to_response("index.html",
                              locals(),
                             context_instance=RequestContext(request))
def about(request):
    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))

def portfolio(request):
    return render_to_response("portfolioMain.html",
                              locals(),
                              context_instance=RequestContext(request))

def contact(request):
    form = ContactUsForm(request.POST or None)
    if form.is_valid():
        subject = form.cleaned_data['subject']
        message = form.cleaned_data['message']
        sender = form.cleaned_data['sender']
        cellphone = form.cleaned_data['cellphone']
        cc_myself = form.cleaned_data['cc_myself']

        recipients = [settings.EMAIL_HOST_USER]
        if cc_myself:
            recipients.append(sender)

        send_mail(subject, message, sender, recipients)

        mail_admins("CONTACT US - BRENDAMANRIQUE.COM",
                    "The message was: %s %s %s %s" % (subject, message, sender, recipients),
                    fail_silently=True)
        return HttpResponseRedirect('/thank-you/')

    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request))

