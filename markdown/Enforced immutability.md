# Enforced immutability

## Task Link
[Rosetta Code - Enforced immutability](https://rosettacode.org/wiki/Enforced_immutability)

## Java Code
### java_code_1.txt
```java
final int immutableInt = 4;
int mutableInt = 4;
mutableInt = 6; //this is fine
immutableInt = 6; //this is an error

```

### java_code_2.txt
```java
final String immutableString = "test";
immutableString = new String("anotherTest"); //this is an error
final StringBuffer immutableBuffer = new StringBuffer();
immutableBuffer.append("a"); //this is fine and it changes the state of the object
immutableBuffer = new StringBuffer("a"); //this is an error

```

### java_code_3.txt
```java
public class Immute{
    private final int num;
    private final String word;
    private final StringBuffer buff; //still mutable inside this class, but there is no access outside this class

    public Immute(int num){
        this.num = num;
        word = num + "";
        buff = new StringBuffer("test" + word);
    }

    public int getNum(){
        return num;
    }

    public String getWord(){
        return word; //String objects are immutable so passing the object back directly won't harm anything
    }

    public StringBuffer getBuff(){
        return new StringBuffer(buff);
        //using "return buff" here compromises immutability, but copying the object via the constructor makes it ok
    }
    //no "set" methods are given
}

```

## Python Code
### python_code_1.txt
```python
>>> s = "Hello"
>>> s[0] = "h"

Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    s[0] = "h"
TypeError: 'str' object does not support item assignment

```

### python_code_2.txt
```python
>>> class Immut(object):
	def __setattr__(self, *args):
		raise TypeError(
			"'Immut' object does not support item assignment")
	
        __delattr__ = __setattr__
	
        def __repr__(self):
		return str(self.value)
	
        def __init__(self, value):
                # assign to the un-assignable the hard way.
		super(Immut, self).__setattr__("value", value)

>>> im = Immut(123)
>>> im
123
>>> im.value = 124

Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    del a.value
  File "<pyshell#23>", line 4, in __setattr__
    "'Immut' object does not support item assignment")
TypeError: 'Immut' object does not support item assignment
>>>

```

