# Polymorphic copy

## Task Link
[Rosetta Code - Polymorphic copy](https://rosettacode.org/wiki/Polymorphic_copy)

## Java Code
### java_code_1.txt
```java
class T implements Cloneable {
    public String name() { return "T"; }
    public T copy() {
        try {
            return (T)super.clone();
        } catch (CloneNotSupportedException e) {
            return null;
        }
    }
}

class S extends T {
    public String name() { return "S"; }
}

public class PolymorphicCopy {
    public static T copier(T x) { return x.copy(); }
    public static void main(String[] args) {
        T obj1 = new T();
        S obj2 = new S();
        System.out.println(copier(obj1).name()); // prints "T"
        System.out.println(copier(obj2).name()); // prints "S"
    }
}

```

## Python Code
### python_code_1.txt
```python
import copy

class T:
   def classname(self): 
      return self.__class__.__name__

   def __init__(self):
      self.myValue = "I'm a T."

   def speak(self):
      print self.classname(), 'Hello', self.myValue

   def clone(self):
      return copy.copy(self)

class S1(T):
   def speak(self):
      print self.classname(),"Meow", self.myValue

class S2(T):
   def speak(self):
      print self.classname(),"Woof", self.myValue


print "creating initial objects of types S1, S2, and T"
a = S1()
a.myValue = 'Green'
a.speak()

b = S2()
b.myValue = 'Blue'
b.speak()

u = T()
u.myValue = 'Purple'
u.speak()

print "Making copy of a as u, colors and types should match"
u = a.clone()
u.speak()
a.speak()
print "Assigning new color to u, A's color should be unchanged."
u.myValue = "Orange"
u.speak()
a.speak()

print "Assigning u to reference same object as b, colors and types should match"
u = b
u.speak()
b.speak()
print "Assigning new color to u. Since u,b references same object b's color changes as well"
u.myValue = "Yellow"
u.speak()
b.speak()

```

### python_code_2.txt
```python
import cPickle as pickle

source = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

target = pickle.loads(pickle.dumps(source))

```

### python_code_3.txt
```python
target = source.__class__()  # Create an object of the same type
if hasattr(source, 'items') and callable(source.items):
    for key,value in source.items:
        target[key] = value
elif hasattr(source, '__len__'):
    target = source[:]
else:  # Following is not recommended. (see below).
    target = source

```

