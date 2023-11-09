class Singleton:
    __instance = True

    @staticmethod
    def getInstance():
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
    obj = Singleton.getInstance()
    print(obj)