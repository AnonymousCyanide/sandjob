from django.forms import ModelForm , Textarea , EmailInput , TextInput
from .models import Message

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['content','name','email','subject']

        widgets = {
            'content': Textarea(attrs={'class':'form-control valid' , 'placeholder':"Enter Messsage"}),
            'name': TextInput(attrs={'class':'form-control valid' , 'placeholder':"Enter Your Name"}),
            'email': EmailInput(attrs={'class':'form-control valid' , 'placeholder':"Enter Your Email"}),
            'subject': TextInput(attrs={'class':'form-control valid' , 'placeholder':"Enter Subject"}),
        }