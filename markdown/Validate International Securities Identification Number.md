# Validate International Securities Identification Number

## Task Link
[Rosetta Code - Validate International Securities Identification Number](https://rosettacode.org/wiki/Validate_International_Securities_Identification_Number)

## Java Code
### java_code_1.txt
```java
public class ISIN {
 
    public static void main(String[] args) {
        String[] isins = {
            "US0378331005", 
            "US0373831005", 
            "U50378331005", 
            "US03378331005",
            "AU0000XVGZA3", 
            "AU0000VXGZA3", 
            "FR0000988040"
        };
        for (String isin : isins)
            System.out.printf("%s is %s\n", isin, ISINtest(isin) ? "valid" : "not valid");
    }
 
    static boolean ISINtest(String isin) {
        isin = isin.trim().toUpperCase();
 
        if (!isin.matches("^[A-Z]{2}[A-Z0-9]{9}\\d$"))
            return false;
 
        StringBuilder sb = new StringBuilder();
        for (char c : isin.substring(0, 12).toCharArray())
            sb.append(Character.digit(c, 36));
 
        return luhnTest(sb.toString());
    }

    static boolean luhnTest(String number) {
        int s1 = 0, s2 = 0;
        String reverse = new StringBuffer(number).reverse().toString();
        for (int i = 0; i < reverse.length(); i++){
            int digit = Character.digit(reverse.charAt(i), 10);
            //This is for odd digits, they are 1-indexed in the algorithm.
            if (i % 2 == 0){
                s1 += digit;
            } else { // Add 2 * digit for 0-4, add 2 * digit - 9 for 5-9.
                s2 += 2 * digit;
                if(digit >= 5){
                    s2 -= 9;
                }
            }
        }
        return (s1 + s2) % 10 == 0;
    }
}

```

## Python Code
### python_code_1.txt
```python
def check_isin(a):
    if len(a) != 12 or not all(c.isalpha() for c in a[:2]) or not all(c.isalnum() for c in a[2:]):
        return False
    s = "".join(str(int(c, 36)) for c in a)
    return 0 == (sum(sum(divmod(2 * (ord(c) - 48), 10)) for c in s[-2::-2]) +
                 sum(ord(c) - 48 for c in s[::-2])) % 10

# A more readable version 
def check_isin_alt(a):
    if len(a) != 12:
        return False
    s = []
    for i, c in enumerate(a):
        if c.isdigit():
            if i < 2:
                return False
            s.append(ord(c) - 48)
        elif c.isupper():
            if i == 11:
                return False
            s += divmod(ord(c) - 55, 10)
        else:
            return False
    v = sum(s[::-2])
    for k in s[-2::-2]:
        k = 2 * k
        v += k - 9 if k > 9 else k
    return v % 10 == 0

[check_isin(s) for s in ["US0378331005", "US0373831005", "U50378331005", "US03378331005",
                         "AU0000XVGZA3", "AU0000VXGZA3", "FR0000988040"]]

# [True, False, False, False, True, True, True]

```

