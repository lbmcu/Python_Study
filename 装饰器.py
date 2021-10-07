'''
    装饰器原则：
    1. 不改变源代码
    2. 不改变调用方式
    装饰器模板
'''

'''
    无形参装饰器模板
'''
# def outter(fun):
#     def wrapper(*args, **kwargs):
#         # 1. 调用原函数
#         # 2. 为期增加新功能
#         res = fun(*args, **kwargs)
#         return res
#     return wrapper

'''
    有形参装饰器模板
'''
# def outter_pram(x):
#     def outter(fun):
#         def wrapper(*args, **kwargs):
#             # 1. 调用原函数
# #           # 2. 为期增加新功能
#             res = fun(*args, **kwargs)
#             return res
#         return wrapper
#     return outter

import time

# 无形参装饰器
def outter(fun):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = fun(*args, **kwargs)
        end_time = time.time()
        print('总时间：%s'%(end_time-start_time))
        return res
    return wrapper

# 有形参装饰器
def outter_pram(x):
    def outter(fun):
        def wrapper(*args, **kwargs):
            print("x = %s"%x)
            res = fun(*args, **kwargs)
            return res
        return wrapper
    return outter


'''
    基本源代码
'''
@outter_pram(5)
def index(x,y):
    time.sleep(2)
    print('sum = %s'%(x+y))


index(3,4)

