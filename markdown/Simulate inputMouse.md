# Simulate input/Mouse

## Task Link
[Rosetta Code - Simulate input/Mouse](https://rosettacode.org/wiki/Simulate_input/Mouse)

## Java Code
### java_code_1.txt
```java
Point p = component.getLocation();
Robot robot = new Robot();
robot.mouseMove(p.getX(), p.getY()); //you may want to move a few pixels closer to the center by adding to these values
robot.mousePress(InputEvent.BUTTON1_MASK); //BUTTON1_MASK is the left button,
                                       //BUTTON2_MASK is the middle button, BUTTON3_MASK is the right button
robot.mouseRelease(InputEvent.BUTTON1_MASK);

```

### java_code_2.txt
```java
button.doClick(); //optionally, give an integer argument for the number of milliseconds to hold the button down

```

## Python Code
### python_code_1.txt
```python
import ctypes

def click():
    ctypes.windll.user32.mouse_event(0x2, 0,0,0,0)    # Mouse LClick Down, relative coords, dx=0, dy=0
    ctypes.windll.user32.mouse_event(0x4, 0,0,0,0)    # Mouse LClick Up, relative coords, dx=0, dy=0

click()

```

### python_code_2.txt
```python
import autopy
import math
import time
import random

TWO_PI = math.pi * 2.0


def sine_mouse_wave():
    """
    Moves the mouse in a sine wave from the left edge of the screen to 
    the right.
    """
    width, height = autopy.screen.get_size()
    height /= 2
    height -= 10  # Stay in the screen bounds.

    for x in xrange(width):
        y = int(height * math.sin((TWO_PI * x) / width) + height)
        autopy.mouse.move(x, y)
        time.sleep(random.uniform(0.001, 0.003))

sine_mouse_wave()

```

### python_code_3.txt
```python
import pyautogui

pyautogui.moveTo(100, 200)      # moves mouse to X of 100, Y of 200.
pyautogui.moveTo(None, 500)     # moves mouse to X of 100, Y of 500.
pyautogui.moveTo(600, None)     # moves mouse to X of 600, Y of 500.
pyautogui.moveTo(100, 200, 2)   # moves mouse to X of 100, Y of 200 over 2 seconds

pyautogui.moveRel(0, 50)        # move the mouse down 50 pixels.
pyautogui.moveRel(-30, 0)       # move the mouse left 30 pixels.

pyautogui.click()                          # Left button click on current position
pyautogui.click(clicks=2)
pyautogui.click(clicks=2, interval=0.25)   # with a quarter second pause in between clicks

pyautogui.click(10, 5)                     # Mouse left button click, x=10, y=5
pyautogui.click(200, 250, button='right')  # Mouse right button click, x=200, y=250

pyautogui.scroll(10)   # scroll up 10 "clicks"
pyautogui.scroll(10, x=100, y=100)  # move mouse cursor to 100, 200, then scroll up 10 "clicks"

```

