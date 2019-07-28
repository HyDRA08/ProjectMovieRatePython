from django import forms
from .models import modelmovie

morf=(
    ('Male','MALE'),
    ('Female','FEMALE'),
)



class formsignup(forms.Form):
    name=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Enter Name'}))
    email = forms.EmailField(max_length=30,widget=forms.TextInput(attrs={'placeholder': 'Enter Email'}))
    # gender=forms.ChoiceField(widget=forms.RadioSelect, choices=morf)
    gender = forms.CharField(widget=forms.Select(choices=morf))
    user_name=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Enter User Name'}))
    password=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Enter Password'}))
    confpassword=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Confirm Password'}))

class formlogin(forms.Form):
    username=forms.CharField(max_length=20,widget=forms.TextInput(attrs={'placeholder': 'Enter Your User Name'}))
    password=forms.CharField(max_length=15,widget=forms.TextInput(attrs={'placeholder': 'Enter Your Password'}))

class formmovie(forms.Form):
    movie_name=forms.CharField(max_length=30,)
    movie_director=forms.CharField(max_length=30)
    movie_studio=forms.CharField(max_length=40)
    movie_year=forms.CharField(max_length=10)
    movie_image=forms.FileField()

class formselectmovie(forms.Form):
    movie_name_get=forms.CharField(max_length=50)

class formratinghold(forms.Form):
    ratings=forms.IntegerField()
    review = forms.CharField(widget=forms.Textarea)

class formmovieholding(forms.Form):
    movie_name_get=forms.CharField(max_length=50)
