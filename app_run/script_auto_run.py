import importlib
import sys
import os
import rpy2.robjects as robjects


def auto_run_py(script_path, **kwargs):
    script_dir = os.path.split(script_path)[0]
    script_dir_root = os.path.dirname(script_dir)
    script_dir_root_root = os.path.dirname(script_dir_root)

    script_name = os.path.splitext(os.path.split(script_path)[1])[0]
    app_name = os.path.basename(script_dir)
    category_name = os.path.basename(script_dir_root)
    sys.path.append(script_dir_root_root)

    script_as_module = importlib.import_module('.%s' % script_name, '%s.%s' % (category_name, app_name))

    app_result = script_as_module.cdap_service_fun(**kwargs)

    return app_result

def auto_run_r(script_path, **kwargs):
    robjects.r.source(script_path)
    main_function = robjects.r['cdap_service_fun']
    return main_function(**kwargs)[0]





