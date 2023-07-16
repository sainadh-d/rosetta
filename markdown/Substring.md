# Substring

## Task Link
[Rosetta Code - Substring](https://rosettacode.org/wiki/Substring)

## Java Code
### java_code_1.txt
```java
public static String Substring(String str, int n, int m){
    return str.substring(n, n+m);
}
public static String Substring(String str, int n){
    return str.substring(n);
}
public static String Substring(String str){
    return str.substring(0, str.length()-1);
}
public static String Substring(String str, char c, int m){
    return str.substring(str.indexOf(c), str.indexOf(c)+m+1);
}
public static String Substring(String str, String sub, int m){
    return str.substring(str.indexOf(sub), str.indexOf(sub)+m+1);
}

```

## Python Code
### python_code_1.txt
```python
>>> s = 'abcdefgh'
>>> n, m, char, chars = 2, 3, 'd', 'cd'
>>> # starting from n=2 characters in and m=3 in length;
>>> s[n-1:n+m-1]
'bcd'
>>> # starting from n characters in, up to the end of the string;
>>> s[n-1:]
'bcdefgh'
>>> # whole string minus last character;
>>> s[:-1]
'abcdefg'
>>> # starting from a known character char="d" within the string and of m length;
>>> indx = s.index(char)
>>> s[indx:indx+m]
'def'
>>> # starting from a known substring chars="cd" within the string and of m length. 
>>> indx = s.index(chars)
>>> s[indx:indx+m]
'cde'
>>>

```

### python_code_2.txt
```python
s <- "abcdefgh"
s.0
=> "a"

# starting from n characters in and of m length;
def (substr s start len)
  (s start start+len)
(substr s 3 2)
=> "de"

# starting from n characters in, up to the end of the string
(s 3 nil)
=> "defgh"

# whole string minus last character;
(s 3 -1)
=> "defg"

# starting from a known character within the string and of <tt>m</tt> length;
# starting from a known substring within the string and of <tt>m</tt> length.
let start (pos s pat)
  (s start start+m)

```

