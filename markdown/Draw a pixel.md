# Draw a pixel

## Task Link
[Rosetta Code - Draw a pixel](https://rosettacode.org/wiki/Draw_a_pixel)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import javax.swing.JFrame;

public class DrawAPixel extends JFrame{
	public DrawAPixel() {
		super("Red Pixel");
		setSize(320, 240);
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setVisible(true);
	}
	@Override
	public void paint(Graphics g) {
		g.setColor(new Color(255, 0, 0));
		g.drawRect(100, 100, 1, 1);
	}
	public static void main(String[] args) {
		new DrawAPixel();
	}
}

```

### java_code_2.txt
```java
import java.awt.Color;
import java.awt.Graphics;
import java.awt.image.BufferedImage;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class DrawAPixel extends JPanel{	
	private BufferedImage puffer;
	private JFrame window;
	private Graphics g;
	public DrawAPixel() {
		window = new JFrame("Red Pixel");
		window.setSize(320, 240);
		window.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		window.setLayout(null);
		setBounds(0, 0, 320, 240);
		window.add(this);
		window.setVisible(true);
	}
	@Override
	public void paint(Graphics gr) {
		if(g == null) {
			puffer = (BufferedImage) createImage(getWidth(), getHeight());
			g = puffer.getGraphics();
		}
		g.setColor(new Color(255, 0, 0));
		g.drawRect(100, 100, 1, 1);
		gr.drawImage(puffer, 0, 0, this);
	}
	public static void main(String[] args) {
		new DrawAPixel();
	}
}

```

## Python Code
### python_code_1.txt
```python
from PIL import Image

img = Image.new('RGB', (320, 240))
pixels = img.load()
pixels[100,100] = (255,0,0)
img.show()

```

