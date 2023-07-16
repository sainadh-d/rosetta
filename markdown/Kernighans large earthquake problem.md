# Kernighans large earthquake problem

## Task Link
[Rosetta Code - Kernighans large earthquake problem](https://rosettacode.org/wiki/Kernighans_large_earthquake_problem)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.FileReader;

public class KernighansLargeEarthquakeProblem {

    public static void main(String[] args) throws Exception {
        try (BufferedReader reader  = new BufferedReader(new FileReader("data.txt")); ) {
            String inLine = null;
            while ( (inLine = reader.readLine()) != null ) {
                String[] split = inLine.split("\\s+");
                double magnitude = Double.parseDouble(split[2]);
                if ( magnitude > 6 ) {
                    System.out.println(inLine);
                }
            }
        }

    }

}

```

## Python Code
### python_code_1.txt
```python
python -c '
with open("data.txt") as f:
    for ln in f:
        if float(ln.strip().split()[2]) > 6:
            print(ln.strip())'

```

### python_code_2.txt
```python
from os.path import expanduser
from functools import (reduce)
from itertools import (chain)


# largeQuakes :: Int -> [String] -> [(String, String, String)]
def largeQuakes(n):
    def quake(threshold):
        def go(x):
            ws = x.split()
            return [tuple(ws)] if threshold < float(ws[2]) else []
        return lambda x: go(x)
    return concatMap(quake(n))


# main :: IO ()
def main():
    print (
        largeQuakes(6)(
            open(expanduser('~/data.txt')).read().splitlines()
        )
    )


# GENERIC ABSTRACTION -------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    return lambda xs: list(
        chain.from_iterable(
            map(f, xs)
        )
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

