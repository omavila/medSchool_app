from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from medical_study_app.models import Notegroup, Notecard, Client
from .forms import NotegroupForm, CreateUserForm, ClientForm
from django.contrib import messages
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from django.contrib.auth.mixins import LoginRequiredMixin

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
        context['w_head'] = 'static/images/w_head'
        return context


class ClientDetailView(LoginRequiredMixin, generic.DetailView):
   model = Client

   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        client = self.object
        context['notecards'] = client.notecard_set.all()
        context['notegroups'] = client.notegroup_set.all()
        return context


@login_required(login_url='login')
@allowed_users(allowed_roles=['Clients'])
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

@login_required(login_url='login')
@allowed_users(allowed_roles=['Clients'])
def deleteNotegroup(request, client_id, notegroup_id):
    notegroup = Notegroup.objects.get(pk=notegroup_id)
    
    if request.method == 'POST':
        notegroup.delete()

        return redirect('client-detail', client_id)

    context = {'notegroup': notegroup}
    return render(request, 'medical_study_app/notegroup_delete.html', context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['Clients'])
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

def registerPage(request):
    form = CreateUserForm()
    
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='Clients')
            user.groups.add(group)
            client = Client.objects.create(user=user,)
            client.name = username
            client.save()

            messages.success(request, 'Account was created for ' + username)
            return redirect('login')
        
    context = {'form':form}
    return render(request, 'registration/register.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['Clients'])
def userPage(request):
    client = request.user.client
    form = ClientForm
    print('client', client)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'medical_study_app/user.html', context)