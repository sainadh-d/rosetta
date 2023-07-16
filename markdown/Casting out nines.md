# Casting out nines

## Task Link
[Rosetta Code - Casting out nines](https://rosettacode.org/wiki/Casting_out_nines)

## Java Code
### java_code_1.txt
```java
import java.util.*;
import java.util.stream.IntStream;

public class CastingOutNines {

    public static void main(String[] args) {
        System.out.println(castOut(16, 1, 255));
        System.out.println(castOut(10, 1, 99));
        System.out.println(castOut(17, 1, 288));
    }

    static List<Integer> castOut(int base, int start, int end) {
        int[] ran = IntStream
                .range(0, base - 1)
                .filter(x -> x % (base - 1) == (x * x) % (base - 1))
                .toArray();

        int x = start / (base - 1);

        List<Integer> result = new ArrayList<>();
        while (true) {
            for (int n : ran) {
                int k = (base - 1) * x + n;
                if (k < start)
                    continue;
                if (k > end)
                    return result;
                result.add(k);
            }
            x++;
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# Casting out Nines
#
# Nigel Galloway: June 27th., 2012,
#
def CastOut(Base=10, Start=1, End=999999):
  ran = [y for y in range(Base-1) if y%(Base-1) == (y*y)%(Base-1)]
  x,y = divmod(Start, Base-1)
  while True:
    for n in ran:
      k = (Base-1)*x + n
      if k < Start:
        continue
      if k > End:
        return
      yield k
    x += 1

for V in CastOut(Base=16,Start=1,End=255):
  print(V, end=' ')

```

