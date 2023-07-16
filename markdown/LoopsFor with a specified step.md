# Loops/For with a specified step

## Task Link
[Rosetta Code - Loops/For with a specified step](https://rosettacode.org/wiki/Loops/For_with_a_specified_step)

## Java Code
### java_code_1.txt
```java
for(int i = 2; i <= 8;i += 2){
   System.out.print(i + ", ");
}
System.out.println("who do we appreciate?");

```

## Python Code
### python_code_1.txt
```python
for i in xrange(2, 9, 2):
    print "%d," % i,
print "who do we appreciate?"

```

### python_code_2.txt
```python
for i in range(2, 9, 2):
    print("%d, " % i, end="")
print("who do we appreciate?")

```

