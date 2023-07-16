# Stair-climbing puzzle

## Task Link
[Rosetta Code - Stair-climbing puzzle](https://rosettacode.org/wiki/Stair-climbing_puzzle)

## Java Code
### java_code_1.txt
```java
public void stepUp() {
  while (!step()) stepUp();
}

```

### java_code_2.txt
```java
public void stepUp(){
  for (int i = 0; i < 1; step() ? ++i : --i);
}

```

## Python Code
### python_code_1.txt
```python
def step_up1():
  """Straightforward implementation: keep track of how many level we
     need to ascend, and stop when this count is zero."""
  deficit = 1
  while deficit > 0:
    if step():
      deficit -= 1
    else:
      deficit += 1

```

### python_code_2.txt
```python
def step_up2():
  "No numbers."
  while not step():
    step_up2() # undo the fall

```

