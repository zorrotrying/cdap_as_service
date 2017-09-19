from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from service_auto_run import auto_run_py, auto_run_r

import json
import os
# Create your views here.

@csrf_exempt
def service_run(request, stype, catg_name, app_name, **kwargs):
    if request.method == 'GET':
        kwargs = dict(item.split('=') for item in kwargs['kwargs'].split('&'))
        if stype == 'python':
            service_result = auto_run_py(catg_name, app_name, **kwargs)
        else:
            service_result = auto_run_r(catg_name, app_name, **kwargs)
        return JsonResponse(service_result, safe=False)
    elif request.method == 'POST':
        kwargs = json.loads(request.body)
        # return JsonResponse(kwargs, safe=False)
        if stype == 'python':
            service_result = auto_run_py(catg_name, app_name, **kwargs)
        else:
            service_result = auto_run_r(catg_name, app_name, **kwargs)
        return JsonResponse(service_result, safe=False)
