from django.http import JsonResponse

from script_auto_identify import auto_identify_py, auto_identify_r

import json

service_url_root = r'http://127.0.0.1:8022'


# Create your views here.
def script_to_service(request, stype, rtype, catg_name, app_name, script_name):
    if rtype == 'GET':
        if stype == 'python':
            arg_of_script = auto_identify_py(catg_name, app_name, script_name)
        else:
            arg_of_script = auto_identify_r(catg_name, app_name, script_name)
        query_arg_dict = dict(zip(arg_of_script['Arg_Name'], arg_of_script['Arg_Value']))
        query_arg_str = '&'.join('='.join((k, str(v))) for k,v in query_arg_dict.items())
        service_demo = {'host_url': '%s/runservice/%s/%s/%s/%s' % (service_url_root, stype, catg_name, app_name, query_arg_str)}

    else:
        if stype == 'python':
            arg_of_script = auto_identify_py(catg_name, app_name, script_name)
        else:
            arg_of_script = auto_identify_r(catg_name, app_name, script_name)
        query_arg_dict = dict(zip(arg_of_script['Arg_Name'], arg_of_script['Arg_Value']))

        service_host_url = '%s/runservice/%s/%s/%s/' % (service_url_root, stype, catg_name, app_name)
        service_query_data = json.dumps(query_arg_dict)
        service_demo = {'host_url': service_host_url, 'query_data': service_query_data}
    return JsonResponse(service_demo, safe=False)
