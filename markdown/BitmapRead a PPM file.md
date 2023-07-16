# Bitmap/Read a PPM file

## Task Link
[Rosetta Code - Bitmap/Read a PPM file](https://rosettacode.org/wiki/Bitmap/Read_a_PPM_file)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.image.BufferedImage;
import java.awt.image.RenderedImage;
import java.io.BufferedInputStream;
import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;

import javax.imageio.ImageIO;

public class ReadPPMFile {

	public static void main(String[] aArgs) throws IOException {
        // Using the file created in the Bitmap task
		String filePath = "output.ppm";
		
		reader = new BufferedInputStream( new FileInputStream(filePath) );
		final char header1 = (char) reader.read();
        final char header2 = (char) reader.read();
        final char header3 = (char) reader.read();
        if ( header1 != 'P' || header2 != '6' || header3 != END_OF_LINE) {
        	reader.close();
        	throw new IllegalArgumentException("Not a valid P6 PPM file");
        }
        
        final int width = processCharacters(SPACE_CHARACTER);  
        final int height = processCharacters(END_OF_LINE);
        final int maxColorValue = processCharacters(END_OF_LINE);
        if ( maxColorValue < 0 || maxColorValue > 255 ) {
        	reader.close();
        	throw new IllegalArgumentException("Maximum color value is outside the range 0..255");
        }            
        
        // Remove any comments before reading data
        reader.mark(1);
        while ( reader.read() == START_OF_COMMENT ) {
        	 while ( reader.read() != END_OF_LINE );
        	 reader.mark(1);
        }
        reader.reset();
                
       // Read data
        BasicBitmapStorage bitmap = new BasicBitmapStorage(width, height);
        
        byte[] buffer = new byte[width * 3];
        for ( int y = 0; y < height; y++ ) {
            reader.read(buffer, 0, buffer.length);
            for ( int x = 0; x < width; x++ ) {                	
                Color color = new Color(Byte.toUnsignedInt(buffer[x * 3]),
                						Byte.toUnsignedInt(buffer[x * 3 + 1]),
                						Byte.toUnsignedInt(buffer[x * 3 + 2]));
                bitmap.setPixel(x, y, color);
            }
        }
        
        reader.close();
        
        // Convert to gray scale and save to a file
        bitmap.convertToGrayscale();
        File grayFile = new File("outputGray.jpg");
        ImageIO.write((RenderedImage) bitmap.getImage(), "jpg", grayFile);  	
	}
	
	private static int processCharacters(char aChar) throws IOException {
		StringBuilder characters = new StringBuilder();
		char ch;		
		while ( ( ch = (char) reader.read() ) != aChar ) {
        	if ( ch == START_OF_COMMENT ) {
        		while ( reader.read() != END_OF_LINE );
        		continue;
        	}
        	characters.append(ch);
        }
		return Integer.valueOf(characters.toString());
	}
	
	private static BufferedInputStream reader;
	
	private static final char START_OF_COMMENT = '#';
	private static final char SPACE_CHARACTER = ' ';
	private static final char END_OF_LINE = '\n';
   
}	
    
final class BasicBitmapStorage {

    public BasicBitmapStorage(int aWidth, int aHeight) {
        image = new BufferedImage(aWidth, aHeight, BufferedImage.TYPE_INT_RGB);
    }

    public void fill(Color aColor) {
        Graphics graphics = image.getGraphics();
        graphics.setColor(aColor);
        graphics.fillRect(0, 0, image.getWidth(), image.getHeight());
    }    

    public Color getPixel(int aX, int aY) {
        return new Color(image.getRGB(aX, aY));
    }
    
    public void setPixel(int aX, int aY, Color aColor) {
        image.setRGB(aX, aY, aColor.getRGB());
    }
    
    public Image getImage() {
    	return image;
    }
    
    public void convertToGrayscale() {        
        for ( int y = 0; y < image.getHeight(); y++ ) {
           	for ( int x = 0; x < image.getWidth(); x++ ) {
                int color = image.getRGB(x, y);

                int alpha = ( color >> 24 ) & 255;
                int red = ( color >> 16 ) & 255;
                int green = ( color >> 8 ) & 255;
                int blue = color & 255;

                final int luminance = (int) ( 0.2126 * red + 0.7152 * green + 0.0722 * blue );

                alpha = alpha << 24;
                red = luminance << 16;
                green = luminance << 8;
                blue = luminance;

                color = alpha + red + green + blue;

                image.setRGB(x, y, color);
            }
        }
    }
    
    private final BufferedImage image;

}

```

## Python Code
### python_code_1.txt
```python
# With help from http://netpbm.sourceforge.net/doc/ppm.html

# String masquerading as ppm file (version P3)
import io

ppmtxt = '''P3
# feep.ppm
4 4
15
 0  0  0    0  0  0    0  0  0   15  0 15
 0  0  0    0 15  7    0  0  0    0  0  0
 0  0  0    0  0  0    0 15  7    0  0  0
15  0 15    0  0  0    0  0  0    0  0  0
'''


def tokenize(f):
    for line in f:
        if line[0] != '#':
            for t in line.split():
                yield t

def ppmp3tobitmap(f):
    t = tokenize(f)
    nexttoken = lambda : next(t)
    assert 'P3' == nexttoken(), 'Wrong filetype'
    width, height, maxval = (int(nexttoken()) for i in range(3))
    bitmap = Bitmap(width, height, Colour(0, 0, 0))
    for h in range(height-1, -1, -1):
        for w in range(0, width):
            bitmap.set(w, h, Colour( *(int(nexttoken()) for i in range(3))))

    return bitmap
    
print('Original Colour PPM file')
print(ppmtxt)
ppmfile = io.StringIO(ppmtxt)
bitmap = ppmp3tobitmap(ppmfile)
print('Grey PPM:')
bitmap.togreyscale()
ppmfileout = io.StringIO('')
bitmap.writeppmp3(ppmfileout)
print(ppmfileout.getvalue())


'''
The print statements above produce the following output:

Original Colour PPM file
P3
# feep.ppm
4 4
15
 0  0  0    0  0  0    0  0  0   15  0 15
 0  0  0    0 15  7    0  0  0    0  0  0
 0  0  0    0  0  0    0 15  7    0  0  0
15  0 15    0  0  0    0  0  0    0  0  0

Grey PPM:
P3
# generated from Bitmap.writeppmp3
4 4
11
    0  0  0    0  0  0    0  0  0    4  4  4
    0  0  0   11 11 11    0  0  0    0  0  0
    0  0  0    0  0  0   11 11 11    0  0  0
    4  4  4    0  0  0    0  0  0    0  0  0

'''

```

