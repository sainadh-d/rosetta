# Biorhythms

## Task Link
[Rosetta Code - Biorhythms](https://rosettacode.org/wiki/Biorhythms)

## Java Code
### java_code_1.txt
```java
import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.temporal.ChronoUnit;
import java.util.List;

public final class Biorythms {

	public static void main(String[] aArgs) {    
	    List<List<String>> datePairs = List.of(
	    	List.of( "1943-03-09", "1972-07-11" ),
	    	List.of( "1809-01-12", "1863-11-19" ),
	    	List.of( "1809-02-12", "1863-11-19" ));
	    
	    for ( List<String> datePair : datePairs ) {
	    	biorhythms(datePair);
	    }
	}
	
	private static void biorhythms(List<String> aDatePair) {
		DateTimeFormatter formatter = DateTimeFormatter.ISO_LOCAL_DATE;
	    LocalDate birthDate = LocalDate.parse(aDatePair.get(0), formatter);
	    LocalDate targetDate = LocalDate.parse(aDatePair.get(1), formatter);
	    final int daysBetween = (int) ChronoUnit.DAYS.between(birthDate, targetDate);
	    System.out.println("Birth date " + birthDate + ", Target date " + targetDate);
	    System.out.println("Days between: " + daysBetween);
	    
	    for ( Cycle cycle : Cycle.values() ) {
	        final int cycleLength = cycle.length();
	        final int positionInCycle = daysBetween % cycleLength;
	        final int quadrantIndex = 4 * positionInCycle / cycleLength;	        
	        final int percentage = (int) Math.round(100 * Math.sin(2 * Math.PI * positionInCycle / cycleLength));
	        
	        String description;
	        if ( percentage > 95 ) {
	        	description = "peak";
	        } else if ( percentage < -95 ) {
	        	description = "valley";
	        } else if ( Math.abs(percentage) < 5 ) {
	            description = "critical transition";
	        } else {
	        	final int daysToTransition = ( cycleLength * ( quadrantIndex + 1 ) / 4 ) - positionInCycle;
		        LocalDate transitionDate = targetDate.plusDays(daysToTransition);
		        List<String> descriptions = cycle.descriptions(quadrantIndex);
		        String trend = descriptions.get(0);
		        String nextTransition = descriptions.get(1);
	            description = percentage + "% (" + trend + ", next " + nextTransition + " " + transitionDate + ")";
	        }
	        
	        System.out.println(cycle + " day " + positionInCycle  + ": " + description);
	    }
	    System.out.println();
	}
	
	private enum Cycle {		
		PHYSICAL(23), EMOTIONAL(28), MENTAL(33);
		
		public int length() {
			return length;
		}
		
		public List<String> descriptions(int aNumber) {
			return DESCRIPTIONS.get(aNumber);
		}
				
		private Cycle(int aLength) {
			length = aLength;
		}	
		
		private final int length;
		
		private static final List<List<String>> DESCRIPTIONS = List.of(
			List.of( "up and rising", "peak" ), List.of( "up but falling", "transition" ),
		    List.of( "down and falling", "valley" ), List.of( "down but rising", "transition" )); 		
	}

}

```

## Python Code
### python_code_1.txt
```python
"""

Python implementation of

http://rosettacode.org/wiki/Biorhythms

"""

from datetime import date, timedelta
from math import floor, sin, pi

def biorhythms(birthdate,targetdate):
    """
    Print out biorhythm data for targetdate assuming you were
    born on birthdate.
    
    birthdate and targetdata are strings in this format:
    
    YYYY-MM-DD e.g. 1964-12-26
    """
    
    # print dates
    
    print("Born: "+birthdate+" Target: "+targetdate)    
    
    # convert to date types - Python 3.7 or later
    
    birthdate = date.fromisoformat(birthdate)
    targetdate = date.fromisoformat(targetdate)
    
    # days between
    
    days = (targetdate - birthdate).days
    
    print("Day: "+str(days))
    
    # cycle logic - mostly from Julia example
    
    cycle_labels = ["Physical", "Emotional", "Mental"]
    cycle_lengths = [23, 28, 33]
    quadrants = [("up and rising", "peak"), ("up but falling", "transition"),
                   ("down and falling", "valley"), ("down but rising", "transition")]
    
    for i in range(3):
        label = cycle_labels[i]
        length = cycle_lengths[i]
        position = days % length
        quadrant = int(floor((4 * position) / length))
        percentage = int(round(100 * sin(2 * pi * position / length),0))
        transition_date = targetdate + timedelta(days=floor((quadrant + 1)/4 * length) - position)
        trend, next = quadrants[quadrant]
        
        if percentage > 95:
            description = "peak"
        elif percentage < -95:
             description = "valley"
        elif abs(percentage) < 5:
             description = "critical transition"
        else:
             description = str(percentage)+"% ("+trend+", next "+next+" "+str(transition_date)+")"
        print(label+" day "+str(position)+": "+description)
    
    
biorhythms("1943-03-09","1972-07-11")

```

