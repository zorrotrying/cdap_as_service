from django.shortcuts import render

from script_auto_identify import auto_identify_py, auto_identify_r

import json
import os

# Create your views here.
def script_to_service(request, stype, rtype, catg_name, app_name, script_name):
    if rtype == 'GET':
        if stype == 'python':
            arg_of_script = auto_identify_py(catg_name, app_name, script_name)
        else:
            arg_of_script = auto_identify_r(catg_name, app_name, script_name)
        query_arg_dict = dict(zip(arg_of_script['Arg_Name'], arg_of_script['Arg_Value']))
        query_arg_str = '&'.join('='.join((k, str(v))) for k,v in query_arg_dict.items())
        service_demo = 'http://127.0.0.1:8080/runservice/%s/%s/%s/%s' % (stype, catg_name, app_name, query_arg_str)

    else:
        if stype == 'python':
            arg_of_script = auto_identify_py(catg_name, app_name, script_name)
        else:
            arg_of_script = auto_identify_r(catg_name, app_name, script_name)
        query_arg_dict = dict(zip(arg_of_script['Arg_Name'], arg_of_script['Arg_Value']))

        service_host_url = 'http://127.0.0.1:8080/runservice/%s/%s/%s/' % (stype, catg_name, app_name)
        service_query_data = json.dumps(query_arg_dict)
        service_demo = {'host_url': service_host_url, 'query_data': service_query_data}
    return render(request, 'service_regist/show_service_demo.html', {'service_demo': service_demo, 'rtype': rtype})
