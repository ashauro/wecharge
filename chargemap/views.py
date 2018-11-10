from django.views import generic
from django.shortcuts import render
from chargemap.models import ChargeStation
from .forms import ContactIndexForm
from django.http import HttpResponse
from django.core.mail import send_mail, BadHeaderError
from . import dojson


class DetailStationView(generic.DetailView):
    model = ChargeStation
    template_name = 'chargemap/detail.html'

class ManagementView(generic.DetailView):
    model = ChargeStation
    template_name = 'chargemap/management.html'

def index(request):
    form = ContactIndexForm()
    return render(request, 'index.html', {'form': form, 'mt': 'index'})

def detail(request):
    return render(request, 'detail.html')

def charge_map(request):
    return render(request, 'charge_map.html', {'mt': 'charge_map'})


def contacts(request):
    form = ContactIndexForm()
    return render(request, 'contacts-page.html', {'mt': 'contacts', 'form': form})


def mail_sender(request):
    if request.method == 'POST':
        form = ContactIndexForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            mail_text = """Новое письмо с вашего сайта от пользователя {}!
            Email: {}
            Текст письма: {}
            """.format(name, email, message)
            subject = 'WattsON - форма обратной связи'

            recipients = ['a.shauro@gmail.com']
            try:
                send_mail(subject, mail_text, 'robot@rudut.ru', recipients)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return render(request, 'thanks.html')
    else:
        form = ContactIndexForm()
    return render(request, 'index.html', {'form': form})
