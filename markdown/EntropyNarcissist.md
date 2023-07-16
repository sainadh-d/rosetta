# Entropy/Narcissist

## Task Link
[Rosetta Code - Entropy/Narcissist](https://rosettacode.org/wiki/Entropy/Narcissist)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.HashMap;
import java.util.Map;

public class EntropyNarcissist {

    private static final String FILE_NAME = "src/EntropyNarcissist.java";
    
    public static void main(String[] args) {
        System.out.printf("Entropy of file \"%s\" = %.12f.%n", FILE_NAME, getEntropy(FILE_NAME));
    }
    
    private static double getEntropy(String fileName) {
        Map<Character,Integer> characterCount = new HashMap<>();
        int length = 0;

        try (BufferedReader reader = new BufferedReader(new FileReader(new File(fileName)));) {        
            int c = 0;
            while ( (c = reader.read()) != -1 ) {
                characterCount.merge((char) c, 1, (v1, v2) -> v1 + v2);
                length++;
            }
        }
        catch ( IOException e ) {
            throw new RuntimeException(e);
        }
        
        double entropy = 0;
        for ( char key : characterCount.keySet() ) {
            double fraction = (double) characterCount.get(key) / length;
            entropy -= fraction * Math.log(fraction);
        }

        return entropy / Math.log(2);
    }

}

```

## Python Code
### python_code_1.txt
```python
import math
from collections import Counter

def entropy(s):
    p, lns = Counter(s), float(len(s))
    return -sum( count/lns * math.log(count/lns, 2) for count in p.values())

with open(__file__) as f:
    b=f.read()
    
print(entropy(b))

```

