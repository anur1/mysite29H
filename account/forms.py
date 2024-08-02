from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets
from django.contrib import messages

class LoginUserForm (AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs )
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"})
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})

    #istersek gelen bilgiyi düzenleyeiliriz
    def clean_username(self):
        username=self.cleaned_data.get("username")

        #login olan kişi admin ise mesaj ver
        if username == "admin":
            messages.add_message(self.request, messages.SUCCESS, "hoşgeldin admin")
        
        return username
    
    #gelen username ü ile başlıyorsa uyarı verebiliriz
    def confirm_login_allowed(self, user):
        if user.username.startswith("ü"):
            raise forms.ValidationError("bu kullanıcı adı ile login olamazsınız")