from django.shortcuts import render
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from django.views.generic import ListView, DetailView
from sito.models import *
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def HomeView(request):
	immagini_list = Immagini.objects.filter(categoria = '1').order_by('id')
	dottori_list = Immagini.objects.filter(categoria = '2').order_by('id')
	scelta_list = Immagini.objects.filter(categoria = '3').order_by('id')
	context = {'immagini_list': immagini_list,
				'dottori_list': dottori_list,
				'scelta_list': scelta_list
				}
   #return render_to_response('home.html', context_instance=RequestContext(request))
	return render(request, 'home.html', context)

def ContactView(request):
   return render_to_response('contact.html', context_instance=RequestContext(request))


def contacta(request):
    if request.method == 'POST': # If the form has been submitted...
        form = LavoraForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'Messaggio da Sito Internet www.br1italia.it'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contact.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['pierangelo1982@gmail.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = LavoraForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })



def contattaci(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContattaForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'Messaggio da Sito Internet www.br1italia.it'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contatta.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['pierangelo1982@gmail.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContattaForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })


def contactnews(request):
    if request.method == 'POST': # If the form has been submitted...
        form = ContactnewsForm(request.POST) # A form bound to the POST data
        if form.is_valid(): # All validation rules pass
            subject = 'Messaggio da Sito Internet www.br1italia.it'
            #message = form.cleaned_data['messaggio']
            message = render_to_string('contactnews.txt', {'post': request.POST})
            sender = form.cleaned_data['email']
            cc_myself = False

            recipients = ['pierangelo1982@gmail.com']
            if cc_myself:
                recipients.append(sender)
        
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/') # Redirect after POST
    else:
        form = ContactnewsForm() # An unbound form

    return render_to_response('contact.html', {
        'form': form,
    })



def Grazie(request):
   return render_to_response('grazie.html', context_instance=RequestContext(request))
