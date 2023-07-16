# JortSort

## Task Link
[Rosetta Code - JortSort](https://rosettacode.org/wiki/JortSort)

## Java Code
### java_code_1.txt
```java
public class JortSort {
    public static void main(String[] args) {
        System.out.println(jortSort(new int[]{1, 2, 3}));
    }

    static boolean jortSort(int[] arr) {
        return true;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def jortsort(sequence):
	return list(sequence) == sorted(sequence)
>>> for data in [(1,2,4,3), (14,6,8), ['a', 'c'], ['s', 'u', 'x'], 'CVGH', 'PQRST']:
	print(f'jortsort({repr(data)}) is {jortsort(data)}')
jortsort((1, 2, 4, 3)) is False
jortsort((14, 6, 8)) is False
jortsort(['a', 'c']) is True
jortsort(['s', 'u', 'x']) is True
jortsort('CVGH') is False
jortsort('PQRST') is True
>>>

```

