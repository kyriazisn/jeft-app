from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


User = get_user_model()


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email", "username", "age_band", "country")
        widgets = {
            "age_band": forms.Select(choices=[
                ("18-20", "18–20"),
                ("21-24", "21–24"),
                ("25-29", "25–29"),
                ("30-34", "30–34"),
                ("35-39", "35–39"),
                ("40+", "40+"),
            ]),
            "country": forms.TextInput(attrs={"maxlength": 2, "placeholder": "US"}),
        }

    def clean_email(self):
        return self.cleaned_data["email"].lower()


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
