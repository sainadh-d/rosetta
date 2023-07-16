# Seven-sided dice from five-sided dice

## Task Link
[Rosetta Code - Seven-sided dice from five-sided dice](https://rosettacode.org/wiki/Seven-sided_dice_from_five-sided_dice)

## Java Code
### java_code_1.txt
```java
import java.util.Random;
public class SevenSidedDice 
{
	private static final Random rnd = new Random();
	public static void main(String[] args)
	{
		SevenSidedDice now=new SevenSidedDice();
		System.out.println("Random number from 1 to 7: "+now.seven());
	}
	int seven()
	{
		int v=21;
		while(v>20)
			v=five()+five()*5-6;
		return 1+v%7;
	}
	int five()
	{
		return 1+rnd.nextInt(5);
	}
}

```

## Python Code
### python_code_1.txt
```python
from random import randint

def dice5():
    return randint(1, 5)

def dice7():
    r = dice5() + dice5() * 5 - 6
    return (r % 7) + 1 if r < 21 else dice7()

```

