"""Module containing examples for error handling"""


def function_4(func_4_param):
    print("We are in Function 4! ", func_4_param)


def function_3(func_3_param):
    print("We are in Function 3! ", func_3_param)

    4/0

    function_4(func_3_param)


def function_2(func_2_param):
    print("We are in Function 2! ", func_2_param)
    try:
        function_3(func_2_param)
    except:
        print("Crisis averted!")

def function_1(func_1_param):
    print("We are in Function 1! ", func_1_param)
    function_2(func_1_param)


function_1("Hello!")
