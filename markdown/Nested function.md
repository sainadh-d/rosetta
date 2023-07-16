# Nested function

## Task Link
[Rosetta Code - Nested function](https://rosettacode.org/wiki/Nested_function)

## Java Code
### java_code_2.txt
```java
import java.util.concurrent.atomic.AtomicInteger;
import java.util.function.Function;

public class NestedFunctionsDemo {

    static String makeList(String separator) {
        AtomicInteger counter = new AtomicInteger(1);

        Function<String, String> makeItem = item -> counter.getAndIncrement() + separator + item + "\n";

        return makeItem.apply("first") + makeItem.apply("second") + makeItem.apply("third");
    }

    public static void main(String[] args) {
        System.out.println(makeList(". "));
    }
}

```

## Python Code
### python_code_1.txt
```python
def makeList(separator):
    counter = 1

    def makeItem(item):
        nonlocal counter
        result = str(counter) + separator + item + "\n"
        counter += 1
        return result

    return makeItem("first") + makeItem("second") + makeItem("third")

print(makeList(". "))

```

