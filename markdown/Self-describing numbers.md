# Self-describing numbers

## Task Link
[Rosetta Code - Self-describing numbers](https://rosettacode.org/wiki/Self-describing_numbers)

## Java Code
### java_code_1.txt
```java
public class SelfDescribingNumbers{
    public static boolean isSelfDescribing(int a){
        String s = Integer.toString(a);
        for(int i = 0; i < s.length(); i++){
            String s0 = s.charAt(i) + "";
            int b = Integer.parseInt(s0); // number of times i-th digit must occur for it to be a self describing number
            int count = 0;
            for(int j = 0; j < s.length(); j++){
                int temp = Integer.parseInt(s.charAt(j) + "");
                if(temp == i){
                    count++;
                }
                if (count > b) return false;
            }
            if(count != b) return false;
        }
        return true;
    }

    public static void main(String[] args){
        for(int i = 0; i < 100000000; i++){
            if(isSelfDescribing(i)){
                System.out.println(i);
             }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def isSelfDescribing(n):
	s = str(n)
	return all(s.count(str(i)) == int(ch) for i, ch in enumerate(s))

>>> [x for x in range(4000000) if isSelfDescribing(x)]
[1210, 2020, 21200, 3211000]
>>> [(x, isSelfDescribing(x)) for x in (1210, 2020, 21200, 3211000, 42101000, 521001000, 6210001000)]
[(1210, True), (2020, True), (21200, True), (3211000, True), (42101000, True), (521001000, True), (6210001000, True)]

```

### python_code_2.txt
```python
def impl(d, c, m):
    if m < 0: return
    if d == c[:len(d)]: print d
    for i in range(c[len(d)],m+1):
        dd = d+[i]
        if i<len(dd) and c[i]==dd[i]: continue
        impl(dd,c[:i]+[c[i]+1]+c[i+1:],m-i)
 
def self(n): impl([], [0]*(n+1), n)
 
self(10)

```

