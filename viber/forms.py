from django import forms

class MessageForm(forms.Form):
    user_id = forms.CharField(label='Viber user id', max_length=120)
    message = forms.CharField(label='Message', max_length=120)
