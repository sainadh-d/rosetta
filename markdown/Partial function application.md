# Partial function application

## Task Link
[Rosetta Code - Partial function application](https://rosettacode.org/wiki/Partial_function_application)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class PartialApplication {
	interface IntegerFunction {
		int call(int arg);
	}

	// Original method fs(f, s).
	static int[] fs(IntegerFunction f, int[] s) {
		int[] r = new int[s.length];
		for (int i = 0; i < s.length; i++)
			r[i] = f.call(s[i]);
		return r;		
	}

	interface SequenceFunction {
		int[] call(int[] arg);
	}

	// Curried method fs(f).call(s),
	// necessary for partial application.
	static SequenceFunction fs(final IntegerFunction f) {
		return new SequenceFunction() {
			public int[] call(int[] s) {
				// Call original method.
				return fs(f, s);
			}
		};
	}

	static IntegerFunction f1 = new IntegerFunction() {
		public int call(int i) {
			return i * 2;
		}
	};

	static IntegerFunction f2 = new IntegerFunction() {
		public int call(int i) {
			return i * i;
		}
	};

	static SequenceFunction fsf1 = fs(f1); // Partial application.

	static SequenceFunction fsf2 = fs(f2);

	public static void main(String[] args) {
		int[][] sequences = {
			{ 0, 1, 2, 3 },
			{ 2, 4, 6, 8 },
		};

		for (int[] array : sequences) {
			System.out.printf(
			    "array: %s\n" +
			    "  fsf1(array): %s\n" +
			    "  fsf2(array): %s\n",
			    Arrays.toString(array),
			    Arrays.toString(fsf1.call(array)),
			    Arrays.toString(fsf2.call(array)));
		}
	}
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.IntUnaryOperator;
import java.util.function.UnaryOperator;
import java.util.stream.Stream;

@FunctionalInterface
public interface PartialApplication<INPUT1, INPUT2, OUTPUT> extends BiFunction<INPUT1, INPUT2, OUTPUT> {
  // Original method fs(f, s).
  public static int[] fs(IntUnaryOperator f, int[] s) {
    return Arrays.stream(s)
      .parallel()
      .map(f::applyAsInt)
      .toArray()
    ;
  }

  // Currying method f.apply(a).apply(b),
  // in lieu of f.apply(a, b),
  // necessary for partial application.
  public default Function<INPUT2, OUTPUT> apply(INPUT1 input1) {
    return input2 -> apply(input1, input2);
  }

  // Original method fs turned into a partially-applicable function.
  public static final PartialApplication<IntUnaryOperator, int[], int[]> fs = PartialApplication::fs;

  public static final IntUnaryOperator f1 = i -> i + i;

  public static final IntUnaryOperator f2 = i -> i * i;

  public static final UnaryOperator<int[]> fsf1 = fs.apply(f1)::apply; // Partial application.

  public static final UnaryOperator<int[]> fsf2 = fs.apply(f2)::apply;

  public static void main(String... args) {
    int[][] sequences = {
      {0, 1, 2, 3},
      {2, 4, 6, 8},
    };

    Arrays.stream(sequences)
      .parallel()
      .map(array ->
        Stream.of(
          array,
          fsf1.apply(array),
          fsf2.apply(array)
        )
          .parallel()
          .map(Arrays::toString)
          .toArray()
      )
      .map(array ->
        String.format(
          String.join("\n",
            "array: %s",
            "  fsf1(array): %s",
            "  fsf2(array): %s"
          ),
          array
        )
      )
      .forEachOrdered(System.out::println)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
from functools import partial

def fs(f, s): return [f(value) for value in s]

def f1(value): return value * 2

def f2(value): return value ** 2

fsf1 = partial(fs, f1)
fsf2 = partial(fs, f2)

s = [0, 1, 2, 3]
assert fs(f1, s) == fsf1(s) # ==  [0, 2, 4, 6]
assert fs(f2, s) == fsf2(s) # ==  [0, 1, 4, 9]

s = [2, 4, 6, 8]
assert fs(f1, s) == fsf1(s) # ==  [4, 8, 12, 16]
assert fs(f2, s) == fsf2(s) # ==  [4, 16, 36, 64]

```

### python_code_2.txt
```python
def partial(f, g):
	def fg(*x): return f(g, *x)
	return fg

def fs(f, *x): return [ f(a) for a in x]
def f1(a): return a * 2
def f2(a): return a * a

fsf1 = partial(fs, f1)
fsf2 = partial(fs, f2)

print fsf1(1, 2, 3, 4)
print fsf2(1, 2, 3, 4)

```

