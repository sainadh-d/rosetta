# Classes

## Task Link
[Rosetta Code - Classes](https://rosettacode.org/wiki/Classes)

## Java Code
### java_code_1.txt
```java
public class MyClass{

  // instance variable
  private int variable;  // Note: instance variables are usually "private"

  /**
  * The constructor
  */
  public MyClass(){
    // creates a new instance
  }

  /**
  * A method
  */
  public void someMethod(){
   this.variable = 1;
  }
}

```

### java_code_2.txt
```java
new MyClass();

```

### java_code_3.txt
```java
class ProgrammingLanguage
{
   // instance variable:
   private String name;
   // constructor (let's use it to give the instance variable a value):
   public ProgrammingLanguage(String name)
   {
      this.name = name;
      // note use of "this" to distinguish the instance variable from the argument
   }
   // a method:
   public void sayHello()
   {
      println("Hello from the programming language " + name);
      // the method has no argument or local variable called "name", so we can omit the "this"
   }
}

```

### java_code_4.txt
```java
// instantiate the class:
ProgrammingLanguage processing = new ProgrammingLanguage("Processing");

// call the method:
processing.sayHello();

```

## Python Code
### python_code_1.txt
```python
class MyClass:
    name2 = 2 # Class attribute

    def __init__(self):
        """
        Constructor  (Technically an initializer rather than a true "constructor")
        """
        self.name1 = 0 # Instance attribute
  
    def someMethod(self):
        """
        Method
        """
        self.name1 = 1
        MyClass.name2 = 3
  
  
myclass = MyClass() # class name, invoked as a function is the constructor syntax.

class MyOtherClass:
    count = 0  # Population of "MyOtherClass" objects
    def __init__(self, name, gender="Male", age=None):
        """
        One initializer required, others are optional (with different defaults)
        """
        MyOtherClass.count += 1
        self.name = name
        self.gender = gender
        if age is not None:
            self.age = age
    def __del__(self):
        MyOtherClass.count -= 1

person1 = MyOtherClass("John")
print person1.name, person1.gender  # "John Male"
print person1.age                   # Raises AttributeError exception!
person2 = MyOtherClass("Jane", "Female", 23)
print person2.name, person2.gender, person2.age  # "Jane Female 23"

```

### python_code_2.txt
```python
class MyClass(object):
    ...

```

