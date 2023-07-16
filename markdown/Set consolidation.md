# Set consolidation

## Task Link
[Rosetta Code - Set consolidation](https://rosettacode.org/wiki/Set_consolidation)

## Java Code
### java_code_1.txt
```java
import java.util.*;

public class SetConsolidation {

    public static void main(String[] args) {
        List<Set<Character>> h1 = hashSetList("AB", "CD");
        System.out.println(consolidate(h1));

        List<Set<Character>> h2 = hashSetList("AB", "BD");
        System.out.println(consolidateR(h2));

        List<Set<Character>> h3 = hashSetList("AB", "CD", "DB");
        System.out.println(consolidate(h3));

        List<Set<Character>> h4 = hashSetList("HIK", "AB", "CD", "DB", "FGH");
        System.out.println(consolidateR(h4));
    }

    // iterative
    private static <E> List<Set<E>>
                consolidate(Collection<? extends Set<E>> sets) {
	List<Set<E>> r = new ArrayList<>();
	for (Set<E> s : sets) {
	    List<Set<E>> new_r = new ArrayList<>();
	    new_r.add(s);
	    for (Set<E> x : r) {
		if (!Collections.disjoint(s, x)) {
		    s.addAll(x);
		} else {
		    new_r.add(x);
		}
	    }
	    r = new_r;
	}
	return r;
    }

    // recursive
    private static <E> List<Set<E>> consolidateR(List<Set<E>> sets) {
        if (sets.size() < 2)
            return sets;
        List<Set<E>> r = new ArrayList<>();
        r.add(sets.get(0));
        for (Set<E> x : consolidateR(sets.subList(1, sets.size()))) {
            if (!Collections.disjoint(r.get(0), x)) {
                r.get(0).addAll(x);
            } else {
                r.add(x);
            }
        }
        return r;
    }

    private static List<Set<Character>> hashSetList(String... set) {
        List<Set<Character>> r = new ArrayList<>();
        for (int i = 0; i < set.length; i++) {
            r.add(new HashSet<Character>());
            for (int j = 0; j < set[i].length(); j++)
                r.get(i).add(set[i].charAt(j));
        }
        return r;
    }
}

```

## Python Code
### python_code_1.txt
```python
def consolidate(sets):
    setlist = [s for s in sets if s]
    for i, s1 in enumerate(setlist):
        if s1:
            for s2 in setlist[i+1:]:
                intersection = s1.intersection(s2)
                if intersection:
                    s2.update(s1)
                    s1.clear()
                    s1 = s2
    return [s for s in setlist if s]

```

### python_code_2.txt
```python
def conso(s):
	if len(s) < 2: return s
 
	r, b = [s[0]], conso(s[1:])
	for x in b:
		if r[0].intersection(x): r[0].update(x)
		else: r.append(x)
	return r

```

### python_code_3.txt
```python
def _test(consolidate=consolidate):
    
    def freze(list_of_sets):
        'return a set of frozensets from the list of sets to allow comparison'
        return set(frozenset(s) for s in list_of_sets)
        
    # Define some variables
    A,B,C,D,E,F,G,H,I,J,K = 'A,B,C,D,E,F,G,H,I,J,K'.split(',')
    # Consolidate some lists of sets
    assert (freze(consolidate([{A,B}, {C,D}])) == freze([{'A', 'B'}, {'C', 'D'}]))
    assert (freze(consolidate([{A,B}, {B,D}])) == freze([{'A', 'B', 'D'}]))
    assert (freze(consolidate([{A,B}, {C,D}, {D,B}])) == freze([{'A', 'C', 'B', 'D'}]))
    assert (freze(consolidate([{H,I,K}, {A,B}, {C,D}, {D,B}, {F,G,H}])) ==
             freze([{'A', 'C', 'B', 'D'}, {'G', 'F', 'I', 'H', 'K'}]))
    assert (freze(consolidate([{A,H}, {H,I,K}, {A,B}, {C,D}, {D,B}, {F,G,H}])) ==
             freze([{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}]))
    assert (freze(consolidate([{H,I,K}, {A,B}, {C,D}, {D,B}, {F,G,H}, {A,H}])) ==
             freze([{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}]))
    # Confirm order-independence
    from copy import deepcopy
    import itertools
    sets = [{H,I,K}, {A,B}, {C,D}, {D,B}, {F,G,H}, {A,H}]
    answer = consolidate(deepcopy(sets))
    for perm in itertools.permutations(sets):
            assert consolidate(deepcopy(perm)) == answer
 
    assert (answer == [{'A', 'C', 'B', 'D', 'G', 'F', 'I', 'H', 'K'}])
    assert (len(list(itertools.permutations(sets))) == 720)
    
    print('_test(%s) complete' % consolidate.__name__)

if __name__ == '__main__':
    _test(consolidate)
    _test(conso)

```

### python_code_4.txt
```python
'''Set consolidation'''

from functools import (reduce)


# consolidated :: Ord a => [Set a] -> [Set a]
def consolidated(sets):
    '''A consolidated list of sets.'''
    def go(xs, s):
        if xs:
            h = xs[0]
            return go(xs[1:], h.union(s)) if (
                h.intersection(s)
            ) else [h] + go(xs[1:], s)
        else:
            return [s]
    return reduce(go, sets, [])


# TESTS ---------------------------------------------------
# main :: IO ()
def main():
    '''Illustrative consolidations.'''

    print(
        tabulated('Consolidation of sets of characters:')(
            lambda x: str(list(map(compose(concat)(list), x)))
        )(str)(
            consolidated
        )(list(map(lambda xs: list(map(set, xs)), [
            ['ab', 'cd'],
            ['ab', 'bd'],
            ['ab', 'cd', 'db'],
            ['hik', 'ab', 'cd', 'db', 'fgh']
        ])))
    )


# DISPLAY OF RESULTS --------------------------------------

# compose (<<<) :: (b -> c) -> (a -> b) -> a -> c
def compose(g):
    '''Right to left function composition.'''
    return lambda f: lambda x: g(f(x))


# concat :: [String] -> String
def concat(xs):
    '''Concatenation of strings in xs.'''
    return ''.join(xs)


# tabulated :: String -> (a -> String) ->
#                        (b -> String) ->
#                        (a -> b) -> [a] -> String
def tabulated(s):
    '''Heading -> x display function -> fx display function ->
          f -> value list -> tabular string.'''
    def go(xShow, fxShow, f, xs):
        w = max(map(compose(len)(xShow), xs))
        return s + '\n' + '\n'.join([
            xShow(x).rjust(w, ' ') + ' -> ' + fxShow(f(x)) for x in xs
        ])
    return lambda xShow: lambda fxShow: (
        lambda f: lambda xs: go(
            xShow, fxShow, f, xs
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

