class App:
    received = []
    turn = ""
    prev_turn = ""
    def __init__(self, turn):
        self.turn = turn
    
    def addMessage(self, message):
        self.received.append(message)

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class MyClass(App, metaclass=Singleton):
    pass
