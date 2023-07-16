# Scope modifiers

## Task Link
[Rosetta Code - Scope modifiers](https://rosettacode.org/wiki/Scope_modifiers)

## Java Code
### java_code_1.txt
```java
public //any class may access this member directly

protected //only this class, subclasses of this class,
//and classes in the same package may access this member directly

private //only this class may access this member directly

static //for use with other modifiers
//limits this member to one reference for the entire JVM

//adding no modifier (sometimes called "friendly") allows access to the member by classes in the same package

// Modifier    | Class | Package | Subclass | World
// ------------|-------|---------|----------|-------
// public      |  Y    |    Y    |    Y     |   Y
// protected   |  Y    |    Y    |    Y     |   N
// no modifier |  Y    |    Y    |    N     |   N
// private     |  Y    |    N    |    N     |   N

//method parameters are available inside the entire method

//Other declarations follow lexical scoping,
//being in the scope of the innermost set of braces ({}) to them.
//You may also create local scopes by surrounding blocks of code with braces.

public void function(int x){
   //can use x here
   int y;
   //can use x and y here
   {
      int z;
      //can use x, y, and z here
   }
   //can use x and y here, but NOT z
}

```

## Python Code
### python_code_1.txt
```python
>>> x="From global scope"
>>> def outerfunc():
    x = "From scope at outerfunc"

    def scoped_local():
        x = "scope local"
        return "scoped_local scope gives x = " + x
    print(scoped_local())

    def scoped_nonlocal():
        nonlocal x
        return "scoped_nonlocal scope gives x = " + x
    print(scoped_nonlocal())

    def scoped_global():
        global x
        return "scoped_global scope gives x = " + x
    print(scoped_global())

    def scoped_notdefinedlocally():
        return "scoped_notdefinedlocally scope gives x = " + x
    print(scoped_notdefinedlocally())

    
>>> outerfunc()
scoped_local scope gives x = scope local
scoped_nonlocal scope gives x = From scope at outerfunc
scoped_global scope gives x = From global scope
scoped_notdefinedlocally scope gives x = From global scope
>>>

```

