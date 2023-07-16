# Bitmap/Histogram

## Task Link
[Rosetta Code - Bitmap/Histogram](https://rosettacode.org/wiki/Bitmap/Histogram)

## Java Code
### java_code_1.txt
```java
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;

public enum ImageProcessing {
    ;

    public static void main(String[] args) throws IOException {
        BufferedImage img = ImageIO.read(new File("example.png"));

        BufferedImage bwimg = toBlackAndWhite(img);

        ImageIO.write(bwimg, "png", new File("example-bw.png"));
    }

    private static int luminance(int rgb) {
        int r = (rgb >> 16) & 0xFF;
        int g = (rgb >> 8) & 0xFF;
        int b = rgb & 0xFF;
        return (r + b + g) / 3;
    }

    private static BufferedImage toBlackAndWhite(BufferedImage img) {
        int width = img.getWidth();
        int height = img.getHeight();

        int[] histo = computeHistogram(img);

        int median = getMedian(width * height, histo);

        BufferedImage bwimg = new BufferedImage(width, height, img.getType());
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                bwimg.setRGB(x, y, luminance(img.getRGB(x, y)) >= median ? 0xFFFFFFFF : 0xFF000000);
            }
        }
        return bwimg;
    }

    private static int[] computeHistogram(BufferedImage img) {
        int width = img.getWidth();
        int height = img.getHeight();

        int[] histo = new int[256];
        for (int y = 0; y < height; y++) {
            for (int x = 0; x < width; x++) {
                histo[luminance(img.getRGB(x, y))]++;
            }
        }
        return histo;
    }

    private static int getMedian(int total, int[] histo) {
        int median = 0;
        int sum = 0;
        for (int i = 0; i < histo.length && sum + histo[i] < total / 2; i++) {
            sum += histo[i];
            median++;
        }
        return median;
    }
}

```

## Python Code
### python_code_1.txt
```python
from PIL import Image

# Open the image
image = Image.open("lena.jpg")
# Get the width and height of the image
width, height = image.size
# Calculate the amount of pixels
amount = width * height

# Total amount of greyscale
total = 0
# B/W image
bw_image = Image.new('L', (width, height), 0)
# Bitmap image
bm_image = Image.new('1', (width, height), 0)

for h in range(0, height):
    for w in range(0, width):
        r, g, b = image.getpixel((w, h))

        greyscale = int((r + g + b) / 3)
        total += greyscale

        bw_image.putpixel((w, h), gray_scale)

# The average greyscale
avg = total / amount

black = 0
white = 1

for h in range(0, height):
    for w in range(0, width):
        v = bw_image.getpixel((w, h))

        if v >= avg:
            bm_image.putpixel((w, h), white)
        else:
            bm_image.putpixel((w, h), black)

bw_image.show()
bm_image.show()

```

