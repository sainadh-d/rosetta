# Yin and yang

## Task Link
[Rosetta Code - Yin and yang](https://rosettacode.org/wiki/Yin_and_yang)

## Java Code
### java_code_1.txt
```java
package org.rosettacode.yinandyang;

import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import javax.swing.ImageIcon;
import javax.swing.JFrame;
import javax.swing.JLabel;

public class YinYangGenerator
{
    private final int size;

    public YinYangGenerator(final int size)
    {
        this.size = size;
    }

    /**
     *  Draw a yin yang symbol on the given graphics context.
     */
    public void drawYinYang(final Graphics graphics)
    {
        // Preserve the color for the caller
        final Color colorSave = graphics.getColor();

        graphics.setColor(Color.WHITE);
        // Use fillOval to draw a filled in circle
        graphics.fillOval(0, 0, size-1, size-1);
        
        graphics.setColor(Color.BLACK);
        // Use fillArc to draw part of a filled in circle
        graphics.fillArc(0, 0, size-1, size-1, 270, 180);
        graphics.fillOval(size/4, size/2, size/2, size/2);
        
        graphics.setColor(Color.WHITE);
        graphics.fillOval(size/4, 0, size/2, size/2);
        graphics.fillOval(7*size/16, 11*size/16, size/8, size/8);

        graphics.setColor(Color.BLACK);
        graphics.fillOval(7*size/16, 3*size/16, size/8, size/8);
        // Use drawOval to draw an empty circle for the outside border
        graphics.drawOval(0, 0, size-1, size-1);
        
        // Restore the color for the caller
        graphics.setColor(colorSave);
    }

    /**
     *  Create an image containing a yin yang symbol.
     */
    public Image createImage(final Color bg)
    {
        // A BufferedImage creates the image in memory
        final BufferedImage image = new BufferedImage(size, size, BufferedImage.TYPE_INT_RGB);
        // Get the graphics object for the image; note in many
        // applications you actually use Graphics2D for the 
        // additional API calls
        final Graphics graphics = image.getGraphics();
        // Color in the background of the image
        graphics.setColor(bg);
        graphics.fillRect(0,0,size,size);
        drawYinYang(graphics);
        return image;
    }

    public static void main(final String args[])
    {
        final int size = Integer.parseInt(args[0]);
        final YinYangGenerator generator = new YinYangGenerator(size);

        final JFrame frame = new JFrame("Yin Yang Generator");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        final Image yinYang = generator.createImage(frame.getBackground());
        // Use JLabel to display an image
        frame.add(new JLabel(new ImageIcon(yinYang)));
        frame.pack();
        frame.setVisible(true);
    }
}

```

### java_code_2.txt
```java
import java.util.Collection;
import java.util.Map;
import java.util.Optional;
import java.util.function.BooleanSupplier;
import java.util.function.Supplier;
import java.util.stream.IntStream;
import java.util.stream.Stream;

import static java.util.Collections.singletonMap;

public interface YinYang {
  public static boolean circle(
    int x,
    int y,
    int c,
    int r
  ) {
    return
      (r * r) >=
        ((x = x / 2) * x)
         + ((y = y - c) * y)
    ;
  }

  public static String pixel(int x, int y, int r) {
    return Stream.<Map<BooleanSupplier, Supplier<String>>>of(
      singletonMap(
        () -> circle(x, y, -r / 2, r / 6),
        () -> "#"
      ),
      singletonMap(
        () -> circle(x, y, r / 2, r / 6),
        () -> "."
      ),
      singletonMap(
        () -> circle(x, y, -r / 2, r / 2),
        () -> "."
      ),
      singletonMap(
        () -> circle(x, y, r / 2, r / 2),
        () -> "#"
      ),
      singletonMap(
        () -> circle(x, y, 0, r),
        () -> x < 0 ? "." : "#"
      )
    )
      .sequential()
      .map(Map::entrySet)
      .flatMap(Collection::stream)
      .filter(e -> e.getKey().getAsBoolean())
      .map(Map.Entry::getValue)
      .map(Supplier::get)
      .findAny()
      .orElse(" ")
    ;
  }

  public static void yinYang(int r) {
    IntStream.rangeClosed(-r, r)
      .mapToObj(
        y ->
          IntStream.rangeClosed(
            0 - r - r,
            r + r
          )
            .mapToObj(x -> pixel(x, y, r))
            .reduce("", String::concat)
      )
      .forEach(System.out::println)
    ;
  }

  public static void main(String... arguments) {
    Optional.of(arguments)
      .filter(a -> a.length == 1)
      .map(a -> a[0])
      .map(Integer::parseInt)
      .ifPresent(YinYang::yinYang)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
import math
def yinyang(n=3):
	radii   = [i * n for i in (1, 3, 6)]
	ranges  = [list(range(-r, r+1)) for r in radii]
	squares = [[ (x,y) for x in rnge for y in rnge]
		   for rnge in ranges]
	circles = [[ (x,y) for x,y in sqrpoints
		     if math.hypot(x,y) <= radius ]
		   for sqrpoints, radius in zip(squares, radii)]
	m = {(x,y):' ' for x,y in squares[-1]}
	for x,y in circles[-1]:
		m[x,y] = '*'
	for x,y in circles[-1]:
		if x>0: m[(x,y)] = '·'
	for x,y in circles[-2]:
		m[(x,y+3*n)] = '*'
		m[(x,y-3*n)] = '·'
	for x,y in circles[-3]:
		m[(x,y+3*n)] = '·'
		m[(x,y-3*n)] = '*'
	return '\n'.join(''.join(m[(x,y)] for x in reversed(ranges[-1])) for y in ranges[-1])

```

### python_code_2.txt
```python
from turtle import *

mode('logo')

def taijitu(r): 
  '''\
  Draw a classic Taoist taijitu of the given radius centered on the current
  turtle position. The "eyes" are placed along the turtle's heading, the
  filled one in front, the open one behind.
  '''

  # useful derivative values
  r2, r4, r8 = (r >> s for s in (1, 2, 3))

  # remember where we started
  x0, y0 = start = pos()
  startcolour = color()
  startheading = heading()
  color('black', 'black')

  # draw outer circle
  pendown()
  circle(r)

  # draw two 'fishes'
  begin_fill(); circle(r, 180); circle(r2, 180); circle(-r2, 180); end_fill()

  # black 'eye'  
  setheading(0); penup(); goto(-(r4 + r8) + x0, y0); pendown()
  begin_fill(); circle(r8); end_fill()

  # white 'eye'
  color('white', 'white'); setheading(0); penup(); goto(-(r+r4+r8) + x0, y0); pendown()
  begin_fill(); circle(r8); end_fill() 

  # put the turtle back where it started
  penup()
  setpos(start)
  setheading(startheading)
  color(*startcolour)


if __name__ == '__main__': 
  # demo code to produce image at right
  reset()
  #hideturtle()
  penup()
  goto(300, 200)
  taijitu(200)
  penup()
  goto(-150, -150)
  taijitu(100)
  hideturtle()

```

