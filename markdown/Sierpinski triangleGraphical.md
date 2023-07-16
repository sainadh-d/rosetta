# Sierpinski triangle/Graphical

## Task Link
[Rosetta Code - Sierpinski triangle/Graphical](https://rosettacode.org/wiki/Sierpinski_triangle/Graphical)

## Java Code
### java_code_1.txt
```java
import javax.swing.*;
import java.awt.*;

/**
* SierpinskyTriangle.java
* Draws a SierpinskyTriangle in a JFrame
* The order of complexity is given from command line, but
* defaults to 3
*
* @author Istarnion
*/ 

class SierpinskyTriangle {

	public static void main(String[] args) {
		int i = 3;		// Default to 3
		if(args.length >= 1) {
			try {
				i = Integer.parseInt(args[0]);
			}
			catch(NumberFormatException e) {
				System.out.println("Usage: 'java SierpinskyTriangle [level]'\nNow setting level to "+i);
			}
		}
		final int level = i;

		JFrame frame = new JFrame("Sierpinsky Triangle - Java");
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		JPanel panel = new JPanel() {
			@Override
			public void paintComponent(Graphics g) {
				g.setColor(Color.BLACK);
				drawSierpinskyTriangle(level, 20, 20, 360, (Graphics2D)g);
			}
		};

		panel.setPreferredSize(new Dimension(400, 400));

		frame.add(panel);
		frame.pack();
		frame.setResizable(false);
		frame.setLocationRelativeTo(null);
		frame.setVisible(true);
	}

	private static void drawSierpinskyTriangle(int level, int x, int y, int size, Graphics2D g) {
		if(level <= 0) return;

		g.drawLine(x, y, x+size, y);
		g.drawLine(x, y, x, y+size);
		g.drawLine(x+size, y, x, y+size);

		drawSierpinskyTriangle(level-1, x, y, size/2, g);
		drawSierpinskyTriangle(level-1, x+size/2, y, size/2, g);
		drawSierpinskyTriangle(level-1, x, y+size/2, size/2, g);
	}
}

```

### java_code_2.txt
```java
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.geom.Path2D;
import javax.swing.*;

public class SierpinskiTriangle extends JPanel {
    private final int dim = 512;
    private final int margin = 20;

    private int limit = dim;

    public SierpinskiTriangle() {
        setPreferredSize(new Dimension(dim + 2 * margin, dim + 2 * margin));
        setBackground(Color.white);
        setForeground(Color.green.darker());

        new Timer(2000, (ActionEvent e) -> {
            limit /= 2;
            if (limit <= 2)
                limit = dim;
            repaint();
        }).start();
    }

    void drawTriangle(Graphics2D g, int x, int y, int size) {
        if (size <= limit) {
            Path2D p = new Path2D.Float();
            p.moveTo(x, y);
            p.lineTo(x + size / 2, y + size);
            p.lineTo(x - size / 2, y + size);
            g.fill(p);
        } else {
            size /= 2;
            drawTriangle(g, x, y, size);
            drawTriangle(g, x + size / 2, y + size, size);
            drawTriangle(g, x - size / 2, y + size, size);
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        g.translate(margin, margin);
        drawTriangle(g, dim / 2, 0, dim);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Sierpinski Triangle");
            f.setResizable(false);
            f.add(new SierpinskiTriangle(), BorderLayout.CENTER);
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
# a very simple version
import turtle as t
def sier(n,length):
    if n == 0:
        return
    for i in range(3):
        sier(n - 1, length / 2)
        t.fd(length)
        t.rt(120)

```

### python_code_2.txt
```python
# otra versión muy simple
from pylab import*
x=[[1,1],[1,0]]
for i in'123':x=kron(x,x)
imsave('a',x)

```

### python_code_3.txt
```python
#!/usr/bin/env python
##########################################################################################
# a very complicated version
# import necessary modules
# ------------------------
from numpy import *
import turtle

##########################################################################################
#	Functions defining the drawing actions
#       (used by the function DrawSierpinskiTriangle).
#	----------------------------------------------
def Left(turn, point, fwd, angle, turt):
	turt.left(angle)
	return [turn, point, fwd, angle, turt]
def Right(turn, point, fwd, angle, turt):
	turt.right(angle)
	return [turn, point, fwd, angle, turt]
def Forward(turn, point, fwd, angle, turt):
	turt.forward(fwd)
	return [turn, point, fwd, angle, turt]

```

### python_code_4.txt
```python
##########################################################################################
#		The drawing function
#		--------------------
#
# level		level of Sierpinski triangle (minimum value = 1)
# ss		screensize (Draws on a screen of size ss x ss. Default value = 400.)
#-----------------------------------------------------------------------------------------
def DrawSierpinskiTriangle(level, ss=400):
	# typical values
	turn = 0		# initial turn (0 to start horizontally)
	angle=60.0 		# in degrees

	# Initialize the turtle
	turtle.hideturtle()
	turtle.screensize(ss,ss)
	turtle.penup()
	turtle.degrees()

	# The starting point on the canvas
	fwd0         = float(ss)
	point=array([-fwd0/2.0, -fwd0/2.0])

	# Setting up the Lindenmayer system
	# Assuming that the triangle will be drawn in the following way:
	#	1.) Start at a point
	#	2.) Draw a straight line - the horizontal line (H)
	#	3.) Bend twice by 60 degrees to the left (--)
	#	4.) Draw a straight line - the slanted line (X)
	#	5.) Bend twice by 60 degrees to the left (--)
	#	6.) Draw a straight line - another slanted line (X)
	# 		This produces the triangle in the first level. (so the axiom to begin with is H--X--X)
	#	7.) For the next level replace each horizontal line using
	#		X->XX
	#		H -> H--X++H++X--H
	#			The lengths will be halved.


	decode    = {'-':Left, '+':Right, 'X':Forward, 'H':Forward}
	axiom     = 'H--X--X'

	# Start the drawing
	turtle.goto(point[0], point[1])
	turtle.pendown()
	turtle.hideturtle()
	turt=turtle.getpen()
	startposition=turt.clone()

	# Get the triangle in the Lindenmayer system
	fwd       = fwd0/(2.0**level)
	path      = axiom
	for i in range(0,level):
		path=path.replace('X','XX')
		path=path.replace('H','H--X++H++X--H')

	# Draw it.
	for i in path:
		[turn, point, fwd, angle, turt]=decode[i](turn, point, fwd, angle, turt)
##########################################################################################

DrawSierpinskiTriangle(5)

```

