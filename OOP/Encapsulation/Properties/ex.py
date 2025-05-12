class Foo:
    def __init__(self, x=None) -> None:
        self._x = x
        
        
    @property
    def x(self) -> int:
        return self._x or 0
    
    @x.setter
    def x(self, value: int) -> None:
        _x = self._x or 0
        _value = value or 0
        self._x += _value
        
    @x.deleter
    def x(self):
        self._x = -1
        

foo = Foo(10)
print(foo.x) #? OUTPUT: 10

foo.x = 10
print(foo.x) #? OUTPUT: 20

del foo.x
print(foo.x) #? OUTPUT: -1