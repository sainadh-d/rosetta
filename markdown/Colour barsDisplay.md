# Colour bars/Display

## Task Link
[Rosetta Code - Colour bars/Display](https://rosettacode.org/wiki/Colour_bars/Display)

## Java Code
### java_code_1.txt
```java
import java.awt.Color;
import java.awt.Graphics;

import javax.swing.JFrame;

public class ColorFrame extends JFrame {
	public ColorFrame(int width, int height) {
		this.setDefaultCloseOperation(EXIT_ON_CLOSE);
		this.setSize(width, height);
		this.setVisible(true);
	}

	@Override
	public void paint(Graphics g) {
		Color[] colors = { Color.black, Color.red, Color.green, Color.blue,
				Color.pink, Color.CYAN, Color.yellow, Color.white };

		for (int i = 0; i < colors.length; i++) {
			g.setColor(colors[i]);
			g.fillRect(this.getWidth() / colors.length * i, 0, this.getWidth()
					/ colors.length, this.getHeight());
		}
	}

	public static void main(String args[]) {
		new ColorFrame(200, 200);
	}
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
#vertical coloured stripes in window in Python 2.7.1

from livewires import *

horiz=640; vert=480
begin_graphics(width=horiz,height=vert,title="v_stripes",background=Colour.black)
NameColors=["black","red","green","dark_blue","purple","blue","yellow","white"]
stepik=horiz/len(NameColors)

for index,each in enumerate(NameColors):
	ExcStrng="set_colour(Colour."+each+")"
	exec ExcStrng
	box(index*stepik,0,(index+1)*stepik,vert,filled=1)

while keys_pressed() != ['x']: # press x key to terminate program
	pass

end_graphics()

```

