from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from app_regist.script_auto_identify import auto_identify_py, auto_identify_r
from service_auto_run import auto_run_py, auto_run_r

import json
import os

# Create your views here.

def script_to_service(request, spath, stype, rtype):
    catgname = os.path.basename(os.path.dirname(os.path.split(spath)[0]))
    appname = os.path.basename(os.path.split(spath)[0])
    if rtype == 'GET':
        if stype == 'python':
            arg_of_script = auto_identify_py(spath)
        else:
            arg_of_script = auto_identify_r(spath)
        query_arg_dict = dict(zip(arg_of_script['Arg_Name'], arg_of_script['Arg_Value']))
        query_arg_str = '&'.join('='.join((k, str(v))) for k,v in query_arg_dict.items())
        service_demo = 'http://127.0.0.1:8080/service/run/%s/%s/%s/%s' % (stype,catgname,appname, query_arg_str)

    else:
        if stype == 'python':
            arg_of_script = auto_identify_py(spath)
        else:
            arg_of_script = auto_identify_r(spath)
        query_arg_dict = dict(zip(arg_of_script['Arg_Name'], arg_of_script['Arg_Value']))

        service_host_url = 'http://127.0.0.1:8080/service/run/%s/%s/%s/' % (stype, catgname, appname)
        service_query_data = json.dumps(query_arg_dict)
        service_demo = {'host_url': service_host_url, 'query_data': service_query_data}
    return render(request, 'service_core/show_service_demo.html', {'service_demo': service_demo, 'rtype': rtype})

@csrf_exempt
def service_run(request, stype, catgname, appname, **kwargs):
    if request.method == 'GET':
        kwargs = dict(item.split('=') for item in kwargs['kwargs'].split('&'))
        if stype == 'python':
            service_result = auto_run_py(catgname, appname, **kwargs)
        else:
            service_result = auto_run_r(catgname, appname, **kwargs)
        return JsonResponse(service_result, safe=False)
    elif request.method == 'POST':
        kwargs = json.loads(request.body)
        # return JsonResponse(kwargs, safe=False)
        if stype == 'python':
            service_result = auto_run_py(catgname, appname, **kwargs)
        else:
            service_result = auto_run_r(catgname, appname, **kwargs)
        return JsonResponse(service_result, safe=False)

@csrf_exempt
def rob_test(request):
    if request.method == 'POST':
        kwargs = json.loads(request.body)
        return JsonResponse(kwargs, safe=False)


