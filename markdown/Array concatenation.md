# Array concatenation

## Task Link
[Rosetta Code - Array concatenation](https://rosettacode.org/wiki/Array_concatenation)

## Java Code
### java_code_1.txt
```java
String[] fruits = ["apples", "oranges"];
String[] grains = ["wheat", "corn"];
String[] all    = fruits + grains;

```

### java_code_2.txt
```java
int[] concat(int[] arrayA, int[] arrayB) {
    int[] array = new int[arrayA.length + arrayB.length];
    System.arraycopy(arrayA, 0, array, 0, arrayA.length);
    System.arraycopy(arrayB, 0, array, arrayA.length, arrayB.length);
    return array;
}

```

### java_code_3.txt
```java
int[] concat(int[] arrayA, int[] arrayB) {
    int[] array = new int[arrayA.length + arrayB.length];
    for (int index = 0; index < arrayA.length; index++)
        array[index] = arrayA[index];
    for (int index = 0; index < arrayB.length; index++)
        array[index + arrayA.length] = arrayB[index];
    return array;
}

```

### java_code_4.txt
```java
int[] concat(int[] arrayA, int[] arrayB) {
    List<Integer> list = new ArrayList<>();
    for (int value : arrayA) list.add(value);
    for (int value : arrayB) list.add(value);
    int[] array = new int[list.size()];
    for (int index = 0; index < list.size(); index++)
        array[index] = list.get(index);
    return array;
}

```

## Python Code
### python_code_1.txt
```python
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
arr3 = [7, 8, 9]
arr4 = arr1 + arr2
assert arr4 == [1, 2, 3, 4, 5, 6]
arr4.extend(arr3)
assert arr4 == [1, 2, 3, 4, 5, 6, 7, 8, 9]

```

### python_code_2.txt
```python
arr5 = [4, 5, 6]
arr6 = [7, 8, 9]
arr6 += arr5
assert arr6 == [7, 8, 9, 4, 5, 6]

```

