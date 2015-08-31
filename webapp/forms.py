from django import forms

class ContactUsForm(forms.Form):
    Name = forms.CharField(max_length=100, error_messages={'required': 'Please enter your name'},widget=forms.TextInput(attrs={'class':'form-control'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Phone_Number = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    Message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    Cc_myself = forms.BooleanField(required=False)
