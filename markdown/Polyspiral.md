# Polyspiral

## Task Link
[Rosetta Code - Polyspiral](https://rosettacode.org/wiki/Polyspiral)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.ActionEvent;
import javax.swing.*;

public class PolySpiral extends JPanel {
    double inc = 0;

    public PolySpiral() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);

        new Timer(40, (ActionEvent e) -> {
            inc = (inc + 0.05) % 360;
            repaint();
        }).start();
    }

    void drawSpiral(Graphics2D g, int len, double angleIncrement) {

        double x1 = getWidth() / 2;
        double y1 = getHeight() / 2;
        double angle = angleIncrement;

        for (int i = 0; i < 150; i++) {

            g.setColor(Color.getHSBColor(i / 150f, 1.0f, 1.0f));

            double x2 = x1 + Math.cos(angle) * len;
            double y2 = y1 - Math.sin(angle) * len;
            g.drawLine((int) x1, (int) y1, (int) x2, (int) y2);
            x1 = x2;
            y1 = y2;

            len += 3;

            angle = (angle + angleIncrement) % (Math.PI * 2);
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawSpiral(g, 5, Math.toRadians(inc));
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("PolySpiral");
            f.setResizable(true);
            f.add(new PolySpiral(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
//Aamrun, 2nd July 2022

int incr = 0, angle, i, length;
float x,y,x1,y1;
double factor = PI/180;
  

void setup() {
  size(1000, 1000);
  stroke(255);

}

void draw() {
    background(51);
    incr = (incr + 5)%360; 
 
    x = width/2;
    y = height/2;
 
    length = 5;
    angle = incr;
 
    for(i=1;i<=150;i++){
      x1 = x + (float)(length*Math.cos(factor*angle));
      y1 = y + (float)(length*Math.sin(factor*angle));
      line(x,y,x1,y1);
 
      length += 3;
 
      angle = (angle + incr)%360;
 
      x = x1;
      y = y1;
  }
}

```

## Python Code
### python_code_1.txt
```python
import math

import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((1024, 600))

pygame.display.set_caption("Polyspiral")

incr = 0

running = True

while running:
	pygame.time.Clock().tick(60)
	for event in pygame.event.get():
		if event.type==QUIT:
			running = False
			break

	incr = (incr + 0.05) % 360
	x1 = pygame.display.Info().current_w / 2
	y1 = pygame.display.Info().current_h / 2
	length = 5
	angle = incr

	screen.fill((255,255,255))

	for i in range(1,151):
		x2 = x1 + math.cos(angle) * length
		y2 = y1 + math.sin(angle) * length
		pygame.draw.line(screen, (255,0,0), (x1, y1), (x2, y2), 1)
		# pygame.draw.aaline(screen, (255,0,0), (x1, y1), (x2, y2)) # Anti-Aliased
		x1, y1 = x2, y2
		length += 3
		angle = (angle + incr) % 360

	pygame.display.flip()

```

