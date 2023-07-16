# Loops/While

## Task Link
[Rosetta Code - Loops/While](https://rosettacode.org/wiki/Loops/While)

## Java Code
### java_code_1.txt
```java
int i = 1024;
while(i > 0){
   System.out.println(i);
   i >>= 1; //also acceptable: i /= 2;
}

```

### java_code_2.txt
```java
for(int i = 1024; i > 0;i /= 2 /*or i>>= 1*/){
   System.out.println(i);
}

```

## Python Code
### python_code_1.txt
```python
n = 1024
while n > 0:
    print n
    n //= 2

```

