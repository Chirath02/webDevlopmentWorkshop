from django.contrib.auth.models import User
from django.views.generic import CreateView


class UserSignUpView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    fields = ['first_name', 'last_name', 'email', 'username', 'password']
