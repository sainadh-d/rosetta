# Increment a numerical string

## Task Link
[Rosetta Code - Increment a numerical string](https://rosettacode.org/wiki/Increment_a_numerical_string)

## Java Code
### java_code_1.txt
```java
String s = "12345";
IntLiteral lit1 = new IntLiteral(s);
IntLiteral lit2 = 6789;
++lit1; // lit1=12346
++lit2; // lit2=6790

```

### java_code_2.txt
```java
String s = "12345";
s = String.valueOf(Integer.parseInt(s) + 1);

```

### java_code_3.txt
```java
String s = "123456789012345678901234567890.12345";
s = new BigDecimal(s).add(BigDecimal.ONE).toString();

```

## Python Code
### python_code_1.txt
```python
next = str(int('123') + 1)

```

### python_code_2.txt
```python
# Dropping or keeping any non-numerics in the string


# succString :: Bool -> String -> String
def succString(blnPruned):
    def go(x):
        try:
            return [str(1 + (float(x) if '.' in x else int(x)))]
        except ValueError:
            return [] if blnPruned else [x]
    return lambda s: ' '.join(concatMap(go)(s.split()))


# TEST ----------------------------------------------------
def main():
    print(
        '\n'.join(
            [succString(bln)(
                '41.0 pine martens in 1491 -1.5 mushrooms ≠ 136'
            ) for bln in [False, True]]
        )
    )


# GENERIC ---------------------------------------------------

# concatMap :: (a -> [b]) -> [a] -> [b]
def concatMap(f):
    return lambda xs: (
        [ys[0] for ys in [f(x) for x in xs] if ys]
    )


# MAIN ---
if __name__ == '__main__':
    main()

```

