# Munching squares

## Task Link
[Rosetta Code - Munching squares](https://rosettacode.org/wiki/Munching_squares)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class XorPattern extends JFrame{
    private JPanel xorPanel;

    public XorPattern(){
        xorPanel = new JPanel(){
            @Override
            public void paint(Graphics g) {
                for(int y = 0; y < getHeight();y++){
                    for(int x = 0; x < getWidth();x++){
                        g.setColor(new Color(0, (x ^ y) % 256, 0));
                        g.drawLine(x, y, x, y);
                    }
                }
            }
        };
        add(xorPanel);
        setSize(300, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args){
        new XorPattern();
    }
}

```

### java_code_2.txt
```java
//Aamrun, 26th June 2022

size(1200,720);

loadPixels();

for(int i=0;i<height;i++){
  for(int j=0;j<width;j++){
    pixels[j + i*width] = color(i^j);
  }
}

updatePixels();

```

## Python Code
### python_code_1.txt
```python
import Image, ImageDraw

image = Image.new("RGB", (256, 256))
drawingTool = ImageDraw.Draw(image)

for x in range(256):
    for y in range(256):
        drawingTool.point((x, y), (0, x^y, 0))

del drawingTool
image.save("xorpic.png", "PNG")

```

