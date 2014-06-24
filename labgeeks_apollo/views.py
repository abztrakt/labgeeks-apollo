from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms_builder.forms.models import *

def closing_procedures(request):
    return render(request, 'closing-procedures.html')

def printer_issue(request):
    return render_to_response('printer-issue.html', context_instance=RequestContext(request))

def login_issue(reqeust):
    return render(request, 'login-issue.html')

def tools_list(request):
    forms = Form.objects.all()
    params = {'forms': forms, 'request': request}
    return render_to_response('tools.html', params)
