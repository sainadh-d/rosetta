# Ackermann function

## Task Link
[Rosetta Code - Ackermann function](https://rosettacode.org/wiki/Ackermann_function)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;

public static BigInteger ack(BigInteger m, BigInteger n) {
    return m.equals(BigInteger.ZERO)
            ? n.add(BigInteger.ONE)
            : ack(m.subtract(BigInteger.ONE),
                        n.equals(BigInteger.ZERO) ? BigInteger.ONE : ack(m, n.subtract(BigInteger.ONE)));
}

```

### java_code_2.txt
```java
@FunctionalInterface
public interface FunctionalField<FIELD extends Enum<?>> {
  public Object untypedField(FIELD field);

  @SuppressWarnings("unchecked")
  public default <VALUE> VALUE field(FIELD field) {
    return (VALUE) untypedField(field);
  }
}

```

### java_code_3.txt
```java
import java.util.function.BiFunction;
import java.util.function.Function;
import java.util.function.Predicate;
import java.util.function.UnaryOperator;
import java.util.stream.Stream;

public interface TailRecursive {
  public static <INPUT, INTERMEDIARY, OUTPUT> Function<INPUT, OUTPUT> new_(Function<INPUT, INTERMEDIARY> toIntermediary, UnaryOperator<INTERMEDIARY> unaryOperator, Predicate<INTERMEDIARY> predicate, Function<INTERMEDIARY, OUTPUT> toOutput) {
    return input ->
      $.new_(
        Stream.iterate(
          toIntermediary.apply(input),
          unaryOperator
        ),
        predicate,
        toOutput
      )
    ;
  }

  public static <INPUT1, INPUT2, INTERMEDIARY, OUTPUT> BiFunction<INPUT1, INPUT2, OUTPUT> new_(BiFunction<INPUT1, INPUT2, INTERMEDIARY> toIntermediary, UnaryOperator<INTERMEDIARY> unaryOperator, Predicate<INTERMEDIARY> predicate, Function<INTERMEDIARY, OUTPUT> toOutput) {
    return (input1, input2) ->
      $.new_(
        Stream.iterate(
          toIntermediary.apply(input1, input2),
          unaryOperator
        ),
        predicate,
        toOutput
      )
    ;
  }

  public enum $ {
    $$;

    private static <INTERMEDIARY, OUTPUT> OUTPUT new_(Stream<INTERMEDIARY> stream, Predicate<INTERMEDIARY> predicate, Function<INTERMEDIARY, OUTPUT> function) {
      return stream
        .filter(predicate)
        .map(function)
        .findAny()
        .orElseThrow(RuntimeException::new)
      ;
    }
  }
}

```

### java_code_4.txt
```java
import java.math.BigInteger;
import java.util.Stack;
import java.util.function.BinaryOperator;
import java.util.stream.Collectors;
import java.util.stream.Stream;

public interface Ackermann {
  public static Ackermann new_(BigInteger number1, BigInteger number2, Stack<BigInteger> stack, boolean flag) {
    return $.new_(number1, number2, stack, flag);
  }
  public static void main(String... arguments) {
    $.main(arguments);
  }
  public BigInteger number1();
  public BigInteger number2();

  public Stack<BigInteger> stack();

  public boolean flag();

  public enum $ {
    $$;

    private static final BigInteger ZERO = BigInteger.ZERO;
    private static final BigInteger ONE = BigInteger.ONE;
    private static final BigInteger TWO = BigInteger.valueOf(2);
    private static final BigInteger THREE = BigInteger.valueOf(3);
    private static final BigInteger FOUR = BigInteger.valueOf(4);

    private static Ackermann new_(BigInteger number1, BigInteger number2, Stack<BigInteger> stack, boolean flag) {
      return (FunctionalAckermann) field -> {
        switch (field) {
          case number1: return number1;
          case number2: return number2;
          case stack: return stack;
          case flag: return flag;
          default: throw new UnsupportedOperationException(
            field instanceof Field
              ? "Field checker has not been updated properly."
              : "Field is not of the correct type."
          );
        }
      };
    }

    private static final BinaryOperator<BigInteger> ACKERMANN = 
      TailRecursive.new_(
        (BigInteger number1, BigInteger number2) ->
          new_(
            number1,
            number2,
            Stream.of(number1).collect(
              Collectors.toCollection(Stack::new)
            ),
            false
          )
        ,
        ackermann -> {
          BigInteger number1 = ackermann.number1();
          BigInteger number2 = ackermann.number2();
          Stack<BigInteger> stack = ackermann.stack();
          if (!stack.empty() && !ackermann.flag()) {
            number1 = stack.pop();
          }
          switch (number1.intValue()) {
            case 0:
              return new_(
                number1,
                number2.add(ONE),
                stack,
                false
              );
            case 1:
              return new_(
                number1,
                number2.add(TWO),
                stack,
                false
              );
            case 2:
              return new_(
                number1,
                number2.multiply(TWO).add(THREE),
                stack,
                false
              );
            default:
              if (ZERO.equals(number2)) {
                return new_(
                  number1.subtract(ONE),
                  ONE,
                  stack,
                  true
                );
              } else {
                stack.push(number1.subtract(ONE));
                return new_(
                  number1,
                  number2.subtract(ONE),
                  stack,
                  true
                );
              }
          }
        },
        ackermann -> ackermann.stack().empty(),
        Ackermann::number2
      )::apply
    ;

    private static void main(String... arguments) {
      System.out.println(ACKERMANN.apply(FOUR, TWO));
    }

    private enum Field {
      number1,
      number2,
      stack,
      flag
    }

    @FunctionalInterface
    private interface FunctionalAckermann extends FunctionalField<Field>, Ackermann {
      @Override
      public default BigInteger number1() {
        return field(Field.number1);
      }

      @Override
      public default BigInteger number2() {
        return field(Field.number2);
      }

      @Override
      public default Stack<BigInteger> stack() {
        return field(Field.stack);
      }

      @Override
      public default boolean flag() {
        return field(Field.flag);
      }
    }
  }
}

```

### java_code_5.txt
```java
/*
 * Source https://stackoverflow.com/a/51092690/5520417
 */

package matematicas;

import java.math.BigInteger;
import java.util.HashMap;
import java.util.Stack;

/**
 * @author rodri
 *
 */

public class IterativeAckermannMemoryOptimization extends Thread {

  /**
   * Max percentage of free memory that the program will use. Default is 10% since
   * the majority of the used devices are mobile and therefore it is more likely
   * that the user will have more opened applications at the same time than in a
   * desktop device
   */
  private static Double SYSTEM_MEMORY_LIMIT_PERCENTAGE = 0.1;

  /**
   * Attribute of the type IterativeAckermann
   */
  private IterativeAckermann iterativeAckermann;

  /**
   * @param iterativeAckermann
   */
  public IterativeAckermannMemoryOptimization(IterativeAckermann iterativeAckermann) {
    super();
    this.iterativeAckermann = iterativeAckermann;
  }

  /**
   * @return
   */
  public IterativeAckermann getIterativeAckermann() {
    return iterativeAckermann;
  }

  /**
   * @param iterativeAckermann
   */
  public void setIterativeAckermann(IterativeAckermann iterativeAckermann) {
    this.iterativeAckermann = iterativeAckermann;
  }

  public static Double getSystemMemoryLimitPercentage() {
    return SYSTEM_MEMORY_LIMIT_PERCENTAGE;
  }

  /**
   * Principal method of the thread. Checks that the memory used doesn't exceed or
   * equal the limit, and informs the user when that happens.
   */
  @Override
  public void run() {
    String operating_system = System.getProperty("os.name").toLowerCase();
    if ( operating_system.equals("windows") || operating_system.equals("linux") || operating_system.equals("macintosh") ) {
      SYSTEM_MEMORY_LIMIT_PERCENTAGE = 0.25;
    }

    while ( iterativeAckermann.getConsumed_heap() >= SYSTEM_MEMORY_LIMIT_PERCENTAGE * Runtime.getRuntime().freeMemory() ) {
      try {
        wait();
      }
      catch ( InterruptedException e ) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
    }
    if ( ! iterativeAckermann.isAlive() )
      iterativeAckermann.start();
    else
      notifyAll();

  }

}


public class IterativeAckermann extends Thread {

  /*
   * Adjust parameters conveniently
   */
  /**
   * 
   */
  private static final int HASH_SIZE_LIMIT = 636;

  /**
   * 
   */
  private BigInteger m;

  /**
   * 
   */
  private BigInteger n;

  /**
   * 
   */
  private Integer hash_size;

  /**
   * 
   */
  private Long consumed_heap;

  /**
   * @param m
   * @param n
   * @param invalid
   * @param invalid2
   */
  public IterativeAckermann(BigInteger m, BigInteger n, Integer invalid, Long invalid2) {
    super();
    this.m = m;
    this.n = n;
    this.hash_size = invalid;
    this.consumed_heap = invalid2;
  }

  /**
   * 
   */
  public IterativeAckermann() {
    // TODO Auto-generated constructor stub
    super();
    m = null;
    n = null;
    hash_size = 0;
    consumed_heap = 0l;
  }

  /**
   * @return
   */
  public static BigInteger getLimit() {
    return LIMIT;
  }

  /**
   * @author rodri
   *
   * @param <T1>
   * @param <T2>
   */
  /**
   * @author rodri
   *
   * @param <T1>
   * @param <T2>
   */
  static class Pair<T1, T2> {

    /**
     * 
     */
    /**
     * 
     */
    T1 x;

    /**
     * 
     */
    /**
     * 
     */
    T2 y;

    /**
     * @param x_
     * @param y_
     */
    /**
     * @param x_
     * @param y_
     */
    Pair(T1 x_, T2 y_) {
      x = x_;
      y = y_;
    }

    /**
     *
     */
    /**
     *
     */
    @Override
    public int hashCode() {
      return x.hashCode() ^ y.hashCode();
    }

    /**
     *
     */
    /**
     *
     */
    @Override
    public boolean equals(Object o_) {

      if ( o_ == null ) {
        return false;
      }
      if ( o_.getClass() != this.getClass() ) {
        return false;
      }
      Pair<?, ?> o = (Pair<?, ?>) o_;
      return x.equals(o.x) && y.equals(o.y);
    }
  }

  /**
   * 
   */
  private static final BigInteger LIMIT = new BigInteger("6");

  /**
   * @param m
   * @param n
   * @return
   */

  /**
   *
   */
  @Override
  public void run() {
    while ( hash_size >= HASH_SIZE_LIMIT ) {
      try {
        this.wait();
      }
      catch ( InterruptedException e ) {
        // TODO Auto-generated catch block
        e.printStackTrace();
      }
    }
    for ( BigInteger i = BigInteger.ZERO; i.compareTo(LIMIT) == - 1; i = i.add(BigInteger.ONE) ) {
      for ( BigInteger j = BigInteger.ZERO; j.compareTo(LIMIT) == - 1; j = j.add(BigInteger.ONE) ) {
        IterativeAckermann iterativeAckermann = new IterativeAckermann(i, j, null, null);
        System.out.printf("Ackmermann(%d, %d) = %d\n", i, j, iterativeAckermann.iterative_ackermann(i, j));

      }
    }
  }

  /**
   * @return
   */
  public BigInteger getM() {
    return m;
  }

  /**
   * @param m
   */
  public void setM(BigInteger m) {
    this.m = m;
  }

  /**
   * @return
   */
  public BigInteger getN() {
    return n;
  }

  /**
   * @param n
   */
  public void setN(BigInteger n) {
    this.n = n;
  }

  /**
   * @return
   */
  public Integer getHash_size() {
    return hash_size;
  }

  /**
   * @param hash_size
   */
  public void setHash_size(Integer hash_size) {
    this.hash_size = hash_size;
  }

  /**
   * @return
   */
  public Long getConsumed_heap() {
    return consumed_heap;
  }

  /**
   * @param consumed_heap
   */
  public void setConsumed_heap(Long consumed_heap) {
    this.consumed_heap = consumed_heap;
  }

  /**
   * @param m
   * @param n
   * @return
   */
  public BigInteger iterative_ackermann(BigInteger m, BigInteger n) {
    if ( m.compareTo(BigInteger.ZERO) != - 1 && m.compareTo(BigInteger.ZERO) != - 1 )
      try {
        HashMap<Pair<BigInteger, BigInteger>, BigInteger> solved_set = new HashMap<Pair<BigInteger, BigInteger>, BigInteger>(900000);
        Stack<Pair<BigInteger, BigInteger>> to_solve = new Stack<Pair<BigInteger, BigInteger>>();
        to_solve.push(new Pair<BigInteger, BigInteger>(m, n));

        while ( ! to_solve.isEmpty() ) {
          Pair<BigInteger, BigInteger> head = to_solve.peek();
          if ( head.x.equals(BigInteger.ZERO) ) {
            solved_set.put(head, head.y.add(BigInteger.ONE));
            to_solve.pop();
          }
          else if ( head.y.equals(BigInteger.ZERO) ) {
            Pair<BigInteger, BigInteger> next = new Pair<BigInteger, BigInteger>(head.x.subtract(BigInteger.ONE), BigInteger.ONE);
            BigInteger result = solved_set.get(next);
            if ( result == null ) {
              to_solve.push(next);
            }
            else {
              solved_set.put(head, result);
              to_solve.pop();
            }
          }
          else {
            Pair<BigInteger, BigInteger> next0 = new Pair<BigInteger, BigInteger>(head.x, head.y.subtract(BigInteger.ONE));
            BigInteger result0 = solved_set.get(next0);
            if ( result0 == null ) {
              to_solve.push(next0);
            }
            else {
              Pair<BigInteger, BigInteger> next = new Pair<BigInteger, BigInteger>(head.x.subtract(BigInteger.ONE), result0);
              BigInteger result = solved_set.get(next);
              if ( result == null ) {
                to_solve.push(next);
              }
              else {
                solved_set.put(head, result);
                to_solve.pop();
              }
            }
          }
        }
        this.hash_size = solved_set.size();
        System.out.println("Hash Size: " + hash_size);
        consumed_heap = (Runtime.getRuntime().totalMemory() / (1024 * 1024));
        System.out.println("Consumed Heap: " + consumed_heap + "m");
        setHash_size(hash_size);
        setConsumed_heap(consumed_heap);
        return solved_set.get(new Pair<BigInteger, BigInteger>(m, n));

      }
      catch ( OutOfMemoryError e ) {
        // TODO: handle exception
        e.printStackTrace();
      }
    throw new IllegalArgumentException("The arguments must be non-negative integers.");
  }

  /**
   * @param args
   */
  /**
   * @param args
   */
  public static void main(String[] args) {
    IterativeAckermannMemoryOptimization iterative_ackermann_memory_optimization = new IterativeAckermannMemoryOptimization(
        new IterativeAckermann());
    iterative_ackermann_memory_optimization.start();
  }
}

```

### java_code_6.txt
```java
int ackermann(int m, int n) {
  if (m == 0)
    return n + 1;
  else if (m > 0 && n == 0)
    return ackermann(m - 1, 1);
  else
    return ackermann( m - 1, ackermann(m, n - 1) );
}

// Call function to produce output:
// the first 4x7 Ackermann numbers
void setup() {
  for (int m=0; m<4; m++) {
    for (int n=0; n<7; n++) {
      print(ackermann(m, n), " ");
    }
    println();
  }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

def setup():
    for m in range(4):
        for n in range(7):
            print("{} ".format(ackermann(m, n)), end = "")
        print()
    # print('finished')

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

```

### python_code_2.txt
```python
def ack1(M, N):
   return (N + 1) if M == 0 else (
      ack1(M-1, 1) if N == 0 else ack1(M-1, ack1(M, N-1)))

```

### python_code_3.txt
```python
from functools import lru_cache

@lru_cache(None)
def ack2(M, N):
    if M == 0:
        return N + 1
    elif N == 0:
        return ack2(M - 1, 1)
    else:
        return ack2(M - 1, ack2(M, N - 1))

```

### python_code_4.txt
```python
>>> import sys
>>> sys.setrecursionlimit(3000)
>>> ack1(0,0)
1
>>> ack1(3,4)
125
>>> ack2(0,0)
1
>>> ack2(3,4)
125

```

### python_code_5.txt
```python
def ack2(M, N):
   return (N + 1)   if M == 0 else (
          (N + 2)   if M == 1 else (
          (2*N + 3) if M == 2 else (
          (8*(2**N - 1) + 5) if M == 3 else (
          ack2(M-1, 1) if N == 0 else ack2(M-1, ack2(M, N-1))))))

```

### python_code_6.txt
```python
from collections import deque

def ack_ix(m, n):
    "Paddy3118's iterative with optimisations on m"

    stack = deque([])
    stack.extend([m, n])

    while  len(stack) > 1:
        n, m = stack.pop(), stack.pop()

        if   m == 0:
            stack.append(n + 1)
        elif m == 1:
            stack.append(n + 2)
        elif m == 2:
            stack.append(2*n + 3)
        elif m == 3:
            stack.append(2**(n + 3) - 3)
        elif n == 0:
            stack.extend([m-1, 1])
        else:
            stack.extend([m-1, m, n-1])

    return stack[0]

```

