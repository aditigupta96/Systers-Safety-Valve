from django import forms
from django.forms import ModelForm
from .models import Complaint
from django.contrib.auth.models import User
from django_countries import countries
from django_countries.fields import LazyTypedChoiceField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Fieldset, ButtonHolder, Field
from crispy_forms.bootstrap import AppendedText, PrependedText, FormActions

class ComplaintForm(forms.Form):
    title = forms.CharField(max_length=100)
    company = forms.CharField(max_length=100)
    person = forms.CharField(max_length=100)
    city = forms.CharField(max_length=100)
    country = LazyTypedChoiceField(choices=countries)
    experience = forms.CharField(max_length=10000, widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super(ComplaintForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_show_labels = False 
    
        # self.helper.layout = Layout(
        # 	Field('title', css_class='input-sm', placeholder="Title"),
        # 	Field('company', css_class='input-sm', placeholder="Company"),
        # 	Field('person', css_class='input-sm', placeholder="Relevant Person"),
        # 	Field('city', css_class='input-sm', placeholder="City"),
        # 	Field('country', css_class='input-sm'),
        # 	Field('experience', css_class='input-sm', placeholder="Write your experience here."),
        #     ButtonHolder(
        #         Submit('submit', 'Submit', css_class='btn btn-lg btn-primary')
        #     )
        # )
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-8'

        self.helper.layout = Layout(
            'title',
            'company',
            'person',
            'city',
            'country',
            'experience',
            ButtonHolder(
                Submit('submit', 'Submit', css_class='btn btn-lg btn-primary')
            )
        )