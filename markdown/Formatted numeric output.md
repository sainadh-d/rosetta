# Formatted numeric output

## Task Link
[Rosetta Code - Formatted numeric output](https://rosettacode.org/wiki/Formatted_numeric_output)

## Java Code
### java_code_1.txt
```java
public class Printing{
	public static void main(String[] args){
		double value = 7.125;
		System.out.printf("%09.3f",value); // System.out.format works the same way
		System.out.println(String.format("%09.3f",value));
	}
}

```

### java_code_2.txt
```java
import java.text.DecimalFormat;
import java.text.NumberFormat;

public class Format {
	public static void main(String[] args){
		NumberFormat numForm = new DecimalFormat();
		numForm.setMinimumIntegerDigits(9);
		//Maximum also available for Integer digits and Fraction digits
		numForm.setGroupingUsed(false);//stops it from inserting commas
		System.out.println(numForm.format(7.125));
		
		//example of Fraction digit options
		numForm.setMinimumIntegerDigits(5);
		numForm.setMinimumFractionDigits(5);
		System.out.println(numForm.format(7.125));
		numForm.setMinimumFractionDigits(0);
		numForm.setMaximumFractionDigits(2);
		System.out.println(numForm.format(7.125));
		System.out.println(numForm.format(7.135));//rounds to even
	}
}

```

## Python Code
### python_code_1.txt
```python
from math import pi, exp
r = exp(pi)-pi
print r
print "e=%e f=%f g=%g G=%G s=%s r=%r!"%(r,r,r,r,r,r)
print "e=%9.4e f=%9.4f g=%9.4g!"%(-r,-r,-r)
print "e=%9.4e f=%9.4f g=%9.4g!"%(r,r,r)
print "e=%-9.4e f=%-9.4f g=%-9.4g!"%(r,r,r)
print "e=%09.4e f=%09.4f g=%09.4g!"%(-r,-r,-r)
print "e=%09.4e f=%09.4f g=%09.4g!"%(r,r,r)
print "e=%-09.4e f=%-09.4f g=%-09.4g!"%(r,r,r)

```

### python_code_2.txt
```python
from math import pi, exp
r = exp(pi)-pi
print(r)
print("e={0:e} f={0:f} g={0:g} G={0:G} s={0!s} r={0!r}!".format(r))
print("e={0:9.4e} f={0:9.4f} g={0:9.4g}!".format(-r))
print("e={0:9.4e} f={0:9.4f} g={0:9.4g}!".format(r))
print("e={0:-9.4e} f={0:-9.4f} g={0:-9.4g}!".format(r))
print("e={0:09.4e} f={0:09.4f} g={0:09.4g}!".format(-r))
print("e={0:09.4e} f={0:09.4f} g={0:09.4g}!".format(r))
print("e={0:-09.4e} f={0:-09.4f} g={0:-09.4g}!".format(r))

```

