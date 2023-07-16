# Call a function

## Task Link
[Rosetta Code - Call a function](https://rosettacode.org/wiki/Call_a_function)

## Java Code
### java_code_1.txt
```java
foo();             // <-- this is "invoking a function in statement context"
Int x = bar();     // <-- this is "invoking a function in expression context"

```

### java_code_10.txt
```java
Object.methodName();

```

### java_code_11.txt
```java
Object.methodName("rosetta", "code");

```

### java_code_12.txt
```java
interface Example {
    int add(int valueA, int valueB);
}

```

### java_code_13.txt
```java
int sum(Example example) {
    return example.add(1, 2);
}

```

### java_code_14.txt
```java
Example example = (valueA, valueB) -> valueA + valueB;
sum(example);

```

### java_code_15.txt
```java
String string = Object.methodName("rosetta", "code");

```

### java_code_16.txt
```java
String methodA();
void methodB();

```

### java_code_17.txt
```java
<X, Y, Z> Function<Y, Z> exampleA(BiFunction<X, Y, Z> exampleB, X value) {
    return y -> exampleB.apply(value, y);
}

```

### java_code_18.txt
```java
myMethod()

```

### java_code_19.txt
```java
myMethod(97, 3.14)

```

### java_code_2.txt
```java
foo(1, 2, 3);
Int x = bar(4, 5, 6);

```

### java_code_20.txt
```java
int myMethod(int a, double b){
    // return result of doing sums with a and b
}

int myMethod(int a){
    return f(a, 1.414);
}

```

### java_code_21.txt
```java
System.out.println( myMethod( 97, 3.14 ) );
System.out.println( myMethod( 97 ) );

```

### java_code_22.txt
```java
void printAll(String... strings){
    for ( String s : strings )
        System.out.println( s );
}

```

### java_code_23.txt
```java
printAll( "Freeman" );
printAll( "Freeman", "Hardy", "Willis" );

```

### java_code_24.txt
```java
int myMethod( Map<String,Object> params ){
    return
       ((Integer)params.get("x")).intValue()
       + ((Integer)params.get("y")).intValue();
}

```

### java_code_25.txt
```java
System.out.println( myMethod(new HashMap<String,Object>(){{put("x",27);put("y",52);}}) );

```

### java_code_26.txt
```java
int i = myMethod(x);

```

### java_code_27.txt
```java
myMethod(List<String> list){
    // If I change the contents of the list here, the caller will see the change
}

```

## Python Code
### python_code_1.txt
```python
def no_args():
    pass
# call
no_args()

def fixed_args(x, y):
    print('x=%r, y=%r' % (x, y))
# call
fixed_args(1, 2)        # x=1, y=2

## Can also called them using the parameter names, in either order:
fixed_args(y=2, x=1)

## Can also "apply" fixed_args() to a sequence:
myargs=(1,2) # tuple
fixed_args(*myargs)

def opt_args(x=1):
    print(x)
# calls
opt_args()              # 1
opt_args(3.141)         # 3.141

def var_args(*v):
    print(v)
# calls	
var_args(1, 2, 3)       # (1, 2, 3)
var_args(1, (2,3))      # (1, (2, 3))
var_args()              # ()

## Named arguments
fixed_args(y=2, x=1)    # x=1, y=2

## As a statement
if 1:
    no_args()

## First-class within an expression
assert no_args() is None

def return_something():
    return 1
x = return_something()

def is_builtin(x):
	print(x.__name__ in dir(__builtins__))
# calls
is_builtin(pow)         # True
is_builtin(is_builtin)  # False

# Very liberal function definition

def takes_anything(*args, **kwargs):
    for each in args:
        print(each)
    for key, value in sorted(kwargs.items()):
        print("%s:%s" % (key, value))
    # Passing those to another, wrapped, function:
    wrapped_fn(*args, **kwargs)
    # (Function being wrapped can have any parameter list
    # ... that doesn't have to match this prototype)

## A subroutine is merely a function that has no explicit
## return statement and will return None.

## Python uses "Call by Object Reference".
## See, for example, http://www.python-course.eu/passing_arguments.php

## For partial function application see:
##   http://rosettacode.org/wiki/Partial_function_application#Python

```

