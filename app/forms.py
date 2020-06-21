from django import forms
from django.contrib.auth.models import User
from .models import Cities,Article

class Signupform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'placeholder': 'Password'}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'placeholder': 'Your Name'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control",'placeholder': 'Your Email'}))

    class Meta():

        model = User

        fields = ('username','email','password')
        
    # def __init__(self,*args,**kwargs):
    #     print(args,kwargs)
    #     super(Signupform,self).__init__(self,*args,**kwargs)
        
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        print(cleaned_data)
class Loginform(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control",'Placeholder':'Password'}))

    username = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control",'Placeholder':'Username'}))

    email = forms.CharField(widget=forms.EmailInput(attrs={"class":"form-control"}))

    class Meta():

        model = User

        fields = ('username','password')

    def clean_username(self):

        cleaned_data = super().clean()

        name = self.cleaned_data.get('username')

        password = self.cleaned_data.get("password")


class CitiesForm(forms.ModelForm):
    class Meta:
        model = Cities
        fields = '__all__'


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        exclude = ['created','updated','author']

    def __init__ (self,*args,**kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['name'] = forms.CharField(max_length=250,widget=forms.TextInput(attrs={"class":"form-control mb-4",'Placeholder':"Article Name"}))
        self.fields['article_type'] = forms.CharField(max_length=250,widget=forms.TextInput(attrs={"class":"form-control mb-4",'Placeholder':"Type"}))
        self.fields['description'] = forms.CharField(max_length=500,widget=forms.TextInput(attrs={"class":"form-control mb-4",'Placeholder':"Short description"}))  
