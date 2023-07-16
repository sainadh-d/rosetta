# Colour pinstripe/Display

## Task Link
[Rosetta Code - Colour pinstripe/Display](https://rosettacode.org/wiki/Colour_pinstripe/Display)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import static java.awt.Color.*;
import javax.swing.*;

public class ColourPinstripeDisplay extends JPanel {
    final static Color[] palette = {black, red, green, blue, magenta,cyan,
        yellow, white};

    final int bands = 4;

    public ColourPinstripeDisplay() {
        setPreferredSize(new Dimension(900, 600));
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        int h = getHeight();
        for (int b = 1; b <= bands; b++) {
            for (int x = 0, colIndex = 0; x < getWidth(); x += b, colIndex++) {
                g.setColor(palette[colIndex % palette.length]);
                g.fillRect(x, (b - 1) * (h / bands), x + b, b * (h / bands));
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("ColourPinstripeDisplay");
            f.add(new ColourPinstripeDisplay(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
from turtle import *

colors = ["black", "red", "green", "blue", "magenta", "cyan", "yellow", "white"]

# Middle of screen is 0,0

screen = getscreen()

left_edge = -screen.window_width()//2

right_edge = screen.window_width()//2

quarter_height = screen.window_height()//4

half_height = quarter_height * 2

speed("fastest")

for quarter in range(4):
    pensize(quarter+1)
    colornum = 0

    min_y = half_height - ((quarter + 1) * quarter_height)
    max_y = half_height - ((quarter) * quarter_height)
    
    for x in range(left_edge,right_edge,quarter+1):
        penup()
        pencolor(colors[colornum])
        colornum = (colornum + 1) % len(colors)
        setposition(x,min_y)
        pendown()
        setposition(x,max_y)
         
notused = input("Hit enter to continue: ")

```

