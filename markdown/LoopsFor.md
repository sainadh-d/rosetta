# Loops/For

## Task Link
[Rosetta Code - Loops/For](https://rosettacode.org/wiki/Loops/For)

## Java Code
### java_code_1.txt
```java
for (Integer i = 0; i < 5; i++) {
    String line = '';

    for (Integer j = 0; j < i; j++) {
        line += '*';
    }

    System.debug(line);
}

List<String> lines = new List<String> {
    '*',
    '**',
    '***',
    '****',
    '*****'
};

for (String line : lines) {
    System.debug(line);
}

```

### java_code_2.txt
```java
for (int i = 0; i < 5; i++) {
   for (int j = 0; j <= i; j++) {
      System.out.print("*");
   }
   System.out.println();
}

```

### java_code_3.txt
```java
size( 105,120 );

for ( int i=20; i<=100; i+=20 )
   for ( int j=10; j<=i; j+=20 )
      text( "*", j,i );

```

## Python Code
### python_code_1.txt
```python
for i in 1..5:
  for j in 1..i:
    stdout.write("*")
  echo("")

```

### python_code_2.txt
```python
import sys
for i in xrange(5):
    for j in xrange(i+1):
        sys.stdout.write("*")
    print

```

### python_code_3.txt
```python
for i in range(1,6):
    print '*' * i

```

### python_code_4.txt
```python
print('\n'.join('*' * i for i in range(1, 6)))

```

