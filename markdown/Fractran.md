# Fractran

## Task Link
[Rosetta Code - Fractran](https://rosettacode.org/wiki/Fractran)

## Java Code
### java_code_1.txt
```java
import java.util.Vector;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Fractran{

   public static void main(String []args){ 

       new Fractran("17/91 78/85 19/51 23/38 29/33 77/29 95/23 77/19 1/17 11/13 13/11 15/14 15/2 55/1", 2);
   }
   final int limit = 15;
   

   Vector<Integer> num = new Vector<>(); 
   Vector<Integer> den = new Vector<>(); 
   public Fractran(String prog, Integer val){
      compile(prog);
      dump();
      exec(2);
    }


   void compile(String prog){
      Pattern regexp = Pattern.compile("\\s*(\\d*)\\s*\\/\\s*(\\d*)\\s*(.*)");
      Matcher matcher = regexp.matcher(prog);
      while(matcher.find()){
         num.add(Integer.parseInt(matcher.group(1)));
         den.add(Integer.parseInt(matcher.group(2)));
         matcher = regexp.matcher(matcher.group(3));
      }
   }

   void exec(Integer val){
       int n = 0;
       while(val != null && n<limit){
           System.out.println(n+": "+val);
           val = step(val);
           n++;
       }
   }
   Integer step(int val){
       int i=0; 
       while(i<den.size() && val%den.get(i) != 0) i++;
       if(i<den.size())
           return num.get(i)*val/den.get(i);
       return null;
   }

   void dump(){
       for(int i=0; i<den.size(); i++)
           System.out.print(num.get(i)+"/"+den.get(i)+" ");
       System.out.println();
   }
}

```

## Python Code
### python_code_1.txt
```python
from fractions import Fraction

def fractran(n, fstring='17 / 91, 78 / 85, 19 / 51, 23 / 38, 29 / 33,'
                        '77 / 29, 95 / 23, 77 / 19, 1 / 17, 11 / 13,'
                        '13 / 11, 15 / 14, 15 / 2, 55 / 1'):
    flist = [Fraction(f) for f in fstring.replace(' ', '').split(',')]

    n = Fraction(n)
    while True:
        yield n.numerator
        for f in flist:
            if (n * f).denominator == 1:
                break
        else:
            break
        n *= f
    
if __name__ == '__main__':
    n, m = 2, 15
    print('First %i members of fractran(%i):\n  ' % (m, n) +
          ', '.join(str(f) for f,i in zip(fractran(n), range(m))))

```

### python_code_2.txt
```python
from fractran import fractran

def fractran_primes():
    for i, fr in enumerate(fractran(2), 1):
        binstr = bin(fr)[2:]
        if binstr.count('1') == 1:
            prime = binstr.count('0')
            if prime > 1:   # Skip 2**0 and 2**1
                yield prime, i

if __name__ == '__main__':
    for (prime, i), j in zip(fractran_primes(), range(15)):
        print("Generated prime %2i from the %6i'th member of the fractran series" % (prime, i))

```

