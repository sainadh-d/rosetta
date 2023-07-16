# Jewels and stones

## Task Link
[Rosetta Code - Jewels and stones](https://rosettacode.org/wiki/Jewels_and_stones)

## Java Code
### java_code_1.txt
```java
import java.util.HashSet;
import java.util.Set;

public class App {
    private static int countJewels(String stones, String jewels) {
        Set<Character> bag = new HashSet<>();
        for (char c : jewels.toCharArray()) {
            bag.add(c);
        }

        int count = 0;
        for (char c : stones.toCharArray()) {
            if (bag.contains(c)) {
                count++;
            }
        }

        return count;
    }

    public static void main(String[] args) {
        System.out.println(countJewels("aAAbbbb", "aA"));
        System.out.println(countJewels("ZZ", "z"));
    }
}

```

## Python Code
### python_code_1.txt
```python
def countJewels(s, j):
    return sum(x in j for x in s)

print countJewels("aAAbbbb", "aA")
print countJewels("ZZ", "z")

```

### python_code_2.txt
```python
def countJewels(stones, jewels):
    jewelset = set(jewels)
    return sum(1 for stone in stones if stone in jewelset)

print(countJewels("aAAbbbb", "aA"))
print(countJewels("ZZ", "z"))

```

