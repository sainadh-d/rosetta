# Animate a pendulum

## Task Link
[Rosetta Code - Animate a pendulum](https://rosettacode.org/wiki/Animate_a_pendulum)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import javax.swing.*;

public class Pendulum extends JPanel implements Runnable {

    private double angle = Math.PI / 2;
    private int length;

    public Pendulum(int length) {
        this.length = length;
        setDoubleBuffered(true);
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.WHITE);
        g.fillRect(0, 0, getWidth(), getHeight());
        g.setColor(Color.BLACK);
        int anchorX = getWidth() / 2, anchorY = getHeight() / 4;
        int ballX = anchorX + (int) (Math.sin(angle) * length);
        int ballY = anchorY + (int) (Math.cos(angle) * length);
        g.drawLine(anchorX, anchorY, ballX, ballY);
        g.fillOval(anchorX - 3, anchorY - 4, 7, 7);
        g.fillOval(ballX - 7, ballY - 7, 14, 14);
    }

    public void run() {
        double angleAccel, angleVelocity = 0, dt = 0.1;
        while (true) {
            angleAccel = -9.81 / length * Math.sin(angle);
            angleVelocity += angleAccel * dt;
            angle += angleVelocity * dt;
            repaint();
            try { Thread.sleep(15); } catch (InterruptedException ex) {}
        }
    }

    @Override
    public Dimension getPreferredSize() {
        return new Dimension(2 * length + 50, length / 2 * 3);
    }

    public static void main(String[] args) {
        JFrame f = new JFrame("Pendulum");
        Pendulum p = new Pendulum(200);
        f.add(p);
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.pack();
        f.setVisible(true);
        new Thread(p).start();
    }
}

```

## Python Code
### python_code_1.txt
```python
import pygame, sys
from pygame.locals import *
from math import sin, cos, radians

pygame.init()

WINDOWSIZE = 250
TIMETICK = 100
BOBSIZE = 15

window = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))
pygame.display.set_caption("Pendulum")

screen = pygame.display.get_surface()
screen.fill((255,255,255))

PIVOT = (WINDOWSIZE/2, WINDOWSIZE/10)
SWINGLENGTH = PIVOT[1]*4

class BobMass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.theta = 45
        self.dtheta = 0
        self.rect = pygame.Rect(PIVOT[0]-SWINGLENGTH*cos(radians(self.theta)),
                                PIVOT[1]+SWINGLENGTH*sin(radians(self.theta)),
                                1,1)
        self.draw()

    def recomputeAngle(self):
        scaling = 3000.0/(SWINGLENGTH**2)

        firstDDtheta = -sin(radians(self.theta))*scaling
        midDtheta = self.dtheta + firstDDtheta
        midtheta = self.theta + (self.dtheta + midDtheta)/2.0

        midDDtheta = -sin(radians(midtheta))*scaling
        midDtheta = self.dtheta + (firstDDtheta + midDDtheta)/2
        midtheta = self.theta + (self.dtheta + midDtheta)/2

        midDDtheta = -sin(radians(midtheta)) * scaling
        lastDtheta = midDtheta + midDDtheta
        lasttheta = midtheta + (midDtheta + lastDtheta)/2.0
        
        lastDDtheta = -sin(radians(lasttheta)) * scaling
        lastDtheta = midDtheta + (midDDtheta + lastDDtheta)/2.0
        lasttheta = midtheta + (midDtheta + lastDtheta)/2.0

        self.dtheta = lastDtheta
        self.theta = lasttheta
        self.rect = pygame.Rect(PIVOT[0]-
                                SWINGLENGTH*sin(radians(self.theta)), 
                                PIVOT[1]+
                                SWINGLENGTH*cos(radians(self.theta)),1,1)


    def draw(self):
        pygame.draw.circle(screen, (0,0,0), PIVOT, 5, 0)
        pygame.draw.circle(screen, (0,0,0), self.rect.center, BOBSIZE, 0)
        pygame.draw.aaline(screen, (0,0,0), PIVOT, self.rect.center)
        pygame.draw.line(screen, (0,0,0), (0, PIVOT[1]), (WINDOWSIZE, PIVOT[1]))

    def update(self):
        self.recomputeAngle()
        screen.fill((255,255,255))
        self.draw()

bob = BobMass()

TICK = USEREVENT + 2
pygame.time.set_timer(TICK, TIMETICK)

def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == TICK:
            bob.update()

while True:
    input(pygame.event.get())
    pygame.display.flip()

```

### python_code_2.txt
```python
''' Python 3.6.5 code using Tkinter graphical user interface.''' 

from tkinter import *
import math

class Animation:
    def __init__(self, gw):
        self.window = gw
        self.xoff, self.yoff = 300, 100
        self.angle = 0
        self.sina = math.sin(self.angle)
        self.cosa = math.cos(self.angle)
        self.rodhyp = 170
        self.bobr = 30
        self.bobhyp = self.rodhyp + self.bobr
        self.rodx0, self.rody0 = self.xoff, self.yoff
        self.ra = self.rodx0
        self.rb = self.rody0
        self.rc = self.xoff + self.rodhyp*self.sina
        self.rd = self.yoff + self.rodhyp*self.cosa
        self.ba = self.xoff - self.bobr + self.bobhyp*self.sina
        self.bb = self.yoff - self.bobr + self.bobhyp*self.cosa
        self.bc = self.xoff + self.bobr + self.bobhyp*self.sina
        self.bd = self.yoff + self.bobr + self.bobhyp*self.cosa
        self.da = math.pi / 360

        # create / fill canvas:
        self.cnv = Canvas(gw, bg='lemon chiffon')
        self.cnv.pack(fill=BOTH, expand=True)

        self.cnv.create_line(0, 100, 600, 100,
                             fill='dodger blue',
                             width=3)
        radius = 8
        self.cnv.create_oval(300-radius, 100-radius,
                             300+radius, 100+radius,
                             fill='navy')    

        self.bob = self.cnv.create_oval(self.ba,
                                        self.bb,
                                        self.bc,
                                        self.bd,
                                        fill='red',
                                        width=2)

        self.rod = self.cnv.create_line(self.ra,
                                        self.rb,
                                        self.rc,
                                        self.rd,
                                        fill='dodger blue',
                                        width=6)

        self.animate()

    def animate(self):
        if abs(self.angle) > math.pi / 2:
            self.da = - self.da
        self.angle += self.da
        self.sina = math.sin(self.angle)
        self.cosa = math.cos(self.angle)
        self.ra = self.rodx0
        self.rb = self.rody0
        self.rc = self.xoff + self.rodhyp*self.sina
        self.rd = self.yoff + self.rodhyp*self.cosa
        self.ba = self.xoff - self.bobr + self.bobhyp*self.sina
        self.bb = self.yoff - self.bobr + self.bobhyp*self.cosa
        self.bc = self.xoff + self.bobr + self.bobhyp*self.sina
        self.bd = self.yoff + self.bobr + self.bobhyp*self.cosa
        
        self.cnv.coords(self.rod,
                        self.ra,
                        self.rb,
                        self.rc,
                        self.rd)
        self.cnv.coords(self.bob,
                        self.ba,
                        self.bb,
                        self.bc,
                        self.bd)
        self.window.update()
        self.cnv.after(5, self.animate)
         
root = Tk()
root.title('Pendulum')
root.geometry('600x400+100+50')
root.resizable(False, False)
a = Animation(root)
root.mainloop()

```

