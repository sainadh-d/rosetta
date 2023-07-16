# Y combinator

## Task Link
[Rosetta Code - Y combinator](https://rosettacode.org/wiki/Y_combinator)

## Java Code
### java_code_1.txt
```java
import java.util.function.Function;

public interface YCombinator {
  interface RecursiveFunction<F> extends Function<RecursiveFunction<F>, F> { }
  public static <A,B> Function<A,B> Y(Function<Function<A,B>, Function<A,B>> f) {
    RecursiveFunction<Function<A,B>> r = w -> f.apply(x -> w.apply(w).apply(x));
    return r.apply(r);
  }

  public static void main(String... arguments) {
    Function<Integer,Integer> fib = Y(f -> n ->
      (n <= 2)
        ? 1
        : (f.apply(n - 1) + f.apply(n - 2))
    );
    Function<Integer,Integer> fac = Y(f -> n ->
      (n <= 1)
        ? 1
        : (n * f.apply(n - 1))
    );

    System.out.println("fib(10) = " + fib.apply(10));
    System.out.println("fac(10) = " + fac.apply(10));
  }
}

```

### java_code_2.txt
```java
    public static <A,B> Function<A,B> Y(Function<Function<A,B>, Function<A,B>> f) {
        return x -> f.apply(Y(f)).apply(x);
    }

```

### java_code_3.txt
```java
    public static <A,B> Function<A,B> Y(Function<Function<A,B>, Function<A,B>> f) {
        return new Function<A,B>() {
	    public B apply(A x) {
		return f.apply(this).apply(x);
	    }
	};
    }

```

### java_code_4.txt
```java
interface Function<A, B> {
    public B call(A x);
}

public class YCombinator {
    interface RecursiveFunc<F> extends Function<RecursiveFunc<F>, F> { }

    public static <A,B> Function<A,B> fix(final Function<Function<A,B>, Function<A,B>> f) {
        RecursiveFunc<Function<A,B>> r =
            new RecursiveFunc<Function<A,B>>() {
            public Function<A,B> call(final RecursiveFunc<Function<A,B>> w) {
                return f.call(new Function<A,B>() {
                        public B call(A x) {
                            return w.call(w).call(x);
                        }
                    });
            }
        };
        return r.call(r);
    }

    public static void main(String[] args) {
        Function<Function<Integer,Integer>, Function<Integer,Integer>> almost_fib =
            new Function<Function<Integer,Integer>, Function<Integer,Integer>>() {
            public Function<Integer,Integer> call(final Function<Integer,Integer> f) {
                return new Function<Integer,Integer>() {
                    public Integer call(Integer n) {
                        if (n <= 2) return 1;
                        return f.call(n - 1) + f.call(n - 2);
                    }
                };
            }
        };

        Function<Function<Integer,Integer>, Function<Integer,Integer>> almost_fac =
            new Function<Function<Integer,Integer>, Function<Integer,Integer>>() {
            public Function<Integer,Integer> call(final Function<Integer,Integer> f) {
                return new Function<Integer,Integer>() {
                    public Integer call(Integer n) {
                        if (n <= 1) return 1;
                        return n * f.call(n - 1);
                    }
                };
            }
        };

        Function<Integer,Integer> fib = fix(almost_fib);
        Function<Integer,Integer> fac = fix(almost_fac);

        System.out.println("fib(10) = " + fib.call(10));
        System.out.println("fac(10) = " + fac.call(10));
    }
}

```

### java_code_5.txt
```java
import java.util.function.Function;

@FunctionalInterface
public interface SelfApplicable<OUTPUT> extends Function<SelfApplicable<OUTPUT>, OUTPUT> {
  public default OUTPUT selfApply() {
    return apply(this);
  }
}

```

### java_code_6.txt
```java
import java.util.function.Function;
import java.util.function.UnaryOperator;

@FunctionalInterface
public interface FixedPoint<FUNCTION> extends Function<UnaryOperator<FUNCTION>, FUNCTION> {}

```

### java_code_7.txt
```java
import java.util.Arrays;
import java.util.Optional;
import java.util.function.Function;
import java.util.function.BiFunction;

@FunctionalInterface
public interface VarargsFunction<INPUTS, OUTPUT> extends Function<INPUTS[], OUTPUT> {
  @SuppressWarnings("unchecked")
  public OUTPUT apply(INPUTS... inputs);

  public static <INPUTS, OUTPUT> VarargsFunction<INPUTS, OUTPUT> from(Function<INPUTS[], OUTPUT> function) {
    return function::apply;
  }

  public static <INPUTS, OUTPUT> VarargsFunction<INPUTS, OUTPUT> upgrade(Function<INPUTS, OUTPUT> function) {
    return inputs -> function.apply(inputs[0]);
  }

  public static <INPUTS, OUTPUT> VarargsFunction<INPUTS, OUTPUT> upgrade(BiFunction<INPUTS, INPUTS, OUTPUT> function) {
    return inputs -> function.apply(inputs[0], inputs[1]);
  }

  @SuppressWarnings("unchecked")
  public default <POST_OUTPUT> VarargsFunction<INPUTS, POST_OUTPUT> andThen(
      VarargsFunction<OUTPUT, POST_OUTPUT> after) {
    return inputs -> after.apply(apply(inputs));
  }

  @SuppressWarnings("unchecked")
  public default Function<INPUTS, OUTPUT> toFunction() {
    return input -> apply(input);
  }

  @SuppressWarnings("unchecked")
  public default BiFunction<INPUTS, INPUTS, OUTPUT> toBiFunction() {
    return (input, input2) -> apply(input, input2);
  }

  @SuppressWarnings("unchecked")
  public default <PRE_INPUTS> VarargsFunction<PRE_INPUTS, OUTPUT> transformArguments(Function<PRE_INPUTS, INPUTS> transformer) {
    return inputs -> apply((INPUTS[]) Arrays.stream(inputs).parallel().map(transformer).toArray());
  }
}

```

### java_code_8.txt
```java
import java.math.BigDecimal;
import java.math.BigInteger;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;
import java.util.function.UnaryOperator;
import java.util.stream.Collectors;
import java.util.stream.LongStream;

@FunctionalInterface
public interface Y<FUNCTION> extends SelfApplicable<FixedPoint<FUNCTION>> {
  public static void main(String... arguments) {
    BigInteger TWO = BigInteger.ONE.add(BigInteger.ONE);

    Function<Number, Long> toLong = Number::longValue;
    Function<Number, BigInteger> toBigInteger = toLong.andThen(BigInteger::valueOf);

    /* Based on https://gist.github.com/aruld/3965968/#comment-604392 */
    Y<VarargsFunction<Number, Number>> combinator = y -> f -> x -> f.apply(y.selfApply().apply(f)).apply(x);
    FixedPoint<VarargsFunction<Number, Number>> fixedPoint = combinator.selfApply();

    VarargsFunction<Number, Number> fibonacci = fixedPoint.apply(
      f -> VarargsFunction.upgrade(
        toBigInteger.andThen(
          n -> (n.compareTo(TWO) <= 0)
            ? 1
            : new BigInteger(f.apply(n.subtract(BigInteger.ONE)).toString())
              .add(new BigInteger(f.apply(n.subtract(TWO)).toString()))
        )
      )
    );

    VarargsFunction<Number, Number> factorial = fixedPoint.apply(
      f -> VarargsFunction.upgrade(
        toBigInteger.andThen(
          n -> (n.compareTo(BigInteger.ONE) <= 0)
            ? 1
            : n.multiply(new BigInteger(f.apply(n.subtract(BigInteger.ONE)).toString()))
        )
      )
    );

    VarargsFunction<Number, Number> ackermann = fixedPoint.apply(
      f -> VarargsFunction.upgrade(
        (BigInteger m, BigInteger n) -> m.equals(BigInteger.ZERO)
          ? n.add(BigInteger.ONE)
          : f.apply(
              m.subtract(BigInteger.ONE),
              n.equals(BigInteger.ZERO)
                ? BigInteger.ONE
                  : f.apply(m, n.subtract(BigInteger.ONE))
            )
      ).transformArguments(toBigInteger)
    );

    Map<String, VarargsFunction<Number, Number>> functions = new HashMap<>();
    functions.put("fibonacci", fibonacci);
    functions.put("factorial", factorial);
    functions.put("ackermann", ackermann);

    Map<VarargsFunction<Number, Number>, Number[]> parameters = new HashMap<>();
    parameters.put(functions.get("fibonacci"), new Number[]{20});
    parameters.put(functions.get("factorial"), new Number[]{10});
    parameters.put(functions.get("ackermann"), new Number[]{3, 2});

    functions.entrySet().stream().parallel().map(
      entry -> entry.getKey()
        + Arrays.toString(parameters.get(entry.getValue()))
        + " = "
        + entry.getValue().apply(parameters.get(entry.getValue()))
    ).forEach(System.out::println);
  }
}

```

## Python Code
### python_code_1.txt
```python
>>> Y = lambda f: (lambda x: x(x))(lambda y: f(lambda *args: y(y)(*args)))
>>> fac = lambda f: lambda n: (1 if n<2 else n*f(n-1))
>>> [ Y(fac)(i) for i in range(10) ]
[1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
>>> fib = lambda f: lambda n: 0 if n == 0 else (1 if n == 1 else f(n-1) + f(n-2))
>>> [ Y(fib)(i) for i in range(10) ]
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

```

### python_code_2.txt
```python
Y = lambda f: lambda *args: f(Y(f))(*args)

```

### python_code_3.txt
```python
Y = lambda b: ((lambda f: b(lambda *x: f(f)(*x)))((lambda f: b(lambda *x: f(f)(*x)))))

```

### python_code_4.txt
```python
# Better names due to Jim Weirich: http://vimeo.com/45140590
def (Y improver)
  ((fn(gen) gen.gen)
   (fn(gen)
     (fn(n)
       ((improver gen.gen) n))))

factorial <- (Y (fn(f)
                  (fn(n)
                    (if zero?.n
                      1
                      (n * (f n-1))))))

prn factorial.5

```

