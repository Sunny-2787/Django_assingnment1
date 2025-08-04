from  django import forms
from Tasks.models import Event ,Participant
class Eventform(forms.ModelForm):
    class  Meta:
        model = Event
        fields  = ['name','description','date','location','catagory']

        
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full mt-5 px-4 py-2 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter event name'
            }),
            'description': forms.Textarea(attrs={
                'class': 'w-full px-4 mt-5 py-2 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter event description',
                'rows': 4,
            }),
            'date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'w-full px-4 mt-5 py-2 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),

            'location': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 mt-5 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Event location'
            }),
            'catagory': forms.Select(attrs={
                'class': 'w-full px-4 py-2 mt-5 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400'
            }),
        }

class participanForm(forms.ModelForm):
    class Meta:
        model = Participant
        fields = '__all__'
        widgets={
            'p_name':forms.TextInput(attrs={
                'class': 'w-full mt-5 px-4 py-2 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Participant name'}),

            'p_email' : forms.EmailInput(attrs={
                'class': 'w-full mt-5 px-4 py-2 border rounded-lg shadow focus:outline-none focus:ring-2 focus:ring-blue-400',
                'placeholder': 'Enter event name'})
        }
