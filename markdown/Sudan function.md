# Sudan function

## Task Link
[Rosetta Code - Sudan function](https://rosettacode.org/wiki/Sudan_function)

## Java Code
### java_code_1.txt
```java
//Aamrun, 11th July 2022

public class Main {

  private static int F(int n,int x,int y) {
  	if (n == 0) {
    	return x + y;
  	}
 
 	 else if (y == 0) {
    	return x;
  	}
 
  	return F(n - 1, F(n, x, y - 1), F(n, x, y - 1) + y);
 }

  public static void main(String[] args) {
    System.out.println("F(1,3,3) = " + F(1,3,3));
  }
}

```

## Python Code
### python_code_1.txt
```python
# Aamrun, 11th July 2022

def F(n,x,y):
  if n==0:
    return x + y
  elif y==0:
    return x
  else:
    return F(n - 1, F(n, x, y - 1), F(n, x, y - 1) + y)
    
    
print("F(1,3,3) = ", F(1,3,3))

```

