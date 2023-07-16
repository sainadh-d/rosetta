# General FizzBuzz

## Task Link
[Rosetta Code - General FizzBuzz](https://rosettacode.org/wiki/General_FizzBuzz)

## Java Code
### java_code_1.txt
```java
public class FizzBuzz {

    public static void main(String[] args) {
        Sound[] sounds = {new Sound(3, "Fizz"), new Sound(5, "Buzz"),  new Sound(7, "Baxx")};
        for (int i = 1; i <= 20; i++) {
            StringBuilder sb = new StringBuilder();
            for (Sound sound : sounds) {
                sb.append(sound.generate(i));
            }
            System.out.println(sb.length() == 0 ? i : sb.toString());
        }
    }

    private static class Sound {
        private final int trigger;
        private final String onomatopoeia;

        public Sound(int trigger, String onomatopoeia) {
            this.trigger = trigger;
            this.onomatopoeia = onomatopoeia;
        }

        public String generate(int i) {
            return i % trigger == 0 ? onomatopoeia : "";
        }

    }

}

```

### java_code_2.txt
```java
import java.util.stream.*;
import java.util.function.*;
import java.util.*;
public class fizzbuzz_general {
    /**
     * To run: java fizzbuzz_general.java 3=Fizz 5=Buzz 7=Baxx 100
     *
     */
    public static void main(String[] args) {
        Function<String[],Function<Integer,String>> make_cycle_function = 
              parts -> j -> j%(Integer.parseInt(parts[0]))==0?parts[1]:"";
        List<Function<Integer,String>> cycle_functions = Stream.of(args)
                     .map(arg -> arg.split("="))
                     .filter(parts->parts.length==2)
                     .map(make_cycle_function::apply)
                     .collect(Collectors.toList());
        Function<Integer,String> moduloTesters = i -> cycle_functions.stream()
                                   .map(fcn->fcn.apply(i))
                                   .collect(Collectors.joining());
        BiFunction<Integer,String,String> formatter = 
                    (i,printThis) -> "".equals(printThis)?Integer.toString(i):printThis;                               
        Function<Integer,String> fizzBuzz = i -> formatter.apply(i,moduloTesters.apply(i));
       
        IntStream.rangeClosed(0,Integer.parseInt(args[args.length-1]))
           .mapToObj(Integer::valueOf)
           .map(fizzBuzz::apply)
           .forEach(System.out::println);
    }
}

```

## Python Code
### python_code_1.txt
```python
def genfizzbuzz(factorwords, numbers):
    # sort entries by factor
    factorwords.sort(key=lambda factor_and_word: factor_and_word[0])
    lines = []
    for num in numbers:
        words = ''.join(word for factor, word in factorwords if (num % factor) == 0)
        lines.append(words if words else str(num))
    return '\n'.join(lines)

if __name__ == '__main__':
    print(genfizzbuzz([(5, 'Buzz'), (3, 'Fizz'), (7, 'Baxx')], range(1, 21)))

```

### python_code_2.txt
```python
n = 20
mappings = {3: "Fizz", 5: "Buzz", 7: "Baxx"}
for i in range(1, n+1): print(''.join(word * (i % key == 0) for key, word in mappings.items()) or i)

```

### python_code_3.txt
```python
from collections import defaultdict

N = 100
FACTOR_TO_WORD = {
    3: "Fizz",
    5: "Buzz",
}

def fizzbuzz(n=N, factor_to_word=FACTOR_TO_WORD):

    factors = defaultdict(list)

    for factor in factor_to_word:
        factors[factor].append(factor)

    for i in range(1, n+1):
        res = ''
        for factor in sorted(factors.pop(i, ())):
            factors[i+factor].append(factor)
            res += factor_to_word[factor]
        yield res or i

if __name__ == '__main__':

    n = int(input('Enter number: '))

    mods = {
      int(k): v
      for k, v in (
        input('Enter "<factor> <word>" (without quotes): ').split(maxsplit=1)
        for _ in range(3)
      )
    }

    for line in fizzbuzz(n, mods):
        print(line)

```

### python_code_4.txt
```python
from collections import defaultdict

n = 100
mods = [
    (3, 'Fizz'),
    (5, 'Buzz'),
]

def fizzbuzz(n=n, mods=mods):
    res = defaultdict(str)

    for num, name in mods:
        for i in range(num, n+1, num):
            res[i] += name

    return '\n'.join(res[i] or str(i) for i in range(1, n+1))


if __name__ == '__main__':
    n = int(input())

    mods = []
    while len(mods) != 3:   # for reading until EOF change 3 to -1
        try:
            line = input()
        except EOFError:
            break
        idx = line.find(' ')                        # preserves whitespace
        num, name = int(line[:idx]), line[idx+1:]   #   after the first space
        mods.append((num, name))    # preserves order and duplicate moduli

    print(fizzbuzz(n, mods))

```

