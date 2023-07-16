# Parametric polymorphism

## Task Link
[Rosetta Code - Parametric polymorphism](https://rosettacode.org/wiki/Parametric_polymorphism)

## Java Code
### java_code_1.txt
```java
public class Tree<T>{
	private T value;
	private Tree<T> left;
	private Tree<T> right;

	public void replaceAll(T value){
		this.value = value;
		if (left != null)
			left.replaceAll(value);
		if (right != null)
			right.replaceAll(value);
	}
}

```

## Python Code
