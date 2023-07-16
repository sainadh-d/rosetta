# Active object

## Task Link
[Rosetta Code - Active object](https://rosettacode.org/wiki/Active_object)

## Java Code
### java_code_1.txt
```java
/**
 * Integrates input function K over time
 * S + (t1 - t0) * (K(t1) + K(t0)) / 2
 */
public class Integrator {

    public interface Function {
        double apply(double timeSinceStartInSeconds);
    }

    private final long start;
    private volatile boolean running;

    private Function func;
    private double t0;
    private double v0;
    private double sum;

    public Integrator(Function func) {
        this.start = System.nanoTime();
        setFunc(func);
        new Thread(this::integrate).start();
    }

    public void setFunc(Function func) {
        this.func = func;
        v0 = func.apply(0.0);
        t0 = 0;
    }

    public double getOutput() {
        return sum;
    }

    public void stop() {
        running = false;
    }

    private void integrate() {
        running = true;
        while (running) {
            try {
                Thread.sleep(1);
                update();
            } catch (InterruptedException e) {
                return;
            }
        }
    }

    private void update() {
        double t1 = (System.nanoTime() - start) / 1.0e9;
        double v1 = func.apply(t1);
        double rect = (t1 - t0) * (v0 + v1) / 2;
        this.sum += rect;
        t0 = t1;
        v0 = v1;
    }

    public static void main(String[] args) throws InterruptedException {
        Integrator integrator = new Integrator(t -> Math.sin(Math.PI * t));
        Thread.sleep(2000);

        integrator.setFunc(t -> 0.0);
        Thread.sleep(500);

        integrator.stop();
        System.out.println(integrator.getOutput());
    }
}

```

## Python Code
### python_code_1.txt
```python
from time import time, sleep
from threading import Thread

class Integrator(Thread):
    'continuously integrate a function `K`, at each `interval` seconds'
    def __init__(self, K=lambda t:0, interval=1e-4):
        Thread.__init__(self)
        self.interval  = interval
        self.K   = K
        self.S   = 0.0
        self.__run = True
        self.start()

    def run(self):
        "entry point for the thread"
        interval = self.interval
        start = time()
        t0, k0 = 0, self.K(0)
        while self.__run:
            sleep(interval)
            t1 = time() - start
            k1 = self.K(t1)
            self.S += (k1 + k0)*(t1 - t0)/2.0
            t0, k0 = t1, k1

    def join(self):
        self.__run = False
        Thread.join(self)

if __name__ == "__main__":
    from math import sin, pi
 
    ai = Integrator(lambda t: sin(pi*t))
    sleep(2)
    print(ai.S)
    ai.K = lambda t: 0
    sleep(0.5)
    print(ai.S)

```

