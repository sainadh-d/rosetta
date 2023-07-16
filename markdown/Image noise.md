# Image noise

## Task Link
[Rosetta Code - Image noise](https://rosettacode.org/wiki/Image_noise)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import java.awt.image.*;
import java.util.Arrays;
import java.util.Random;
import javax.swing.*;

public class ImageNoise {
    int framecount = 0;
    int fps = 0;
    BufferedImage image;
    Kernel kernel;
    ConvolveOp cop;
    JFrame frame = new JFrame("Java Image Noise");

    JPanel panel = new JPanel() {
        private int show_fps = 0; // 0 = blur + FPS; 1 = FPS only; 2 = neither
        private MouseAdapter ma = new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                show_fps = (show_fps + 1) % 3;
            }
        };
        {addMouseListener(ma);}

        @Override
        public Dimension getPreferredSize() {
            return new Dimension(320, 240);
        }

        @Override
        @SuppressWarnings("fallthrough")
        public void paintComponent(Graphics g1) {
            Graphics2D g = (Graphics2D) g1;
            drawNoise();
            g.drawImage(image, 0, 0, null);

            switch (show_fps) {
            case 0: 
                // add blur behind FPS
                int xblur = getWidth() - 130, yblur = getHeight() - 32;
                BufferedImage bc = image.getSubimage(xblur, yblur, 115, 32);
                BufferedImage bs = new BufferedImage(bc.getWidth(), bc.getHeight(),
                                                     BufferedImage.TYPE_BYTE_GRAY);
                cop.filter(bc, bs);
                g.drawImage(bs, xblur, yblur , null);
            case 1: 
                // add FPS text; case fallthough is deliberate
                g.setColor(Color.RED);
                g.setFont(new Font("Monospaced", Font.BOLD, 20));
                g.drawString("FPS: " + fps, getWidth() - 120, getHeight() - 10);
            }
            framecount++;
        }
    };
    
    // Timer to trigger update display, with 1 ms delay
    Timer repainter = new Timer(1, new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            panel.repaint();
        }
    });
    
    // Timer to check FPS, once per second
    Timer framerateChecker = new Timer(1000, new ActionListener() {
        @Override
        public void actionPerformed(ActionEvent e) {
            fps = framecount;
            framecount = 0;
        }
    });
    
    public ImageNoise() {
        // Intitalize kernel describing blur, and convolve operation based on this
        float[] vals = new float[121];
        Arrays.fill(vals, 1/121f);
        kernel = new Kernel(11, 11, vals);
        cop = new ConvolveOp(kernel, ConvolveOp.EDGE_NO_OP, null);
        
        // Initialize frame and timers
        frame.add(panel);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setVisible(true);
        repainter.start();
        framerateChecker.start();
    }

    void drawNoise() {
        int w = panel.getWidth(), h = panel.getHeight();
        
        // Check if our image is null or window has been resized, requiring new image
        if (null == image || image.getWidth() != w || image.getHeight() != h) {
            image = new BufferedImage(w, h, BufferedImage.TYPE_BYTE_GRAY);
        }
        Random rand = new Random();
        int[] data = new int[w * h];
        // Each int has 32 bits so we can use each bit for a different pixel - much faster
        for (int x = 0; x < w * h / 32; x++) {
            int r = rand.nextInt();
            for (int i = 0; i < 32; i++) {
                data[x * 32 + i] = (r & 1) * Integer.MAX_VALUE;
                r >>>= 1;
            }
        }
        // Copy raw data to the image's raster
        image.getRaster().setPixels(0, 0, w, h, data);
    }
    
    public static void main(String[] args) {
        // Invoke GUI on the Event Dispatching Thread
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                ImageNoise i = new ImageNoise();
            }
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
black = color(0)
white = color(255)

def setup():
    size(320, 240)
    # frameRate(30) # 60 by default


def draw():
    loadPixels()
    for i in range(len(pixels)):
        if random(1) < 0.5:
            pixels[i] = black
        else:
            pixels[i] = white

    updatePixels()
    fill(0, 128)
    rect(0, 0, 60, 20)
    fill(255)
    text(frameRate, 5, 15)

```

### python_code_2.txt
```python
import time
import random
import Tkinter
import Image, ImageTk # PIL libray

class App(object):
    def __init__(self, size, root):
        self.root = root
        self.root.title("Image Noise Test")

        self.img = Image.new("RGB", size)
        self.label = Tkinter.Label(root)
        self.label.pack()

        self.time = 0.0
        self.frames = 0
        self.size = size
        self.loop()

    def loop(self):
        self.ta = time.time()
        # 13 FPS boost. half integer idea from C#.
        rnd = random.random
        white = (255, 255, 255)
        black = (0, 0, 0)
        npixels = self.size[0] * self.size[1]
        data = [white if rnd() > 0.5 else black for i in xrange(npixels)]
        self.img.putdata(data)
        self.pimg = ImageTk.PhotoImage(self.img)
        self.label["image"] = self.pimg
        self.tb = time.time()

        self.time += (self.tb - self.ta)
        self.frames += 1

        if self.frames == 30:
            try:
                self.fps = self.frames / self.time
            except:
                self.fps = "INSTANT"
            print ("%d frames in %3.2f seconds (%s FPS)" %
                  (self.frames, self.time, self.fps))
            self.time = 0
            self.frames = 0

        self.root.after(1, self.loop)

def main():
    root = Tkinter.Tk()
    app = App((320, 240), root)
    root.mainloop()

main()

```

