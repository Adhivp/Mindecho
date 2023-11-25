from django.shortcuts import *
from Dreamvista_journel.models import *

# Create your views here.
def journal_input(request):


    if request.method=="POST":
        entry_date = request.POST.get('entry-date')
        enter_title = request.POST.get('enter-title')
        journal_entry = request.POST.get('journal-entry')
        user =journel(date = entry_date,title = enter_title,experience = journal_entry)
        user.save()

    return render(request,'journal_input.html')

from django import forms

class JournalEntryForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    title = forms.CharField(max_length=255)
    contents = forms.CharField(widget=forms.Textarea)

from datetime import datetime

def journal_view(request):
    if request.method == "POST":
        entry_date = request.POST.get('entry-date')

        try:
            entry_date = datetime.strptime(entry_date, '%Y-%m-%d').date()
            entries = journel.objects.filter(date=entry_date)
        except journel.DoesNotExist:
            entries = None

        return render(request, 'journal_view.html', {'entries': entries})

    return render(request, 'journal_view.html', {'entries': None})