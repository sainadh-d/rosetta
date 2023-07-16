# Ulam spiral (for primes)

## Task Link
[Rosetta Code - Ulam spiral (for primes)](https://rosettacode.org/wiki/Ulam_spiral_(for_primes))

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;

public class Ulam{
	enum Direction{
		RIGHT, UP, LEFT, DOWN;
	}
	
	private static String[][] genUlam(int n){
		return genUlam(n, 1);
	}

	private static String[][] genUlam(int n, int i){
		String[][] spiral = new String[n][n];
		Direction dir = Direction.RIGHT;
		int j = i;
		int y = n / 2;
		int x = (n % 2 == 0) ? y - 1 : y; //shift left for even n's
		while(j <= ((n * n) - 1 + i)){
			spiral[y][x] = isPrime(j) ? String.format("%4d", j) : " ---";

			switch(dir){
			case RIGHT:
				if(x <= (n - 1) && spiral[y - 1][x] == null && j > i) dir = Direction.UP; break;
			case UP:
				if(spiral[y][x - 1] == null) dir = Direction.LEFT; break;
			case LEFT:
				if(x == 0 || spiral[y + 1][x] == null) dir = Direction.DOWN; break;
			case DOWN:
				if(spiral[y][x + 1] == null) dir = Direction.RIGHT; break;
			}
			
			switch(dir){
				case RIGHT:	x++; break;
				case UP: 	y--; break;
				case LEFT:	x--; break;
				case DOWN:	y++; break;
			}
			j++;
		}
		return spiral;
	}
	
	public static boolean isPrime(int a){
		   if(a == 2) return true;
		   if(a <= 1 || a % 2 == 0) return false;
		   long max = (long)Math.sqrt(a);
		   for(long n = 3; n <= max; n += 2){
		      if(a % n == 0) return false;
		   }
		   return true;
		}
	
	public static void main(String[] args){
		String[][] ulam = genUlam(9);
		for(String[] row : ulam){
			System.out.println(Arrays.toString(row).replaceAll(",", ""));
		}
		System.out.println();
		
		for(String[] row : ulam){
			System.out.println(Arrays.toString(row).replaceAll("\\[\\s+\\d+", "[  * ").replaceAll("\\s+\\d+", "   * ").replaceAll(",", ""));
		}
	}
}

```

### java_code_2.txt
```java
import java.awt.*;
import javax.swing.*;

public class LargeUlamSpiral extends JPanel {

    public LargeUlamSpiral() {
        setPreferredSize(new Dimension(605, 605));
        setBackground(Color.white);
    }

    private boolean isPrime(int n) {
        if (n <= 2 || n % 2 == 0)
            return n == 2;
        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0)
                return false;
        return true;
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        g.setColor(getForeground());

        double angle = 0.0;
        int x = 300, y = 300, dx = 1, dy = 0;

        for (int i = 1, step = 1, turn = 1; i < 40_000; i++) {

            if (isPrime(i))
                g.fillRect(x, y, 2, 2);

            x += dx * 3;
            y += dy * 3;

            if (i == turn) {

                angle += 90.0;

                if ((dx == 0 && dy == -1) || (dx == 0 && dy == 1))
                    step++;

                turn += step;

                dx = (int) Math.cos(Math.toRadians(angle));
                dy = (int) Math.sin(Math.toRadians(-angle));
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Large Ulam Spiral");
            f.setResizable(false);
            f.add(new LargeUlamSpiral(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

### java_code_3.txt
```java
import java.awt.*;
import javax.swing.*;

public class UlamSpiral extends JPanel {

    Font primeFont = new Font("Arial", Font.BOLD, 20);
    Font compositeFont = new Font("Arial", Font.PLAIN, 16);

    public UlamSpiral() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);
    }

    private boolean isPrime(int n) {
        if (n <= 2 || n % 2 == 0)
            return n == 2;
        for (int i = 3; i * i <= n; i += 2)
            if (n % i == 0)
                return false;
        return true;
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        g.setStroke(new BasicStroke(2));

        double angle = 0.0;
        int x = 280, y = 330, dx = 1, dy = 0;

        g.setColor(getForeground());
        g.drawLine(x, y - 5, x + 50, y - 5);

        for (int i = 1, step = 1, turn = 1; i < 100; i++) {

            g.setColor(getBackground());
            g.fillRect(x - 5, y - 20, 30, 30);
            g.setColor(getForeground());
            g.setFont(isPrime(i) ? primeFont : compositeFont);
            g.drawString(String.valueOf(i), x + (i < 10 ? 4 : 0), y);

            x += dx * 50;
            y += dy * 50;

            if (i == turn) {
                angle += 90.0;

                if ((dx == 0 && dy == -1) || (dx == 0 && dy == 1))
                    step++;

                turn += step;

                dx = (int) Math.cos(Math.toRadians(angle));
                dy = (int) Math.sin(Math.toRadians(-angle));

                g.translate(9, -5);
                g.drawLine(x, y, x + dx * step * 50, y + dy * step * 50);
                g.translate(-9, 5);
            }
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Ulam Spiral");
            f.setResizable(false);
            f.add(new UlamSpiral(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
# coding=UTF-8
from __future__ import print_function, division
from math import sqrt

def cell(n, x, y, start=1):
    d, y, x = 0, y - n//2, x - (n - 1)//2
    l = 2*max(abs(x), abs(y))
    d = (l*3 + x + y) if y >= x else (l - x - y)
    return (l - 1)**2 + d + start - 1

def show_spiral(n, symbol='# ', start=1, space=None):
    top = start + n*n + 1
    is_prime = [False,False,True] + [True,False]*(top//2)
    for x in range(3, 1 + int(sqrt(top))):
        if not is_prime[x]: continue
        for i in range(x*x, top, x*2):
            is_prime[i] = False

    cell_str = lambda x: f(x) if is_prime[x] else space
    f = lambda _: symbol # how to show prime cells

    if space == None: space = ' '*len(symbol)

    if not len(symbol): # print numbers instead
        max_str = len(str(n*n + start - 1))
        if space == None: space = '.'*max_str + ' '
        f = lambda x: ('%' + str(max_str) + 'd ')%x

    for y in range(n):
        print(''.join(cell_str(v) for v in [cell(n, x, y, start) for x in range(n)]))
    print()

show_spiral(10, symbol=u'♞', space=u'♘') # black are the primes
show_spiral(9, symbol='', space=' - ')
# for filling giant terminals
#show_spiral(1001, symbol='*', start=42)

```

