# Keyboard macros

## Task Link
[Rosetta Code - Keyboard macros](https://rosettacode.org/wiki/Keyboard_macros)

## Java Code
### java_code_1.txt
```java
package keybord.macro.demo;

import javax.swing.JFrame;
import javax.swing.JLabel;
import java.awt.event.KeyAdapter;
import java.awt.event.KeyEvent;

class KeyboardMacroDemo {
    public static void main( String [] args ) {
        final JFrame frame = new JFrame();
        
        String directions = "<html><b>Ctrl-S</b> to show frame title<br>"
                                 +"<b>Ctrl-H</b> to hide it</html>";
                                 
        frame.add( new JLabel(directions));
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        
        frame.addKeyListener( new KeyAdapter(){
            public void keyReleased( KeyEvent e ) {
                if( e.isControlDown() && e.getKeyCode() == KeyEvent.VK_S){
                    frame.setTitle("Hello there");
                }else if( e.isControlDown() && e.getKeyCode() == KeyEvent.VK_H){
                    frame.setTitle("");
                }
            }
        });
        frame.pack();
        frame.setVisible(true);
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
import curses

def print_message():
    stdscr.addstr('This is the message.\n')

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(1)

stdscr.addstr('CTRL+P for message or q to quit.\n')
while True:
    c = stdscr.getch()
    if c == 16: print_message()
    elif c == ord('q'): break

curses.nocbreak()
stdscr.keypad(0)
curses.echo()
curses.endwin()

```

