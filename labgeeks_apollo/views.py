from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms_builder.forms.models import *

@login_required
def closing_procedures(request):
    return render_to_response('closing-procedures.html', context_instance=RequestContext(request))

@login_required
def printer_issue(request):
    return render_to_response('printer-issue.html', context_instance=RequestContext(request))

@login_required
def login_issue(request):
    return render_to_response('login-issue.html', context_instance=RequestContext(request))

@login_required
def tools_list(request):
    forms = Form.objects.all()
    params = {'forms': forms, 'request': request}
    return render_to_response('tools.html', params, context_instance=RequestContext(request))
