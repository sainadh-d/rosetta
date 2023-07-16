# Superellipse

## Task Link
[Rosetta Code - Superellipse](https://rosettacode.org/wiki/Superellipse)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.geom.Path2D;
import static java.lang.Math.pow;
import java.util.Hashtable;
import javax.swing.*;
import javax.swing.event.*;

public class SuperEllipse extends JPanel implements ChangeListener {
    private double exp = 2.5;

    public SuperEllipse() {
        setPreferredSize(new Dimension(650, 650));
        setBackground(Color.white);
        setFont(new Font("Serif", Font.PLAIN, 18));
    }

    void drawGrid(Graphics2D g) {
        g.setStroke(new BasicStroke(2));
        g.setColor(new Color(0xEEEEEE));

        int w = getWidth();
        int h = getHeight();
        int spacing = 25;

        for (int i = 0; i < w / spacing; i++) {
            g.drawLine(0, i * spacing, w, i * spacing);
            g.drawLine(i * spacing, 0, i * spacing, w);
        }
        g.drawLine(0, h - 1, w, h - 1);

        g.setColor(new Color(0xAAAAAA));
        g.drawLine(0, w / 2, w, w / 2);
        g.drawLine(w / 2, 0, w / 2, w);
    }

    void drawLegend(Graphics2D g) {
        g.setColor(Color.black);
        g.setFont(getFont());
        g.drawString("n = " + String.valueOf(exp), getWidth() - 150, 45);
        g.drawString("a = b = 200", getWidth() - 150, 75);
    }

    void drawEllipse(Graphics2D g) {

        final int a = 200; // a = b
        double[] points = new double[a + 1];

        Path2D p = new Path2D.Double();
        p.moveTo(a, 0);

        // calculate first quadrant
        for (int x = a; x >= 0; x--) {
            points[x] = pow(pow(a, exp) - pow(x, exp), 1 / exp); // solve for y
            p.lineTo(x, -points[x]);
        }

        // mirror to others
        for (int x = 0; x <= a; x++)
            p.lineTo(x, points[x]);

        for (int x = a; x >= 0; x--)
            p.lineTo(-x, points[x]);

        for (int x = 0; x <= a; x++)
            p.lineTo(-x, -points[x]);

        g.translate(getWidth() / 2, getHeight() / 2);
        g.setStroke(new BasicStroke(2));

        g.setColor(new Color(0x25B0C4DE, true));
        g.fill(p);

        g.setColor(new Color(0xB0C4DE)); // LightSteelBlue
        g.draw(p);
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);
        g.setRenderingHint(RenderingHints.KEY_TEXT_ANTIALIASING,
                RenderingHints.VALUE_TEXT_ANTIALIAS_ON);

        drawGrid(g);
        drawLegend(g);
        drawEllipse(g);
    }

    @Override
    public void stateChanged(ChangeEvent e) {
        JSlider source = (JSlider) e.getSource();
        exp = source.getValue() / 2.0;
        repaint();
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Super Ellipse");
            f.setResizable(false);
            SuperEllipse panel = new SuperEllipse();
            f.add(panel, BorderLayout.CENTER);

            JSlider exponent = new JSlider(JSlider.HORIZONTAL, 1, 9, 5);
            exponent.addChangeListener(panel);
            exponent.setMajorTickSpacing(1);
            exponent.setPaintLabels(true);
            exponent.setBackground(Color.white);
            exponent.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));

            Hashtable<Integer, JLabel> labelTable = new Hashtable<>();
            for (int i = 1; i < 10; i++)
                labelTable.put(i, new JLabel(String.valueOf(i * 0.5)));
            exponent.setLabelTable(labelTable);

            f.add(exponent, BorderLayout.SOUTH);

            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_2.txt
```java
//Aamrun, 29th June 2022

float a = 200, b = 200, n = 2.5;
float i, incr = 0.001;
int xMul,yMul;

size(500,500);

stroke(#ff0000);

for(i=0;i<2*PI;i+=incr){
  if(PI/2<i && i<3*PI/2)
    xMul = -1;
  else
    xMul = 1;
  if(PI<i && i<2*PI)
    yMul = -1;
  else
    yMul = 1;
    
  ellipse(width/2 + xMul * a*pow(abs(cos(i)),2/n),height/2 + yMul * b*pow(abs(sin(i)),2/n),1,1);
}

```

## Python Code
### python_code_1.txt
```python
# Superellipse drawing in Python 2.7.9
# pic can see at http://www.imgup.cz/image/712

import matplotlib.pyplot as plt
from math import sin, cos, pi

def sgn(x):
	return ((x>0)-(x<0))*1

a,b,n=200,200,2.5 # param n making shape
na=2/n
step=100 # accuracy
piece=(pi*2)/step
xp=[];yp=[]

t=0
for t1 in range(step+1):
	# because sin^n(x) is mathematically the same as (sin(x))^n...
	x=(abs((cos(t)))**na)*a*sgn(cos(t))
	y=(abs((sin(t)))**na)*b*sgn(sin(t))
	xp.append(x);yp.append(y)
	t+=piece

plt.plot(xp,yp) # plotting all point from array xp, yp
plt.title("Superellipse with parameter "+str(n))
plt.show()

```

