# Mouse position

## Task Link
[Rosetta Code - Mouse position](https://rosettacode.org/wiki/Mouse_position)

## Java Code
### java_code_1.txt
```java
Point mouseLocation = MouseInfo.getPointerInfo().getLocation();

```

### java_code_2.txt
```java
void setup(){
    size(640, 480);
}

void draw(){
  // mouseX and mouseY provide the current mouse position
  ellipse(mouseX, mouseY, 5, 5); // graphic output example
  println("x:" + mouseX + " y:" + mouseY);
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    size(640, 480)

def draw():
    # mouseX and mouseY provide the current mouse position
    ellipse(mouseX, mouseY, 5, 5) # graphic output example
    println("x:{} y:{}".format(mouseX, mouseY))

```

### python_code_2.txt
```python
import Tkinter as tk

def showxy(event):
    xm, ym = event.x, event.y
    str1 = "mouse at x=%d  y=%d" % (xm, ym)
    # show cordinates in title
    root.title(str1)
    # switch color to red if mouse enters a set location range
    x,y, delta = 100, 100, 10
    frame.config(bg='red'
                 if abs(xm - x) < delta and abs(ym - y) < delta
                 else 'yellow')

root = tk.Tk()
frame = tk.Frame(root, bg= 'yellow', width=300, height=200)
frame.bind("<Motion>", showxy)
frame.pack()

root.mainloop()

```

### python_code_3.txt
```python
#simple way of ,get cursor xy data

from Tkinter import *
win=Tk()
win.geometry("200x300")
def xy(event):
    xm, ym = event.x, event.y
    xy_data = "x=%d  y=%d" % (xm, ym)
    lab=Label(win,text=xy_data)
    lab.grid(row=0,column=0)

win.bind("<Motion>",xy)
mainloop()

```

