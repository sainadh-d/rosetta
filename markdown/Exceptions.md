# Exceptions

## Task Link
[Rosetta Code - Exceptions](https://rosettacode.org/wiki/Exceptions)

## Java Code
### java_code_1.txt
```java
//Checked exception
public class MyException extends Exception {
   //Put specific info in here
}

//Unchecked exception
public class MyRuntimeException extends RuntimeException {}

```

### java_code_2.txt
```java
public void fooChecked() throws MyException {
   throw new MyException();
}

public void fooUnchecked() {
   throw new MyRuntimeException();
}

```

### java_code_3.txt
```java
try {
   fooChecked();
}
catch(MyException exc) {
   //Catch only your specified type of exception
}
catch(Exception exc) {
   //Catch any non-system error exception
}
catch(Throwable exc) {
   //Catch everything including system errors (not recommended)
}
finally {
   //This code is always executed after exiting the try block
}

```

### java_code_4.txt
```java
public void foo() throws UnsupportedDataTypeException{
    try{
        throwsNumberFormatException();
        //the following methods throw exceptions which extend IOException
        throwsUnsupportedDataTypeException();
        throwsFileNotFoundException();
    }catch(FileNotFoundException | NumberFormatException ex){
        //deal with these two Exceptions without duplicating code
    }catch(IOException e){
        //deal with the UnsupportedDataTypeException as well as any other unchecked IOExceptions
        throw e;
    }
}

```

## Python Code
### python_code_1.txt
```python
import exceptions
class SillyError(exceptions.Exception):
    def __init__(self,args=None):
         self.args=args

```

### python_code_2.txt
```python
class MyInvalidArgument(ValueError):
   pass

```

### python_code_3.txt
```python
def spam():
    raise SillyError # equivalent to raise SillyError()

```

### python_code_4.txt
```python
def spam():
    raise SillyError, 'egg' # equivalent to raise SillyError('egg')

```

### python_code_5.txt
```python
def spam():
    raise SillyError('egg')

```

### python_code_6.txt
```python
try:
   foo()
except SillyError, se:
   print se.args
   bar()
else:
   # no exception occurred
   quux()
finally:
   baz()

```

### python_code_7.txt
```python
try:
   foo()
except SillyError as se:
   print(se.args)
   bar()
else:
   # no exception occurred
   quux()
finally:
   baz()

```

