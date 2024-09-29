from django import forms
from G2k23.models import Item

# class SignUpForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['first_name', 'last_name', 'dob','mobile_number','email','address','password']
#         widgets = {
#             'password': forms.PasswordInput(),
        

class NewItemform(forms.ModelForm):
    class meta:
        model = Item
        fields = ('Category','name','description','price','image')          