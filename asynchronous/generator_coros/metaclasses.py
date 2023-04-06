from typing import Any


def create_class_with_type():
    print("create_class_with_type:")
    # type - метакласс - объект, создающий новые классы
    MyClass = type('MyClass', (object,), {'test_attr': 15})
    my_class_instance = MyClass()

    print(type(MyClass))
    print(my_class_instance.test_attr)


def create_metaclass():
    print("create_metaclass:")
    """Метакласс - любой callable объект с параметрами"""
    def metaclass_creator(class_name: str, parents: list[type], attrs: list[Any]):
        return "Simple metaclass"

    class MyClass(metaclass=metaclass_creator):
        pass

    print(MyClass)
    print(type(MyClass))
#

def create_class_type():
    print("create_class_type:")
    class MyMeta(type):
        def __new__(cls, cls_name, parents, attrs):
            print("my_meta: вызвали метод __new__")
            return super().__new__(cls, cls_name, parents, attrs)

        def __call__(self, *args, **kwargs):
            """Метод самого объекта класса, а не экземпляра класса"""

            print("my_meta: вызвали метод __call__")
            return super().__call__(*args, **kwargs)


    class MyClass(metaclass=MyMeta):
        pass

    inst = MyClass()


def create_singleton_class():
    print("create_singleton_class:")
    class SingletonMeta(type):
        _instances = {}
    
        def __call__(cls, *args, **kwargs):
            if cls not in cls._instances:
                cls._instances[cls] = super().__call__(*args, **kwargs)
            return cls._instances[cls]


    class MySingleton(metaclass=SingletonMeta):
        pass

    singleton1 = MySingleton()
    singleton2 = MySingleton()

    assert id(singleton1) == id(singleton2)


if __name__ == "__main__":
    create_class_with_type()
    create_metaclass()
    create_class_type()
    create_singleton_class()
