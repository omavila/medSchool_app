from django.forms import ModelForm
from .models import Notegroup, Client
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#create class for project form
class NotegroupForm(ModelForm):
    class Meta:
        model = Notegroup
        fields =('title', 'description', 'is_private')

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ('name', 'email')
        exclude = ['user']

class CreateUserForm(UserCreationForm) :
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']