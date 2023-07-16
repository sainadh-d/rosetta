# Multi-dimensional array

## Task Link
[Rosetta Code - Multi-dimensional array](https://rosettacode.org/wiki/Multi-dimensional_array)

## Java Code
### java_code_1.txt
```java
public class MultiDimensionalArray {
    public static void main(String[] args) {
        // create a regular 4 dimensional array and initialize successive elements to the values 1 to 120
        int m = 1;
        int[][][][] a4 = new int[5][4][3][2];
        for (int i = 0; i < a4.length; ++i) {
            for (int j = 0; j < a4[0].length; ++j) {
                for (int k = 0; k < a4[0][0].length; ++k) {
                    for (int l = 0; l < a4[0][0][0].length; ++l) {
                        a4[i][j][k][l] = m++;
                    }
                }
            }
        }

        System.out.println("First element = " + a4[0][0][0][0]);  // access and print value of first element
        a4[0][0][0][0] = 121;                                     // change value of first element
        System.out.println();

        for (int i = 0; i < a4.length; ++i) {
            for (int j = 0; j < a4[0].length; ++j) {
                for (int k = 0; k < a4[0][0].length; ++k) {
                    for (int l = 0; l < a4[0][0][0].length; ++l) {
                        System.out.printf("%4d", a4[i][j][k][l]);
                    }
                }
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> from pprint import pprint as pp   # Pretty printer
>>> from itertools import product
>>> 
>>> def dict_as_mdarray(dimensions=(2, 3), init=0.0):
...     return {indices: init for indices in product(*(range(i) for i in dimensions))}
... 
>>> 
>>> mdarray = dict_as_mdarray((2, 3, 4, 5))
>>> pp(mdarray)
{(0, 0, 0, 0): 0.0,
 (0, 0, 0, 1): 0.0,
 (0, 0, 0, 2): 0.0,
 (0, 0, 0, 3): 0.0,
 (0, 0, 0, 4): 0.0,
 (0, 0, 1, 0): 0.0,
...
 (1, 2, 3, 0): 0.0,
 (1, 2, 3, 1): 0.0,
 (1, 2, 3, 2): 0.0,
 (1, 2, 3, 3): 0.0,
 (1, 2, 3, 4): 0.0}
>>> mdarray[(0, 1, 2, 3)]
0.0
>>> mdarray[(0, 1, 2, 3)] = 6.78
>>> mdarray[(0, 1, 2, 3)]
6.78
>>> mdarray[(0, 1, 2, 3)] = 5.4321
>>> mdarray[(0, 1, 2, 3)]
5.4321
>>> pp(mdarray)
{(0, 0, 0, 0): 0.0,
 (0, 0, 0, 1): 0.0,
 (0, 0, 0, 2): 0.0,
...
 (0, 1, 2, 2): 0.0,
 (0, 1, 2, 3): 5.4321,
 (0, 1, 2, 4): 0.0,
...
 (1, 2, 3, 3): 0.0,
 (1, 2, 3, 4): 0.0}
>>>

```

### python_code_2.txt
```python
import numpy as np
a = np.array([[1, 2], [3, 4]], order="C")
b = np.array([[1, 2], [3, 4]], order="F")
np.reshape(a, (4,))             # [1, 2, 3, 4]
np.reshape(b, (4,))             # [1, 2, 3, 4]
np.reshape(b, (4,), order="A")  # [1, 3, 2, 4]

```

### python_code_3.txt
```python
>>> from numpy import *
>>> 
>>> mdarray = zeros((2, 3, 4, 5), dtype=int8, order='F')

>>> mdarray
array([[[[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]],


       [[[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]],

        [[0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0]]]], dtype=int8)
>>> mdarray[0, 1, 2, 3]
0
>>> mdarray[0, 1, 2, 3] = 123
>>> mdarray[0, 1, 2, 3]
123
>>> mdarray[0, 1, 2, 3] = 666
>>> mdarray[0, 1, 2, 3]
-102
>>> mdarray[0, 1, 2, 3] = 255
>>> mdarray[0, 1, 2, 3]
-1
>>> mdarray[0, 1, 2, 3] = -128
>>> mdarray[0, 1, 2, 3]
-128
>>> mdarray
array([[[[   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0]],

        [[   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0, -128,    0],
         [   0,    0,    0,    0,    0]],

        [[   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0]]],


       [[[   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0]],

        [[   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0]],

        [[   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0],
         [   0,    0,    0,    0,    0]]]], dtype=int8)
>>>

```

