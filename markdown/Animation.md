# Animation

## Task Link
[Rosetta Code - Animation](https://rosettacode.org/wiki/Animation)

## Java Code
### java_code_1.txt
```java
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Timer;
import java.util.TimerTask;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.WindowConstants;

public class Rotate {

    private static class State {
        private final String text = "Hello World! ";
        private int startIndex = 0;
        private boolean rotateRight = true;
    }

    public static void main(String[] args) {
        State state = new State();

        JLabel label = new JLabel(state.text);
        label.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent event) {
                state.rotateRight = !state.rotateRight;
            }
        });

        TimerTask task = new TimerTask() {
            public void run() {
                int delta = state.rotateRight ? 1 : -1;
                state.startIndex = (state.startIndex + state.text.length() + delta) % state.text.length();
                label.setText(rotate(state.text, state.startIndex));
            }
        };
        Timer timer = new Timer(false);
        timer.schedule(task, 0, 500);

        JFrame rot = new JFrame();
        rot.setDefaultCloseOperation(WindowConstants.DISPOSE_ON_CLOSE);
        rot.add(label);
        rot.pack();
        rot.setLocationRelativeTo(null);
        rot.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosed(WindowEvent e) {
                timer.cancel();
            }
        });
        rot.setVisible(true);
    }

    private static String rotate(String text, int startIdx) {
        char[] rotated = new char[text.length()];
        for (int i = 0; i < text.length(); i++) {
            rotated[i] = text.charAt((i + startIdx) % text.length());
        }
        return String.valueOf(rotated);
    }
}

```

## Python Code
### python_code_1.txt
```python
txt = "Hello, world! "
left = True

def draw():
    global txt
    background(128)
    text(txt, 10, height / 2)
    if frameCount % 10 == 0:
        if (left):
            txt = rotate(txt, 1)
        else:
            txt = rotate(txt, -1)
        println(txt)

def mouseReleased():
    global left
    left = not left

def rotate(text, startIdx):
    rotated = text[startIdx:] + text[:startIdx]
    return rotated

```

### python_code_2.txt
```python
#!/usr/bin/env python3
import sys

from PyQt5.QtCore import QBasicTimer, Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QLabel


class Marquee(QLabel):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.right_to_left_direction = True
        self.initUI()
        self.timer = QBasicTimer()
        self.timer.start(80, self)

    def initUI(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setText("Hello World! ")
        self.setFont(QFont(None, 50, QFont.Bold))
        # make more irritating for the authenticity with <marquee> element
        self.setStyleSheet("QLabel {color: cyan; }")

    def timerEvent(self, event):
        i = 1 if self.right_to_left_direction else -1
        self.setText(self.text()[i:] + self.text()[:i])  # rotate

    def mouseReleaseEvent(self, event):  # change direction on mouse release
        self.right_to_left_direction = not self.right_to_left_direction

    def keyPressEvent(self, event):  # exit on Esc
        if event.key() == Qt.Key_Escape:
            self.close()


app = QApplication(sys.argv)
w = Marquee()
# center widget on the screen
w.adjustSize()  # update w.rect() now
w.move(QApplication.instance().desktop().screen().rect().center()
       - w.rect().center())
w.show()
sys.exit(app.exec())

```

### python_code_3.txt
```python
import pygame, sys
from pygame.locals import *
pygame.init()

YSIZE = 40
XSIZE = 150

TEXT = "Hello World! "
FONTSIZE = 32

LEFT = False
RIGHT = True

DIR = RIGHT

TIMETICK = 180
TICK = USEREVENT + 2

TEXTBOX = pygame.Rect(10,10,XSIZE,YSIZE)

pygame.time.set_timer(TICK, TIMETICK)

window = pygame.display.set_mode((XSIZE, YSIZE))
pygame.display.set_caption("Animation")

font = pygame.font.SysFont(None, FONTSIZE)
screen = pygame.display.get_surface()

def rotate():
    index = DIR and -1 or 1
    global TEXT
    TEXT = TEXT[index:]+TEXT[:index]

def click(position):
    if TEXTBOX.collidepoint(position):
        global DIR
        DIR = not DIR

def draw():
    surface = font.render(TEXT, True, (255,255,255), (0,0,0))
    global TEXTBOX
    TEXTBOX = screen.blit(surface, TEXTBOX)
    
def input(event):
    if event.type == QUIT:
        sys.exit(0)
    elif event.type == MOUSEBUTTONDOWN:
        click(event.pos)
    elif event.type == TICK:
        draw()
        rotate()

while True:
    input(pygame.event.wait())
    pygame.display.flip()

```

### python_code_4.txt
```python
import Tkinter as tki

def scroll_text(s, how_many):
    return s[how_many:] + s[:how_many]

direction = 1
tk = tki.Tk()
var = tki.Variable(tk)

def mouse_handler(point):
    global direction
    direction *= -1

def timer_handler():
    var.set(scroll_text(var.get(),direction))
    tk.after(125, timer_handler)

var.set('Hello, World! ')
tki.Label(tk, textvariable=var).pack()
tk.bind("<Button-1>", mouse_handler)
tk.after(125, timer_handler)
tk.title('Python Animation')
tki.mainloop()

```

