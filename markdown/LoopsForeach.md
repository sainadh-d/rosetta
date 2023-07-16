# Loops/Foreach

## Task Link
[Rosetta Code - Loops/Foreach](https://rosettacode.org/wiki/Loops/Foreach)

## Java Code
### java_code_2.txt
```java
Iterable<Type> collect;
...
for(Type i:collect){
   System.out.println(i);
}

```

### java_code_3.txt
```java
Iterable collect;
...
collect.forEach(o -> System.out.println(o));

```

## Python Code
### python_code_1.txt
```python
for i in collection:
   print i

```

### python_code_2.txt
```python
lines = words = characters = 0
f = open('somefile','r')
for eachline in f:
    lines += 1
    for eachword in eachline.split():
        words += 1
        for eachchar in eachword:
            characters += 1

print lines, words, characters

```

### python_code_3.txt
```python
d = {3: "Earth", 1: "Mercury", 4: "Mars", 2: "Venus"}
for k in sorted(d):
    print("%i: %s" % (k, d[k]))

d = {"London": "United Kingdom", "Berlin": "Germany", "Rome": "Italy", "Paris": "France"}
for k in sorted(d):
    print("%s: %s" % (k, d[k]))

```

### python_code_4.txt
```python
d = {"fortytwo": 42, 3.14159: "pi", 23: "twentythree", "zero": 0, 13: "thirteen"}
for k in sorted(d):
    print("%s: %s" % (k, d[k]))

```

