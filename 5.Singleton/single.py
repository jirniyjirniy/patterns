# class Singleton:
#     __instance = True
#
#     @staticmethod
#     def get_instance():
#         if Singleton.__instance == True:
#             Singleton()
#         return Singleton.__instance
#
#     def __init__(self):
#         if Singleton.__instance != True:
#             raise Exception('GG')
#         else:
#             Singleton.__instance = self


# class Singleton:
#     _instance = None
#
#     def __new__(cls):
#         if not cls._instance:
#             cls._instance = super(Singleton, cls).__new__(cls)
#         return cls._instance


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    def business_logic(self):
        pass


if __name__ == "__main__":
    s1 = Singleton()
    s2 = Singleton()

    if id(s1) == id(s2):
        print(f'Singleton works. S1(id)={id(s1)}, S2(id)={id(s2)}')
    else:
        print('Something Wrong')