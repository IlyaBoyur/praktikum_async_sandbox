from typing import Any, List

# type - метакласс - объект, создающий новые классы
MyClass = type('MyClass', (object,), {'test_attr': 15})
print(type(MyClass))

my_class_inst = MyClass()
# 
print(my_class_inst.test_attr)

# Метакласс - любой callable объект с параметрами 
def metaclass_creator(class_name: str, parents: List[type], attrs: List[Any]):
    return "Simple metaclass"

class MyClass(metaclass=metaclass_creator):
    pass

print(MyClass)
print(type(MyClass))

class MyMeta(type):
    def __new__(cls, cls_name, parents, attrs):
        print("my_meta: вызвали метод __new__")
        return super().__new__(cls, cls_name, parents, attrs)

    def __call__(self, *args, **kwargs):
        # Метод самого объекта класса, а не экземпляра класса
        print("my_meta: вызвали метод __call__")
        return super().__call__(*args, **kwargs)

class MyClass(metaclass=MyMeta):
    pass



class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MySingleton(metaclass=SingletonMeta):
    pass

if __name__ == "__main__":
    inst = MyClass()

    singleton1 = MySingleton()
    singleton2 = MySingleton()

    print(id(singleton1))
    print(id(singleton2))
    print(singleton1 == singleton2)