from django import forms
from Tasks.models import Event, Participant, Catagory


class CatagoryForm(forms.ModelForm):
    class Meta:
        model = Catagory
        fields = ['C_name', 'C_Description']
        widgets = {
            'C_name': forms.TextInput(attrs={'class': 'w-full border rounded px-2 py-1'}),
            'C_Description': forms.Textarea(attrs={'class': 'w-full border rounded px-2 py-1', 'rows': 4}),
        }


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'description', 'date', 'location', 'catagory']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'w-full border rounded px-2 py-1'}),
            'description': forms.Textarea(attrs={'class': 'w-full border rounded px-2 py-1', 'rows': 4}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'w-full border rounded px-2 py-1'}),
            'location': forms.TextInput(attrs={'class': 'w-full border rounded px-2 py-1'}),
            'catagory': forms.Select(attrs={'class': 'w-full border rounded px-2 py-1'}),
        }


class ParticipantForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = ['p_name', 'p_email', 'events']
        widgets = {
            'p_name': forms.TextInput(attrs={'class': 'w-full border rounded px-2 py-1'}),
            'p_email': forms.EmailInput(attrs={'class': 'w-full border rounded px-2 py-1'}),
            'events': forms.SelectMultiple(attrs={'class': 'w-full border rounded px-2 py-1'}),
        }

