# Loop over multiple arrays simultaneously

## Task Link
[Rosetta Code - Loop over multiple arrays simultaneously](https://rosettacode.org/wiki/Loop_over_multiple_arrays_simultaneously)

## Java Code
### java_code_2.txt
```java
String[][] list1 = {{"a","b","c"}, {"A", "B", "C"}, {"1", "2", "3"}};
        for (int i = 0; i < list1.length; i++) {
            for (String[] lista : list1) {
                System.out.print(lista[i]);
            }
            System.out.println();
        }

```

## Python Code
### python_code_1.txt
```python
>>> print ( '\n'.join(''.join(x) for x in 
zip('abc', 'ABC', '123')) )
aA1
bB2
cC3
>>>

```

### python_code_2.txt
```python
>>> print(*map(''.join, zip('abc', 'ABC', '123')), sep='\n')
aA1
bB2
cC3
>>>

```

### python_code_3.txt
```python
from itertools import imap

def join3(a,b,c):
   print a+b+c

imap(join3,'abc','ABC','123')

```

### python_code_4.txt
```python
>>> from itertools import zip_longest
>>> print ( '\n'.join(''.join(x) for x in zip_longest('abc', 
'ABCD', '12345', fillvalue='#')) )
aA1
bB2
cC3
#D4
##5
>>>

```

