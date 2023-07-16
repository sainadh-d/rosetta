# Call an object method

## Task Link
[Rosetta Code - Call an object method](https://rosettacode.org/wiki/Call_an_object_method)

## Java Code
### java_code_1.txt
```java
// Static
MyClass.method(someParameter);

// Instance
myInstance.method(someParameter);

```

### java_code_3.txt
```java
ClassWithStaticMethod.staticMethodName(argument1, argument2);//for methods with no arguments, use empty parentheses

```

### java_code_4.txt
```java
ClassWithMethod varName = new ClassWithMethod();
varName.methodName(argument1, argument2);
//or
new ClassWithMethod().methodName(argument1, argument2);

```

## Python Code
### python_code_1.txt
```python
class MyClass(object):
	@classmethod
	def myClassMethod(self, x):
		pass
	@staticmethod
	def myStaticMethod(x):
		pass
	def myMethod(self, x):
		return 42 + x

myInstance = MyClass()

# Instance method
myInstance.myMethod(someParameter)
# A method can also be retrieved as an attribute from the class, and then explicitly called on an instance:
MyClass.myMethod(myInstance, someParameter)


# Class or static methods
MyClass.myClassMethod(someParameter)
MyClass.myStaticMethod(someParameter)
# You can also call class or static methods on an instance, which will simply call it on the instance's class
myInstance.myClassMethod(someParameter)
myInstance.myStaticMethod(someParameter)

```

