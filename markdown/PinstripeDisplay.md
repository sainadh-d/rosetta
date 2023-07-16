# Pinstripe/Display

## Task Link
[Rosetta Code - Pinstripe/Display](https://rosettacode.org/wiki/Pinstripe/Display)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import javax.swing.*;

public class PinstripeDisplay extends JPanel {

    final int bands = 4;

    public PinstripeDisplay() {
        setPreferredSize(new Dimension(900, 600));
    }

    @Override
    public void paintComponent(Graphics g) {
        super.paintComponent(g);
        int h = getHeight();
        for (int b = 1; b <= bands; b++) {
            for (int x = 0, colIndex = 0; x < getWidth(); x += b, colIndex++) {
                g.setColor(colIndex % 2 == 0 ? Color.white : Color.black);
                g.fillRect(x, (b - 1) * (h / bands), x + b, b * (h / bands));
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                JFrame f = new JFrame();
                f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                f.setTitle("PinstripeDisplay");
                f.add(new PinstripeDisplay(), BorderLayout.CENTER);
                f.pack();
                f.setLocationRelativeTo(null);
                f.setVisible(true);
            }
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
#Python task for Pinstripe/Display 
#Tested for Python2.7 by Benjamin Curutchet

#Import PIL libraries
from PIL import Image
from PIL import ImageColor
from PIL import ImageDraw

#Create the picture (size parameter 1660x1005 like the example)
x_size = 1650
y_size = 1000
im = Image.new('RGB',(x_size, y_size))

#Create a full black picture
draw = ImageDraw.Draw(im)

#RGB code for the White Color
White  = (255,255,255) 

#First loop in order to create four distinct lines
y_delimiter_list = []
for y_delimiter in range(1,y_size,y_size/4):
	y_delimiter_list.append(y_delimiter)


#Four different loops in order to draw columns in white depending on the
#number of the line

for x in range(1,x_size,2):
	for y in range(1,y_delimiter_list[1],1):
		draw.point((x,y),White)

for x in range(1,x_size-1,4):
	for y in range(y_delimiter_list[1],y_delimiter_list[2],1):
		draw.point((x,y),White)
		draw.point((x+1,y),White)
		
for x in range(1,x_size-2,6):
	for y in range(y_delimiter_list[2],y_delimiter_list[3],1):
		draw.point((x,y),White)
		draw.point((x+1,y),White)
		draw.point((x+2,y),White)
		
for x in range(1,x_size-3,8):
	for y in range(y_delimiter_list[3],y_size,1):
		draw.point((x,y),White)
		draw.point((x+1,y),White)
		draw.point((x+2,y),White)
		draw.point((x+3,y),White)
	
				
		
#Save the picture under a name as a jpg file.
print "Your picture is saved"		
im.save('PictureResult.jpg')

```

