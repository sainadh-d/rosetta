# Brownian tree

## Task Link
[Rosetta Code - Brownian tree](https://rosettacode.org/wiki/Brownian_tree)

## Java Code
### java_code_1.txt
```java
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import java.util.*;
import javax.swing.JFrame;

public class BrownianTree extends JFrame implements Runnable {

    BufferedImage I;
    private List<Particle> particles;
    static Random rand = new Random();

    public BrownianTree() {
        super("Brownian Tree");
        setBounds(100, 100, 400, 300);
        setDefaultCloseOperation(EXIT_ON_CLOSE);
        I = new BufferedImage(getWidth(), getHeight(), BufferedImage.TYPE_INT_RGB);
        I.setRGB(I.getWidth() / 2, I.getHeight() / 2, 0xff00);
        particles = new LinkedList<Particle>();
    }

    @Override
    public void paint(Graphics g) {
        g.drawImage(I, 0, 0, this);
    }

    public void run() {
        for (int i = 0; i < 20000; i++) {
            particles.add(new Particle());
        }
        while (!particles.isEmpty()) {
            for (Iterator<Particle> it = particles.iterator(); it.hasNext();) {
                if (it.next().move()) {
                    it.remove();
                }
            }
            repaint();
        }
    }

    public static void main(String[] args) {
        BrownianTree b = new BrownianTree();
        b.setVisible(true);
        new Thread(b).start();
    }

    private class Particle {

        private int x, y;

        private Particle() {
            x = rand.nextInt(I.getWidth());
            y = rand.nextInt(I.getHeight());
        }

        /* returns true if either out of bounds or collided with tree */
        private boolean move() {
            int dx = rand.nextInt(3) - 1;
            int dy = rand.nextInt(3) - 1;
            if ((x + dx < 0) || (y + dy < 0)
                    || (y + dy >= I.getHeight()) || (x + dx >= I.getWidth())) {
                return true;
            }
            x += dx;
            y += dy;
            if ((I.getRGB(x, y) & 0xff00) == 0xff00) {
                I.setRGB(x - dx, y - dy, 0xff00);
                return true;
            }
            return false;
        }
    }
}

```

### java_code_2.txt
```java
import java.awt.Point;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;

import javax.imageio.ImageIO;

public class BasicBrownianTree {

    private int pixelsLost;
    private Point p;
    private Point nextP;
    private int pixelCount;
    private int width;
    private int height;
    private int color;
    private BufferedImage img;

    public BasicBrownianTree( int argb, int size, double density ) {
        pixelsLost = 0;
        p = new Point();
        nextP = new Point();
        width = size;
        height = size;
        color = argb;
        pixelCount = (int) ( width * height * density );
        img = new BufferedImage( width, height, BufferedImage.TYPE_INT_ARGB );
    }

    public void generate() {
        // print text to the console
        System.out.println( "Drawing " + pixelCount + " pixels" );
        int background = img.getRGB( 0, 0 );
        img.setRGB( width / 2, height / 2, color );

        for( int i = 0; i < pixelCount; i++ ) {
            p.x = (int) ( Math.random() * width );
            p.y = (int) ( Math.random() * height );

            while ( true ) {
                int dx = (int) ( Math.random() * 3 ) - 1;
                int dy = (int) ( Math.random() * 3 ) - 1;
                nextP.setLocation( p.x + dx, p.y + dy );
                // handle out-of-bounds
                if ( nextP.x < 0 || nextP.x >= width || nextP.y < 0
                        || nextP.y >= height ) {
                        // increment the number of pixels lost and escape the loop
                    pixelsLost++;
                    break;
                }
                if ( img.getRGB( nextP.x, nextP.y ) != background ) {
                    img.setRGB( p.x, p.y, color );
                    break;
                }
                p.setLocation( nextP );
            }
            // Print a message every 2%
            if ( i % ( pixelCount / 50 ) == 0 ) {
                System.out.println( "Done with " + i + " pixels" );
            }
        }
        // We're done. Let the user know how many pixels were lost
        System.out.println( "Finished. Pixels lost = " + pixelsLost );
    }

    public BufferedImage getImage() {
        return img;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public static void main( String[] args ) {
        // create the new generator
        BasicBrownianTree generator = new BasicBrownianTree( 0x664444ff, 400, 0.4 );
        // generate the image
        generator.generate();
        try {
            // save the image to the file "image.png"
            ImageIO.write( generator.getImage(), "png", new File( "image.png" ) );
        } catch ( IOException e ) {
            e.printStackTrace();
        }
    }
}

```

### java_code_3.txt
```java
boolean SIDESTICK = false;
boolean[][] isTaken;

void setup() {
  size(512, 512);
  background(0);
  isTaken = new boolean[width][height];
  isTaken[width/2][height/2] = true;
}

void draw() {
  int x = floor(random(width));
  int y = floor(random(height));
  if (isTaken[x][y]) { 
    return;
  }
  while (true) {
    int xp = x + floor(random(-1, 2));
    int yp = y + floor(random(-1, 2));
    boolean iscontained = (
      0 <= xp && xp < width  && 
      0 <= yp && yp < height
      );
    if (iscontained && !isTaken[xp][yp]) {
      x = xp;
      y = yp;
      continue;
    } else {
      if (SIDESTICK || (iscontained && isTaken[xp][yp])) {
        isTaken[x][y] = true;
        set(x, y, #FFFFFF);
      }
      break;
    }
  }
  if (frameCount > width * height) {
    noLoop();
  }
}

```

## Python Code
### python_code_1.txt
```python
SIDESTICK = False

def setup() :
    global is_taken
    size(512, 512)
    background(0)
    is_taken = [[False] * height for _ in range(width)]
    is_taken[width/2][height/2] = True


def draw() :
    x = floor(random(width))
    y = floor(random(height))
    if is_taken[x][y]: 
        return
    while True:
        xp = x + floor(random(-1, 2))
        yp = y + floor(random(-1, 2))
        is_contained = 0 <= xp < width and 0 <= yp < height
        if is_contained and not is_taken[xp][yp]:
            x = xp
            y = yp
            continue
        else:
            if SIDESTICK or (is_contained and is_taken[xp][yp]):
                is_taken[x][y] = True
                set(x, y, color(255))            
            break
        
    if frameCount > width * height:
        noLoop()

```

### python_code_2.txt
```python
import pygame, sys, os
from pygame.locals import *
from random import randint
pygame.init()

MAXSPEED = 15
SIZE = 3
COLOR = (45, 90, 45)
WINDOWSIZE = 400
TIMETICK = 1
MAXPART = 50

freeParticles = pygame.sprite.Group()
tree = pygame.sprite.Group()

window = pygame.display.set_mode((WINDOWSIZE, WINDOWSIZE))
pygame.display.set_caption("Brownian Tree")

screen = pygame.display.get_surface()


class Particle(pygame.sprite.Sprite):
    def __init__(self, vector, location, surface):
        pygame.sprite.Sprite.__init__(self)
        self.vector = vector
        self.surface = surface
        self.accelerate(vector)
        self.add(freeParticles)
        self.rect = pygame.Rect(location[0], location[1], SIZE, SIZE)
        self.surface.fill(COLOR, self.rect)

    def onEdge(self):
        if self.rect.left <= 0:
            self.vector = (abs(self.vector[0]), self.vector[1])
        elif self.rect.top <= 0:
            self.vector = (self.vector[0], abs(self.vector[1]))
        elif self.rect.right >= WINDOWSIZE:
            self.vector = (-abs(self.vector[0]), self.vector[1])
        elif self.rect.bottom >= WINDOWSIZE:
            self.vector = (self.vector[0], -abs(self.vector[1]))

    def update(self):
        if freeParticles in self.groups():
            self.surface.fill((0,0,0), self.rect)
            self.remove(freeParticles)
            if pygame.sprite.spritecollideany(self, freeParticles):
                self.accelerate((randint(-MAXSPEED, MAXSPEED), 
                                 randint(-MAXSPEED, MAXSPEED)))
                self.add(freeParticles)
            elif pygame.sprite.spritecollideany(self, tree):
                self.stop()
            else:
                self.add(freeParticles)
                
            self.onEdge()

            if (self.vector == (0,0)) and tree not in self.groups():
                self.accelerate((randint(-MAXSPEED, MAXSPEED), 
                                 randint(-MAXSPEED, MAXSPEED)))
            self.rect.move_ip(self.vector[0], self.vector[1])
        self.surface.fill(COLOR, self.rect)

    def stop(self):
        self.vector = (0,0)
        self.remove(freeParticles)
        self.add(tree)

    def accelerate(self, vector):
        self.vector = vector

NEW = USEREVENT + 1
TICK = USEREVENT + 2

pygame.time.set_timer(NEW, 50)
pygame.time.set_timer(TICK, TIMETICK)


def input(events):
    for event in events:
        if event.type == QUIT:
            sys.exit(0)
        elif event.type == NEW and (len(freeParticles) < MAXPART):
            Particle((randint(-MAXSPEED,MAXSPEED),
                      randint(-MAXSPEED,MAXSPEED)),
                     (randint(0, WINDOWSIZE), randint(0, WINDOWSIZE)), 
                     screen)
        elif event.type == TICK:
            freeParticles.update()


half = WINDOWSIZE/2
tenth = WINDOWSIZE/10

root = Particle((0,0),
                (randint(half-tenth, half+tenth), 
                 randint(half-tenth, half+tenth)), screen)
root.stop()

while True:
    input(pygame.event.get())
    pygame.display.flip()

```

