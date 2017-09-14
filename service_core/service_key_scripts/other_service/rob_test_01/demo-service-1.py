import math
def cdap_service_fun(a=2,b=3):
    a = int(a)
    b = int(b)
    sum_value = a + b
    prod_value = a*b
    power_value = a**b
    exp_value = math.exp(a) + math.exp(b)
    return {'Sum of a b': sum_value,
            'prod of a b': prod_value,
            'power of a b': power_value,
            'exp of a and b': exp_value}

