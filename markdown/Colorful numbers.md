# Colorful numbers

## Task Link
[Rosetta Code - Colorful numbers](https://rosettacode.org/wiki/Colorful_numbers)

## Java Code
### java_code_1.txt
```java
public class ColorfulNumbers {
    private int count[] = new int[8];
    private boolean used[] = new boolean[10];
    private int largest = 0;

    public static void main(String[] args) {
        System.out.printf("Colorful numbers less than 100:\n");
        for (int n = 0, count = 0; n < 100; ++n) {
            if (isColorful(n))
                System.out.printf("%2d%c", n, ++count % 10 == 0 ? '\n' : ' ');
        }

        ColorfulNumbers c = new ColorfulNumbers();

        System.out.printf("\n\nLargest colorful number: %,d\n", c.largest);

        System.out.printf("\nCount of colorful numbers by number of digits:\n");
        int total = 0;
        for (int d = 0; d < 8; ++d) {
            System.out.printf("%d   %,d\n", d + 1, c.count[d]);
            total += c.count[d];
        }
        System.out.printf("\nTotal: %,d\n", total);
    }

    private ColorfulNumbers() {
        countColorful(0, 0, 0);
    }

    public static boolean isColorful(int n) {
        // A colorful number cannot be greater than 98765432.
        if (n < 0 || n > 98765432)
            return false;
        int digit_count[] = new int[10];
        int digits[] = new int[8];
        int num_digits = 0;
        for (int m = n; m > 0; m /= 10) {
            int d = m % 10;
            if (n > 9 && (d == 0 || d == 1))
                return false;
            if (++digit_count[d] > 1)
                return false;
            digits[num_digits++] = d;
        }
        // Maximum number of products is (8 x 9) / 2.
        int products[] = new int[36];
        for (int i = 0, product_count = 0; i < num_digits; ++i) {
            for (int j = i, p = 1; j < num_digits; ++j) {
                p *= digits[j];
                for (int k = 0; k < product_count; ++k) {
                    if (products[k] == p)
                        return false;
                }
                products[product_count++] = p;
            }
        }
        return true;
    }

    private void countColorful(int taken, int n, int digits) {
        if (taken == 0) {
            for (int d = 0; d < 10; ++d) {
                used[d] = true;
                countColorful(d < 2 ? 9 : 1, d, 1);
                used[d] = false;
            }
        } else {
            if (isColorful(n)) {
                ++count[digits - 1];
                if (n > largest)
                    largest = n;
            }
            if (taken < 9) {
                for (int d = 2; d < 10; ++d) {
                    if (!used[d]) {
                        used[d] = true;
                        countColorful(taken + 1, n * 10 + d, digits + 1);
                        used[d] = false;
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
from math import prod

largest = [0]

def iscolorful(n):
    if 0 <= n < 10:
        return True
    dig = [int(c) for c in str(n)]
    if 1 in dig or 0 in dig or len(dig) > len(set(dig)):
        return False
    products = list(set(dig))
    for i in range(len(dig)):
        for j in range(i+2, len(dig)+1):
            p = prod(dig[i:j])
            if p in products:
                return False
            products.append(p)

    largest[0] = max(n, largest[0])
    return True

print('Colorful numbers for 1:25, 26:50, 51:75, and 76:100:')
for i in range(1, 101, 25):
    for j in range(25):
        if iscolorful(i + j):
            print(f'{i + j: 5,}', end='')
    print()

csum = 0
for i in range(8):
    j = 0 if i == 0 else 10**i
    k = 10**(i+1) - 1
    n = sum(iscolorful(x) for x in range(j, k+1))
    csum += n
    print(f'The count of colorful numbers between {j} and {k} is {n}.')

print(f'The largest possible colorful number is {largest[0]}.')
print(f'The total number of colorful numbers is {csum}.')

```

