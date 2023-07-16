# Loops/N plus one half

## Task Link
[Rosetta Code - Loops/N plus one half](https://rosettacode.org/wiki/Loops/N_plus_one_half)

## Java Code
### java_code_1.txt
```java
var out = System.out
for(i in 1..10) {
  if(i > 1) out.print(", ")
  out.print(i)
}

```

### java_code_2.txt
```java
public static void main(String[] args) {
    for (int i = 1; ; i++) {
        System.out.print(i);
        if (i == 10)
            break;
        System.out.print(", ");
    }
    System.out.println();
}

```

## Python Code
### python_code_1.txt
```python
print ( ', '.join(str(i+1) for i in range(10)) )

```

### python_code_2.txt
```python
>>> from sys import stdout
>>> write = stdout.write
>>> n, i = 10, 1
>>> while True:
    write(i)
    i += 1
    if i > n:
        break
    write(', ')

    
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
>>>

```

### python_code_3.txt
```python
[print(str(i+1) + ", ",end='') if i < 9 else print(i+1) for i in range(10)]

```

### python_code_4.txt
```python
n, i = 10, 1
while True:
    print(i, end="")
    i += 1
    if i > n:
        break
    print(", ", end="")

```

