from django.forms import ModelForm
from .models import Notegroup

#create class for project form
class NotegroupForm(ModelForm):
    class Meta:
        model = Notegroup
        fields =('title', 'description', 'is_private')
