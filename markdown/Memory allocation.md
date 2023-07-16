# Memory allocation

## Task Link
[Rosetta Code - Memory allocation](https://rosettacode.org/wiki/Memory_allocation)

## Java Code
### java_code_1.txt
```java
//All of these objects will be deallocated automatically once the program leaves
//their scope and there are no more pointers to the objects
Object foo = new Object(); //Allocate an Object and a reference to it
int[] fooArray = new int[size]; //Allocate all spaces in an array and a reference to it
int x = 0; //Allocate an integer and set its value to 0

```

### java_code_2.txt
```java
public class Blah{
   //...other methods/data members...
   protected void finalize() throws Throwable{
      //Finalization code here
   }
   //...other methods/data members...
}

```

### java_code_3.txt
```java
public class NoFinalize {
    public static final void main(String[] params) {
        NoFinalize nf = new NoFinalize();
    }
    public NoFinalize() {
        System.out.println("created");
    }
    @Override
    protected void finalize() {
        System.out.println("finalized");
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from array import array
>>> argslist = [('l', []), ('c', 'hello world'), ('u', u'hello \u2641'),
	('l', [1, 2, 3, 4, 5]), ('d', [1.0, 2.0, 3.14])]
>>> for typecode, initializer in argslist:
	a = array(typecode, initializer)
	print a
	del a

	
array('l')
array('c', 'hello world')
array('u', u'hello \u2641')
array('l', [1, 2, 3, 4, 5])
array('d', [1.0, 2.0, 3.1400000000000001])
>>>

```

