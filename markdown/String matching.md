# String matching

## Task Link
[Rosetta Code - String matching](https://rosettacode.org/wiki/String_matching)

## Java Code
### java_code_1.txt
```java
String string = "string matching";
String suffix = "ing";

```

### java_code_10.txt
```java
public class JavaApplication6 {
    public static void main(String[] args) {
        String strOne = "complexity";
        String strTwo = "udacity";
        stringMatch(strOne, strTwo);
    }

    public static void stringMatch(String one, String two) {
        boolean match = false;
        if (one.charAt(0) == two.charAt(0)) {
            System.out.println(match = true);   // returns true
        } else {
            System.out.println(match);       // returns false
        }
        for (int i = 0; i < two.length(); i++) {  
            int temp = i;
            for (int x = 0; x < one.length(); x++) {
                if (two.charAt(temp) == one.charAt(x)) {
                    System.out.println(match = true);    //returns true
                    i = two.length();
                }
            }
        }
        int num1 = one.length() - 1;
        int num2 = two.length() - 1;
        if (one.charAt(num1) == two.charAt(num2)) {
            System.out.println(match = true);
        } else {
            System.out.println(match = false);
        }
    }
}

```

### java_code_2.txt
```java
string.startsWith(suffix)

```

### java_code_3.txt
```java
string.substring(0, suffix.length()).equals(suffix)

```

### java_code_4.txt
```java
string.contains(suffix)

```

### java_code_5.txt
```java
string.indexOf(suffix) != -1

```

### java_code_6.txt
```java
string.endsWith(suffix);

```

### java_code_7.txt
```java
string.substring(string.length() - suffix.length()).equals(suffix)

```

### java_code_8.txt
```java
int indexOf;
int offset = 0;
while ((indexOf = string.indexOf(suffix, offset)) != -1) {
    System.out.printf("'%s' @ %d to %d%n", suffix, indexOf, indexOf + suffix.length() - 1);
    offset = indexOf + 1;
}

```

### java_code_9.txt
```java
"abcd".startsWith("ab") //returns true
"abcd".endsWith("zn") //returns false
"abab".contains("bb") //returns false
"abab".contains("ab") //returns true
int loc = "abab".indexOf("bb") //returns -1
loc = "abab".indexOf("ab") //returns 0
loc = "abab".indexOf("ab",loc+1) //returns 2

```

## Python Code
### python_code_1.txt
```python
"abcd".startswith("ab") #returns True
"abcd".endswith("zn") #returns False
"bb" in "abab" #returns False
"ab" in "abab" #returns True
loc = "abab".find("bb") #returns -1
loc = "abab".find("ab") #returns 0
loc = "abab".find("ab",loc+1) #returns 2

```

