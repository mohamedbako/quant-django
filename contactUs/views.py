from django.shortcuts import render
from .models import Info
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def sendMessage(request):
    myInfo = Info.objects.first()

    if request.method == 'POST':
        subject = request.POST['subject']
        email = request.POST['email']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER, # from
            [email], # to
            fail_silently=False,
         )
        

        return render(request, 'contact/contact.html', {'subject' : subject})
    else:
        return render(request, 'contact/contact.html', {'myInfo' : myInfo})

