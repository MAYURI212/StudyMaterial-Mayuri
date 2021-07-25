from django import forms

 
class Login_user(forms.Form):
    user_name=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'username','title':'Enter Your name'}),label='Your name ',max_length=50,min_length=11,required=True) 
    password=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'password','title':'Enter Your password'}),label='Your password',max_length=50,min_length=10,required=True) 
    