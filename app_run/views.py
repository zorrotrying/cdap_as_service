from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


from script_auto_run import auto_run_py, auto_run_r
import json

# Create your views here.

#
# def script_run(request, spath, type, **kwargs):
#     if type == 'python':
#         app_result_json = auto_run_py(spath, **kwargs)
#     else:
#         app_result_json = auto_run_r(spath, **kwargs)
#     return JsonResponse(app_result_json)

@csrf_exempt
def script_run(request):
    if request.method == 'POST':
        query_data = json.loads(request.body)
        script_type = query_data['stype']
        catg_name = query_data['catg_name']
        app_name = query_data['app_name']
        script_name = query_data['script_name']
        kwargs = query_data['args_dict']

        if script_type == 'python':
            app_result_json = auto_run_py(catg_name, app_name, script_name, **kwargs)
        else:
            app_result_json = auto_run_r(catg_name, app_name, script_name, **kwargs)
        return JsonResponse(app_result_json, safe=False)
