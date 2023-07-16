# Singleton

## Task Link
[Rosetta Code - Singleton](https://rosettacode.org/wiki/Singleton)

## Java Code
### java_code_1.txt
```java
class Singleton
{
    private static Singleton myInstance;
    public static Singleton getInstance()
    {
        if (myInstance == null)
        {
            synchronized(Singleton.class)
            {
                if (myInstance == null)
                {
                    myInstance = new Singleton();
                }
            }
        }

        return myInstance;
    }

    protected Singleton()
    {
        // Constructor code goes here.
    }

    // Any other methods
}

```

### java_code_2.txt
```java
public class Singleton {
    private Singleton() {
        // Constructor code goes here.
    }

    private static class LazyHolder {
        private static final Singleton INSTANCE = new Singleton();
    }

    public static Singleton getInstance() {
        return LazyHolder.INSTANCE;
    }
}

```

### java_code_3.txt
```java
class Singleton
{
    private static Singleton myInstance;
    public static Singleton getInstance()
    {
        if (myInstance == null)
        {
            myInstance = new Singleton();
        }

        return myInstance;
    }

    protected Singleton()
    {
        // Constructor code goes here.
    }

    // Any other methods
}

```

## Python Code
### python_code_1.txt
```python
>>> class Borg(object):
	__state = {}
	def __init__(self):
		self.__dict__ = self.__state
	# Any other class names/methods

	
>>> b1 = Borg()
>>> b2 = Borg()
>>> b1 is b2
False
>>> b1.datum = range(5)
>>> b1.datum
[0, 1, 2, 3, 4]
>>> b2.datum
[0, 1, 2, 3, 4]
>>> b1.datum is b2.datum
True
>>> # For any datum!

```

### python_code_2.txt
```python
import abc

class Singleton(object):
    """
    Singleton class implementation
    """
    __metaclass__ = abc.ABCMeta
    
    state = 1 #class attribute to be used as the singleton's attribute
    
    @abc.abstractmethod
    def __init__(self):
        pass #this prevents instantiation!
    
    @classmethod
    def printSelf(cls):
        print cls.state #prints out the value of the singleton's state

#demonstration
if __name__ == "__main__":
    try:
        a = Singleton() #instantiation will fail!
    except TypeError as err:
        print err
    Singleton.printSelf()
    print Singleton.state
    Singleton.state = 2
    Singleton.printSelf()
    print Singleton.state

```

### python_code_3.txt
```python
class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Logger(object):
    __metaclass__ = Singleton

```

### python_code_4.txt
```python
class Logger(metaclass=Singleton):
    pass

```

