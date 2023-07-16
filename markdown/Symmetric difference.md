# Symmetric difference

## Task Link
[Rosetta Code - Symmetric difference](https://rosettacode.org/wiki/Symmetric_difference)

## Java Code
### java_code_1.txt
```java
Set<String> setA = new Set<String>{'John', 'Bob', 'Mary', 'Serena'};
Set<String> setB = new Set<String>{'Jim', 'Mary', 'John', 'Bob'};

// Option 1
Set<String> notInSetA = setB.clone();
notInSetA.removeAll(setA);

Set<String> notInSetB = setA.clone();
notInSetB.removeAll(setB);

Set<String> symmetricDifference = new Set<String>();
symmetricDifference.addAll(notInSetA);
symmetricDifference.addAll(notInSetB);

// Option 2
Set<String> union = setA.clone();
union.addAll(setB);

Set<String> intersection = setA.clone();
intersection.retainAll(setB);

Set<String> symmetricDifference2 = union.clone();
symmetricDifference2.removeAll(intersection);

System.debug('Not in set A: ' + notInSetA);
System.debug('Not in set B: ' + notInSetB);
System.debug('Symmetric Difference: ' + symmetricDifference);
System.debug('Symmetric Difference 2: ' + symmetricDifference2);

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class SymmetricDifference {
    public static void main(String[] args) {
        Set<String> setA = new HashSet<String>(Arrays.asList("John", "Serena", "Bob", "Mary", "Serena"));
        Set<String> setB = new HashSet<String>(Arrays.asList("Jim", "Mary", "John", "Jim", "Bob"));

        // Present our initial data set
        System.out.println("In set A: " + setA);
        System.out.println("In set B: " + setB);

        // Option 1: union of differences
        // Get our individual differences.
        Set<String> notInSetA = new HashSet<String>(setB);
        notInSetA.removeAll(setA);
        Set<String> notInSetB = new HashSet<String>(setA);
        notInSetB.removeAll(setB);
 
        // The symmetric difference is the concatenation of the two individual differences
        Set<String> symmetricDifference = new HashSet<String>(notInSetA);
        symmetricDifference.addAll(notInSetB);
        
        // Option 2: union minus intersection
        // Combine both sets
        Set<String> union = new HashSet<String>(setA);
        union.addAll(setB);
        
        // Get the intersection
        Set<String> intersection = new HashSet<String>(setA);
        intersection.retainAll(setB);
        
        // The symmetric difference is the union of the 2 sets minus the intersection
        Set<String> symmetricDifference2 = new HashSet<String>(union);
        symmetricDifference2.removeAll(intersection);
 
        // Present our results
        System.out.println("Not in set A: " + notInSetA);
        System.out.println("Not in set B: " + notInSetB);
        System.out.println("Symmetric Difference: " + symmetricDifference);
        System.out.println("Symmetric Difference 2: " + symmetricDifference2);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> setA = {"John", "Bob", "Mary", "Serena"}
>>> setB = {"Jim", "Mary", "John", "Bob"}
>>> setA ^ setB # symmetric difference of A and B
{'Jim', 'Serena'}
>>> setA - setB # elements in A that are not in B
{'Serena'}
>>> setB - setA # elements in B that are not in A
{'Jim'}
>>> setA | setB # elements in A or B (union)
{'John', 'Bob', 'Jim', 'Serena', 'Mary'}
>>> setA & setB # elements in both A and B (intersection)
{'Bob', 'John', 'Mary'}

```

### python_code_2.txt
```python
>>> setA = set(["John", "Bob", "Mary", "Serena"])
>>> setB = set(["Jim", "Mary", "John", "Bob"])
>>> setA ^ setB # symmetric difference of A and B
set(['Jim', 'Serena'])
>>> setA - setB # elements in A that are not in B
set(['Serena'])
>>> # and so on...

```

### python_code_3.txt
```python
>>> setA.symmetric_difference(setB)
{'Jim', 'Serena'}
>>> setA.difference(setB)
{'Serena'}
>>> setB.difference(setA)
{'Jim'}
>>> setA.union(setB)
{'Jim', 'Mary', 'Serena', 'John', 'Bob'}
>>> setA.intersection(setB)
{'Mary', 'John', 'Bob'}

```

