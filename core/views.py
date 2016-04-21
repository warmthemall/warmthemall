from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from .models import *
from django.core.exceptions import PermissionDenied
from django.db import connection
from django.db.models import Sum, Count
import datetime
from registration.backends.simple.views import RegistrationView
from forms import UserProfileRegistrationForm
from .forms import *



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

  def get_context_data(self, **kwargs):
    context = super(UserDetailView, self).get_context_data(**kwargs)
    user_in_view = User.objects.get(username=self.kwargs['slug'])
    contributions = Contribution.objects.filter(user=user_in_view)
    context['contributions'] = contributions
    pledges = Pledge.objects.filter(user=user_in_view)
    context['pledges'] = pledges
    userprofile = UserProfile.objects.filter(user=user_in_view)
    context['userprofile'] = userprofile
    return context


class UserUpdateView(UpdateView):
  model = User
  slug_field = "username"
  template_name = "user/user_form.html"
  form_class = UserProfileUpdateForm

  def get_success_url(self):
    return reverse('user_detail', args=[self.request.user.username])

  def get_object(self, *args, **kwargs):
    object = super(UserUpdateView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object

class AboutUsView(TemplateView):
  template_name = "about_us.html"

class ParentTipsView(TemplateView):
  template_name = "parent_tips.html"

class UserListView(ListView):
  model = User
  template_name = 'leaderboards.html'

  def get_queryset(self):
    queryset = super(UserListView, self).get_queryset()
    return queryset.annotate(
        contributions_count=Count('contribution'),
        contributions_total=Sum('contribution__amount'),
    ).order_by("-contributions_total")[:5]

class MonthlyListView(ListView):
  model = User
  template_name = 'monthly_leaderboards.html'

  def get_queryset(self):
    queryset = super(MonthlyListView, self).get_queryset()
    today = datetime.date.today()
    this_month_start = today.replace(day = 1)
    if today.month == 12:
      next_month_start = today.replace(year=today.year + 1, month=1, day=1)
    else:
      next_month_start = today.replace(month=today.month + 1, day=1)
    User.objects.filter(
      contribution__date__gte = this_month_start,
      contribution__date__lt = next_month_start,
    ).annotate(
       monthly_count=Count('contribution'),
       monthly_total=Sum('contribution__amount')
    ).order_by("-monthly_total")[:5]
    return queryset


class SearchContributionListView(ContributionListView):
  def get_queryset(self):
    incoming_query_string = self.request.GET.get('query', '')
    return Contribution.objects.filter(notes__icontains=incoming_query_string)

class UserDeleteView(DeleteView):
  model = User
  slug_field = "username"
  template_name = 'user/user_confirm_delete.html'

  def get_success_url(self):
    return reverse_lazy('logout')

  def get_object(self, *args, **kwargs):
    object = super(UserDeleteView, self).get_object(*args, **kwargs)
    if object != self.request.user:
      raise PermissionDenied()
    return object

  def delete(self, request, *args, **kwargs):
    user = super(UserDeleteView, self).get_object(*args)
    user.is_active = False
    user.save()
    return redirect(self.get_success_url())

class UserProfileRegistrationView(RegistrationView):
  form_class = UserProfileRegistrationForm

  def register(self, request, form_class):
    new_user = super(UserProfileRegistrationView, self).register(request, form_class)
    user_profile = UserProfile()
    user_profile.user = new_user
    user_profile.state = form_class.cleaned_data['state']
    user_profile.save()
    return user_profile

  def get_success_url(self, request, user):
        return reverse_lazy('home')