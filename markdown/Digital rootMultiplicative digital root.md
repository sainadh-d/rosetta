# Digital root/Multiplicative digital root

## Task Link
[Rosetta Code - Digital root/Multiplicative digital root](https://rosettacode.org/wiki/Digital_root/Multiplicative_digital_root)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class MultiplicativeDigitalRoot {

    public static void main(String[] args) {

        System.out.println("NUMBER  MDR   MP");
        for (long n : new long[]{123321, 7739, 893, 899998}) {
            long[] a = multiplicativeDigitalRoot(n);
            System.out.printf("%6d %4d %4d%n", a[0], a[1], a[2]);
        }

        System.out.println();

        Map<Long, List<Long>> table = new HashMap<>();
        for (long i = 0; i < 10; i++)
            table.put(i, new ArrayList<>());

        for (long cnt = 0, n = 0; cnt < 10;) {
            long[] res = multiplicativeDigitalRoot(n++);
            List<Long> list = table.get(res[1]);
            if (list.size() < 5) {
                list.add(res[0]);
                cnt = list.size() == 5 ? cnt + 1 : cnt;
            }
        }

        System.out.println("MDR: first five numbers with same MDR");
        table.forEach((key, lst) -> {
            System.out.printf("%3d: ", key);
            lst.forEach(e -> System.out.printf("%6s ", e));
            System.out.println();
        });
    }

    public static long[] multiplicativeDigitalRoot(long n) {
        int mp = 0;
        long mdr = n;
        while (mdr > 9) {
            long m = mdr;
            long total = 1;
            while (m > 0) {
                total *= m % 10;
                m /= 10;
            }
            mdr = total;
            mp++;
        }
        return new long[]{n, mdr, mp};
    }
}

```

## Python Code
### python_code_1.txt
```python
try:
    from functools import reduce
except:
    pass

def mdroot(n):
    'Multiplicative digital root'
    mdr = [n]
    while mdr[-1] > 9:
        mdr.append(reduce(int.__mul__, (int(dig) for dig in str(mdr[-1])), 1))
    return len(mdr) - 1, mdr[-1]

if __name__ == '__main__':
    print('Number: (MP, MDR)\n======  =========')
    for n in (123321, 7739, 893, 899998):
        print('%6i: %r' % (n, mdroot(n)))
        
    table, n = {i: [] for i in range(10)}, 0
    while min(len(row) for row in table.values()) < 5:
        mpersistence, mdr = mdroot(n)
        table[mdr].append(n)
        n += 1
    print('\nMP: [n0..n4]\n==  ========')
    for mp, val in sorted(table.items()):
        print('%2i: %r' % (mp, val[:5]))

```

### python_code_2.txt
```python
def mdroot(n):
    count, mdr = 0, n 
    while mdr > 9:
        m, digitsMul = mdr, 1
        while m:
            m, md = divmod(m, 10)
            digitsMul *= md
        mdr = digitsMul
        count += 1
    return count, mdr

```

