from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


from script_auto_identify import auto_identify_py, auto_identify_r

# Create your views here.

def script_identify(request, spath, type):
    if type == 'python':
        arg_of_script = auto_identify_py(spath)
    else:
        arg_of_script = auto_identify_r(spath)
    return JsonResponse(arg_of_script)

