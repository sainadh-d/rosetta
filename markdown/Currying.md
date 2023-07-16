# Currying

## Task Link
[Rosetta Code - Currying](https://rosettacode.org/wiki/Currying)

## Java Code
### java_code_2.txt
```java
    public class Currier<ARG1, ARG2, RET> {
        public interface CurriableFunctor<ARG1, ARG2, RET> {
            RET evaluate(ARG1 arg1, ARG2 arg2);
        }
    
        public interface CurriedFunctor<ARG2, RET> {
            RET evaluate(ARG2 arg);
        }
    
        final CurriableFunctor<ARG1, ARG2, RET> functor;
    
        public Currier(CurriableFunctor<ARG1, ARG2, RET> fn) { functor = fn; }
        
        public CurriedFunctor<ARG2, RET> curry(final ARG1 arg1) {
            return new CurriedFunctor<ARG2, RET>() {
                public RET evaluate(ARG2 arg2) {
                    return functor.evaluate(arg1, arg2);
                }
            };
        }
    
        public static void main(String[] args) {
            Currier.CurriableFunctor<Integer, Integer, Integer> add
                = new Currier.CurriableFunctor<Integer, Integer, Integer>() {
                    public Integer evaluate(Integer arg1, Integer arg2) {
                        return new Integer(arg1.intValue() + arg2.intValue());
                    }
            };
            
            Currier<Integer, Integer, Integer> currier
                = new Currier<Integer, Integer, Integer>(add);
            
            Currier.CurriedFunctor<Integer, Integer> add5
                = currier.curry(new Integer(5));
            
            System.out.println(add5.evaluate(new Integer(2)));
        }
    }

```

### java_code_3.txt
```java
import java.util.function.BiFunction;
import java.util.function.Function;

public class Curry {
	
	//Curry a method
	public static <T, U, R> Function<T, Function<U, R>> curry(BiFunction<T, U, R> biFunction) {
		return t -> u -> biFunction.apply(t, u);
	}
	
	public static int add(int x, int y) {
		return x + y;
	}
	
	public static void curryMethod() {
		BiFunction<Integer, Integer, Integer> bif = Curry::add;
		Function<Integer, Function<Integer, Integer>> add = curry(bif);
		Function<Integer, Integer> add5 = add.apply(5);
		System.out.println(add5.apply(2));
	}

	//Or declare the curried function in one line
	public static void curryDirectly() {
		Function<Integer, Function<Integer, Integer>> add = x -> y -> x + y;
		Function<Integer, Integer> add5 = add.apply(5);
		System.out.println(add5.apply(2));
	}
	
	//prints 7 and 7
	public static void main(String[] args) {
		curryMethod();
		curryDirectly();
	}
}

```

## Python Code
### python_code_1.txt
```python
 def addN(n):
     def adder(x):
         return x + n
     return adder

```

### python_code_2.txt
```python
 >>> add2 = addN(2)
 >>> add2
 <function adder at 0x009F1E30>
 >>> add2(7)
 9

```

### python_code_3.txt
```python
>>> from functools import partial
>>> from operator import add
>>> add2 = partial(add, 2)
>>> add2
functools.partial(<built-in function add>, 2)
>>> add2(7)
9
>>> double = partial(map, lambda x: x*2)
>>> print(*double(range(5)))
0 2 4 6 8

```

### python_code_4.txt
```python
>>> from toolz import curry
>>> import operator
>>> add = curry(operator.add)
>>> add2 = add(2)
>>> add2
<built-in function add>
>>> add2(7)
9
>>> # Toolz also has pre-curried versions of most HOFs from builtins, stdlib, and toolz
>>>from toolz.curried import map
>>> double = map(lambda x: x*2)
>>> print(*double(range(5)))
0 2 4 6 8

```

### python_code_5.txt
```python
# AUTOMATIC CURRYING AND UNCURRYING OF EXISTING FUNCTIONS


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    return lambda a: lambda b: f(a, b)


# uncurry :: (a -> b -> c) -> ((a, b) -> c)
def uncurry(f):
    return lambda x, y: f(x)(y)


# EXAMPLES --------------------------------------

# A plain uncurried function with 2 arguments,

# justifyLeft :: Int -> String -> String
def justifyLeft(n, s):
    return (s + (n * ' '))[:n]


# and a similar, but manually curried, function.

# justifyRight :: Int -> String -> String
def justifyRight(n):
    return lambda s: (
        ((n * ' ') + s)[-n:]
    )


# CURRYING and UNCURRYING at run-time:

def main():
    for s in [
        'Manually curried using a lambda:',
        '\n'.join(map(
            justifyRight(5),
            ['1', '9', '10', '99', '100', '1000']
        )),

        '\nAutomatically uncurried:',
        uncurry(justifyRight)(5, '10000'),

        '\nAutomatically curried',
        '\n'.join(map(
            curry(justifyLeft)(10),
            ['1', '9', '10', '99', '100', '1000']
        ))
    ]:
        print (s)


main()

```

