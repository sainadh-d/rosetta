# Golden ratio/Convergence

## Task Link
[Rosetta Code - Golden ratio/Convergence](https://rosettacode.org/wiki/Golden_ratio/Convergence)

## Java Code
### java_code_1.txt
```java
public class GoldenRatio {
    static void iterate() {
        double oldPhi = 1.0, phi = 1.0, limit = 1e-5;
        int iters = 0;
        while (true) {
            phi = 1.0 + 1.0 / oldPhi;
            iters++;
            if (Math.abs(phi - oldPhi) <= limit) break;
            oldPhi = phi;
        }
        System.out.printf("Final value of phi : %16.14f\n", phi);
        double actualPhi = (1.0 + Math.sqrt(5.0)) / 2.0;
        System.out.printf("Number of iterations : %d\n", iters);
        System.out.printf("Error (approx) : %16.14f\n", phi - actualPhi);
    }

    public static void main(String[] args) {
        iterate();
    }
}

```

## Python Code
### python_code_1.txt
```python
import math

oldPhi = 1.0
phi = 1.0
iters = 0
limit = 1e-5
while True:
    phi = 1.0 + 1.0 / oldPhi
    iters += 1
    if math.fabs(phi - oldPhi) <= limit: break
    oldPhi = phi

print(f'Final value of phi : {phi:16.14f}')
actualPhi = (1.0 + math.sqrt(5.0)) / 2.0
print(f'Number of iterations : {iters}')
print(f'Error (approx) : {phi - actualPhi:16.14f}')

```

