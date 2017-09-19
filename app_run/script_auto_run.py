import importlib
import sys
import os
import rpy2.robjects as robjects

app_dir_root = r'H:\RobinWorks\01_Projects\10_cDAP\SourceCode\cDAP_workspace\sourcecode\TestingServer\app_core_scripts'


def auto_run_py(catg_name, app_name, script_name, **kwargs):
    sys.path.append(app_dir_root)

    script_as_module = importlib.import_module('.%s' % os.path.splitext(script_name)[0], '%s.%s' % (catg_name, app_name))
    app_result = script_as_module.cdap_service_fun(**kwargs)
    return app_result

def auto_run_r(catg_name, app_name, script_name, **kwargs):
    script_path = os.path.join(app_dir_root, catg_name, app_name, script_name)
    robjects.r.source(script_path)
    main_function = robjects.r['cdap_service_fun']
    return main_function(**kwargs)[0]





