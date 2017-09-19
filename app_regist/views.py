from django.shortcuts import render
from django.http import JsonResponse, HttpResponse


from script_auto_identify import auto_identify_py, auto_identify_r

# Create your views here.

def script_identify(request, stype, catg_name, app_name, script_name):
    if stype == 'python':
        arg_of_script = auto_identify_py(catg_name, app_name, script_name)
    else:
        arg_of_script = auto_identify_r(catg_name, app_name, script_name)
    return JsonResponse(arg_of_script)

