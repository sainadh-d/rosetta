# Nautical bell

## Task Link
[Rosetta Code - Nautical bell](https://rosettacode.org/wiki/Nautical_bell)

## Java Code
### java_code_1.txt
```java
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.TimeZone;

public class NauticalBell extends Thread {

    public static void main(String[] args) {
        NauticalBell bells = new NauticalBell();
        bells.setDaemon(true);
        bells.start();
        try {
            bells.join();
        } catch (InterruptedException e) {
            System.out.println(e);
        }
    }

    @Override
    public void run() {
        DateFormat sdf = new SimpleDateFormat("HH:mm:ss");
        sdf.setTimeZone(TimeZone.getTimeZone("UTC"));

        int numBells = 0;
        long time = System.currentTimeMillis();
        long next = time - (time % (24 * 60 * 60 * 1000)); // midnight

        while (next < time) {
            next += 30 * 60 * 1000; // 30 minutes
            numBells = 1 + (numBells % 8);
        }

        while (true) {
            long wait = 100L;
            time = System.currentTimeMillis();
            if (time - next >= 0) {
                String bells = numBells == 1 ? "bell" : "bells";
                String timeString = sdf.format(time);
                System.out.printf("%s : %d %s\n", timeString, numBells, bells);
                next += 30 * 60 * 1000;
                wait = next - time;
                numBells = 1 + (numBells % 8);
            }
            try {
                Thread.sleep(wait);
            } catch (InterruptedException e) {
                return;
            }
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import time, calendar, sched, winsound

duration = 750      # Bell duration in ms
freq = 1280         # Bell frequency in hertz
bellchar = "\u2407"
watches = 'Middle,Morning,Forenoon,Afternoon,First/Last dog,First'.split(',')

def gap(n=1):
    time.sleep(n * duration / 1000)
off = gap
 
def on(n=1):
    winsound.Beep(freq, n * duration)
 
def bong():
    on(); off(0.5)

def bongs(m):
    for i in range(m):
        print(bellchar, end=' ')
        bong()
        if i % 2:
            print('  ', end='')
            off(0.5)
    print('')
        
scheds =  sched.scheduler(time.time, time.sleep)

def ships_bell(now=None):
    def adjust_to_half_hour(atime):
        atime[4] = (atime[4] // 30) * 30
        atime[5] = 0
        return atime

    debug = now is not None
    rightnow = time.gmtime()
    if not debug:
        now = adjust_to_half_hour( list(rightnow) )
    then = now[::]
    then[4] += 30
    hr, mn = now[3:5]
    watch, b = divmod(int(2 * hr + mn // 30 - 1), 8)
    b += 1
    bells = '%i bell%s' % (b, 's' if b > 1 else ' ')
    if debug:
        print("%02i:%02i, %-20s %s" % (now[3], now[4], watches[watch] + ' watch', bells), end=' ')
    else:
        print("%02i:%02i, %-20s %s" % (rightnow[3], rightnow[4], watches[watch] + ' watch', bells), end=' ')
    bongs(b)
    if not debug:
        scheds.enterabs(calendar.timegm(then), 0, ships_bell)
        #print(time.struct_time(then))
        scheds.run()

def dbg_tester():
    for h in range(24):
        for m in (0, 30):
            if (h,m) == (24,30): break
            ships_bell( [2013, 3, 2, h, m, 15, 5, 61, 0] )
        
    
if __name__ == '__main__':
    ships_bell()

```

