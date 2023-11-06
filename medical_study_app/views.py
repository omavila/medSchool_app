from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from medical_study_app.models import Notegroup, Notecard, Client

# Create your views here.
class NotegroupListView(generic.ListView):
   model = Notegroup
class NotegroupDetailView(generic.DetailView):
   model = Notegroup

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notegroup = self.object
        context['notecards'] = notegroup.notecard_set.all()
        return context
   
class NotecardDetailView(generic.DetailView):
   model = Notecard

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        notecard = self.object
        notecard_id = self.kwargs['pk']
        context['notegroup'] = Notegroup.objects.filter(notecard__id=notecard_id).first()
        return context

class ClientDetailView(generic.DetailView):
   model = Client

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.object
        context['notecards'] = client.notecard_set.all()
        context['notegroups'] = client.notegroup_set.all()
        return context

def index(request):
   
   return render( request, 'medical_study_app/index.html')
