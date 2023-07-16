# Cartesian product of two or more lists

## Task Link
[Rosetta Code - Cartesian product of two or more lists](https://rosettacode.org/wiki/Cartesian_product_of_two_or_more_lists)

## Java Code
### java_code_1.txt
```java
import static java.util.Arrays.asList;
import static java.util.Collections.emptyList;
import static java.util.Optional.of;
import static java.util.stream.Collectors.toList;

import java.util.List;

public class CartesianProduct {

    public List<?> product(List<?>... a) {
        if (a.length >= 2) {
            List<?> product = a[0];
            for (int i = 1; i < a.length; i++) {
                product = product(product, a[i]);
            }
            return product;
        }

        return emptyList();
    }

    private <A, B> List<?> product(List<A> a, List<B> b) {
        return of(a.stream()
                .map(e1 -> of(b.stream().map(e2 -> asList(e1, e2)).collect(toList())).orElse(emptyList()))
                .flatMap(List::stream)
                .collect(toList())).orElse(emptyList());
    }
}

```

### java_code_2.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class CartesianProduct<V> {

	public List<List<V>> product(List<List<V>> lists) {
		List<List<V>> product = new ArrayList<>();

		// We first create a list for each value of the first list
		product(product, new ArrayList<>(), lists);

		return product;
	}

	private void product(List<List<V>> result, List<V> existingTupleToComplete, List<List<V>> valuesToUse) {
		for (V value : valuesToUse.get(0)) {
			List<V> newExisting = new ArrayList<>(existingTupleToComplete);
			newExisting.add(value);

			// If only one column is left
			if (valuesToUse.size() == 1) {
				// We create a new list with the exiting tuple for each value with the value
				// added
				result.add(newExisting);
			} else {
				// If there are still several columns, we go into recursion for each value
				List<List<V>> newValues = new ArrayList<>();
				// We build the next level of values
				for (int i = 1; i < valuesToUse.size(); i++) {
					newValues.add(valuesToUse.get(i));
				}

				product(result, newExisting, newValues);
			}
		}
	}

	public static void main(String[] args) {
		List<Integer> list1 = new ArrayList<>(Arrays.asList(new Integer[] { 1776, 1789 }));
		List<Integer> list2 = new ArrayList<>(Arrays.asList(new Integer[] { 7, 12 }));
		List<Integer> list3 = new ArrayList<>(Arrays.asList(new Integer[] { 4, 14, 23 }));
		List<Integer> list4 = new ArrayList<>(Arrays.asList(new Integer[] { 0, 1 }));

		List<List<Integer>> input = new ArrayList<>();
		input.add(list1);
		input.add(list2);
		input.add(list3);
		input.add(list4);

		CartesianProduct<Integer> cartesianProduct = new CartesianProduct<>();
		List<List<Integer>> product = cartesianProduct.product(input);
		System.out.println(product);
	}
}

```

## Python Code
### python_code_1.txt
```python
import itertools

def cp(lsts):
    return list(itertools.product(*lsts))

if __name__ == '__main__':
    from pprint import pprint as pp
    
    for lists in [[[1,2],[3,4]], [[3,4],[1,2]], [[], [1, 2]], [[1, 2], []],
                  ((1776, 1789),  (7, 12), (4, 14, 23), (0, 1)),
                  ((1, 2, 3), (30,), (500, 100)),
                  ((1, 2, 3), (), (500, 100))]:
        print(lists, '=>')
        pp(cp(lists), indent=2)

```

### python_code_2.txt
```python
# ap (<*>) :: [(a -> b)] -> [a] -> [b]
def ap(fs):
    return lambda xs: foldl(
        lambda a: lambda f: a + foldl(
            lambda a: lambda x: a + [f(x)])([])(xs)
    )([])(fs)

```

### python_code_3.txt
```python
ap(map(Tuple, xs))

```

### python_code_4.txt
```python
# nAryCartProd :: [[a], [b], [c] ...] -> [(a, b, c ...)]
def nAryCartProd(xxs):
    return foldl1(cartesianProduct)(
        xxs
    )

```

### python_code_5.txt
```python
# Two lists -> list of tuples


# cartesianProduct :: [a] -> [b] -> [(a, b)]
def cartesianProduct(xs):
    return ap(map(Tuple, xs))


# List of lists -> list of tuples

# nAryCartProd :: [[a], [b], [c] ...] -> [(a, b, c ...)]
def nAryCartProd(xxs):
    return foldl1(cartesianProduct)(
        xxs
    )


# main :: IO ()
def main():
    # Product of lists of different types
    print (
        'Product of two lists of different types:'
    )
    print(
        cartesianProduct(['a', 'b', 'c'])(
            [1, 2]
        )
    )

    # TESTS OF PRODUCTS OF TWO LISTS

    print(
        '\nSpecified tests of products of two lists:'
    )
    print(
        cartesianProduct([1, 2])([3, 4]),
        ' <--> ',
        cartesianProduct([3, 4])([1, 2])
    )
    print (
        cartesianProduct([1, 2])([]),
        ' <--> ',
        cartesianProduct([])([1, 2])
    )

    # TESTS OF N-ARY CARTESIAN PRODUCTS

    print('\nSpecified tests of nAry products:')
    for xs in nAryCartProd([[1776, 1789], [7, 12], [4, 14, 23], [0, 1]]):
        print(xs)

    for xs in (
        map_(nAryCartProd)(
            [
                [[1, 2, 3], [30], [500, 100]],
                [[1, 2, 3], [], [500, 100]]
            ]
        )
    ):
        print(
            xs
        )

# GENERIC -------------------------------------------------


# Applicative function for lists

# ap (<*>) :: [(a -> b)] -> [a] -> [b]
def ap(fs):
    return lambda xs: foldl(
        lambda a: lambda f: a + foldl(
            lambda a: lambda x: a + [f(x)])([])(xs)
    )([])(fs)


# foldl :: (a -> b -> a) -> a -> [b] -> a
def foldl(f):
    def go(v, xs):
        a = v
        for x in xs:
            a = f(a)(x)
        return a
    return lambda acc: lambda xs: go(acc, xs)


# foldl1 :: (a -> a -> a) -> [a] -> a
def foldl1(f):
    return lambda xs: foldl(f)(xs[0])(
        xs[1:]
    ) if xs else None


# map :: (a -> b) -> [a] -> [b]
def map_(f):
    return lambda xs: list(map(f, xs))


# Tuple :: a -> b -> (a, b)
def Tuple(x):
    return lambda y: (
        x + (y,)
    ) if tuple is type(x) else (x, y)


# TEST ----------------------------------------------------
if __name__ == '__main__':
    main()

```

