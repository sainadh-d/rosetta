# Cistercian numerals

## Task Link
[Rosetta Code - Cistercian numerals](https://rosettacode.org/wiki/Cistercian_numerals)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.List;

public class Cistercian {
    private static final int SIZE = 15;
    private final char[][] canvas = new char[SIZE][SIZE];

    public Cistercian(int n) {
        initN();
        draw(n);
    }

    public void initN() {
        for (var row : canvas) {
            Arrays.fill(row, ' ');
            row[5] = 'x';
        }
    }

    private void horizontal(int c1, int c2, int r) {
        for (int c = c1; c <= c2; c++) {
            canvas[r][c] = 'x';
        }
    }

    private void vertical(int r1, int r2, int c) {
        for (int r = r1; r <= r2; r++) {
            canvas[r][c] = 'x';
        }
    }

    private void diagd(int c1, int c2, int r) {
        for (int c = c1; c <= c2; c++) {
            canvas[r + c - c1][c] = 'x';
        }
    }

    private void diagu(int c1, int c2, int r) {
        for (int c = c1; c <= c2; c++) {
            canvas[r - c + c1][c] = 'x';
        }
    }

    private void draw(int v) {
        var thousands = v / 1000;
        v %= 1000;

        var hundreds = v / 100;
        v %= 100;

        var tens = v / 10;
        var ones = v % 10;

        drawPart(1000 * thousands);
        drawPart(100 * hundreds);
        drawPart(10 * tens);
        drawPart(ones);
    }

    private void drawPart(int v) {
        switch (v) {
            case 1:
                horizontal(6, 10, 0);
                break;
            case 2:
                horizontal(6, 10, 4);
                break;
            case 3:
                diagd(6, 10, 0);
                break;
            case 4:
                diagu(6, 10, 4);
                break;
            case 5:
                drawPart(1);
                drawPart(4);
                break;
            case 6:
                vertical(0, 4, 10);
                break;
            case 7:
                drawPart(1);
                drawPart(6);
                break;
            case 8:
                drawPart(2);
                drawPart(6);
                break;
            case 9:
                drawPart(1);
                drawPart(8);
                break;

            case 10:
                horizontal(0, 4, 0);
                break;
            case 20:
                horizontal(0, 4, 4);
                break;
            case 30:
                diagu(0, 4, 4);
                break;
            case 40:
                diagd(0, 4, 0);
                break;
            case 50:
                drawPart(10);
                drawPart(40);
                break;
            case 60:
                vertical(0, 4, 0);
                break;
            case 70:
                drawPart(10);
                drawPart(60);
                break;
            case 80:
                drawPart(20);
                drawPart(60);
                break;
            case 90:
                drawPart(10);
                drawPart(80);
                break;

            case 100:
                horizontal(6, 10, 14);
                break;
            case 200:
                horizontal(6, 10, 10);
                break;
            case 300:
                diagu(6, 10, 14);
                break;
            case 400:
                diagd(6, 10, 10);
                break;
            case 500:
                drawPart(100);
                drawPart(400);
                break;
            case 600:
                vertical(10, 14, 10);
                break;
            case 700:
                drawPart(100);
                drawPart(600);
                break;
            case 800:
                drawPart(200);
                drawPart(600);
                break;
            case 900:
                drawPart(100);
                drawPart(800);
                break;

            case 1000:
                horizontal(0, 4, 14);
                break;
            case 2000:
                horizontal(0, 4, 10);
                break;
            case 3000:
                diagd(0, 4, 10);
                break;
            case 4000:
                diagu(0, 4, 14);
                break;
            case 5000:
                drawPart(1000);
                drawPart(4000);
                break;
            case 6000:
                vertical(10, 14, 0);
                break;
            case 7000:
                drawPart(1000);
                drawPart(6000);
                break;
            case 8000:
                drawPart(2000);
                drawPart(6000);
                break;
            case 9000:
                drawPart(1000);
                drawPart(8000);
                break;

        }
    }

    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (var row : canvas) {
            builder.append(row);
            builder.append('\n');
        }
        return builder.toString();
    }

    public static void main(String[] args) {
        for (int number : List.of(0, 1, 20, 300, 4000, 5555, 6789, 9999)) {
            System.out.printf("%d:\n", number);
            var c = new Cistercian(number);
            System.out.println(c);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
# -*- coding: utf-8 -*-
"""
Some UTF-8 chars used:
    
‾	8254	203E	&oline;	OVERLINE
┃	9475	2503	 	BOX DRAWINGS HEAVY VERTICAL
╱	9585	2571	 	BOX DRAWINGS LIGHT DIAGONAL UPPER RIGHT TO LOWER LEFT
╲	9586	2572	 	BOX DRAWINGS LIGHT DIAGONAL UPPER LEFT TO LOWER RIGHT
◸	9720	25F8	 	UPPER LEFT TRIANGLE
◹	9721	25F9	 	UPPER RIGHT TRIANGLE
◺	9722	25FA	 	LOWER LEFT TRIANGLE
◻	9723	25FB	 	WHITE MEDIUM SQUARE
◿	9727	25FF	 	LOWER RIGHT TRIANGLE

"""

#%% digit sections

def _init():
    "digit sections for forming numbers"
    digi_bits = """
#0  1   2  3  4  5  6   7   8   9
#
 .  ‾   _  ╲  ╱  ◸  .|  ‾|  _|  ◻
#
 .  ‾   _  ╱  ╲  ◹  |.  |‾  |_  ◻
#
 .  _  ‾   ╱  ╲  ◺  .|  _|  ‾|  ◻
#
 .  _  ‾   ╲  ╱  ◿  |.  |_  |‾  ◻
 
""".strip()

    lines = [[d.replace('.', ' ') for d in ln.strip().split()]
             for ln in digi_bits.strip().split('\n')
             if '#' not in ln]
    formats = '<2 >2 <2 >2'.split()
    digits = [[f"{dig:{f}}" for dig in line]
              for f, line in zip(formats, lines)]

    return digits

_digits = _init()


#%% int to 3-line strings
def _to_digits(n):
    assert 0 <= n < 10_000 and int(n) == n
    
    return [int(digit) for digit in f"{int(n):04}"][::-1]

def num_to_lines(n):
    global _digits
    d = _to_digits(n)
    lines = [
        ''.join((_digits[1][d[1]], '┃',  _digits[0][d[0]])),
        ''.join((_digits[0][   0], '┃',  _digits[0][   0])),
        ''.join((_digits[3][d[3]], '┃',  _digits[2][d[2]])),
        ]
    
    return lines

def cjoin(c1, c2, spaces='   '):
    return [spaces.join(by_row) for by_row in zip(c1, c2)]

#%% main
if __name__ == '__main__':
    #n = 6666
    #print(f"Arabic {n} to Cistercian:\n")
    #print('\n'.join(num_to_lines(n)))
    
    for pow10 in range(4):    
        step = 10 ** pow10
        print(f'\nArabic {step}-to-{9*step} by {step} in Cistercian:\n')
        lines = num_to_lines(step)
        for n in range(step*2, step*10, step):
            lines = cjoin(lines, num_to_lines(n))
        print('\n'.join(lines))
    

    numbers = [0, 5555, 6789, 6666]
    print(f'\nArabic {str(numbers)[1:-1]} in Cistercian:\n')
    lines = num_to_lines(numbers[0])
    for n in numbers[1:]:
        lines = cjoin(lines, num_to_lines(n))
    print('\n'.join(lines))

```

