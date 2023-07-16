# First-class functions

## Task Link
[Rosetta Code - First-class functions](https://rosettacode.org/wiki/First-class_functions)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;

public class FirstClass{
	
	public interface Function<A,B>{
		B apply(A x);
	}
	
	public static <A,B,C> Function<A, C> compose(
			final Function<B, C> f, final Function<A, B> g) {
		return new Function<A, C>() {
			@Override public C apply(A x) {
				return f.apply(g.apply(x));
			}
		};
	}
	 
	public static void main(String[] args){
		ArrayList<Function<Double, Double>> functions =
			new ArrayList<Function<Double,Double>>();
		
		functions.add(
				new Function<Double, Double>(){
					@Override public Double apply(Double x){
						return Math.cos(x);
					}
				});
		functions.add(
				new Function<Double, Double>(){
					@Override public Double apply(Double x){
						return Math.tan(x);
					}
				});
		functions.add(
				new Function<Double, Double>(){
					@Override public Double apply(Double x){
						return x * x;
					}
				});
		
		ArrayList<Function<Double, Double>> inverse = new ArrayList<Function<Double,Double>>();
		
		inverse.add(
				new Function<Double, Double>(){
					@Override public Double apply(Double x){
						return Math.acos(x);
					}
				});
		inverse.add(
				new Function<Double, Double>(){
					@Override public Double apply(Double x){
						return Math.atan(x);
					}
				});
		inverse.add(
				new Function<Double, Double>(){
					@Override public Double apply(Double x){
						return Math.sqrt(x);
					}
				});
		System.out.println("Compositions:");
		for(int i = 0; i < functions.size(); i++){
			System.out.println(compose(functions.get(i), inverse.get(i)).apply(0.5));
		}
		System.out.println("Hard-coded compositions:");
		System.out.println(Math.cos(Math.acos(0.5)));
		System.out.println(Math.tan(Math.atan(0.5)));
		System.out.println(Math.pow(Math.sqrt(0.5), 2));
	}
}

```

### java_code_2.txt
```java
import java.util.ArrayList;
import java.util.function.Function;

public class FirstClass{
	
	public static void main(String... arguments){
		ArrayList<Function<Double, Double>> functions = new ArrayList<>();
		
		functions.add(Math::cos);
		functions.add(Math::tan);
		functions.add(x -> x * x);
		
		ArrayList<Function<Double, Double>> inverse = new ArrayList<>();
		
		inverse.add(Math::acos);
		inverse.add(Math::atan);
		inverse.add(Math::sqrt);
		System.out.println("Compositions:");
		for (int i = 0; i < functions.size(); i++){
			System.out.println(functions.get(i).compose(inverse.get(i)).apply(0.5));
		}
		System.out.println("Hard-coded compositions:");
		System.out.println(Math.cos(Math.acos(0.5)));
		System.out.println(Math.tan(Math.atan(0.5)));
		System.out.println(Math.pow(Math.sqrt(0.5), 2));
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> # Some built in functions and their inverses
>>> from math import sin, cos, acos, asin
>>> # Add a user defined function and its inverse
>>> cube = lambda x: x * x * x
>>> croot = lambda x: x ** (1/3.0)
>>> # First class functions allow run-time creation of functions from functions
>>> # return function compose(f,g)(x) == f(g(x))
>>> compose = lambda f1, f2: ( lambda x: f1(f2(x)) )
>>> # first class functions should be able to be members of collection types
>>> funclist = [sin, cos, cube]
>>> funclisti = [asin, acos, croot]
>>> # Apply functions from lists as easily as integers
>>> [compose(inversef, f)(.5) for f, inversef in zip(funclist, funclisti)]
[0.5, 0.4999999999999999, 0.5]
>>>

```

### python_code_2.txt
```python
'''First-class functions'''

from math import (acos, cos, asin, sin)
from inspect import signature


# main :: IO ()
def main():
    '''Composition of several functions.'''

    pwr = flip(curry(pow))

    fs = [sin, cos, pwr(3.0)]
    ifs = [asin, acos, pwr(1 / 3.0)]

    print([
        f(0.5) for f in
        zipWith(compose)(fs)(ifs)
    ])


# GENERIC FUNCTIONS ------------------------------


# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# curry :: ((a, b) -> c) -> a -> b -> c
def curry(f):
    '''A curried function derived
       from an uncurried function.'''
    return lambda a: lambda b: f(a, b)


# flip :: (a -> b -> c) -> b -> a -> c
def flip(f):
    '''The (curried or uncurried) function f with its
       two arguments reversed.'''
    if 1 < len(signature(f).parameters):
        return lambda a, b: f(b, a)
    else:
        return lambda a: lambda b: f(b)(a)


# zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
def zipWith(f):
    '''A list constructed by zipping with a
       custom function, rather than with the
       default tuple constructor.'''
    return lambda xs: lambda ys: [
        f(a)(b) for (a, b) in zip(xs, ys)
    ]


if __name__ == '__main__':
    main()

```

