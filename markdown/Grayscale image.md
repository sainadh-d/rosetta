# Grayscale image

## Task Link
[Rosetta Code - Grayscale image](https://rosettacode.org/wiki/Grayscale_image)

## Java Code
### java_code_1.txt
```java
void convertToGrayscale(final BufferedImage image){
    for(int i=0; i<image.getWidth(); i++){
        for(int j=0; j<image.getHeight(); j++){
            int color = image.getRGB(i,j);

            int alpha = (color >> 24) & 255;
            int red = (color >> 16) & 255;
            int green = (color >> 8) & 255;
            int blue = (color) & 255;

            final int lum = (int)(0.2126 * red + 0.7152 * green + 0.0722 * blue);

            alpha = (alpha << 24);
            red = (lum << 16);
            green = (lum << 8);
            blue = lum;

            color = alpha + red + green + blue;

            image.setRGB(i,j,color);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# String masquerading as ppm file (version P3)
import io
ppmfileout = io.StringIO('')

def togreyscale(self):
    for h in range(self.height):
        for w in range(self.width):
            r, g, b = self.get(w, h)
            l = int(0.2126 * r + 0.7152 * g + 0.0722 * b)
            self.set(w, h, Colour(l, l, l))

Bitmap.togreyscale = togreyscale    


# Draw something simple
bitmap = Bitmap(4, 4, white)
bitmap.fillrect(1, 0, 1, 2, Colour(127, 0, 63))
bitmap.set(3, 3, Colour(0, 127, 31))
print('Colour:')
# Write to the open 'file' handle
bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())
print('Grey:')
bitmap.togreyscale()
ppmfileout = io.StringIO('')
bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())


'''
The print statement above produces the following output :

Colour:
P3
# generated from Bitmap.writeppmp3
4 4
255
   255 255 255   255 255 255   255 255 255     0 127  31
   255 255 255   255 255 255   255 255 255   255 255 255
   255 255 255   127   0  63   255 255 255   255 255 255
   255 255 255   127   0  63   255 255 255   255 255 255

Grey:
P3
# generated from Bitmap.writeppmp3
4 4
254
   254 254 254   254 254 254   254 254 254    93  93  93
   254 254 254   254 254 254   254 254 254   254 254 254
   254 254 254    31  31  31   254 254 254   254 254 254
   254 254 254    31  31  31   254 254 254   254 254 254

'''

```

