# Keyboard input/Keypress check

## Task Link
[Rosetta Code - Keyboard input/Keypress check](https://rosettacode.org/wiki/Keyboard_input/Keypress_check)

## Java Code
### java_code_1.txt
```java
import java.awt.event.*;
import javax.swing.*;

public class Test extends JFrame {

    Test() {
        addKeyListener(new KeyAdapter() {
            @Override
            public void keyPressed(KeyEvent e) {
                int keyCode = e.getKeyCode();
                System.out.println(keyCode);
            }
        });
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            Test f = new Test();
            f.setFocusable(true);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, unicode_literals, print_function

import tty, termios
import sys
if sys.version_info.major < 3:
    import thread as _thread
else:
    import _thread
import time


try:
    from msvcrt import getch  # try to import Windows version
except ImportError:
    def getch():   # define non-Windows version
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def keypress():
    global char
    char = getch()

def main():
    global char
    char = None
    _thread.start_new_thread(keypress, ())

    while True:
        if char is not None:
            try:
                print("Key pressed is " + char.decode('utf-8'))
            except UnicodeDecodeError:
                print("character can not be decoded, sorry!")
                char = None
            _thread.start_new_thread(keypress, ())
            if char == 'q' or char == '\x1b':  # x1b is ESC
                exit()
            char = None
        print("Program is running")
        time.sleep(1)

if __name__ == "__main__":
    main()

```

