from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='email address')
    email2 = forms.EmailField(label='confirm email address')
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'email2',
            'password',
        ]
    
    def clean(self, *args, **kwargs):
        email = self.cleaned_data.get('email')
        email2 = self.cleaned_data.get('email2')

        if email != email2:
            raise forms.ValidationError('Email not match')
        
        email_qs = User.objects.filter(email=email)

        if email_qs.exists():
            raise forms.ValidationError(
                'This email is already used'
            )
        
        return super(UserRegistrationForm, self).clean(*args, **kwargs)


