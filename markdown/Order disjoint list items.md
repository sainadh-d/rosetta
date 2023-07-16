# Order disjoint list items

## Task Link
[Rosetta Code - Order disjoint list items](https://rosettacode.org/wiki/Order_disjoint_list_items)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.BitSet;
import org.apache.commons.lang3.ArrayUtils;

public class OrderDisjointItems {

    public static void main(String[] args) {
        final String[][] MNs = {{"the cat sat on the mat", "mat cat"},
        {"the cat sat on the mat", "cat mat"},
        {"A B C A B C A B C", "C A C A"}, {"A B C A B D A B E", "E A D A"},
        {"A B", "B"}, {"A B", "B A"}, {"A B B A", "B A"}, {"X X Y", "X"}};

        for (String[] a : MNs) {
            String[] r = orderDisjointItems(a[0].split(" "), a[1].split(" "));
            System.out.printf("%s | %s -> %s%n", a[0], a[1], Arrays.toString(r));
        }
    }

    // if input items cannot be null
    static String[] orderDisjointItems(String[] m, String[] n) {
        for (String e : n) {
            int idx = ArrayUtils.indexOf(m, e);
            if (idx != -1)
                m[idx] = null;
        }
        for (int i = 0, j = 0; i < m.length; i++) {
            if (m[i] == null)
                m[i] = n[j++];
        }
        return m;
    }

    // otherwise
    static String[] orderDisjointItems2(String[] m, String[] n) {
        BitSet bitSet = new BitSet(m.length);
        for (String e : n) {
            int idx = -1;
            do {
                idx = ArrayUtils.indexOf(m, e, idx + 1);
            } while (idx != -1 && bitSet.get(idx));
            if (idx != -1)
                bitSet.set(idx);
        }
        for (int i = 0, j = 0; i < m.length; i++) {
            if (bitSet.get(i))
                m[i] = n[j++];
        }
        return m;
    }
}

```

## Python Code
### python_code_1.txt
```python
from __future__ import print_function

def order_disjoint_list_items(data, items):
    #Modifies data list in-place
    itemindices = []
    for item in set(items):
        itemcount = items.count(item)
        #assert data.count(item) >= itemcount, 'More of %r than in data' % item
        lastindex = [-1]
        for i in range(itemcount):
            lastindex.append(data.index(item, lastindex[-1] + 1))
        itemindices += lastindex[1:]
    itemindices.sort()
    for index, item in zip(itemindices, items):
        data[index] = item

if __name__ == '__main__':
    tostring = ' '.join
    for data, items in [ (str.split('the cat sat on the mat'), str.split('mat cat')),
                         (str.split('the cat sat on the mat'), str.split('cat mat')),
                         (list('ABCABCABC'), list('CACA')),
                         (list('ABCABDABE'), list('EADA')),
                         (list('AB'), list('B')),
                         (list('AB'), list('BA')),
                         (list('ABBA'), list('BA')),
                         (list(''), list('')),
                         (list('A'), list('A')),
                         (list('AB'), list('')),
                         (list('ABBA'), list('AB')),
                         (list('ABAB'), list('AB')),
                         (list('ABAB'), list('BABA')),
                         (list('ABCCBA'), list('ACAC')),
                         (list('ABCCBA'), list('CACA')),
                       ]:
        print('Data M: %-24r Order N: %-9r' % (tostring(data), tostring(items)), end=' ')
        order_disjoint_list_items(data, items)
        print("-> M' %r" % tostring(data))

```

