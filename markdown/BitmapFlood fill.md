# Bitmap/Flood fill

## Task Link
[Rosetta Code - Bitmap/Flood fill](https://rosettacode.org/wiki/Bitmap/Flood_fill)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Point;
import java.awt.image.BufferedImage;
import java.util.Deque;
import java.util.LinkedList;

public class FloodFill {
  public void floodFill(BufferedImage image, Point node, Color targetColor, Color replacementColor) {
    int width = image.getWidth();
    int height = image.getHeight();
    int target = targetColor.getRGB();
    int replacement = replacementColor.getRGB();
    if (target != replacement) {
      Deque<Point> queue = new LinkedList<Point>();
      do {
        int x = node.x;
        int y = node.y;
        while (x > 0 && image.getRGB(x - 1, y) == target) {
          x--;
        }
        boolean spanUp = false;
        boolean spanDown = false;
        while (x < width && image.getRGB(x, y) == target) {
          image.setRGB(x, y, replacement);
          if (!spanUp && y > 0 && image.getRGB(x, y - 1) == target) {
            queue.add(new Point(x, y - 1));
            spanUp = true;
          } else if (spanUp && y > 0 && image.getRGB(x, y - 1) != target) {
            spanUp = false;
          }
          if (!spanDown && y < height - 1 && image.getRGB(x, y + 1) == target) {
            queue.add(new Point(x, y + 1));
            spanDown = true;
          } else if (spanDown && y < height - 1 && image.getRGB(x, y + 1) != target) {
            spanDown = false;
          }
          x++;
        }
      } while ((node = queue.pollFirst()) != null);
    }
  }
}

```

### java_code_2.txt
```java
import java.io.IOException;
import java.awt.Color;
import java.awt.Point;
import java.awt.image.BufferedImage;
import java.io.File;
import javax.imageio.ImageIO;

public class Test {
  public Test() throws IOException {
    BufferedImage image = ImageIO.read(new File("Unfilledcirc.png"));
    new FloodFill().floodFill(image, new Point(50, 50), Color.WHITE, Color.RED);
    ImageIO.write(image, "png", new File("output.png"));
  }

  public static void main(String[] args) throws IOException {
    new Test();
  }
}

```

### java_code_3.txt
```java
import java.awt.Point;
import java.util.Queue;
import java.util.LinkedList;

PImage img;
int tolerance;
color fill_color;
boolean allowed;

void setup() {
  size(600, 400);
  img = loadImage("image.png");
  fill_color = color(250, 0, 0);  
  fill(0, 0, 100);
  tolerance = 15;
  image(img, 0, 0, width, height);
  textSize(18);
  text("Tolerance = "+tolerance+"  (Use mouse wheel to change)", 100, height-30);
  text("Right click to reset", 100, height-10);
}

void draw() { 
  if (allowed) {
    image(img, 0, 0, width, height);
    text("Tolerance = "+tolerance+"  (Use mouse wheel to change)", 100, height-30);
    text("Right click to reset", 100, height-10);
    allowed = false;
  }
}

void mousePressed() {
  if (mouseButton == RIGHT) {
    img = loadImage("image.png");
  } else {   
    img.loadPixels(); 
    flood(mouseX, mouseY);
    img.updatePixels(); 
    allowed = true;
  }
}

void mouseWheel(MouseEvent event) {
  float e = event.getCount();
  tolerance += 2*e;
  if (tolerance > 128) tolerance = 128;
  if (tolerance < 0) tolerance = 0;
  allowed = true;
}

void flood(int x, int y) {
  color target_color = img.pixels[pixel_position(mouseX, mouseY)]; 
  if (target_color != fill_color) {
    Queue<Point> queue = new LinkedList<Point>();
    queue.add(new Point(x, y));
    while (!queue.isEmpty()) {
      Point p = queue.remove();
      if (check(p.x, p.y, target_color)) {     
        queue.add(new Point(p.x, p.y-1)); 
        queue.add(new Point(p.x, p.y+1)); 
        queue.add(new Point(p.x-1, p.y)); 
        queue.add(new Point(p.x+1, p.y));
      }
    }
  }
}

int pixel_position(int x, int y) {
  return x + (y * img.width);
}

boolean check(int x, int y, color target_color) {
  if (x < 0 || y < 0 || y >= img.height || x >= img.width) return false;
  int pp = img.pixels[pixel_position(x, y)];
  boolean test_tolerance = (abs(green(target_color)-green(pp)) < tolerance
                         && abs(  red(target_color)-  red(pp)) < tolerance
                         && abs( blue(target_color)- blue(pp)) < tolerance);
  if (!test_tolerance) return false; 
  img.pixels[pixel_position(x, y)] = fill_color;
  return true;
}

```

## Python Code
### python_code_1.txt
```python
from collections import deque

image_file = "image.png"
fill_color = color(250, 0, 0)
tolerance = 15
allowed = False

def setup():
    global img
    size(600, 400)
    img = loadImage(image_file)
    fill(0, 0, 100)
    textSize(18)
    show()
    
def show():
    image(img, 0, 0, width, height)
    text("Tolerance = {}    (Use mouse wheel to change)".format(tolerance),
         100, height - 30)
    text("Right click to reset", 100, height - 10)
 
def draw():
    global allowed
    if allowed:
        show()
        allowed = False

def mousePressed():
    global allowed, img
    if mouseButton == RIGHT:
        img = loadImage(image_file)
    else:
        img.loadPixels()
        flood(mouseX, mouseY)
        img.updatePixels()
    allowed = True    

def mouseWheel(event):
    global allowed, tolerance
    e = event.getCount()
    tolerance += 2 * e
    if tolerance > 128:
        tolerance = 128
    if tolerance < 0:
        tolerance = 0
    allowed = True

def flood(x, y):
    target_color = img.pixels[pixel_position(mouseX, mouseY)]
    if target_color != fill_color:
        queue = deque()
        queue.append((x, y))
        while len(queue) > 0:
            p_x, p_y = queue.popleft()
            if (check(p_x, p_y, target_color)):
                queue.append((p_x, p_y - 1))
                queue.append((p_x, p_y + 1))
                queue.append((p_x - 1, p_y))
                queue.append((p_x + 1, p_y))

def pixel_position(x, y):
    return x + (y * img.width)

def check(x, y, target_color):
    if x < 0 or y < 0 or y >= img.height or x >= img.width:
        return False
    pp = img.pixels[pixel_position(x, y)]
    test_tolerance = (abs(green(target_color) - green(pp)) < tolerance
                      and abs(red(target_color) - red(pp)) < tolerance
                      and abs(blue(target_color) - blue(pp)) < tolerance)
    if not test_tolerance:
        return False
    img.pixels[pixel_position(x, y)] = fill_color
    return True

```

### python_code_2.txt
```python
import Image
def FloodFill( fileName, initNode, targetColor, replaceColor ):
   img = Image.open( fileName )
   pix = img.load()
   xsize, ysize = img.size
   Q = []
   if pix[ initNode[0], initNode[1] ] != targetColor:
      return img
   Q.append( initNode )
   while Q != []:
      node = Q.pop(0)
      if pix[ node[0], node[1] ] == targetColor:
         W = list( node )
         if node[0] + 1 < xsize:
            E = list( [ node[0] + 1, node[1] ] )
         else:
            E = list( node )
      # Move west until color of node does not match targetColor
      while pix[ W[0], W[1] ] == targetColor:
         pix[ W[0], W[1] ] = replaceColor
         if W[1] + 1 < ysize:
            if pix[ W[0], W[1] + 1 ] == targetColor:
               Q.append( [ W[0], W[1] + 1 ] )
         if W[1] - 1 >= 0:
            if pix[ W[0], W[1] - 1 ] == targetColor:
               Q.append( [ W[0], W[1] - 1 ] )
         if W[0] - 1 >= 0:
            W[0] = W[0] - 1
         else:
            break
      # Move east until color of node does not match targetColor
      while pix[ E[0], E[1] ] == targetColor:
         pix[ E[0], E[1] ] = replaceColor
         if E[1] + 1 < ysize:
            if pix[ E[0], E[1] + 1 ] == targetColor:
               Q.append( [ E[0], E[1] + 1 ] )
         if E[1] - 1 >= 0:
            if pix[ E[0], E[1] - 1 ] == targetColor:
               Q.append( [ E[0], E[1] -1 ] )
         if E[0] + 1 < xsize:
            E[0] = E[0] + 1
         else:
            break
      return img

```

### python_code_3.txt
```python
# "FloodFillClean.png" is name of input file
# [55,55] the x,y coordinate where fill starts
# (0,0,0,255) the target colour being filled( black in this example )
# (255,255,255,255) the final colour ( white in this case )
img = FloodFill( "FloodFillClean.png", [55,55], (0,0,0,255), (255,255,255,255) )
#The resulting image is saved as Filled.png
img.save( "Filled.png" )

```

