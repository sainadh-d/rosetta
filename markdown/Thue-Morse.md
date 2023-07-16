# Thue-Morse

## Task Link
[Rosetta Code - Thue-Morse](https://rosettacode.org/wiki/Thue-Morse)

## Java Code
### java_code_1.txt
```java
public class ThueMorse {

    public static void main(String[] args) {
        sequence(6);
    }

    public static void sequence(int steps) {
        StringBuilder sb1 = new StringBuilder("0");
        StringBuilder sb2 = new StringBuilder("1");
        for (int i = 0; i < steps; i++) {
            String tmp = sb1.toString();
            sb1.append(sb2);
            sb2.append(tmp);
        }
        System.out.println(sb1);
    }
}

```

## Python Code
### python_code_1.txt
```python
m='0'
print(m)
for i in range(0,6):
     m0=m
     m=m.replace('0','a')
     m=m.replace('1','0')
     m=m.replace('a','1')
     m=m0+m
     print(m)

```

### python_code_2.txt
```python
>>> def thue_morse_digits(digits):
...     return  [bin(n).count('1') % 2 for n in range(digits)]
... 
>>> thue_morse_digits(20)
[0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1, 0, 0, 1]

>>>

```

### python_code_3.txt
```python
>>> def thue_morse_subs(chars):
...     ans = '0'
...     while len(ans) < chars:
...         ans = ans.replace('0', '0_').replace('1', '10').replace('_', '1')
...     return ans[:chars]
... 
>>> thue_morse_subs(20)
'01101001100101101001'
>>>

```

### python_code_4.txt
```python
>>> def thue_morse(n):
...     (v, i) = ('0', '1')
...     for _ in range(0,n):
...         (v, i) = (v + i, i + v)
...     return v
... 
>>> thue_morse(6)
'0110100110010110100101100110100110010110011010010110100110010110'
>>>

```

