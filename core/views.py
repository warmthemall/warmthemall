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
  paginate_by = 10

class ContributionListView(ListView):
  model = Contribution
  template_name = "contribution/contribution_list.html"
  paginate_by = 10

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

  def get_object(self, *args, **kwargs):
    object = super(PledgeUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class ContributionUpdateView(UpdateView):
  model = Contribution
  template_name = 'contribution/contribution_form.html'
  fields = ['amount', 'notes']

  def get_object(self, *args, **kwargs):
    object = super(ContributionUpdateView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class PledgeDeleteView(DeleteView):
  model = Pledge
  template_name = 'pledge/pledge_confirm_delete.html'
  success_url = reverse_lazy('pledge_list')

  def get_object(self, *args, **kwargs):
    object = super(PledgeDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class ContributionDeleteView(DeleteView):
  model = Contribution
  template_name = 'contribution/contribution_confirm_delete.html'
  success_url = reverse_lazy('contribution_list')

  def get_object(self, *args, **kwargs):
    object = super(ContributionDeleteView, self).get_object(*args, **kwargs)
    if object.user != self.request.user:
      raise PermissionDenied()
    return object

class UserDetailView(DetailView):
  model = User
  slug_field = 'username'
  template_name = 'user/user_detail.html'
  context_object_name = 'user_in_view'


class UserUpdateView(UpdateView):
  model = User
  slug_field = "username"
  template_name = "user/user_form.html"
  fields = ['email', 'first_name', 'state']

  def get_success_url(self):
    return reverse('user_detail', args=[self.request.user.username])

  def get_object(self, *args, **kwargs):
    object = super(UserUpdateView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object

class AboutUsView(TemplateView):
  template_name = "about_us.html"


class SearchContributionListView(ContributionListView):
  def get_queryset(self):
    incoming_query_string = self.request.GET.get('query', '')
    return Contribution.objects.filter(notes__icontains=incoming_query_string)