# Bitmap

## Task Link
[Rosetta Code - Bitmap](https://rosettacode.org/wiki/Bitmap)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;

public class BasicBitmapStorage {

    private final BufferedImage image;

    public BasicBitmapStorage(int width, int height) {
        image = new BufferedImage(width, height, BufferedImage.TYPE_INT_RGB);
    }

    public void fill(Color c) {
        Graphics g = image.getGraphics();
        g.setColor(c);
        g.fillRect(0, 0, image.getWidth(), image.getHeight());
    }

    public void setPixel(int x, int y, Color c) {
        image.setRGB(x, y, c.getRGB());
    }

    public Color getPixel(int x, int y) {
        return new Color(image.getRGB(x, y));
    }

    public Image getImage() {
        return image;
    }
}

```

### java_code_2.txt
```java
import static org.junit.Assert.assertEquals;

import java.awt.Color;
import org.junit.Test;

public class BasicBitmapStorageTest {

    @Test
    public void testHappy() {
        int width = 640;
        int height = 480;

        BasicBitmapStorage bbs = new BasicBitmapStorage(width, height);
        bbs.fill(Color.CYAN);
        bbs.setPixel(width / 2, height / 2, Color.BLACK);
        Color c1 = bbs.getPixel(width / 2, height / 2);
        Color c2 = bbs.getPixel(20, 20);

        assertEquals(Color.BLACK, c1);
        assertEquals(Color.CYAN, c2);
    }
}

```

### java_code_3.txt
```java
PGraphics bitmap = createGraphics(100,100); // Create the bitmap
bitmap.beginDraw();
bitmap.background(255, 0, 0); // Fill bitmap with red rgb color
bitmap.endDraw();
image(bitmap, 0, 0); // Place bitmap on screen.
color b = color(0, 0, 255); // Define a blue rgb color
set(50, 50, b); // Set blue colored pixel in the middle of the screen
color c = get(50, 50); // Get the color of same pixel
if(b == c) print("Color changed correctly"); // Verify

```

## Python Code
