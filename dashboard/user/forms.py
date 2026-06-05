from django import forms
from django.contrib.auth import forms as auth_form
from accounts.models import Profile, User

class UserProfileWeditForm(forms.ModelForm):
    
    username = forms.CharField()

    class Meta:
        model = Profile
        fields = ["first_name", "last_name", "username"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].initial = self.instance.user.username

    def clean_username(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("یوزرنیم درحال حاضر وجود دارد.")
        return username
    
    def save(self, commit=True):
        profile = super().save(commit=False)
        profile.user.username = self.cleaned_data["username"]

        if commit:
            profile.user.save()
            profile.save()
        return profile

class UserChangePasswordForm(auth_form.PasswordChangeForm):

    error_messages = {
        "password_incorrect":
            "پسوورد قدیمی شما اشتباه است.",
        "password_mismatch":
            "پسوورد های جدید همخوانی ندارند"
    }


