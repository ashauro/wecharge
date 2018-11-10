from django import forms


class ContactIndexForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text',
                                                           'placeholder': 'Имя',}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'email',
                                                           'placeholder': 'Email',}))
    message = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'type': 'text',
                                                           'placeholder': 'Текст сообщения',}))
