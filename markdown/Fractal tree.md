# Fractal tree

## Task Link
[Rosetta Code - Fractal tree](https://rosettacode.org/wiki/Fractal_tree)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

public class FractalTree extends JFrame {

    public FractalTree() {
        super("Fractal Tree");
        setBounds(100, 100, 800, 600);
        setResizable(false);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
    }

    private void drawTree(Graphics g, int x1, int y1, double angle, int depth) {
        if (depth == 0) return;
        int x2 = x1 + (int) (Math.cos(Math.toRadians(angle)) * depth * 10.0);
        int y2 = y1 + (int) (Math.sin(Math.toRadians(angle)) * depth * 10.0);
        g.drawLine(x1, y1, x2, y2);
        drawTree(g, x2, y2, angle - 20, depth - 1);
        drawTree(g, x2, y2, angle + 20, depth - 1);
    }

    @Override
    public void paint(Graphics g) {
        g.setColor(Color.BLACK);
        drawTree(g, 400, 500, -90, 9);
    }

    public static void main(String[] args) {
        new FractalTree().setVisible(true);
    }
}

```

### java_code_2.txt
```java
void setup() {
  size(600, 600);
  background(0);
  stroke(255);
  drawTree(300, 550, 9);
}

void drawTree(float x, float y, int depth) {
  float forkAngle = radians(20);
  float baseLen = 10.0;
  if (depth > 0) {
    pushMatrix();
    translate(x, y - baseLen * depth);
    line(0, baseLen * depth, 0, 0);  
    rotate(forkAngle);
    drawTree(0, 0, depth - 1);  
    rotate(2 * -forkAngle);
    drawTree(0, 0, depth - 1); 
    popMatrix();
  }
}

```

### java_code_3.txt
```java
void setup() {
  size(600, 600);
  background(0);
  stroke(255);
  drawTree(300, 550, -90, 9);
}

void drawTree(float x1, float y1, float angle, int depth) {
  float forkAngle = 20;
  float baseLen = 10.0;
  if (depth > 0) {
    float x2 = x1 + cos(radians(angle)) * depth * baseLen;
    float y2 = y1 + sin(radians(angle)) * depth * baseLen;
    line(x1, y1, x2, y2);
    drawTree(x2, y2, angle - forkAngle, depth - 1);
    drawTree(x2, y2, angle + forkAngle, depth - 1);
  }
}

```

## Python Code
### python_code_1.txt
```python
def setup():
    size(600, 600)
    background(0)
    stroke(255)
    drawTree(300, 550, 9)
    
def drawTree(x, y, depth):
    fork_ang = radians(20)
    base_len = 10
    if depth > 0:
        pushMatrix()
        translate(x, y - baseLen * depth)
        line(0, baseLen * depth, 0, 0)  
        rotate(fork_ang)
        drawTree(0, 0, depth - 1)  
        rotate(2 * -fork_ang)
        drawTree(0, 0, depth - 1) 
        popMatrix()

```

### python_code_2.txt
```python
def setup():
    size(600, 600)
    background(0)
    stroke(255)
    drawTree(300, 550, -90, 9)

def drawTree(x1, y1, angle, depth):
    fork_angle = 20
    base_len = 10.0
    if depth > 0:
        x2 = x1 + cos(radians(angle)) * depth * base_len
        y2 = y1 + sin(radians(angle)) * depth * base_len
        line(x1, y1, x2, y2)
        drawTree(x2, y2, angle - fork_angle, depth - 1)
        drawTree(x2, y2, angle + fork_angle, depth - 1)

```

### python_code_3.txt
```python
import pygame, math

pygame.init()
window = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Fractal Tree")
screen = pygame.display.get_surface()

def drawTree(x1, y1, angle, depth):
    fork_angle = 20
    base_len = 10.0
    if depth > 0:
        x2 = x1 + int(math.cos(math.radians(angle)) * depth * base_len)
        y2 = y1 + int(math.sin(math.radians(angle)) * depth * base_len)
        pygame.draw.line(screen, (255,255,255), (x1, y1), (x2, y2), 2)
        drawTree(x2, y2, angle - fork_angle, depth - 1)
        drawTree(x2, y2, angle + fork_angle, depth - 1)

def input(event):
    if event.type == pygame.QUIT:
        exit(0)

drawTree(300, 550, -90, 9)
pygame.display.flip()
while True:
    input(pygame.event.wait())

```

