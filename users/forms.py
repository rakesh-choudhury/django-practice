from django import forms
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
	"""docstring for ClassName"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email','password1','password2']

class UserUpdateForm(forms.ModelForm):
	"""docstring for ClassName"""
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username','email']
		
class ProfileUpdateForm(forms.ModelForm):
	class Meta(object):
		model = Profile
		fields = ['image']
			
		
