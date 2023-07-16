# Sort disjoint sublist

## Task Link
[Rosetta Code - Sort disjoint sublist](https://rosettacode.org/wiki/Sort_disjoint_sublist)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Disjoint {
    public static <T extends Comparable<? super T>> void sortDisjoint(
            List<T> array, int[] idxs) {
        Arrays.sort(idxs);
        List<T> disjoint = new ArrayList<T>();
        for (int idx : idxs) {
            disjoint.add(array.get(idx));
        }
        Collections.sort(disjoint);
        int i = 0;
        for (int idx : idxs) {
            array.set(idx, disjoint.get(i++));
        }
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(7, 6, 5, 4, 3, 2, 1, 0);
        int[] indices = {6, 1, 7};
        System.out.println(list);
        sortDisjoint(list, indices);
        System.out.println(list);
    }
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.AbstractList;

public class Disjoint {
    public static <T extends Comparable<? super T>> void sortDisjoint(
            final List<T> array, final int[] idxs) {
        Arrays.sort(idxs);
        Collections.sort(new AbstractList<T>() {
		public int size() { return idxs.length; }
		public T get(int i) { return array.get(idxs[i]); }
		public T set(int i, T x) { return array.set(idxs[i], x); }
	    });
    }

    public static void main(String[] args) {
        List<Integer> list = Arrays.asList(7, 6, 5, 4, 3, 2, 1, 0);
        int[] indices = {6, 1, 7};
        System.out.println(list);
        sortDisjoint(list, indices);
        System.out.println(list);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def sort_disjoint_sublist(data, indices):
	indices = sorted(indices)
	values  = sorted(data[i] for i in indices)
	for index, value in zip(indices, values):
		data[index] = value

		
>>> d = [7, 6, 5, 4, 3, 2, 1, 0]
>>> i = set([6, 1, 7])
>>> sort_disjoint_sublist(d, i)
>>> d
[7, 0, 5, 4, 3, 2, 1, 6]
>>> # Which could be more cryptically written as:
>>> def sort_disjoint_sublist(data, indices):
	for index, value in zip(sorted(indices), sorted(data[i] for i in indices)): data[index] = value

	
>>>

```

### python_code_2.txt
```python
'''Disjoint sublist sorting'''


# --------------------- DISJOINT SORT ----------------------

# disjointSort :: [Int] -> [Int] -> [Int]
def disjointSort(ixs):
    '''A copy of the list xs, in which the disjoint sublist
       of items at zero-based indexes ixs is sorted in a
       default numeric or lexical order.'''
    def go(xs):
        ks = sorted(ixs)
        dct = dict(zip(ks, sorted(xs[k] for k in ks)))
        return [
            dct[i] if i in dct else x 
            for i, x in enumerate(xs)
        ]
    return go


# -------------------------- TEST --------------------------
# main :: IO ()
def main():
    '''Disjoint sublist at three indices.'''
    print(
        tabulated(
            'Disjoint sublist at indices [6, 1, 7] sorted:\n'
        )
        (str)(str)(
            disjointSort([6, 1, 7])
        )([
            [7, 6, 5, 4, 3, 2, 1, 0],
            ['h', 'g', 'f', 'e', 'd', 'c', 'b', 'a']
        ])
    )


# ------------------------ DISPLAY -------------------------

# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
                f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join(
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        )
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Function composition.'''
    return lambda f: lambda x: g(f(x))


if __name__ == '__main__':
    main()

```

