from django.core.exceptions import ValidationError
from django.forms import ModelForm

from .models import Message


def add_placeholder(field, placeholder_val):
    field.widget.attrs['placeholder'] = placeholder_val

class SendMessage(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        add_placeholder(self.fields['nome'], 'Ex: Leonardo')
        add_placeholder(self.fields['email'], 'Ex: oaooaoao@gmail.com')
        add_placeholder(self.fields['mensagem'], 'Ex.: Que legal seu portfolio!')
    class Meta:
        model = Message
        fields = [
            'nome',
            'email',
            'mensagem',
        ]

    labels = help_texts = {
        'nome': 'O nome não pode estar em branco',
        'email': 'O email precisa ser válido'
    }
    error_messages = {
        'nome': {
            'required': 'Esse campo não pode ser deixado em branco',
        }
    }