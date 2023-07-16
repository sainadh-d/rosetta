# Peano curve

## Task Link
[Rosetta Code - Peano curve](https://rosettacode.org/wiki/Peano_curve)

## Java Code
### java_code_1.txt
```java
import java.io.*;

public class PeanoCurve {
    public static void main(final String[] args) {
        try (Writer writer = new BufferedWriter(new FileWriter("peano_curve.svg"))) {
            PeanoCurve s = new PeanoCurve(writer);
            final int length = 8;
            s.currentAngle = 90;
            s.currentX = length;
            s.currentY = length;
            s.lineLength = length;
            s.begin(656);
            s.execute(rewrite(4));
            s.end();
        } catch (final Exception ex) {
            ex.printStackTrace();
        }
    }

    private PeanoCurve(final Writer writer) {
        this.writer = writer;
    }

    private void begin(final int size) throws IOException {
        write("<svg xmlns='http://www.w3.org/2000/svg' width='%d' height='%d'>\n", size, size);
        write("<rect width='100%%' height='100%%' fill='white'/>\n");
        write("<path stroke-width='1' stroke='black' fill='none' d='");
    }

    private void end() throws IOException {
        write("'/>\n</svg>\n");
    }

    private void execute(final String s) throws IOException {
        write("M%g,%g\n", currentX, currentY);
        for (int i = 0, n = s.length(); i < n; ++i) {
            switch (s.charAt(i)) {
                case 'F':
                    line(lineLength);
                    break;
                case '+':
                    turn(ANGLE);
                    break;
                case '-':
                    turn(-ANGLE);
                    break;
            }
        }
    }

    private void line(final double length) throws IOException {
        final double theta = (Math.PI * currentAngle) / 180.0;
        currentX += length * Math.cos(theta);
        currentY += length * Math.sin(theta);
        write("L%g,%g\n", currentX, currentY);
    }

    private void turn(final int angle) {
        currentAngle = (currentAngle + angle) % 360;
    }

    private void write(final String format, final Object... args) throws IOException {
        writer.write(String.format(format, args));
    }

    private static String rewrite(final int order) {
        String s = "L";
        for (int i = 0; i < order; ++i) {
            final StringBuilder sb = new StringBuilder();
            for (int j = 0, n = s.length(); j < n; ++j) {
                final char ch = s.charAt(j);
                if (ch == 'L')
                    sb.append("LFRFL-F-RFLFR+F+LFRFL");
                else if (ch == 'R')
                    sb.append("RFLFR+F+LFRFL-F-RFLFR");
                else
                    sb.append(ch);
            }
            s = sb.toString();
        }
        return s;
    }

    private final Writer writer;
    private double lineLength;
    private double currentX;
    private double currentY;
    private int currentAngle;
    private static final int ANGLE = 90;
}

```

### java_code_2.txt
```java
//Abhishek Ghosh, 28th June 2022

void Peano(int x, int y, int lg, int i1, int i2) {
 
  if (lg == 1) {
    ellipse(x,y,1,1);
    return;
  }
 
  lg = lg/3;
  Peano(x+(2*i1*lg), y+(2*i1*lg), lg, i1, i2);
  Peano(x+((i1-i2+1)*lg), y+((i1+i2)*lg), lg, i1, 1-i2);
  Peano(x+lg, y+lg, lg, i1, 1-i2);
  Peano(x+((i1+i2)*lg), y+((i1-i2+1)*lg), lg, 1-i1, 1-i2);
  Peano(x+(2*i2*lg), y+(2*(1-i2)*lg), lg, i1, i2);
  Peano(x+((1+i2-i1)*lg), y+((2-i1-i2)*lg), lg, i1, i2);
  Peano(x+(2*(1-i1)*lg), y+(2*(1-i1)*lg), lg, i1, i2);
  Peano(x+((2-i1-i2)*lg), y+((1+i2-i1)*lg), lg, 1-i1, i2);
  Peano(x+(2*(1-i2)*lg), y+(2*i2*lg), lg, 1-i1, i2);
}

void setup(){
  size(1000,1000);
  Peano(0, 0, 1000, 0, 0);
}

```

## Python Code
### python_code_1.txt
```python
import turtle as tt
import inspect

stack = [] # Mark the current stacks in run.
def peano(iterations=1):
    global stack

    # The turtle Ivan:
    ivan = tt.Turtle(shape = "classic", visible = True)


    # The app window:
    screen = tt.Screen()
    screen.title("Desenhin do Peano")
    screen.bgcolor("#232323")
    screen.delay(0) # Speed on drawing (if higher, more slow)
    screen.setup(width=0.95, height=0.9)

    # The size of each step walked (here, named simply "walk"). It's not a pixel scale. This may stay still:
    walk = 1

    def screenlength(k):
        # A function to make the image good to see (without it would result in a partial image).
        # This will guarantee that we can see the the voids and it's steps.
        if k != 0:
            length = screenlength(k-1)
            return 2*length + 1
        else: return 0

    kkkj = screenlength(iterations)
    screen.setworldcoordinates(-1, -1, kkkj + 1, kkkj + 1)
    ivan.color("#EEFFFF", "#FFFFFF")


    # The magic  \(^-^)/:
    def step1(k):
        global stack
        stack.append(len(inspect.stack()))
        if k != 0:
            ivan.left(90)
            step2(k - 1)
            ivan.forward(walk)
            ivan.right(90)
            step1(k - 1)
            ivan.forward(walk)
            step1(k - 1)
            ivan.right(90)
            ivan.forward(walk)
            step2(k - 1)
            ivan.left(90)
    def step2(k):
        global stack
        stack.append(len(inspect.stack()))
        if k != 0:
            ivan.right(90)
            step1(k - 1)
            ivan.forward(walk)
            ivan.left(90)
            step2(k - 1)
            ivan.forward(walk)
            step2(k - 1)
            ivan.left(90)
            ivan.forward(walk)
            step1(k - 1)
            ivan.right(90)

    # Making the program work:
    ivan.left(90)
    step2(iterations)

    tt.done()

if __name__ == "__main__":
    peano(4)
    import pylab as P # This plot, after closing the drawing window, the "stack" graphic.
    P.plot(stack)
    P.show()

```

