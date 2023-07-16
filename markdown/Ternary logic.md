# Ternary logic

## Task Link
[Rosetta Code - Ternary logic](https://rosettacode.org/wiki/Ternary_logic)

## Java Code
### java_code_1.txt
```java
public class Logic{
	public static enum Trit{
		TRUE, MAYBE, FALSE;
		
		public Trit and(Trit other){
			if(this == TRUE){
				return other;
			}else if(this == MAYBE){
				return (other == FALSE) ? FALSE : MAYBE;
			}else{
				return FALSE;
			}
		}
		
		public Trit or(Trit other){
			if(this == TRUE){
				return TRUE;
			}else if(this == MAYBE){
				return (other == TRUE) ? TRUE : MAYBE;
			}else{
				return other;
			}
		}
		
		public Trit tIf(Trit other){
			if(this == TRUE){
				return other;
			}else if(this == MAYBE){
				return (other == TRUE) ? TRUE : MAYBE;
			}else{
				return TRUE;
			}
		}
		
		public Trit not(){
			if(this == TRUE){
				return FALSE;
			}else if(this == MAYBE){
				return MAYBE;
			}else{
				return TRUE;
			}
		}
		
		public Trit equals(Trit other){
			if(this == TRUE){
				return other;
			}else if(this == MAYBE){
				return MAYBE;
			}else{
				return other.not();
			}
		}
	}
	public static void main(String[] args){
		for(Trit a:Trit.values()){
			System.out.println("not " + a + ": " + a.not());
		}
		for(Trit a:Trit.values()){
			for(Trit b:Trit.values()){
				System.out.println(a+" and "+b+": "+a.and(b)+
						"\t "+a+" or "+b+": "+a.or(b)+
						"\t "+a+" implies "+b+": "+a.tIf(b)+
						"\t "+a+" = "+b+": "+a.equals(b));
			}
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
class Trit(int):
    def __new__(cls, value):
        if value == 'TRUE':
            value = 1
        elif value == 'FALSE':
            value = 0
        elif value == 'MAYBE':
            value = -1
        return super(Trit, cls).__new__(cls, value // (abs(value) or 1)) 

    def __repr__(self):
        if self > 0:
            return 'TRUE'
        elif self == 0:
            return 'FALSE'
        return 'MAYBE'

    def __str__(self):
        return repr(self)

    def __bool__(self):
        if self > 0:
            return True
        elif self == 0:
            return False
        else:
            raise ValueError("invalid literal for bool(): '%s'" % self)

    def __or__(self, other):
        if isinstance(other, Trit):
            return _ttable[(self, other)][1]
        else:
            try:
                return _ttable[(self, Trit(bool(other)))][1]
            except:
                return NotImplemented

    def __ror__(self, other):
        if isinstance(other, Trit):
            return _ttable[(self, other)][1]
        else:
            try:
                return _ttable[(self, Trit(bool(other)))][1]
            except:
                return NotImplemented

    def __and__(self, other):
        if isinstance(other, Trit):
            return _ttable[(self, other)][0]
        else:
            try:
                return _ttable[(self, Trit(bool(other)))][0]
            except:
                return NotImplemented

    def __rand__(self, other):
        if isinstance(other, Trit):
            return _ttable[(self, other)][0]
        else:
            try:
                return _ttable[(self, Trit(bool(other)))][0]
            except:
                return NotImplemented

    def __xor__(self, other):
        if isinstance(other, Trit):
            return _ttable[(self, other)][2]
        else:
            try:
                return _ttable[(self, Trit(bool(other)))][2]
            except:
                return NotImplemented

    def __rxor__(self, other):
        if isinstance(other, Trit):
            return _ttable[(self, other)][2]
        else:
            try:
                return _ttable[(self, Trit(bool(other)))][2]
            except:
                return NotImplemented

    def __invert__(self):
        return _ttable[self]
    
    def __getattr__(self, name):
        if name in ('_n', 'flip'):
            # So you can do x._n == x.flip; the inverse of x
            # In Python 'not' is strictly boolean so we can't write `not x`
            # Same applies to keywords 'and' and 'or'.
            return _ttable[self]
        else:
            raise AttributeError 


        
TRUE, FALSE, MAYBE = Trit(1), Trit(0), Trit(-1)

_ttable = {
    #    A: -> flip_A
         TRUE: FALSE,
        FALSE:  TRUE,
        MAYBE: MAYBE,
    #     (A, B): -> (A_and_B, A_or_B, A_xor_B)
        (MAYBE, MAYBE): (MAYBE, MAYBE, MAYBE),
        (MAYBE, FALSE): (FALSE, MAYBE, MAYBE),
        (MAYBE,  TRUE): (MAYBE,  TRUE, MAYBE),
        (FALSE, MAYBE): (FALSE, MAYBE, MAYBE),
        (FALSE, FALSE): (FALSE, FALSE, FALSE),
        (FALSE,  TRUE): (FALSE,  TRUE,  TRUE),
        ( TRUE, MAYBE): (MAYBE,  TRUE, MAYBE),
        ( TRUE, FALSE): (FALSE,  TRUE,  TRUE),
        ( TRUE,  TRUE): ( TRUE,  TRUE, FALSE),
    }


values = ('FALSE', 'TRUE ', 'MAYBE')

print("\nTrit logical inverse, '~'")
for a in values:
    expr = '~%s' % a
    print('  %s = %s' % (expr, eval(expr)))

for op, ophelp in (('&', 'and'), ('|', 'or'), ('^', 'exclusive-or')):
    print("\nTrit logical %s, '%s'" % (ophelp, op))
    for a in values:
        for b in values:
            expr = '%s %s %s' % (a, op, b)
            print('  %s = %s' % (expr, eval(expr)))

```

