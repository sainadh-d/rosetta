# Variadic function

## Task Link
[Rosetta Code - Variadic function](https://rosettacode.org/wiki/Variadic_function)

## Java Code
### java_code_2.txt
```java
public static void printAll(Object... things){
   // "things" is an Object[]
   for(Object i:things){
      System.out.println(i);
   }
}

```

### java_code_3.txt
```java
printAll(4, 3, 5, 6, 4, 3);
printAll(4, 3, 5);
printAll("Rosetta", "Code", "Is", "Awesome!");

```

### java_code_4.txt
```java
Object[] args = {"Rosetta", "Code", "Is", "Awesome!"};
printAll(args);

```

### java_code_5.txt
```java
Object[] args = {"Rosetta", "Code", "Is", "Awesome,"};
printAll(args, "Dude!");//does not print "Rosetta Code Is Awesome, Dude!"
//instead prints the type and hashcode for args followed by "Dude!"

```

### java_code_6.txt
```java
printAll((Object)args);

```

## Python Code
### python_code_1.txt
```python
def print_all(*things):
    for x in things:
        print x

```

### python_code_2.txt
```python
print_all(4, 3, 5, 6, 4, 3)
print_all(4, 3, 5)
print_all("Rosetta", "Code", "Is", "Awesome!")

```

### python_code_3.txt
```python
args = ["Rosetta", "Code", "Is", "Awesome!"]
print_all(*args)

```

### python_code_4.txt
```python
>>> def printargs(*positionalargs, **keywordargs):
	print "POSITIONAL ARGS:\n  " + "\n  ".join(repr(x) for x in positionalargs)
	print "KEYWORD ARGS:\n  " + '\n  '.join(
		"%r = %r" % (k,v) for k,v in keywordargs.iteritems())

	
>>> printargs(1,'a',1+0j, fee='fi', fo='fum')
POSITIONAL ARGS:
  1
  'a'
  (1+0j)
KEYWORD ARGS:
  'fee' = 'fi'
  'fo' = 'fum'
>>> alist = [1,'a',1+0j]
>>> adict = {'fee':'fi', 'fo':'fum'}
>>> printargs(*alist, **adict)
POSITIONAL ARGS:
  1
  'a'
  (1+0j)
KEYWORD ARGS:
  'fee' = 'fi'
  'fo' = 'fum'
>>>

```

