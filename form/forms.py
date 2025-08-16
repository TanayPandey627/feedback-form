from django import forms
from .models import Feedback

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone_number',
            'overall_satisfaction',
            'product_quality',
            'delivery_service_rating',
            'recommendation',
            'additional_feedback',
            'terms_agreed',
            'image',
        ]

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
            
            # Will customize overall satisfaction in HTML (emoji-based)
            'product_quality': forms.NumberInput(attrs={'type': 'hidden'}),
            'delivery_service_rating': forms.NumberInput(attrs={'type': 'hidden'}),
            
            'recommendation': forms.Select(attrs={'class': 'form-control'}),
            'additional_feedback': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'terms_agreed': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
