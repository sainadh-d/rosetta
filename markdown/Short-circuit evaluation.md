# Short-circuit evaluation

## Task Link
[Rosetta Code - Short-circuit evaluation](https://rosettacode.org/wiki/Short-circuit_evaluation)

## Java Code
### java_code_2.txt
```java
public class ShortCirc {
    public static void main(String[] args){
        System.out.println("F and F = " + (a(false) && b(false)) + "\n");
        System.out.println("F or F = " + (a(false) || b(false)) + "\n");

        System.out.println("F and T = " + (a(false) && b(true)) + "\n");
        System.out.println("F or T = " + (a(false) || b(true)) + "\n");

        System.out.println("T and F = " + (a(true) && b(false)) + "\n");
        System.out.println("T or F = " + (a(true) || b(false)) + "\n");

        System.out.println("T and T = " + (a(true) && b(true)) + "\n");
        System.out.println("T or T = " + (a(true) || b(true)) + "\n");
    }

    public static boolean a(boolean a){
        System.out.println("a");
        return a;
    }

    public static boolean b(boolean b){
        System.out.println("b");
        return b;
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def a(answer):
	print("  # Called function a(%r) -> %r" % (answer, answer))
	return answer

>>> def b(answer):
	print("  # Called function b(%r) -> %r" % (answer, answer))
	return answer

>>> for i in (False, True):
	for j in (False, True):
		print ("\nCalculating: x = a(i) and b(j)")
		x = a(i) and b(j)
		print ("Calculating: y = a(i) or  b(j)")
		y = a(i) or  b(j)

		

Calculating: x = a(i) and b(j)
  # Called function a(False) -> False
Calculating: y = a(i) or  b(j)
  # Called function a(False) -> False
  # Called function b(False) -> False

Calculating: x = a(i) and b(j)
  # Called function a(False) -> False
Calculating: y = a(i) or  b(j)
  # Called function a(False) -> False
  # Called function b(True) -> True

Calculating: x = a(i) and b(j)
  # Called function a(True) -> True
  # Called function b(False) -> False
Calculating: y = a(i) or  b(j)
  # Called function a(True) -> True

Calculating: x = a(i) and b(j)
  # Called function a(True) -> True
  # Called function b(True) -> True
Calculating: y = a(i) or  b(j)
  # Called function a(True) -> True

```

### python_code_2.txt
```python
>>> for i in (False, True):
	for j in (False, True):
		print ("\nCalculating: x = a(i) and b(j) using x = b(j) if a(i) else False")
		x = b(j) if a(i) else False
		print ("Calculating: y = a(i) or  b(j) using y = b(j) if not a(i) else True")
		y = b(j) if not a(i) else True

		

Calculating: x = a(i) and b(j) using x = b(j) if a(i) else False
  # Called function a(False) -> False
Calculating: y = a(i) or  b(j) using y = b(j) if not a(i) else True
  # Called function a(False) -> False
  # Called function b(False) -> False

Calculating: x = a(i) and b(j) using x = b(j) if a(i) else False
  # Called function a(False) -> False
Calculating: y = a(i) or  b(j) using y = b(j) if not a(i) else True
  # Called function a(False) -> False
  # Called function b(True) -> True

Calculating: x = a(i) and b(j) using x = b(j) if a(i) else False
  # Called function a(True) -> True
  # Called function b(False) -> False
Calculating: y = a(i) or  b(j) using y = b(j) if not a(i) else True
  # Called function a(True) -> True

Calculating: x = a(i) and b(j) using x = b(j) if a(i) else False
  # Called function a(True) -> True
  # Called function b(True) -> True
Calculating: y = a(i) or  b(j) using y = b(j) if not a(i) else True
  # Called function a(True) -> True

```

