# Check Machin-like formulas

## Task Link
[Rosetta Code - Check Machin-like formulas](https://rosettacode.org/wiki/Check_Machin-like_formulas)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.math.BigInteger;
import java.util.ArrayList;
import java.util.List;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class CheckMachinFormula {
    
    private static String FILE_NAME = "MachinFormula.txt";
    
    public static void main(String[] args) {
        try {
            runPrivate();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static void runPrivate() throws IOException {
        try (BufferedReader reader = new BufferedReader(new FileReader(new File(FILE_NAME)));) {        
            String inLine = null;
            while ( (inLine = reader.readLine()) != null ) {
                String[] split = inLine.split("=");
                System.out.println(tanLeft(split[0].trim()) + " = " + split[1].trim().replaceAll("\\s+", " ") + " = " + tanRight(split[1].trim()));
            }
        }
    }
    
    private static String tanLeft(String formula) {
        if ( formula.compareTo("pi/4") == 0 ) {
            return "1";
        }
        throw new RuntimeException("ERROR 104:  Unknown left side: " + formula);
    }
    
    private static final Pattern ARCTAN_PATTERN = Pattern.compile("(-{0,1}\\d+)\\*arctan\\((\\d+)/(\\d+)\\)");
    
    private static Fraction tanRight(String formula) {
        Matcher matcher = ARCTAN_PATTERN.matcher(formula);
        List<Term> terms = new ArrayList<>();
        while ( matcher.find() ) {
            terms.add(new Term(Integer.parseInt(matcher.group(1)), new Fraction(matcher.group(2), matcher.group(3))));
        }
        return evaluateArctan(terms);
    }
    
    private static Fraction evaluateArctan(List<Term> terms) {
        if ( terms.size() == 1 ) {
            Term term = terms.get(0);
            return evaluateArctan(term.coefficient, term.fraction);
        }
        int size = terms.size();
        List<Term> left = terms.subList(0, (size+1) / 2);
        List<Term> right = terms.subList((size+1) / 2, size);
        return arctanFormula(evaluateArctan(left), evaluateArctan(right));
    }
    
    private static Fraction evaluateArctan(int coefficient, Fraction fraction) {
        //System.out.println("C = " + coefficient + ", F = " + fraction);
        if ( coefficient == 1 ) {
            return fraction;
        }
        else if ( coefficient < 0 ) {
            return evaluateArctan(-coefficient, fraction).negate();
        }
        if ( coefficient % 2 == 0 ) {
            Fraction f = evaluateArctan(coefficient/2, fraction);
            return arctanFormula(f, f);
        }
        Fraction a = evaluateArctan(coefficient/2, fraction);
        Fraction b = evaluateArctan(coefficient - (coefficient/2), fraction);
        return arctanFormula(a, b);
    }
    
    private static Fraction arctanFormula(Fraction f1, Fraction f2) {
        return f1.add(f2).divide(Fraction.ONE.subtract(f1.multiply(f2)));
    }
    
    private static class Fraction {
        
        public static final Fraction ONE = new Fraction("1", "1");
        
        private BigInteger numerator;
        private BigInteger denominator;
        
        public Fraction(String num, String den) {
            numerator = new BigInteger(num);
            denominator = new BigInteger(den);
        }

        public Fraction(BigInteger num, BigInteger den) {
            numerator = num;
            denominator = den;
        }

        public Fraction negate() {
            return new Fraction(numerator.negate(), denominator);
        }
        
        public Fraction add(Fraction f) {
            BigInteger gcd = denominator.gcd(f.denominator);
            BigInteger first = numerator.multiply(f.denominator.divide(gcd));
            BigInteger second = f.numerator.multiply(denominator.divide(gcd));
            return new Fraction(first.add(second), denominator.multiply(f.denominator).divide(gcd));
        }
        
        public Fraction subtract(Fraction f) {
            return add(f.negate());
        }
        
        public Fraction multiply(Fraction f) {
            BigInteger num = numerator.multiply(f.numerator);
            BigInteger den = denominator.multiply(f.denominator);
            BigInteger gcd = num.gcd(den);
            return new Fraction(num.divide(gcd), den.divide(gcd));
        }

        public Fraction divide(Fraction f) {
            return multiply(new Fraction(f.denominator, f.numerator));
        }
        
        @Override
        public String toString() {
            if ( denominator.compareTo(BigInteger.ONE) == 0 ) {
                return numerator.toString();
            }
            return numerator + " / " + denominator;
        }
    }
    
    private static class Term {
        
        private int coefficient;
        private Fraction fraction;
        
        public Term(int c, Fraction f) {
            coefficient = c;
            fraction = f;
        }
    }
    
}

```

## Python Code
### python_code_1.txt
```python
import re
from fractions import Fraction
from pprint import pprint as pp


equationtext = '''\
  pi/4 = arctan(1/2) + arctan(1/3) 
  pi/4 = 2*arctan(1/3) + arctan(1/7)
  pi/4 = 4*arctan(1/5) - arctan(1/239)
  pi/4 = 5*arctan(1/7) + 2*arctan(3/79)
  pi/4 = 5*arctan(29/278) + 7*arctan(3/79)
  pi/4 = arctan(1/2) + arctan(1/5) + arctan(1/8) 
  pi/4 = 4*arctan(1/5) - arctan(1/70) + arctan(1/99) 
  pi/4 = 5*arctan(1/7) + 4*arctan(1/53) + 2*arctan(1/4443)
  pi/4 = 6*arctan(1/8) + 2*arctan(1/57) + arctan(1/239)
  pi/4 = 8*arctan(1/10) - arctan(1/239) - 4*arctan(1/515)
  pi/4 = 12*arctan(1/18) + 8*arctan(1/57) - 5*arctan(1/239)
  pi/4 = 16*arctan(1/21) + 3*arctan(1/239) + 4*arctan(3/1042)
  pi/4 = 22*arctan(1/28) + 2*arctan(1/443) - 5*arctan(1/1393) - 10*arctan(1/11018)
  pi/4 = 22*arctan(1/38) + 17*arctan(7/601) + 10*arctan(7/8149)
  pi/4 = 44*arctan(1/57) + 7*arctan(1/239) - 12*arctan(1/682) + 24*arctan(1/12943)
  pi/4 = 88*arctan(1/172) + 51*arctan(1/239) + 32*arctan(1/682) + 44*arctan(1/5357) + 68*arctan(1/12943)
  pi/4 = 88*arctan(1/172) + 51*arctan(1/239) + 32*arctan(1/682) + 44*arctan(1/5357) + 68*arctan(1/12944)
'''

def parse_eqn(equationtext=equationtext):
    eqn_re = re.compile(r"""(?mx)
    (?P<lhs> ^ \s* pi/4 \s* = \s*)?             # LHS of equation
    (?:                                         # RHS
        \s* (?P<sign> [+-])? \s* 
        (?: (?P<mult> \d+) \s* \*)? 
        \s* arctan\( (?P<numer> \d+) / (?P<denom> \d+)
    )""")

    found = eqn_re.findall(equationtext)
    machins, part = [], []
    for lhs, sign, mult, numer, denom in eqn_re.findall(equationtext):
        if lhs and part:
            machins.append(part)
            part = []
        part.append( ( (-1 if sign == '-' else 1) * ( int(mult) if mult else 1),
                       Fraction(int(numer), (int(denom) if denom else 1)) ) )
    machins.append(part)
    return machins


def tans(xs):
    xslen = len(xs)
    if xslen == 1:
        return tanEval(*xs[0])
    aa, bb = xs[:xslen//2], xs[xslen//2:]
    a, b = tans(aa), tans(bb)
    return (a + b) / (1 - a * b)

def tanEval(coef, f):
    if coef == 1:
        return f
    if coef < 0:
        return -tanEval(-coef, f)
    ca = coef // 2
    cb = coef - ca
    a, b = tanEval(ca, f), tanEval(cb, f)
    return (a + b) / (1 - a * b)


if __name__ == '__main__':
    machins = parse_eqn()
    #pp(machins, width=160)
    for machin, eqn in zip(machins, equationtext.split('\n')):
        ans = tans(machin)
        print('%5s: %s' % ( ('OK' if ans == 1 else 'ERROR'), eqn))

```

