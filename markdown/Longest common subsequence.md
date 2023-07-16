# Longest common subsequence

## Task Link
[Rosetta Code - Longest common subsequence](https://rosettacode.org/wiki/Longest_common_subsequence)

## Java Code
### java_code_1.txt
```java
public static String lcs(String a, String b){
    int aLen = a.length();
    int bLen = b.length();
    if(aLen == 0 || bLen == 0){
        return "";
    }else if(a.charAt(aLen-1) == b.charAt(bLen-1)){
        return lcs(a.substring(0,aLen-1),b.substring(0,bLen-1))
            + a.charAt(aLen-1);
    }else{
        String x = lcs(a, b.substring(0,bLen-1));
        String y = lcs(a.substring(0,aLen-1), b);
        return (x.length() > y.length()) ? x : y;
    }
}

```

### java_code_2.txt
```java
public static String lcs(String a, String b) {
    int[][] lengths = new int[a.length()+1][b.length()+1];

    // row 0 and column 0 are initialized to 0 already

    for (int i = 0; i < a.length(); i++)
        for (int j = 0; j < b.length(); j++)
            if (a.charAt(i) == b.charAt(j))
                lengths[i+1][j+1] = lengths[i][j] + 1;
            else
                lengths[i+1][j+1] =
                    Math.max(lengths[i+1][j], lengths[i][j+1]);

    // read the substring out from the matrix
    StringBuffer sb = new StringBuffer();
    for (int x = a.length(), y = b.length();
         x != 0 && y != 0; ) {
        if (lengths[x][y] == lengths[x-1][y])
            x--;
        else if (lengths[x][y] == lengths[x][y-1])
            y--;
        else {
            assert a.charAt(x-1) == b.charAt(y-1);
            sb.append(a.charAt(x-1));
            x--;
            y--;
        }
    }

    return sb.reverse().toString();
}

```

## Python Code
### python_code_1.txt
```python
def lcs(xstr, ystr):
    """
    >>> lcs('thisisatest', 'testing123testing')
    'tsitest'
    """
    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return str(lcs(xs, ys)) + x
    else:
        return max(lcs(xstr, ys), lcs(xs, ystr), key=len)

```

### python_code_2.txt
```python
if __name__=="__main__":
    import doctest; doctest.testmod()

```

### python_code_3.txt
```python
def lcs(a, b):
    # generate matrix of length of longest common subsequence for substrings of both words
    lengths = [[0] * (len(b)+1) for _ in range(len(a)+1)]
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])

    # read a substring from the matrix
    result = ''
    j = len(b)
    for i in range(1, len(a)+1):
        if lengths[i][j] != lengths[i-1][j]:
            result += a[i-1]

    return result

```

