# Sorting algorithms/Sleep sort

## Task Link
[Rosetta Code - Sorting algorithms/Sleep sort](https://rosettacode.org/wiki/Sorting_algorithms/Sleep_sort)

## Java Code
### java_code_1.txt
```java
import java.util.concurrent.CountDownLatch;

public class SleepSort {
	public static void sleepSortAndPrint(int[] nums) {
		final CountDownLatch doneSignal = new CountDownLatch(nums.length);
		for (final int num : nums) {
			new Thread(new Runnable() {
				public void run() {
					doneSignal.countDown();
					try {
						doneSignal.await();

						//using straight milliseconds produces unpredictable
						//results with small numbers
						//using 1000 here gives a nifty demonstration
						Thread.sleep(num * 1000);
						System.out.println(num);
					} catch (InterruptedException e) {
						e.printStackTrace();
					}
				}
			}).start();
		}
	}
	public static void main(String[] args) {
		int[] nums = new int[args.length];
		for (int i = 0; i < args.length; i++)
			nums[i] = Integer.parseInt(args[i]);
		sleepSortAndPrint(nums);
	}
}

```

## Python Code
### python_code_1.txt
```python
from time import sleep
from threading import Timer

def sleepsort(values):
    sleepsort.result = []
    def add1(x):
        sleepsort.result.append(x)
    mx = values[0]
    for v in values:
        if mx < v: mx = v
        Timer(v, add1, [v]).start()
    sleep(mx+1)
    return sleepsort.result

if __name__ == '__main__':
    x = [3,2,4,7,3,6,9,1]
    if sleepsort(x) == sorted(x):
        print('sleep sort worked for:',x)
    else:
        print('sleep sort FAILED for:',x)

```

### python_code_2.txt
```python
#!/usr/bin/env python3
from asyncio import run, sleep, wait
from sys import argv

async def f(n):
    await sleep(n)
    print(n)

if __name__ == '__main__': 
    run(wait(map(f, map(int, argv[1:]))))

```

