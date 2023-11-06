from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from medical_study_app.models import Notegroup, Notecard, Client
from .forms import NotegroupForm

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



def createNotegroup(request, client_id):
    form = NotegroupForm()
    client = Client.objects.get(pk=client_id)
    
    if request.method == 'POST':

        notegroup_data = request.POST.copy()
        notegroup_data['client_id'] = client_id
        
        form = NotegroupForm(notegroup_data)
        if form.is_valid():

            notegroup = form.save(commit=False)

            notegroup.client = client
            notegroup.save()

            return redirect('client-detail', client_id)

    context = {'form': form}
    return render(request, 'medical_study_app/notegroup_form.html', context)


def deleteNotegroup(request, client_id, notegroup_id):
    notegroup = Notegroup.objects.get(pk=notegroup_id)
    
    if request.method == 'POST':
        notegroup.delete()

        return redirect('client-detail', client_id)

    context = {'notegroup': notegroup}
    return render(request, 'medical_study_app/notegroup_delete.html', context)

def updateNotegroup(request, client_id, notegroup_id):
    client = Client.objects.get(pk=client_id)
    notegroup = Notegroup.objects.get(pk=notegroup_id)
    if request.method == 'POST':
        form = NotegroupForm(request.POST, instance=notegroup)

        if form.is_valid():
            notegroup = form.save()
            return redirect('client-detail', client_id)
    form = NotegroupForm(instance=notegroup)

    

    context = {'form': form, 'client_id': client_id, 'notegroup_id': notegroup_id}
    return render(request, 'medical_study_app/notegroup_form.html', context)



    
def index(request):
   
   return render( request, 'medical_study_app/index.html')
