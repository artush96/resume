from django import forms
from .models import *


# class DemoLoginForm(forms.ModelForm):
#     class Meta:
#         model = User
#         fields = ['username', 'password']
#         widgets = {
#             'password': forms.PasswordInput(attrs={'initial': '', 'size': '80'})
#         }

class AboutMeCreateForm(forms.ModelForm):
    class Meta:
        model = AboutMe
        fields = ['age', 'location', 'specialty', 'body']
        widgets = {
            'age': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Age'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Location'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Specialty'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '6', 'placeholder': '* Body'}),
        }

class ServicesCreateForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ['title_1', 'body_1', 'title_2', 'body_2', 'title_3', 'body_3', 'title_4', 'body_4']
        widgets = {
            'title_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Service Name'}),
            'body_1': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': '* Service Characteristics'}),
            'title_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Service Name'}),
            'body_2': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': '* Service Characteristics'}),
            'title_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Service Name'}),
            'body_3': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': '* Service Characteristics'}),
            'title_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Service Name'}),
            'body_4': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': '* Service Characteristics'}),
        }

class PricingCreateForm(forms.ModelForm):
    class Meta:
        model = Pricing
        fields = ['title_l', 'price_l', 'option_l_1', 'option_l_2', 'option_l_3', 'option_l_4',
                  'title_c', 'price_c', 'option_c_1', 'option_c_2', 'option_c_3', 'option_c_4',
                  'title_r', 'price_r', 'option_r_1', 'option_r_2', 'option_r_3', 'option_r_4']
        widgets = {
            'title_l': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Pricing Plain'}),
            'price_l': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Price'}),
            'option_l_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_l_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_l_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_l_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'title_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Pricing Plain'}),
            'price_c': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Price'}),
            'option_c_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_c_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_c_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_c_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'title_r': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Pricing Plain'}),
            'price_r': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Price'}),
            'option_r_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_r_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_r_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
            'option_r_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Option'}),
        }

class FactsCreateForm(forms.ModelForm):
    class Meta:
        model = Facts
        fields = ['count_1', 'fact_1', 'count_2', 'fact_2', 'count_3', 'fact_3', 'count_4', 'fact_4']
        widgets = {
            'count_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Count'}),
            'fact_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Fact'}),
            'count_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Count'}),
            'fact_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Fact'}),
            'count_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Count'}),
            'fact_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Fact'}),
            'count_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Count'}),
            'fact_4': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Fact'}),
        }

class ClientsCreateForm(forms.ModelForm):
    class Meta:
        model = Clients
        fields = ['client_logo', 'client_url']
        widgets = {
            'client_logo': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': '* Logo'}),
            'client_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Url'}),
        }

class ContactCreateForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['introduction', 'location', 'phone', 'mail', 'telegram', 'telegram_name']
        widgets = {
            'introduction': forms.Textarea(attrs={'class': 'form-control', 'rows': '4', 'placeholder': '* Introduction'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Location'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Phone'}),
            'mail': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Mail'}),
            'telegram': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Telegram'}),
            'telegram_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Telegram Name'}),
        }

class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'user']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Title'}),
            'user': forms.HiddenInput()
        }

class WorksCreateForm(forms.ModelForm):
    class Meta:
        model = Works
        category = forms.ModelChoiceField(queryset=Category.objects.all(), to_field_name='title',
                                          widget=forms.Select(
                                              attrs={'class': 'form-control', 'placeholder': '* Category'}))
        fields = ['image', 'title', 'category', 'work_url']
        widgets = {
            'image': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': '* Image'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Title'}),
            'work_url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Work Url'}),
        }

class ExperienceCreateForm(forms.ModelForm):
    class Meta:
        model = Experience
        fields = ['option_1', 'option_2', 'option_3', 'body']
        widgets = {
            'option_1': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Experience'}),
            'option_2': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Experience'}),
            'option_3': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Experience'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '5', 'placeholder': '* Experience'}),
        }

class SkillsCreateForm(forms.ModelForm):
    class Meta:
        model = Skills
        fields = ['skills', 'skill_level']
        widgets = {
            'skills': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Skill'}),
            'skill_level': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Level'}),
        }

class EducationCreateForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['year', 'schooll', 'location', 'body']
        widgets = {
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Education Year'}),
            'schooll': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* School/University'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Education Location'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': '* Specialty'}),
        }

class WorkExprerienceCreateForm(forms.ModelForm):
    class Meta:
        model = WorkExprerience
        fields = ['year', 'specialty', 'location', 'body']
        widgets = {
            'year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Exprerience Year'}),
            'specialty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Speciality'}),
            'location': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Exprerience Location'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'rows': '3', 'placeholder': '* Job Description'}),
        }

class AboutCreateForm(forms.ModelForm):
    class Meta:
        model = About
        fields = ['img', 'name', 'speciality', 'cv', 'fb', 'lin', 'gt', 'tm']
        widgets = {
            'img': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': '* Profile Picture'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Full Name '}),
            'speciality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Speciality'}),
            'cv': forms.FileInput(attrs={'class': 'form-control-file', 'placeholder': '* CV File'}),
            'fb': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Facebook'}),
            'lin': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* LinkedIn'}),
            'gt': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* GitHub'}),
            'tm': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '* Telegram'}),
        }

