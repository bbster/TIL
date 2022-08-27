# # 어트리뷰트란 클래스 내부에 포함되어 있는 변수나 메서드를 의미
# class Drama:
#     # 클래스 속성 메서드 단계와 동일한 위치
#     def __init__(self, name, broadcaster, episode): # 초기화를 위한 메서드  / 인스턴스화 할때 반드시 처음에 실행되는 메서드
#         self.name = name # 어트리뷰트
#         self.broadcaster = broadcaster
#         self.episode = episode
#
#     def my_watching_broadcast(self): # 클래스의 메서드
#             return self.name, self.broadcaster, self.episode
#
# drama_instance = Drama("wooyoungwoo", "netflix", 1) # Drama라는 클래스의 인스턴스 생성
# print(f"내가 현재 시청하는 드라마: {drama_instance.my_watching_broadcast()}")
#
# # getattr(object, name, default)
# # 해당 객체의 어트리뷰트를 돌려준다.
# # drama_instance라는 객체의 속성값에 name이 있으면 그 name값 리턴
# getattr_result = getattr(drama_instance, "name") # 공식 문서에 따르면 drama_instance.name과 동일하다
# print(f"getattr : {getattr_result}")
# # getattr_result = getattr(drama_instance, "name", "broadcaster") # 첫번째 name에 대한 값만 리턴
# # print(f"getattr : {getattr_result}")
# getattr_result = getattr(drama_instance, "broadcaster")
# print(f"getattr : {getattr_result}")
# getattr_result = getattr(drama_instance, "episode", "episode")
# print(f"getattr : {getattr_result}")
# print(f"getattr_ids : {id(getattr_result)}")
#
# # setattr(object, name, value)
# # 해당 객체의 어트리뷰트 중 새로운 값으로 수정할수 있다.
# # drama_instance라는 객체의 episode라는 속성의 값을 2로 세팅한다.
# setattr_result = setattr(drama_instance, "episode", 2)
# getattr_result = getattr(drama_instance, "episode", "episode")
# print(f"setattr후 결과값 : {getattr_result}")
# print(f"getattr_ids : {id(getattr_result)}")
#
# # hasattr(object, name)
# print(f"hasattr : {hasattr(drama_instance, 'name')}")
# print(f"hasattr : {hasattr(drama_instance, 'nothing')}")
#
# def something(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# def first_class_function(param):
#     return param * param
#
# func = first_class_function
#
# print(func(5))
#
# def sum(a,b):
#     return a+b
#
# def execute(func, *args):
#     return func(*args)
#
# first_class_func_variable = sum
# execute(first_class_func_variable, 3, 5)
#
# # cons arr= [1,2,3,4,5]
# # const {length, a: arr[lengtn-1]}=arr
# # arr[arr.lgneth-1]
# # const a = [1,2,3,4,5]
# # a[1] = 3
#
# some_tuple1 = (1,2,3,4,5)
# [_, *some_tuple2] = (1,2,3,4,5)
#
# some_list = list(some_tuple1)
# some_list[0] = 2
#
# print(f"_: {_}")
# print(f"some_tuple: {some_tuple2}")
# print(f"some_tuple: {len(some_tuple2)}")
# print(f"some_tuple: {type(some_tuple2)}")
#
# def closure_func(some_param):
#
#     def inner_func(some_inner_param):
#         return some_param + some_inner_param
#
#     return inner_func
#
# closure1 = closure_func(1)
# closure2 = closure_func(2)
#
# print(f"closure1: {type(closure1)}")
# print(f"closure1: {type(closure_func(1))}")
# print(f"closure1: {id(closure_func(1))}")
# print(f"closure1: {id(closure1)}")
# print(f"closure2: {type(closure2)}")
#
# print(f"closure1: {closure1(3)}")
# print(f"closure1: {id(3)}")
# print(f"closure2: {closure2(4)}")
#
# print(f"closure1: {type(closure1(3))}")
# print(f"closure1: {id(closure1(3))}")
# print(f"closure2: {type(closure2(4))}")
#
# def outer_func(x):
#     num = 1              # global 변수 대신 사용 가능
#     def inner_func():
#         nonlocal num     # nonlocal
#         num = num + x
#         print(f"num: {num}")
#     return inner_func
#
# myfunc = outer_func(10)
# myfunc()

import datetime


def datetime_decorator(func): # 데코레이터로 사용할 함수 만들어줌 closure 형태로
    def decorated():
        print(f"docorator_inner_function_before_work: {datetime.datetime.now()}")
        func()
        print(f"docorator_inner_function_after_work: {datetime.datetime.now()}")
    return decorated()

@datetime_decorator
def main_function_1():
    print("Main function1 start")

@datetime_decorator
def main_function_2():
    print("Main function2 start")

@datetime_decorator
def main_function_3():
    print("Main function3 start")


main_function_1()
main_function_2()
main_function_3()
