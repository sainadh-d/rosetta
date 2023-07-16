# Random number generator (device)

## Task Link
[Rosetta Code - Random number generator (device)](https://rosettacode.org/wiki/Random_number_generator_(device))

## Java Code
### java_code_1.txt
```java
import java.security.SecureRandom;

public class RandomExample {
  public static void main(String[] args) {
    SecureRandom rng = new SecureRandom();

    /* Prints a random signed 32-bit integer. */
    System.out.println(rng.nextInt());
  }
}

```

## Python Code
### python_code_1.txt
```python
import random
rand = random.SystemRandom()
rand.randint(1,10)

```

