# Loops/Wrong ranges

## Task Link
[Rosetta Code - Loops/Wrong ranges](https://rosettacode.org/wiki/Loops/Wrong_ranges)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;

public class LoopsWrongRanges {

    public static void main(String[] args) {
        runTest(new LoopTest(-2, 2, 1, "Normal"));
        runTest(new LoopTest(-2, 2, 0, "Zero increment"));
        runTest(new LoopTest(-2, 2, -1, "Increments away from stop value"));
        runTest(new LoopTest(-2, 2, 10, "First increment is beyond stop value"));
        runTest(new LoopTest(2, -2, 1, "Start more than stop: positive increment"));
        runTest(new LoopTest(2, 2, 1, "Start equal stop: positive increment"));
        runTest(new LoopTest(2, 2, -1, "Start equal stop: negative increment"));
        runTest(new LoopTest(2, 2, 0, "Start equal stop: zero increment"));
        runTest(new LoopTest(0, 0, 0, "Start equal stop equal zero: zero increment"));
    }
    
    private static void runTest(LoopTest loopTest) {
        List<Integer> values = new ArrayList<>();
        for (int i = loopTest.start ; i <= loopTest.stop ; i += loopTest.increment ) {
            values.add(i);
            if ( values.size() >= 10 ) {
                break;
            }
        }
        System.out.printf("%-45s %s%s%n", loopTest.comment, values, values.size()==10 ? " (loops forever)" : "");
    }
    
    private static class LoopTest {
        int start;
        int stop;
        int increment;
        String comment;
        public LoopTest(int start, int stop, int increment, String comment) {
            this.start = start;
            this.stop = stop;
            this.increment = increment;
            this.comment = comment;
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
import re
from itertools import islice # To limit execution if it would generate huge values 
# list(islice('ABCDEFG', 2)) --> ['A', 'B']
# list(islice('ABCDEFG', 4)) --> ['A', 'B', 'C', 'D']


data = '''
start 	stop 	increment 	Comment
-2 	2 	1 	Normal
-2 	2 	0 	Zero increment
-2 	2 	-1 	Increments away from stop value
-2 	2 	10 	First increment is beyond stop value
2 	-2 	1 	Start more than stop: positive increment
2 	2 	1 	Start equal stop: positive increment
2 	2 	-1 	Start equal stop: negative increment
2 	2 	0 	Start equal stop: zero increment
0 	0 	0 	Start equal stop equal zero: zero increment 
'''

table = [re.split(r'\s\s+', line.strip()) for line in data.strip().split('\n')]
#%%
for _start, _stop, _increment, comment in table[1:]:
    start, stop, increment = [int(x) for x in (_start, _stop, _increment)]
    print(f'{comment.upper()}:\n  range({start}, {stop}, {increment})')
    values = None
    try: 
        values = list(islice(range(start, stop, increment), 999))
    except ValueError as e:
        print('  !!ERROR!!', e)
    if values is not None:
        if len(values) < 22:
            print('    =', values)
        else:
            print('    =', str(values[:22])[:-1], '...')

```

