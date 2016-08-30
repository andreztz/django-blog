from django.forms import forms
from django.core.mail import send_mail
from django.settings import settings


class ContactForm(forms.Form):

    name = forms.CharField(label='Nome', max_length=100)
    email = forms.EmailField(label='Email')
    message = forms.CharField(label='Mensagem', widget=forms.TextArea)

    def send_mail(self, subject='Usuário do André Santos Blog.'):
        subject = subject
        message = 'Nome: {name}; E-mail: {email}; {message}'
        context = {
            'name': self.cleaned_data['name'],
            'email': self.cleaned_data['email'],
            'message': self.cleaned_data['message']
        }
        message = message.format(context)
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_EMAIL]
        )
