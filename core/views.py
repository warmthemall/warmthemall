from django.shortcuts import render
from django.views.generic import TemplateView, CreateView
from django.core.urlresolvers import reverse_lazy
from .models import *

class Home(TemplateView):
  template_name = "home.html"

class PledgeCreateView(CreateView):
  model = Pledge
  template_name = "pledge/pledge_form.html"
  fields = ['amount']
  success_url = reverse_lazy('home')

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super(PledgeCreateView, self).form_valid(form)

class ContributionCreateView(CreateView):
  model = Contribution
  template_name = "contribution/contribution_form.html"
  fields = ['amount', 'notes']
  success_url = reverse_lazy('home')

  def form_valid(self,form):
    form.instance.user = self.request.user
    return super(ContributionCreateView, self).form_valid(form)

# Create your views here.
