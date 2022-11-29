from django.forms import forms
from .models import *

class PartyForm(forms.Form):
    model = Party
    field = "__all__"