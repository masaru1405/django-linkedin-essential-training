from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect

from .models import Note
from .forms import NotesForm

class NotesDeleteView(DeleteView):
  model = Note
  success_url = '/smart/notes'
  template_name = 'notes/notes_delete.html'

class NotesUpdateView(UpdateView):
  model = Note
  success_url = '/smart/notes'
  form_class = NotesForm
  template_name = 'notes/notes_form.html'

class NotesCreateView(LoginRequiredMixin ,CreateView):
  model = Note
  #fields = ['title', 'text']
  form_class = NotesForm
  template_name = 'notes/notes_form.html'
  success_url = '/smart/notes'
  login_url = '/admin'

  def form_valid(self, form):
    self.object = form.save(commit=False)
    self.object.user = self.request.user
    self.object.save()
    return HttpResponseRedirect(self.get_success_url())

class NotesListView(LoginRequiredMixin, ListView):
  model = Note
  context_object_name = 'notes'
  template_name = 'notes/notes_list.html'
  login_url = '/login'

  def get_queryset(self):
    return self.request.user.notes.all()

class NotesDetailView(DetailView):
  model = Note
  context_object_name = "note"
  template_name = 'notes/notes_detail.html'

""" def list(request):
  all_notes = Note.objects.all()
  context = {
    'notes': all_notes
  }
  return render(request, 'notes/notes_list.html', context) """

""" def detail(request, id):
  note = get_object_or_404(Note, pk=id)
  context = {
    'note': note
  }
  return render(request, 'notes/notes_detail.html', context) """
