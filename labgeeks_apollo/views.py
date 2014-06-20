from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms_builder.forms.signal import *
from forms_builder.forms.form import FormForForm

def closing_procedure(request):
    return render(request, 'closing-procedures.html')
