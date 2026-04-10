from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from .models import Avatar


class RegistroFormulario(UserCreationForm):
    email = forms.EmailField(
        required=True, help_text="Obligatorio. Poné un email válido."
    )

    class Meta:
        model = User
        fields = ["username", "email"]


class UserEditForm(UserChangeForm):
    password = None

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        help_texts = {k: "" for k in ["email", "first_name", "last_name"]}


class AvatarUpdateForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ["imagen", "biografia"]
        widgets = {
            "biografia": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
        }
