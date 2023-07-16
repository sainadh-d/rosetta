# Averages/Simple moving average

## Task Link
[Rosetta Code - Averages/Simple moving average](https://rosettacode.org/wiki/Averages/Simple_moving_average)

## Java Code
### java_code_1.txt
```java
import java.util.LinkedList;
import java.util.Queue;

public class MovingAverage {
    private final Queue<Double> window = new LinkedList<Double>();
    private final int period;
    private double sum;

    public MovingAverage(int period) {
        assert period > 0 : "Period must be a positive integer";
        this.period = period;
    }

    public void newNum(double num) {
        sum += num;
        window.add(num);
        if (window.size() > period) {
            sum -= window.remove();
        }
    }

    public double getAvg() {
        if (window.isEmpty()) return 0.0; // technically the average is undefined
        return sum / window.size();
    }

    public static void main(String[] args) {
        double[] testData = {1, 2, 3, 4, 5, 5, 4, 3, 2, 1};
        int[] windowSizes = {3, 5};
        for (int windSize : windowSizes) {
            MovingAverage ma = new MovingAverage(windSize);
            for (double x : testData) {
                ma.newNum(x);
                System.out.println("Next number = " + x + ", SMA = " + ma.getAvg());
            }
            System.out.println();
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
from collections import deque

def simplemovingaverage(period):
    assert period == int(period) and period > 0, "Period must be an integer >0"
    
    summ = n = 0.0
    values = deque([0.0] * period)     # old value queue

    def sma(x):
        nonlocal summ, n
        
        values.append(x)
        summ += x - values.popleft()
        n = min(n+1, period)
        return summ / n

    return sma

```

### python_code_2.txt
```python
from collections import deque

class Simplemovingaverage():
    def __init__(self, period):
        assert period == int(period) and period > 0, "Period must be an integer >0"
        self.period = period
        self.stream = deque()
        
    def __call__(self, n):
        stream = self.stream
        stream.append(n)    # appends on the right
        streamlength = len(stream)
        if streamlength > self.period:
            stream.popleft()
            streamlength -= 1
        if streamlength == 0:
            average = 0
        else:
            average = sum( stream ) / streamlength

        return average

```

### python_code_3.txt
```python
if __name__ == '__main__':
    for period in [3, 5]:
        print ("\nSIMPLE MOVING AVERAGE (procedural): PERIOD =", period)
        sma = simplemovingaverage(period)
        for i in range(1,6):
            print ("  Next number = %-2g, SMA = %g " % (i, sma(i)))
        for i in range(5, 0, -1):
            print ("  Next number = %-2g, SMA = %g " % (i, sma(i)))
    for period in [3, 5]:
        print ("\nSIMPLE MOVING AVERAGE (class based): PERIOD =", period)
        sma = Simplemovingaverage(period)
        for i in range(1,6):
            print ("  Next number = %-2g, SMA = %g " % (i, sma(i)))
        for i in range(5, 0, -1):
            print ("  Next number = %-2g, SMA = %g " % (i, sma(i)))

```

