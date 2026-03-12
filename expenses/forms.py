from django import forms
from .models import Expense
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
class ExpenseForm(forms.ModelForm):
    class Meta:
        model=Expense
        fields=['title','amount','category','date']
        widgets={
            'title':forms.TextInput(attrs={
                'class':'ml-8 rounded-2xl border-b-2 border-blue-400 focus:outline-none  bg-transparent pl-2 text-white',
                'placeholder':'e.g. Lunch at cafe'
                }),
            'amount':forms.NumberInput(attrs={
                'class':'ml-2 rounded-2xl border-b-2 border-blue-400 focus:outline-none  bg-transparent pl-2 text-white',
                'placeholder':'0.00'
                }),
            'category':forms.TextInput(attrs={
                'class':'ml-2 rounded-2xl border-b-2 border-blue-400 focus:outline-none  bg-transparent pl-2 text-white',
                'placeholder':'e.g. Food'
                }),
            'date':forms.DateInput(attrs={
                'class':'ml-10 rounded-2xl border-b-2 border-blue-400 focus:outline-none  bg-transparent pl-2 text-white',
                'placeholder':'YYYY-MM-DD'
                }),
        }

class CustomUserCreationForm(UserCreationForm):
    def __init__ (self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.help_text=None
            field.widget.attrs.update({"class":'ml-5 focus:outline-none pl-2 focus:ring-2 rounded-xl focus:ring-blue-400'})
class CustomLoginForm(AuthenticationForm):
    def __init__ (self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.help_text=None            
            field.widget.attrs.update({"class":'ml-5 rounded-xl focus:outline-none pl-2 focus:ring-2 focus:ring-blue-400'})
