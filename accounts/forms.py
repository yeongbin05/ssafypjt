from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm,UserCreationForm


class CustomUserChangeForm(UserChangeForm):
    
    class Meta(UserChangeForm.Meta):
       
        model = get_user_model()
        fields = ('email','first_name','last_name','username')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        password = self.fields.get("password")
        if password:
            password.help_text = ''
        print(password.label)

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username','email','first_name','last_name')