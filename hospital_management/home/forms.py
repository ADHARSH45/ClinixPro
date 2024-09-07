from django import forms
from .models import booking
class Dateinput(forms.DateInput):
    input_type = 'date'

class bookingform(forms.ModelForm):
    class Meta:
        model = booking
        fields = '__all__'
        widgets = {
            'booking_date' : Dateinput()
        }

        labels = {
            'p_name':"Name",
            'p_phone':"Phone",
            'p_email':"Email",
            'doct_name':"Doctor Nmae",
            'booking_date':"Bookind Date",
            "booked_on":"Booked On"
        }