from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# Now these classes are not using
class CreateUserForm (UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']