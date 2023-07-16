# Loops/Continue

## Task Link
[Rosetta Code - Loops/Continue](https://rosettacode.org/wiki/Loops/Continue)

## Java Code
### java_code_1.txt
```java
for(int i = 1;i <= 10; i++){
   System.out.print(i);
   if(i % 5 == 0){
      System.out.println();
      continue;
   }
   System.out.print(", ");
}

```

## Python Code
### python_code_1.txt
```python
for i in range(1, 11):
    if i % 5 == 0:
        print(i)
        continue
    print(i, end=', ')

```

