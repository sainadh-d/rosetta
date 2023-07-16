# Disarium numbers

## Task Link
[Rosetta Code - Disarium numbers](https://rosettacode.org/wiki/Disarium_numbers)

## Java Code
### java_code_1.txt
```java
import java.lang.Math;

public class DisariumNumbers {
    public static boolean is_disarium(int num) {
        int n = num;
        int len = Integer.toString(n).length();
        int sum = 0;
        int i = 1;
        while (n > 0) {
            sum += Math.pow(n % 10, len - i + 1);
            n /= 10;
            i ++;
        }
        return sum  == num;
    }

    public static void main(String[] args) {
        int i = 0;
        int count = 0;
        while (count <= 18) {
            if (is_disarium(i)) {
                System.out.printf("%d ", i);
                count++;
            }
            i++;
        }
        System.out.printf("%s", "\n");
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python

def isDisarium(n):
    digitos = len(str(n))
    suma = 0
    x = n
    while x != 0:
        suma += (x % 10) ** digitos
        digitos -= 1
        x //= 10
    if suma == n:
        return True
    else:
        return False

if __name__ == '__main__':
    limite = 19
    cont = 0
    n = 0
    print("The first",limite,"Disarium numbers are:")
    while cont < limite:
        if isDisarium(n):
            print(n, end = " ")
            cont += 1
        n += 1

```

