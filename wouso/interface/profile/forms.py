from django import forms


class PasswordForm(forms.Form):
    new_password1 = forms.CharField(max_length=30, label='New password',
            widget=forms.PasswordInput, required=True)
    new_password2 = forms.CharField(max_length=30, label='Repeat new password',
            widget=forms.PasswordInput, required=True)

    def clean(self):
        cleaned_data = super(PasswordForm, self).clean()
        p1 = cleaned_data.get('new_password1')
        p2 = cleaned_data.get('new_password2')
        if p1 != p2:
            raise forms.ValidationError("Passwords do not match.")
        return cleaned_data
