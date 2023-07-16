# Abstract type

## Task Link
[Rosetta Code - Abstract type](https://rosettacode.org/wiki/Abstract_type)

## Java Code
### java_code_1.txt
```java
interface Example {
    String stringA = "rosetta";
    String stringB = "code";

    private String methodA() {
        return stringA + " " + stringB;
    }

    default int methodB(int value) {
        return value + 100;
    }

    int methodC(int valueA, int valueB);
}

```

### java_code_2.txt
```java
class ExampleImpl implements Example {
    public int methodB(int value) {
        return value + 200;
    }

    public int methodC(int valueA, int valueB) {
        return valueA + valueB;
    }
}

```

### java_code_3.txt
```java
abstract class Example {
    String stringA = "rosetta";
    String stringB = "code";

    private String methodA() {
        return stringA + " " + stringB;
    }

    protected int methodB(int value) {
        return value + 100;
    }

    public abstract int methodC(int valueA, int valueB);
}

```

### java_code_4.txt
```java
class ExampleImpl extends Example {
    public int methodC(int valueA, int valueB) {
        return valueA + valueB;
    }
}

```

## Python Code
### python_code_1.txt
```python
class BaseQueue(object):
    """Abstract/Virtual Class 
    """
    def __init__(self):
        self.contents = list()
        raise NotImplementedError
    def Enqueue(self, item):
        raise NotImplementedError
    def Dequeue(self):
        raise NotImplementedError
    def Print_Contents(self):
        for i in self.contents:
            print i,

```

### python_code_2.txt
```python
from abc import ABCMeta, abstractmethod

class BaseQueue():
    """Abstract Class 
    """
    __metaclass__ = ABCMeta

    def __init__(self):
        self.contents = list()

    @abstractmethod
    def Enqueue(self, item):
        pass

    @abstractmethod
    def Dequeue(self):
        pass

    def Print_Contents(self):
        for i in self.contents:
            print i,

```

