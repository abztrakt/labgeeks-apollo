from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from forms_builder.forms.models import *

@login_required
def tool(request, formid):
    form = Form.objects.get(id=formid)
    params = {'formid': formid, 'form': form}
    return render_to_response('tool.html', params, context_instance=RequestContext(request))

@login_required
def tools_list(request):
    forms = Form.objects.all()
    params = {'forms': forms, 'request': request}
    return render_to_response('tools.html', params, context_instance=RequestContext(request))
