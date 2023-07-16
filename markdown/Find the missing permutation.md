# Find the missing permutation

## Task Link
[Rosetta Code - Find the missing permutation](https://rosettacode.org/wiki/Find_the_missing_permutation)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;

import com.google.common.base.Joiner;
import com.google.common.collect.ImmutableSet;
import com.google.common.collect.Lists;

public class FindMissingPermutation {
	public static void main(String[] args) {
		Joiner joiner = Joiner.on("").skipNulls();
		ImmutableSet<String> s = ImmutableSet.of("ABCD", "CABD", "ACDB",
				"DACB", "BCDA", "ACBD", "ADCB", "CDAB", "DABC", "BCAD", "CADB",
				"CDBA", "CBAD", "ABDC", "ADBC", "BDCA", "DCBA", "BACD", "BADC",
				"BDAC", "CBDA", "DBCA", "DCAB");

		for (ArrayList<Character> cs : Utils.Permutations(Lists.newArrayList(
				'A', 'B', 'C', 'D')))
			if (!s.contains(joiner.join(cs)))
				System.out.println(joiner.join(cs));
	}
}

```

### java_code_2.txt
```java
public class FindMissingPermutation
{
  public static void main(String[] args)
  {
    String[] givenPermutations = { "ABCD", "CABD", "ACDB", "DACB", "BCDA", "ACBD",
                                   "ADCB", "CDAB", "DABC", "BCAD", "CADB", "CDBA",
                                   "CBAD", "ABDC", "ADBC", "BDCA", "DCBA", "BACD",
                                   "BADC", "BDAC", "CBDA", "DBCA", "DCAB" };
    String characterSet = givenPermutations[0];
    // Compute n! * (n - 1) / 2
    int maxCode = characterSet.length() - 1;
    for (int i = characterSet.length(); i >= 3; i--)
      maxCode *= i;
    StringBuilder missingPermutation = new StringBuilder();
    for (int i = 0; i < characterSet.length(); i++)
    {
      int code = 0;
      for (String permutation : givenPermutations)
        code += characterSet.indexOf(permutation.charAt(i));
      missingPermutation.append(characterSet.charAt(maxCode - code));
    }
    System.out.println("Missing permutation: " + missingPermutation.toString());
  }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import permutations

given = '''ABCD CABD ACDB DACB BCDA ACBD ADCB CDAB DABC BCAD CADB CDBA
           CBAD ABDC ADBC BDCA DCBA BACD BADC BDAC CBDA DBCA DCAB'''.split()

allPerms = [''.join(x) for x in permutations(given[0])]

missing = list(set(allPerms) - set(given)) # ['DBAC']

```

### python_code_2.txt
```python
def missing_permutation(arr):
  "Find the missing permutation in an array of N! - 1 permutations."
  
  # We won't validate every precondition, but we do have some basic
  # guards.
  if len(arr) == 0: raise Exception("Need more data")
  if len(arr) == 1:
      return [arr[0][1] + arr[0][0]]
  
  # Now we know that for each position in the string, elements should appear
  # an even number of times (N-1 >= 2).  We can use a set to detect the element appearing
  # an odd number of times.  Detect odd occurrences by toggling admission/expulsion
  # to and from the set for each value encountered.  At the end of each pass one element
  # will remain in the set.
  missing_permutation = ''
  for pos in range(len(arr[0])):
      s = set()
      for permutation in arr:
          c = permutation[pos]
          if c in s:
            s.remove(c)
          else:
            s.add(c)
      missing_permutation += list(s)[0]
  return missing_permutation
  
given = '''ABCD CABD ACDB DACB BCDA ACBD ADCB CDAB DABC BCAD CADB CDBA
           CBAD ABDC ADBC BDCA DCBA BACD BADC BDAC CBDA DBCA DCAB'''.split()
           
print missing_permutation(given)

```

### python_code_3.txt
```python
>>> from collections import Counter
>>> given = '''ABCD CABD ACDB DACB BCDA ACBD ADCB CDAB DABC BCAD CADB CDBA
           CBAD ABDC ADBC BDCA DCBA BACD BADC BDAC CBDA DBCA DCAB'''.split()
>>> ''.join(Counter(x).most_common()[-1][0] for x in zip(*given))
'DBAC'
>>>

```

### python_code_4.txt
```python
>>> from pprint import pprint as pp
>>> pp(list(zip(*given)), width=120)
[('A', 'C', 'A', 'D', 'B', 'A', 'A', 'C', 'D', 'B', 'C', 'C', 'C', 'A', 'A', 'B', 'D', 'B', 'B', 'B', 'C', 'D', 'D'),
 ('B', 'A', 'C', 'A', 'C', 'C', 'D', 'D', 'A', 'C', 'A', 'D', 'B', 'B', 'D', 'D', 'C', 'A', 'A', 'D', 'B', 'B', 'C'),
 ('C', 'B', 'D', 'C', 'D', 'B', 'C', 'A', 'B', 'A', 'D', 'B', 'A', 'D', 'B', 'C', 'B', 'C', 'D', 'A', 'D', 'C', 'A'),
 ('D', 'D', 'B', 'B', 'A', 'D', 'B', 'B', 'C', 'D', 'B', 'A', 'D', 'C', 'C', 'A', 'A', 'D', 'C', 'C', 'A', 'A', 'B')]
>>> pp([Counter(x).most_common() for x in zip(*given)])
[[('C', 6), ('B', 6), ('A', 6), ('D', 5)],
 [('D', 6), ('C', 6), ('A', 6), ('B', 5)],
 [('D', 6), ('C', 6), ('B', 6), ('A', 5)],
 [('D', 6), ('B', 6), ('A', 6), ('C', 5)]]
>>> pp([Counter(x).most_common()[-1] for x in zip(*given)])
[('D', 5), ('B', 5), ('A', 5), ('C', 5)]
>>> pp([Counter(x).most_common()[-1][0] for x in zip(*given)])
['D', 'B', 'A', 'C']
>>> ''.join([Counter(x).most_common()[-1][0] for x in zip(*given)])
'DBAC'
>>>

```

### python_code_5.txt
```python
'''Find the missing permutation'''

from functools import reduce
from operator import xor


print(''.join([
    chr(i) for i in reduce(
        lambda a, s: map(
            xor,
            a,
            [ord(c) for c in list(s)]
        ), [
            'ABCD', 'CABD', 'ACDB', 'DACB',
            'BCDA', 'ACBD', 'ADCB', 'CDAB',
            'DABC', 'BCAD', 'CADB', 'CDBA',
            'CBAD', 'ABDC', 'ADBC', 'BDCA',
            'DCBA', 'BACD', 'BADC', 'BDAC',
            'CBDA', 'DBCA', 'DCAB'
        ],
        [0, 0, 0, 0]
    )
]))

```

