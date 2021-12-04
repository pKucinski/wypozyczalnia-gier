from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    class Meta:

        model = User
        email = forms.CharField()

<<<<<<< Updated upstream
        fields = ('username', 'email', 'password1', 'password2', )
=======
        fields = ('username', 'email', 'password1', 'password2', )


>>>>>>> Stashed changes
