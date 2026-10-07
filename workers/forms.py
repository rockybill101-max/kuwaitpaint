from django import forms
from .models import Worker, Enquiry

class WorkerForm(forms.ModelForm):
    class Meta:
        model = Worker
        fields = ['name', 'phone', 'area', 'experience']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your full name'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone number (e.g. 51234567)'}),
            'area': forms.TextInput(attrs={'placeholder': 'Area (e.g. Salmiya)'}),
            'experience': forms.TextInput(attrs={'placeholder': 'Experience (e.g. 5 years)'}),
        }


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = Enquiry
        fields = ['customer_name', 'customer_phone', 'customer_email', 'area', 'details']
        widgets = {
            'customer_name': forms.TextInput(attrs={'placeholder': 'Your name'}),
            'customer_phone': forms.TextInput(attrs={'placeholder': 'Your phone (e.g. 51234567)'}),
            'customer_email': forms.EmailInput(attrs={'placeholder': 'Your email'}),
            'area': forms.TextInput(attrs={'placeholder': 'Area (e.g. Salmiya)'}),
            'details': forms.Textarea(attrs={'placeholder': 'Describe your paint work (rooms, size, etc.)', 'rows': 4}),
        }
