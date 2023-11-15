class Singleton:
    __instance = True

    @staticmethod
    def get_instance():
        if Singleton.__instance == True:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != True:
            raise Exception('GG')
        else:
            Singleton.__instance = self


if __name__ == "__main__":
    obj = Singleton()
    print(obj)
    obj = Singleton.get_instance()
    print(obj)
