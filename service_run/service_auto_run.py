from django.conf import settings

import importlib
import sys
import os
import rpy2.robjects as robjects

service_dir_root = r'H:\RobinWorks\01_Projects\10_cDAP\SourceCode\cDAP_workspace\sourcecode\TestingServer\service_key_scripts'


def auto_run_py(catg_name, app_name, **kwargs):
    sys.path.append(service_dir_root)
    s_list = os.listdir(os.path.join(service_dir_root, catg_name, app_name))
    s_list_filter = filter(lambda a: a != '__init__.py' and a.endswith('.py'), s_list)
    if len(s_list_filter) == 1:
        script_name = os.path.splitext(s_list_filter[0])[0]
    else:
        script_name = 'cdap_main_fun'
    script_as_module = importlib.import_module('.%s' % script_name, '%s.%s' % (catg_name, app_name))
    app_result = script_as_module.cdap_service_fun(**kwargs)
    return app_result

def auto_run_r(catg_name, app_name, **kwargs):
    script_dir = os.path.join(service_dir_root, catg_name, app_name)
    s_list = os.listdir(script_dir)
    s_list_filter = filter(lambda a: a.endswith('.R'), s_list)
    if len(s_list_filter) == 1:
        script_path = os.path.join(script_dir, s_list_filter[0])
    else:
        script_path = os.path.join(script_dir, 'cdap_main_fun.R')
    robjects.r.source(script_path)
    main_function = robjects.r['cdap_service_fun']
    return main_function(**kwargs)[0]





