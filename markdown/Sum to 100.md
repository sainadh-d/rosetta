# Sum to 100

## Task Link
[Rosetta Code - Sum to 100](https://rosettacode.org/wiki/Sum_to_100)

## Java Code
### java_code_1.txt
```java
/* 
 * RossetaCode: Sum to 100, Java 8. 
 *
 * Find solutions to the "sum to one hundred" puzzle.
 */
package rosettacode;

import java.io.PrintStream;
import java.util.Arrays;
import java.util.Collections;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Iterator;
import java.util.Map;
import java.util.Set;

public class SumTo100 implements Runnable {

    public static void main(String[] args) {
        new SumTo100().run();
    }

    void print(int givenSum) {
        Expression expression = new Expression();
        for (int i = 0; i < Expression.NUMBER_OF_EXPRESSIONS; i++, expression.next()) {
            if (expression.toInt() == givenSum) {
                expression.print();
            }
        }
    }

    void comment(String commentString) {
        System.out.println();
        System.out.println(commentString);
        System.out.println();
    }

    @Override
    public void run() {
        final Stat stat = new Stat();

        comment("Show all solutions that sum to 100");
        final int givenSum = 100;
        print(givenSum);

        comment("Show the sum that has the maximum number of solutions");
        final int maxCount = Collections.max(stat.sumCount.keySet());
        int maxSum;
        Iterator<Integer> it = stat.sumCount.get(maxCount).iterator();
        do {
            maxSum = it.next();
        } while (maxSum < 0);
        System.out.println(maxSum + " has " + maxCount + " solutions");

        comment("Show the lowest positive number that can't be expressed");
        int value = 0;
        while (stat.countSum.containsKey(value)) {
            value++;
        }
        System.out.println(value);

        comment("Show the ten highest numbers that can be expressed");
        final int n = stat.countSum.keySet().size();
        final Integer[] sums = stat.countSum.keySet().toArray(new Integer[n]);
        Arrays.sort(sums);
        for (int i = n - 1; i >= n - 10; i--) {
            print(sums[i]);
        }
    }

    private static class Expression {

        private final static int NUMBER_OF_DIGITS = 9;
        private final static byte ADD = 0;
        private final static byte SUB = 1;
        private final static byte JOIN = 2;

        final byte[] code = new byte[NUMBER_OF_DIGITS];
        final static int NUMBER_OF_EXPRESSIONS = 2 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3;

        Expression next() {
            for (int i = 0; i < NUMBER_OF_DIGITS; i++) {
                if (++code[i] > JOIN) {
                    code[i] = ADD;
                } else {
                    break;
                }
            }
            return this;
        }

        int toInt() {
            int value = 0;
            int number = 0;
            int sign = (+1);
            for (int digit = 1; digit <= 9; digit++) {
                switch (code[NUMBER_OF_DIGITS - digit]) {
                    case ADD:
                        value += sign * number;
                        number = digit;
                        sign = (+1);
                        break;
                    case SUB:
                        value += sign * number;
                        number = digit;
                        sign = (-1);
                        break;
                    case JOIN:
                        number = 10 * number + digit;
                        break;
                }
            }
            return value + sign * number;
        }

        @Override
        public String toString() {
            StringBuilder s = new StringBuilder(2 * NUMBER_OF_DIGITS + 1);
            for (int digit = 1; digit <= NUMBER_OF_DIGITS; digit++) {
                switch (code[NUMBER_OF_DIGITS - digit]) {
                    case ADD:
                        if (digit > 1) {
                            s.append('+');
                        }
                        break;
                    case SUB:
                        s.append('-');
                        break;
                }
                s.append(digit);
            }
            return s.toString();
        }

        void print() {
            print(System.out);
        }

        void print(PrintStream printStream) {
            printStream.format("%9d", this.toInt());
            printStream.println(" = " + this);
        }
    }

    private static class Stat {

        final Map<Integer, Integer> countSum = new HashMap<>();
        final Map<Integer, Set<Integer>> sumCount = new HashMap<>();

        Stat() {
            Expression expression = new Expression();
            for (int i = 0; i < Expression.NUMBER_OF_EXPRESSIONS; i++, expression.next()) {
                int sum = expression.toInt();
                countSum.put(sum, countSum.getOrDefault(sum, 0) + 1);
            }
            for (Map.Entry<Integer, Integer> entry : countSum.entrySet()) {
                Set<Integer> set;
                if (sumCount.containsKey(entry.getValue())) {
                    set = sumCount.get(entry.getValue());
                } else {
                    set = new HashSet<>();
                }
                set.add(entry.getKey());
                sumCount.put(entry.getValue(), set);
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import product, islice


def expr(p):
    return "{}1{}2{}3{}4{}5{}6{}7{}8{}9".format(*p)


def gen_expr():
    op = ['+', '-', '']
    return [expr(p) for p in product(op, repeat=9) if p[0] != '+']


def all_exprs():
    values = {}
    for expr in gen_expr():
        val = eval(expr)
        if val not in values:
            values[val] = 1
        else:
            values[val] += 1
    return values


def sum_to(val):
    for s in filter(lambda x: x[0] == val, map(lambda x: (eval(x), x), gen_expr())):
        print(s)


def max_solve():
    print("Sum {} has the maximum number of solutions: {}".
          format(*max(all_exprs().items(), key=lambda x: x[1])))


def min_solve():
    values = all_exprs()
    for i in range(123456789):
        if i not in values:
            print("Lowest positive sum that can't be expressed: {}".format(i))
            return


def highest_sums(n=10):
    sums = map(lambda x: x[0],
               islice(sorted(all_exprs().items(), key=lambda x: x[0], reverse=True), n))
    print("Highest Sums: {}".format(list(sums)))


sum_to(100)
max_solve()
min_solve()
highest_sums()

```

### python_code_2.txt
```python
import itertools
from collections import defaultdict, Counter

s = "123456789"
h = defaultdict(list)
for v in itertools.product(["+", "-", ""], repeat=9):
    if v[0] != "+":
        e = "".join("".join(u) for u in zip(v, s))
        h[eval(e)].append(e)

print("Solutions for 100")
for e in h[100]:
    print(e)

c = Counter({k: len(v) for k, v in h.items() if k >= 0})

k, m = c.most_common(1)[0]
print("Maximum number of solutions for %d (%d solutions)" % (k, m))

v = sorted(c.keys())

for i in range(v[-1]):
    if i not in c:
        print("Lowest impossible sum: %d" % i)
        break

print("Ten highest sums")
for k in reversed(v[-10:]):
    print(k)

```

