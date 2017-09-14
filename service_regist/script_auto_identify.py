import inspect
import importlib
import sys
import os
import rpy2.robjects as robjects


def auto_identify_py(script_path):
    script_dir = os.path.split(script_path)[0]
    script_dir_root = os.path.dirname(script_dir)
    script_dir_root_root = os.path.dirname(script_dir_root)

    script_name = os.path.splitext(os.path.split(script_path)[1])[0]
    app_name = os.path.basename(script_dir)
    category_name = os.path.basename(script_dir_root)
    sys.path.append(script_dir_root_root)

    script_as_module = importlib.import_module('.%s' % script_name, '%s.%s' % (category_name, app_name))
    arg_temp_list = inspect.getargspec(eval('%s.%s' % ('script_as_module', 'cdap_service_fun')))
    arg_dict = {'Arg_Name': arg_temp_list[0], 'Arg_Value': arg_temp_list[3], }

    return arg_dict

def auto_identify_r(script_path):
    robjects.r.source(script_path)
    arg_temp_list = robjects.r['formals']('cdap_service_fun')
    arg_name = []
    arg_value = ()
    for key in arg_temp_list.names:
        arg_name.append(key)
        arg_value+=(arg_temp_list.rx2(key)[0],)
    arg_dict = {'Arg_Name': arg_name, 'Arg_Value': arg_value, }
    return arg_dict


