# Window creation/X11

## Task Link
[Rosetta Code - Window creation/X11](https://rosettacode.org/wiki/Window_creation/X11)

## Java Code
### java_code_1.txt
```java
import javax.swing.JFrame;
import javax.swing.SwingUtilities;

public class WindowExample {

  public static void main(String[] args) {
    Runnable runnable = new Runnable() {
      public void run() {
	createAndShow();
      }
    };
    SwingUtilities.invokeLater(runnable);
  }
	
  static void createAndShow() {
    JFrame frame = new JFrame("Hello World");
    frame.setSize(640,480);
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    frame.setVisible(true);
  }
}

```

### java_code_2.txt
```java
import java.awt.*;
import java.awt.event.*;
import java.awt.geom.*;
import javax.swing.*;

public class WindowExample extends JApplet {
    public void paint(Graphics g) {
        Graphics2D g2 = (Graphics2D) g;

        g2.setStroke(new BasicStroke(2.0f));
        g2.drawString("Hello java", 20, 20);
        g2.setPaint(Color.blue);
        g2.draw(new Rectangle2D.Double(40, 40, 20, 20));
    }

    public static void main(String s[]) {
        JFrame f = new JFrame("ShapesDemo2D");
        f.addWindowListener(new WindowAdapter() {
            public void windowClosing(WindowEvent e) {System.exit(0);}
        });
        JApplet applet = new ShapesDemo2D();
        f.getContentPane().add("Center", applet);
        f.pack();
        f.setSize(new Dimension(150, 150));
        f.setVisible(true);
    }
}

```

## Python Code
### python_code_1.txt
```python
from Xlib import X, display

class Window:
    def __init__(self, display, msg):
        self.display = display
        self.msg = msg
        
        self.screen = self.display.screen()
        self.window = self.screen.root.create_window(
            10, 10, 100, 100, 1,
            self.screen.root_depth,
            background_pixel=self.screen.white_pixel,
            event_mask=X.ExposureMask | X.KeyPressMask,
            )
        self.gc = self.window.create_gc(
            foreground = self.screen.black_pixel,
            background = self.screen.white_pixel,
            )

        self.window.map()

    def loop(self):
        while True:
            e = self.display.next_event()
                
            if e.type == X.Expose:
                self.window.fill_rectangle(self.gc, 20, 20, 10, 10)
                self.window.draw_text(self.gc, 10, 50, self.msg)
            elif e.type == X.KeyPress:
                raise SystemExit

                
if __name__ == "__main__":
    Window(display.Display(), "Hello, World!").loop()

```

### python_code_2.txt
```python
import xcb
from xcb.xproto import *
import xcb.render

def main():
  conn = xcb.connect()
  conn.render = conn(xcb.render.key)

  setup = conn.get_setup()
  root = setup.roots[0].root
  depth = setup.roots[0].root_depth
  visual = setup.roots[0].root_visual
  white = setup.roots[0].white_pixel

  window = conn.generate_id()
  conn.core.CreateWindow(depth, window, root,
                         0, 0, 640, 480, 0,
                         WindowClass.InputOutput,
                         visual,
                         CW.BackPixel | CW.EventMask,
                         [ white, EventMask.Exposure |
                                  EventMask.KeyPress ])

  conn.core.MapWindow(window)
  conn.flush()

  while True:
    event = conn.wait_for_event()

    if isinstance(event, ExposeEvent):
      color = (0, 0, 65535, 65535)
      rectangle = (20, 20, 40, 40)
      # TODO, fixme:
      # I haven't been able to find what I should put for the parameter "op"
   #  conn.render.FillRectangles(op, window, color, 1, rectangle)
      conn.flush()

    elif isinstance(event, KeyPressEvent):
      break

  conn.disconnect()

main()

```

