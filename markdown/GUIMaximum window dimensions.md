# GUI/Maximum window dimensions

## Task Link
[Rosetta Code - GUI/Maximum window dimensions](https://rosettacode.org/wiki/GUI/Maximum_window_dimensions)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import javax.swing.JFrame;

public class Test extends JFrame {

    public static void main(String[] args) {
        new Test();
    }

    Test() {
        Toolkit toolkit = Toolkit.getDefaultToolkit();

        Dimension screenSize = toolkit.getScreenSize();
        System.out.println("Physical screen size: " + screenSize);

        Insets insets = toolkit.getScreenInsets(getGraphicsConfiguration());
        System.out.println("Insets: " + insets);

        screenSize.width -= (insets.left + insets.right);
        screenSize.height -= (insets.top + insets.bottom);
        System.out.println("Max available: " + screenSize);
    }
}

```

### java_code_2.txt
```java
//Aamrun, 26th June 2022

fullScreen();
fill(0);
textSize(50);
text("Screen Height : " + str(height), 100, 100);
text("Screen Width : " + str(width), 100, 200);

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

import tkinter as tk # import the module.

root = tk.Tk() # Create an instance of the class.
root.state('zoomed') # Maximized the window.
root.update_idletasks() # Update the display.
tk.Label(root, text=(str(root.winfo_width())+ " x " +str(root.winfo_height())),
         font=("Helvetica", 25)).pack() # add a label and set the size to text.
root.mainloop()

```

