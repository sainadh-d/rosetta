# Introspection

## Task Link
[Rosetta Code - Introspection](https://rosettacode.org/wiki/Introspection)

## Java Code
### java_code_1.txt
```java
public class VersCheck {
	public static void main(String[] args) {
		String vers = System.getProperty("java.version");
		vers = vers.substring(0,vers.indexOf('.')) + "." +  //some String fiddling to get the version number into a usable form
			vers.substring(vers.indexOf('.')+1,vers.lastIndexOf('.'));
		if(Double.parseDouble(vers) >= 1.5){
			System.out.println("YAY!");
		}else{
			System.err.println("Must use Java >=1.5");
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
# Checking for system version
 import sys
 major, minor, bugfix = sys.version_info[:3]
 if major < 2:
     sys.exit('Python 2 is required')
 
 
 def defined(name): # LBYL (Look Before You Leap)
     return name in globals() or name in locals() or name in vars(__builtins__)

 def defined2(name): # EAFP (Easier to Ask Forgiveness than Permission)
     try:
          eval(name)
          return True
     except NameError:
          return False

 if defined('bloop') and defined('abs') and callable(abs):
     print abs(bloop)

 if defined2('bloop') and defined2('abs') and callable(abs):
     print abs(bloop)

```

### python_code_2.txt
```python
try:
    print abs(bloop)
except (NameError, TypeError):
    print "Something's missing"

```

### python_code_3.txt
```python
def sum_of_global_int_vars():
    variables = vars(__builtins__).copy()
    variables.update(globals())
    print sum(v for v in variables.itervalues() if type(v) == int)

sum_of_global_int_vars()

```

