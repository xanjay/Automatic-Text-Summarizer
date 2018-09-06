# Create your views here.
from django.urls import reverse_lazy
from django.views import generic
from accounts.forms import RegisterForm


class SingUp(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('index', current_app='summarizer')
    template_name = 'registration/signup_form.html'
