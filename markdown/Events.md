# Events

## Task Link
[Rosetta Code - Events](https://rosettacode.org/wiki/Events)

## Java Code
## Python Code
### python_code_1.txt
```python
import threading
import time


def wait_for_event(event):
    event.wait()
    print("Thread: Got event")

e = threading.Event()

t = threading.Thread(target=wait_for_event, args=(e,))
t.start()

print("Main: Waiting one second")
time.sleep(1.0)
print("Main: Setting event")
e.set()
time.sleep(1.0)
print("Main: Done")
t.join()

```

