from django import forms

from django.contrib.auth.models import User


class NewUserForm(forms.ModelForm):
    password1 = forms.CharField(
        label=("Password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),

    )

    password2 = forms.CharField(
        label=("Password Confirm: "),
        widget = forms.PasswordInput(attrs={"autocomplete":"new-password"})
    )

    class Meta:
        model = User
        fields = ["username","email"]

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password1"] and cd["password2"] and cd["password1"] != cd["password2"]:
            raise forms.ValidationError("Passwords mismatch occred.")
        return cd["password1"]

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
