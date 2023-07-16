# Zeckendorf arithmetic

## Task Link
[Rosetta Code - Zeckendorf arithmetic](https://rosettacode.org/wiki/Zeckendorf_arithmetic)

## Java Code
### java_code_1.txt
```java
import java.util.List;

public class Zeckendorf implements Comparable<Zeckendorf> {
    private static List<String> dig = List.of("00", "01", "10");
    private static List<String> dig1 = List.of("", "1", "10");

    private String x;
    private int dVal = 0;
    private int dLen = 0;

    public Zeckendorf() {
        this("0");
    }

    public Zeckendorf(String x) {
        this.x = x;

        int q = 1;
        int i = x.length() - 1;
        dLen = i / 2;
        while (i >= 0) {
            dVal += (x.charAt(i) - '0') * q;
            q *= 2;
            i--;
        }
    }

    private void a(int n) {
        int i = n;
        while (true) {
            if (dLen < i) dLen = i;
            int j = (dVal >> (i * 2)) & 3;
            switch (j) {
                case 0:
                case 1:
                    return;
                case 2:
                    if (((dVal >> ((i + 1) * 2)) & 1) != 1) return;
                    dVal += 1 << (i * 2 + 1);
                    return;
                case 3:
                    int temp = 3 << (i * 2);
                    temp ^= -1;
                    dVal = dVal & temp;
                    b((i + 1) * 2);
                    break;
            }
            i++;
        }
    }

    private void b(int pos) {
        if (pos == 0) {
            Zeckendorf thiz = this;
            thiz.inc();
            return;
        }
        if (((dVal >> pos) & 1) == 0) {
            dVal += 1 << pos;
            a(pos / 2);
            if (pos > 1) a(pos / 2 - 1);
        } else {
            int temp = 1 << pos;
            temp ^= -1;
            dVal = dVal & temp;
            b(pos + 1);
            b(pos - (pos > 1 ? 2 : 1));
        }
    }

    private void c(int pos) {
        if (((dVal >> pos) & 1) == 1) {
            int temp = 1 << pos;
            temp ^= -1;
            dVal = dVal & temp;
            return;
        }
        c(pos + 1);
        if (pos > 0) {
            b(pos - 1);
        } else {
            Zeckendorf thiz = this;
            thiz.inc();
        }
    }

    public Zeckendorf inc() {
        dVal++;
        a(0);
        return this;
    }

    public void plusAssign(Zeckendorf other) {
        for (int gn = 0; gn < (other.dLen + 1) * 2; gn++) {
            if (((other.dVal >> gn) & 1) == 1) {
                b(gn);
            }
        }
    }

    public void minusAssign(Zeckendorf other) {
        for (int gn = 0; gn < (other.dLen + 1) * 2; gn++) {
            if (((other.dVal >> gn) & 1) == 1) {
                c(gn);
            }
        }
        while ((((dVal >> dLen * 2) & 3) == 0) || (dLen == 0)) {
            dLen--;
        }
    }

    public void timesAssign(Zeckendorf other) {
        Zeckendorf na = other.copy();
        Zeckendorf nb = other.copy();
        Zeckendorf nt;
        Zeckendorf nr = new Zeckendorf();
        for (int i = 0; i < (dLen + 1) * 2; i++) {
            if (((dVal >> i) & 1) > 0) {
                nr.plusAssign(nb);
            }
            nt = nb.copy();
            nb.plusAssign(na);
            na = nt.copy();
        }
        dVal = nr.dVal;
        dLen = nr.dLen;
    }

    private Zeckendorf copy() {
        Zeckendorf z = new Zeckendorf();
        z.dVal = dVal;
        z.dLen = dLen;
        return z;
    }

    @Override
    public int compareTo(Zeckendorf other) {
        return ((Integer) dVal).compareTo(other.dVal);
    }

    @Override
    public String toString() {
        if (dVal == 0) {
            return "0";
        }

        int idx = (dVal >> (dLen * 2)) & 3;
        StringBuilder stringBuilder = new StringBuilder(dig1.get(idx));
        for (int i = dLen - 1; i >= 0; i--) {
            idx = (dVal >> (i * 2)) & 3;
            stringBuilder.append(dig.get(idx));
        }
        return stringBuilder.toString();
    }

    public static void main(String[] args) {
        System.out.println("Addition:");
        Zeckendorf g = new Zeckendorf("10");
        g.plusAssign(new Zeckendorf("10"));
        System.out.println(g);
        g.plusAssign(new Zeckendorf("10"));
        System.out.println(g);
        g.plusAssign(new Zeckendorf("1001"));
        System.out.println(g);
        g.plusAssign(new Zeckendorf("1000"));
        System.out.println(g);
        g.plusAssign(new Zeckendorf("10101"));
        System.out.println(g);

        System.out.println("\nSubtraction:");
        g = new Zeckendorf("1000");
        g.minusAssign(new Zeckendorf("101"));
        System.out.println(g);
        g = new Zeckendorf("10101010");
        g.minusAssign(new Zeckendorf("1010101"));
        System.out.println(g);

        System.out.println("\nMultiplication:");
        g = new Zeckendorf("1001");
        g.timesAssign(new Zeckendorf("101"));
        System.out.println(g);
        g = new Zeckendorf("101010");
        g.plusAssign(new Zeckendorf("101"));
        System.out.println(g);
    }
}

```

## Python Code
### python_code_1.txt
```python
import copy

class Zeckendorf:
    def __init__(self, x='0'):
        q = 1
        i = len(x) - 1
        self.dLen = int(i / 2)
        self.dVal = 0
        while i >= 0:
            self.dVal = self.dVal + (ord(x[i]) - ord('0')) * q
            q = q * 2
            i = i -1

    def a(self, n):
        i = n
        while True:
            if self.dLen < i:
                self.dLen = i
            j = (self.dVal >> (i * 2)) & 3
            if j == 0 or j == 1:
                return
            if j == 2:
                if (self.dVal >> ((i + 1) * 2) & 1) != 1:
                    return
                self.dVal = self.dVal + (1 << (i * 2 + 1))
                return
            if j == 3:
                temp = 3 << (i * 2)
                temp = temp ^ -1
                self.dVal = self.dVal & temp
                self.b((i + 1) * 2)
            i = i + 1

    def b(self, pos):
        if pos == 0:
            self.inc()
            return
        if (self.dVal >> pos) & 1 == 0:
            self.dVal = self.dVal + (1 << pos)
            self.a(int(pos / 2))
            if pos > 1:
                self.a(int(pos / 2) - 1)
        else:
            temp = 1 << pos
            temp = temp ^ -1
            self.dVal = self.dVal & temp
            self.b(pos + 1)
            self.b(pos - (2 if pos > 1 else 1))

    def c(self, pos):
        if (self.dVal >> pos) & 1 == 1:
            temp = 1 << pos
            temp = temp ^ -1
            self.dVal = self.dVal & temp
            return
        self.c(pos + 1)
        if pos > 0:
            self.b(pos - 1)
        else:
            self.inc()

    def inc(self):
        self.dVal = self.dVal + 1
        self.a(0)

    def __add__(self, rhs):
        copy = self
        rhs_dVal = rhs.dVal
        limit = (rhs.dLen + 1) * 2
        for gn in range(0, limit):
            if ((rhs_dVal >> gn) & 1) == 1:
                copy.b(gn)
        return copy

    def __sub__(self, rhs):
        copy = self
        rhs_dVal = rhs.dVal
        limit = (rhs.dLen + 1) * 2
        for gn in range(0, limit):
            if (rhs_dVal >> gn) & 1 == 1:
                copy.c(gn)
        while (((copy.dVal >> ((copy.dLen * 2) & 31)) & 3) == 0) or (copy.dLen == 0):
            copy.dLen = copy.dLen - 1
        return copy

    def __mul__(self, rhs):
        na = copy.deepcopy(rhs)
        nb = copy.deepcopy(rhs)
        nr = Zeckendorf()
        dVal = self.dVal
        for i in range(0, (self.dLen + 1) * 2):
            if ((dVal >> i) & 1) > 0:
                nr = nr + nb
            nt = copy.deepcopy(nb)
            nb = nb + na
            na = copy.deepcopy(nt)
        return nr

    def __str__(self):
        dig = ["00", "01", "10"]
        dig1 = ["", "1", "10"]

        if self.dVal == 0:
            return '0'
        idx = (self.dVal >> ((self.dLen * 2) & 31)) & 3
        sb = dig1[idx]
        i = self.dLen - 1
        while i >= 0:
            idx = (self.dVal >> (i * 2)) & 3
            sb = sb + dig[idx]
            i = i - 1
        return sb

# main
print "Addition:"
g = Zeckendorf("10")
g = g + Zeckendorf("10")
print g
g = g + Zeckendorf("10")
print g
g = g + Zeckendorf("1001")
print g
g = g + Zeckendorf("1000")
print g
g = g + Zeckendorf("10101")
print g
print

print "Subtraction:"
g = Zeckendorf("1000")
g = g - Zeckendorf("101")
print g
g = Zeckendorf("10101010")
g = g - Zeckendorf("1010101")
print g
print

print "Multiplication:"
g = Zeckendorf("1001")
g = g * Zeckendorf("101")
print g
g = Zeckendorf("101010")
g = g + Zeckendorf("101")
print g

```

