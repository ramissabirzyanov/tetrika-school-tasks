# Необходимо реализовать декоратор @strict
# Декоратор проверяет соответствие типов переданных в вызов функции аргументов типам аргументов,
# объявленным в прототипе функции.
# (подсказка: аннотации типов аргументов можно получить из атрибута объекта функции
# func.__annotations__ или с помощью модуля inspect)
# При несоответствии типов бросать исключение TypeError
# Гарантируется, что параметры в декорируемых функциях будут следующих типов: bool, int, float, str
# Гарантируется, что в декорируемых функциях не будет значений параметров, заданных по умолчанию


# @strict
# def sum_two(a: int, b: int) -> int:
#     return a + b
# print(sum_two(1, 2))  # >>> 3
# print(sum_two(1, 2.4))  # >>> TypeError

def strict(func):
    def wrapper(*args):
        annotations = list(func.__annotations__.values())
        default_annotations = annotations[:-1]
        args_annotations = [type(arg) for arg in args]
        if default_annotations == args_annotations:
            return func(*args)
        else:
            raise TypeError
    return wrapper
