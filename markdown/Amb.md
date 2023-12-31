# Amb

## Task Link
[Rosetta Code - Amb](https://rosettacode.org/wiki/Amb)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;
import java.util.function.BiFunction;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public final class AmbTask {

	public static void main(String[] aArgs) {
		List<List<String>> words = List.of(
			List.of( "the", "that", "a" ),
		    List.of( "frog", "elephant", "thing" ),
		    List.of( "walked", "treaded", "grows" ),
		    List.of( "slowly", "quickly" ) );		

		System.out.println(Amb(words));		
	}
	
	private static String Amb(List<List<String>> aOptions) {
		BiFunction<String, String, Boolean> continues = (before, after) -> before.endsWith(after.substring(0, 1));		
		List<String> ambResult = amb(continues, aOptions, "");
		return ( ambResult.isEmpty() ) ? "No match found" : String.join(" ", ambResult);		
	}
	
	private static List<String> amb(
			BiFunction<String, String, Boolean> aBiFunction, List<List<String>> aOptions, String aPrevious) {
		
		if ( aOptions.isEmpty() ) {
			return new ArrayList<String>();
		}

		for ( String option : aOptions.get(0) ) {
		    if ( ! aPrevious.isEmpty() && ! aBiFunction.apply(aPrevious, option) ) {
		    	continue;
			}
	
		    if ( aOptions.size() == 1 ) {
		    	return Stream.of(option).collect(Collectors.toList());
		    }
	
		    List<String> result = (ArrayList<String>) amb(aBiFunction, aOptions.subList(1, aOptions.size()), option);
	
		    if ( ! result.isEmpty() ) {
				result.add(0, option);
				return result;
			}	  
		}
		
		return new ArrayList<String>();
	}
	
}

```

## Python Code
### python_code_1.txt
```python
import itertools as _itertools
 
class Amb(object):
    def __init__(self):
        self._names2values   = {}       # set of values for each global name
        self._func           = None     # Boolean constraint function
        self._valueiterator  = None     # itertools.product of names values
        self._funcargnames   = None     # Constraint parameter names
 
    def __call__(self, arg=None):
        if hasattr(arg, '__code__'):                
            ##
            ## Called with a constraint function. 
            ##
            globls = arg.__globals__ if hasattr(arg, '__globals__') else arg.func_globals
            # Names used in constraint
            argv = arg.__code__.co_varnames[:arg.__code__.co_argcount]
            for name in argv:
                if name not in self._names2values:
                    assert name in globls, \
                           "Global name %s not found in function globals" % name
                    self._names2values[name] = globls[name]
            # Gather the range of values of all names used in the constraint
            valuesets = [self._names2values[name] for name in argv]
            self._valueiterator = _itertools.product(*valuesets)
            self._func = arg
            self._funcargnames = argv
            return self
        elif arg is not None:
            ##
            ## Assume called with an iterable set of values
            ##
            arg = frozenset(arg)
            return arg
        else:
            ##
            ## blank call tries to return next solution
            ##
            return self._nextinsearch()
 
    def _nextinsearch(self):
        arg = self._func
        globls = arg.__globals__
        argv = self._funcargnames
        found = False
        for values in self._valueiterator:
            if arg(*values):
                # Set globals.
                found = True
                for n, v in zip(argv, values):
                    globls[n] = v
                break
        if not found: raise StopIteration
        return values
 
    def __iter__(self):
        return self
 
    def __next__(self):
        return self()
    next = __next__ # Python 2
 
if __name__ == '__main__':
    if True:
        amb = Amb()
 
        print("\nSmall Pythagorean triples problem:")
        x = amb(range(1,11))
        y = amb(range(1,11))
        z = amb(range(1,11))
 
        for _dummy in amb( lambda x, y, z: x*x + y*y == z*z ):
            print ('%s %s %s' % (x, y, z))
 
 
    if True:
        amb = Amb()
 
        print("\nRosetta Code Amb problem:")
        w1 = amb(["the", "that", "a"])
        w2 = amb(["frog", "elephant", "thing"])
        w3 = amb(["walked", "treaded", "grows"])
        w4 = amb(["slowly", "quickly"])
 
        for _dummy in amb( lambda w1, w2, w3, w4: \
                             w1[-1] == w2[0] and \
                             w2[-1] == w3[0] and \
                             w3[-1] == w4[0] ):
            print ('%s %s %s %s' % (w1, w2, w3, w4))
 
    if True:
        amb = Amb()
 
        print("\nAmb problem from "
            "http://www.randomhacks.net/articles/2005/10/11/amb-operator:")
        x = amb([1, 2, 3])
        y = amb([4, 5, 6])
 
        for _dummy in amb( lambda x, y: x * y != 8 ):
            print ('%s %s' % (x, y))

```

### python_code_2.txt
```python
# joins :: String -> String -> Bool
def joins(a, b):
    return a[-1] == b[0]


print (
    [
        ' '.join([w1, w2, w3, w4])
        for w1 in ['the', 'that', 'a']
        for w2 in ['frog', 'elephant', 'thing']
        for w3 in ['walked', 'treaded', 'grows']
        for w4 in ['slowly', 'quickly']
        if joins(w1, w2) and joins(w2, w3) and joins(w3, w4)
    ]
)

```

### python_code_3.txt
```python
def main():
    print (
        unlines([
            unwords([w1, w2, w3, w4])

            for w1 in ['the', 'that', 'a']
            if True

            for w2 in ['frog', 'elephant', 'thing']
            if joins(w1, w2)

            for w3 in ['walked', 'treaded', 'grows']
            if joins(w2, w3)

            for w4 in ['slowly', 'quickly']
            if joins(w3, w4)
        ])
    )


# joins :: String -> String -> Bool
def joins(a, b):
    return a[-1] == b[0]


# unlines :: [String] -> String
def unlines(xs):
    return '\n'.join(xs)


# unwords :: [String] -> String
def unwords(xs):
    return ' '.join(xs)


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
from itertools import chain


# amb :: [a] -> (a -> [b]) -> [b]
def amb(xs):
    return lambda f: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# main :: IO ()
def main():

    xs = enumFromTo(1)(10)
    print ('Pythagorean triples from integers 1-10:')
    print (
        amb(xs)(
            lambda x: amb(xs)
            (lambda y: amb(xs)
                (lambda z: when(
                    x * x + y * y == z * z
                )(
                    (x, y, z)
                )
            ))
        )
    )

    # joins :: String -> String -> Bool
    def joins(a, b):
        return a[-1] == b[0]

    print ('\nRC problem given above:')
    print (
        amb(['the', 'that', 'a'])(
            lambda w1: amb(
                ['frog', 'elephant', 'thing']
            )(lambda w2: amb(
                ['walked', 'treaded', 'grows']
            )(lambda w3: amb(
                ['slowly', 'quickly']
            )(lambda w4: when(
                joins(w1, w2) and joins(w2, w3) and joins(w3, w4)
            )(
                (w1, w2, w3, w4)
            ))))
        )
    )
    print('\nAdditional problem reference in procedural version above:')
    print(
        amb([1, 2, 3])
        (
            lambda x: amb([4, 5, 6])
            (
                lambda y: when(x * y != 8)
                (
                    (x, y)
                )
            )
        )
    )

# GENERIC -------------------------------------------------


# enumFromTo :: (Int, Int) -> [Int]
def enumFromTo(m):
    return lambda n: list(range(m, 1 + n))


# when :: Bool -> [a] -> [a]
def when(p):
    return lambda x: [x] if p else []

# MAIN ---
if __name__ == '__main__':
    main()

```

### python_code_5.txt
```python
from itertools import chain


# amb :: [a] -> (a -> [b]) -> [b]
def amb(xs):
    return lambda f: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# when :: Bool -> [a] -> [a]
def when(p):
    return lambda xs: xs if p else []


# TEST ----------------------------------------------------

# joins :: String -> String -> Bool
def joins(a, b):
    return a[-1] == b[0]


print (
    amb(['the', 'that', 'a'])(
        lambda w1: when(True)

        (amb(['frog', 'elephant', 'thing'])
         (lambda w2: when(joins(w1, w2))

          (amb(['walked', 'treaded', 'grows'])
           (lambda w3: when(joins(w2, w3))

            (amb(['slowly', 'quickly'])
             (lambda w4: when(joins(w3, w4))(

                 [w1, w2, w3, w4]
             ))))))
         )
    )
)

```

