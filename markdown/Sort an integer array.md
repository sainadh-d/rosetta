# Sort an integer array

## Task Link
[Rosetta Code - Sort an integer array](https://rosettacode.org/wiki/Sort_an_integer_array)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Example {
    public static void main(String[] args)
    {
        int[] nums = {2,4,3,1,2};
        Arrays.sort(nums);
    }
}

```

### java_code_2.txt
```java
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Example {
    public static void main(String[] args)
    {
        List<Integer> nums = Arrays.asList(2,4,3,1,2);
        Collections.sort(nums);
    }
}

```

## Python Code
### python_code_1.txt
```python
nums = [2,4,3,1,2]
nums.sort()

```

### python_code_2.txt
```python
nums = sorted([2,4,3,1,2])

```

