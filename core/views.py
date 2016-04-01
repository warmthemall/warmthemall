from django.shortcuts import render
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.core.exceptions import PermissionDenied


# Create your views here.

class Home(TemplateView):
  template_name = "home.html"

class PledgeCreateView(CreateView):
  model = Pledge
  template_name = "pledge/pledge_form.html"
  fields = ['amount']
  success_url = reverse_lazy('pledge_list')

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super(PledgeCreateView, self).form_valid(form)

class ContributionCreateView(CreateView):
  model = Contribution
  template_name = "contribution/contribution_form.html"
  fields = ['amount', 'notes']
  success_url = reverse_lazy('contribution_list')

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super(ContributionCreateView, self).form_valid(form)

class PledgeListView(ListView):
  model = Pledge
  template_name = "pledge/pledge_list.html"

class ContributionListView(ListView):
  model = Contribution
  template_name = "contribution/contribution_list.html"

class PledgeDetailView(DetailView):
  model = Pledge
  template_name = 'pledge/pledge_detail.html'

class ContributionDetailView(DetailView):
  model = Contribution
  template_name = 'contribution/contribution_detail.html'

class PledgeUpdateView(UpdateView):
  model = Pledge
  template_name = 'pledge/pledge_form.html'
  fields = ['amount']

class ContributionUpdateView(UpdateView):
  model = Contribution
  template_name = 'contribution/contribution_form.html'
  fields = ['amount', 'notes']

class PledgeDeleteView(DeleteView):
  model = Pledge
  template_name = 'pledge/pledge_confirm_delete.html'
  success_url = reverse_lazy('pledge_list')

class ContributionDeleteView(DeleteView):
  model = Contribution
  template_name = 'contribution/contribution_confirm_delete.html'
  success_url = reverse_lazy('contribution_list')