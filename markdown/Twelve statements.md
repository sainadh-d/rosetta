# Twelve statements

## Task Link
[Rosetta Code - Twelve statements](https://rosettacode.org/wiki/Twelve_statements)

## Java Code
### java_code_1.txt
```java
public class LogicPuzzle
{
    boolean S[] = new boolean[13];
    int Count = 0;

    public boolean check2 ()
    {
        int count = 0;
        for (int k = 7; k <= 12; k++)
            if (S[k]) count++;
        return S[2] == (count == 3);
    }

    public boolean check3 ()
    {
        int count = 0;
        for (int k = 2; k <= 12; k += 2)
            if (S[k]) count++;
        return S[3] == (count == 2);
    }

    public boolean check4 ()
    {
        return S[4] == ( !S[5] || S[6] && S[7]);
    }

    public boolean check5 ()
    {
        return S[5] == ( !S[2] && !S[3] && !S[4]);
    }

    public boolean check6 ()
    {
        int count = 0;
        for (int k = 1; k <= 11; k += 2)
            if (S[k]) count++;
        return S[6] == (count == 4);
    }

    public boolean check7 ()
    {
        return S[7] == ((S[2] || S[3]) && !(S[2] && S[3]));
    }

    public boolean check8 ()
    {
        return S[8] == ( !S[7] || S[5] && S[6]);
    }

    public boolean check9 ()
    {
        int count = 0;
        for (int k = 1; k <= 6; k++)
            if (S[k]) count++;
        return S[9] == (count == 3);
    }

    public boolean check10 ()
    {
        return S[10] == (S[11] && S[12]);
    }

    public boolean check11 ()
    {
        int count = 0;
        for (int k = 7; k <= 9; k++)
            if (S[k]) count++;
        return S[11] == (count == 1);
    }

    public boolean check12 ()
    {
        int count = 0;
        for (int k = 1; k <= 11; k++)
            if (S[k]) count++;
        return S[12] == (count == 4);
    }

    public void check ()
    {
        if (check2() && check3() && check4() && check5() && check6()
            && check7() && check8() && check9() && check10() && check11()
            && check12())
        {
            for (int k = 1; k <= 12; k++)
                if (S[k]) System.out.print(k + " ");
            System.out.println();
            Count++;
        }
    }

    public void recurseAll (int k)
    {
        if (k == 13)
            check();
        else
        {
            S[k] = false;
            recurseAll(k + 1);
            S[k] = true;
            recurseAll(k + 1);
        }
    }

    public static void main (String args[])
    {
        LogicPuzzle P = new LogicPuzzle();
        P.S[1] = true;
        P.recurseAll(2);
        System.out.println();
        System.out.println(P.Count + " Solutions found.");
    }
}

```

## Python Code
### python_code_1.txt
```python
from itertools import product
#from pprint import pprint as pp

constraintinfo = (  
  (lambda st: len(st) == 12                 ,(1, 'This is a numbered list of twelve statements')),
  (lambda st: sum(st[-6:]) == 3             ,(2, 'Exactly 3 of the last 6 statements are true')),
  (lambda st: sum(st[1::2]) == 2            ,(3, 'Exactly 2 of the even-numbered statements are true')),
  (lambda st: (st[5]&st[6]) if st[4] else 1 ,(4, 'If statement 5 is true, then statements 6 and 7 are both true')),
  (lambda st: sum(st[1:4]) == 0             ,(5, 'The 3 preceding statements are all false')),
  (lambda st: sum(st[0::2]) == 4            ,(6, 'Exactly 4 of the odd-numbered statements are true')),
  (lambda st: sum(st[1:3]) == 1             ,(7, 'Either statement 2 or 3 is true, but not both')),
  (lambda st: (st[4]&st[5]) if st[6] else 1 ,(8, 'If statement 7 is true, then 5 and 6 are both true')),
  (lambda st: sum(st[:6]) == 3              ,(9, 'Exactly 3 of the first 6 statements are true')),
  (lambda st: (st[10]&st[11])               ,(10, 'The next two statements are both true')),
  (lambda st: sum(st[6:9]) == 1             ,(11, 'Exactly 1 of statements 7, 8 and 9 are true')),
  (lambda st: sum(st[0:11]) == 4            ,(12, 'Exactly 4 of the preceding statements are true')),
)  

def printer(st, matches):
    if False in matches:
        print('Missed by one statement: %i, %s' % docs[matches.index(False)])
    else:
        print('Full match:')
    print('  ' + ', '.join('%i:%s' % (i, 'T' if t else 'F') for i, t in enumerate(st, 1)))

funcs, docs = zip(*constraintinfo)

full, partial = [], []

for st in product( *([(False, True)] * 12) ):
    truths = [bool(func(st)) for func in funcs]
    matches = [s == t for s,t in zip(st, truths)]
    mcount = sum(matches)
    if mcount == 12:
        full.append((st, matches))
    elif mcount == 11:
        partial.append((st, matches))

for stm in full + partial:
    printer(*stm)

```

