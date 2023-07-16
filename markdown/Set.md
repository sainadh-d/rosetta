# Set

## Task Link
[Rosetta Code - Set](https://rosettacode.org/wiki/Set)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.Set;
import java.util.TreeSet;

public class Sets {
    public static void main(String[] args){
        Set<Integer> a = new TreeSet<>();
        //TreeSet sorts on natural ordering (or an optional comparator)
        //other options: HashSet (hashcode)
        //               LinkedHashSet (insertion order)
        //               EnumSet (optimized for enum values)
        //others at: http://download.oracle.com/javase/7/docs/api/java/util/Set.html
        Set<Integer> b = new TreeSet<>();
        Set<Integer> c = new TreeSet<>();
        Set<Integer> d = new TreeSet<>();
        
        a.addAll(Arrays.asList(1, 2, 3, 4, 5));
        b.addAll(Arrays.asList(2, 3, 4, 5, 6, 8));
        c.addAll(Arrays.asList(2, 3, 4));
        d.addAll(Arrays.asList(2, 3, 4));
        System.out.println("a: " + a);
        System.out.println("b: " + b);
        System.out.println("c: " + c);
        System.out.println("d: " + d);
        
        System.out.println("2 in a: " + a.contains(2));
        System.out.println("6 in a: " + a.contains(6));
        
        Set<Integer> ab = new TreeSet<>();
        ab.addAll(a);
        ab.addAll(b);
        System.out.println("a union b: " + ab);
        
        Set<Integer> a_b = new TreeSet<>();
        a_b.addAll(a);
        a_b.removeAll(b);
        System.out.println("a - b: " + a_b);
        
        System.out.println("c subset of a: " + a.containsAll(c));
        //use a.conatins() for single elements
        
        System.out.println("c = d: " + c.equals(d));
        System.out.println("d = c: " + d.equals(c));
        
        Set<Integer> aib = new TreeSet<>();
        aib.addAll(a);
        aib.retainAll(b);
        System.out.println("a intersect b: " + aib);
        
        System.out.println("add 7 to a: " + a.add(7));
        System.out.println("add 2 to a again: " + a.add(2));
        
        //other noteworthy things related to sets:
        Set<Integer> empty = Collections.EMPTY_SET; //immutable empty set
        //empty.add(2);  would fail
        empty.isEmpty(); //test if a set is empty
        empty.size();
        Collections.disjoint(a, b); //returns true if the sets have no common elems (based on their .equals() methods)
        Collections.unmodifiableSet(a); //returns an immutable copy of a
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> s1, s2 = {1, 2, 3, 4}, {3, 4, 5, 6}
>>> s1 | s2 # Union
{1, 2, 3, 4, 5, 6}
>>> s1 & s2 # Intersection
{3, 4}
>>> s1 - s2 # Difference
{1, 2}
>>> s1 < s1 # True subset
False
>>> {3, 1} < s1 # True subset
True
>>> s1 <= s1 # Subset
True
>>> {3, 1} <= s1 # Subset
True
>>> {3, 2, 4, 1} == s1 # Equality
True
>>> s1 == s2 # Equality
False
>>> 2 in s1 # Membership
True
>>> 10 not in s1 # Non-membership
True
>>> {1, 2, 3, 4, 5} > s1 # True superset
True
>>> {1, 2, 3, 4} > s1 # True superset
False
>>> {1, 2, 3, 4} >= s1 # Superset
True
>>> s1 ^ s2 # Symmetric difference
{1, 2, 5, 6}
>>> len(s1) # Cardinality
4
>>> s1.add(99) # Mutability
>>> s1
{99, 1, 2, 3, 4}
>>> s1.discard(99) # Mutability
>>> s1
{1, 2, 3, 4}
>>> s1 |= s2 # Mutability
>>> s1
{1, 2, 3, 4, 5, 6}
>>> s1 -= s2 # Mutability
>>> s1
{1, 2}
>>> s1 ^= s2 # Mutability
>>> s1
{1, 2, 3, 4, 5, 6}
>>>

```

