class Singleton(object):
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance
    
    def __init__(self):
        self.val = 0
    
    def add(self, a: int):
        self.val += a
        print(self.val)

if __name__ == "__main__":
    singleton = Singleton()
new_singleton = Singleton()

print(singleton is new_singleton)

singleton.singl_variable = "Singleton Variable"
print(new_singleton.singl_variable)

print(singleton.val)
singleton.add(3)
print(new_singleton.val)