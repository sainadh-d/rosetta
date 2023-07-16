# ISBN13 check digit

## Task Link
[Rosetta Code - ISBN13 check digit](https://rosettacode.org/wiki/ISBN13_check_digit)

## Java Code
### java_code_1.txt
```java
public static void main(String[] args) {
    String[] isbn13s = {
        "978-0596528126",
        "978-0596528120",
        "978-1788399081",
        "978-1788399083"
    };
    for (String isbn13 : isbn13s)
        System.out.printf("%s %b%n", isbn13, validateISBN13(isbn13));
}

static boolean validateISBN13(String string) {
    int[] digits = digits(string.strip().replace("-", ""));
    return digits[12] == checksum(digits);
}

static int[] digits(String string) {
    int[] digits = new int[13];
    int index = 0;
    for (char character : string.toCharArray()) {
        if (character < '0' || character > '9')
            throw new IllegalArgumentException("Invalid ISBN-13");
        /* convert ascii to integer */
        digits[index++] = Character.digit(character, 10);
    }
    return digits;
}

static int checksum(int[] digits) {
    int total = 0;
    int index = 0;
    for (int digit : digits) {
        if (index == 12) break;
        if (index++ % 2 == 1) digit *= 3;
        total += digit;
    }
    return 10 - (total % 10);
}

```

### java_code_2.txt
```java
public static void main(){
        System.out.println(isISBN13("978-1734314502"));
        System.out.println(isISBN13("978-1734314509"));
        System.out.println(isISBN13("978-1788399081"));
        System.out.println(isISBN13("978-1788399083"));
    }
public static boolean isISBN13(String in){
        int pre = Integer.parseInt(in.substring(0,3));
        if (pre!=978)return false;
        String postStr = in.substring(4);
        if (postStr.length()!=10)return false;
        int post = Integer.parseInt(postStr);
        int sum = 38;
        for(int x = 0; x<10;x+=2)
        sum += (postStr.charAt(x)-48)*3 + ((postStr.charAt(x+1)-48));
        if(sum%10==0) return true;
        return false;
    }

```

## Python Code
### python_code_1.txt
```python
def is_isbn13(n):
    n = n.replace('-','').replace(' ', '')
    if len(n) != 13:
        return False
    product = (sum(int(ch) for ch in n[::2]) 
               + sum(int(ch) * 3 for ch in n[1::2]))
    return product % 10 == 0

if __name__ == '__main__':
    tests = '''
978-1734314502
978-1734314509
978-1788399081
978-1788399083'''.strip().split()
    for t in tests:
        print(f"ISBN13 {t} validates {is_isbn13(t)}")

```

### python_code_2.txt
```python
'''ISBN13 check digit'''


from itertools import cycle


# isISBN13 :: String -> Bool
def isISBN13(s):
    '''True if s is a valid ISBN13 string
    '''
    digits = [int(c) for c in s if c.isdigit()]
    return 13 == len(digits) and (
        0 == sum(map(
            lambda f, x: f(x),
            cycle([
                lambda x: x,
                lambda x: 3 * x
            ]),
            digits
        )) % 10
    )


# ------------------------- TEST -------------------------
# main :: IO ()
def main():
    '''Test strings for ISBN-13 validity.'''

    print('\n'.join(
        repr((s, isISBN13(s))) for s
        in ["978-1734314502",
            "978-1734314509",
            "978-1788399081",
            "978-1788399083"
            ]
    ))


# MAIN ---
if __name__ == '__main__':
    main()

```

