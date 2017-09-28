import inspect
import importlib
import sys
import os
import rpy2.robjects as robjects


app_dir_root = r'H:\RobinWorks\01_Projects\10_cDAP\SourceCode\cDAP_workspace\sourcecode\TestingServer\app_core_scripts'


def auto_identify_py(catg_name, app_name, script_name):
    sys.path.append(app_dir_root)

    script_as_module = importlib.import_module('.%s' % os.path.splitext(script_name)[0], '%s.%s' % (catg_name, app_name))
    arg_temp_list = inspect.getargspec(eval('%s.%s' % ('script_as_module', 'cdap_service_fun')))
    arg_dict = {'Arg_Name': arg_temp_list[0], 'Arg_Value': arg_temp_list[3], }

    return arg_dict

def auto_identify_r(catg_name, app_name, script_name):
    script_path = os.path.join(app_dir_root, catg_name, app_name, script_name)
    robjects.r.source(script_path)
    arg_temp_list = robjects.r['formals']('cdap_service_fun')
    arg_name = []
    arg_value = ()
    for key in arg_temp_list.names:
        arg_name.append(key)
        arg_value+=(arg_temp_list.rx2(key)[0],)
    arg_dict = {'Arg_Name': arg_name, 'Arg_Value': arg_value, }
    return arg_dict


