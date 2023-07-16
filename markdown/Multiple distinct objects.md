# Multiple distinct objects

## Task Link
[Rosetta Code - Multiple distinct objects](https://rosettacode.org/wiki/Multiple_distinct_objects)

## Java Code
### java_code_1.txt
```java
Foo[] foos = new Foo[n]; // all elements initialized to null
for (int i = 0; i < foos.length; i++)
    foos[i] = new Foo();

// incorrect version:
Foo[] foos_WRONG = new Foo[n];
Arrays.fill(foos, new Foo());  // new Foo() only evaluated once

```

### java_code_2.txt
```java
List<Foo> foos = new ArrayList<Foo>();
for (int i = 0; i < n; i++)
    foos.add(new Foo());

// incorrect:
List<Foo> foos_WRONG = Collections.nCopies(n, new Foo());  // new Foo() only evaluated once

```

### java_code_3.txt
```java
public static <E> List<E> getNNewObjects(int n, Class<? extends E> c){
	List<E> ans = new LinkedList<E>();
	try {
		for(int i=0;i<n;i++)
			ans.add(c.newInstance());//can't call new on a class object
	} catch (InstantiationException e) {
		e.printStackTrace();
	} catch (IllegalAccessException e) {
		e.printStackTrace();
	}
	return ans;
}

public static List<Object> getNNewObjects(int n, String className)
throws ClassNotFoundException{
	return getNNewObjects(n, Class.forName(className));
}

```

## Python Code
### python_code_1.txt
```python
[Foo()] * n # here Foo() can be any expression that returns a new object

```

### python_code_2.txt
```python
[Foo() for i in range(n)]

```

