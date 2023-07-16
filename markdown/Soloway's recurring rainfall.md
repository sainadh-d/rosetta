# Soloway's recurring rainfall

## Task Link
[Rosetta Code - Soloway's recurring rainfall](https://rosettacode.org/wiki/Soloway%27s_recurring_rainfall)

## Java Code
### java_code_1.txt
```java
class recurringrainfall
{ 
	private static int GetNextInt()
	{
		while (true)
		{
			System.out.print("Enter rainfall int, 99999 to quit: ");
			String input = System.console().readLine();
        
			try
			{
				int n = Integer.parseInt(input);
				return n;
			}
			catch (Exception e)
			{
				System.out.println("Invalid input");
			}
		}
	}
	
    private static void recurringRainfall() {
		float currentAverage = 0;
		int currentEntryNumber = 0;
		
		while (true) {
			int entry = GetNextInt();
			
			if (entry == 99999)
				return;
			
			currentEntryNumber++;
			currentAverage = currentAverage + ((float)1/currentEntryNumber)*entry - ((float)1/currentEntryNumber)*currentAverage;
			
			System.out.println("New Average: " + currentAverage);
		}
    }
    
    public static void main(String args[]) { 
        recurringRainfall();
    } 
}

```

## Python Code
### python_code_1.txt
```python
import sys

def get_next_input():
    try:
        num = int(input("Enter rainfall int, 99999 to quit: "))
    except:
        print("Invalid input")
        return get_next_input()
    return num

current_average = 0.0
current_count = 0

while True:
    next = get_next_input()

    if next == 99999:
        sys.exit()
    else:
        current_count += 1
        current_average = current_average + (1.0/current_count)*next - (1.0/current_count)*current_average
        
        print("New average: ", current_average)

```

