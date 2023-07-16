# Parsing/RPN calculator algorithm

## Task Link
[Rosetta Code - Parsing/RPN calculator algorithm](https://rosettacode.org/wiki/Parsing/RPN_calculator_algorithm)

## Java Code
### java_code_1.txt
```java
grammar rpnC ;
//
//  rpn Calculator
//
//  Nigel Galloway - April 7th., 2012
//
@members {
Stack<Double> s = new Stack<Double>();
}
rpn	:	(WS* (num|op) (WS | WS* NEWLINE {System.out.println(s.pop());}))*;
num	:	'-'? Digit+ ('.' Digit+)? {s.push(Double.parseDouble($num.text));};
Digit	:	'0'..'9';
op	:	'-' {double x = s.pop(); s.push(s.pop() - x);}
	|	'/' {double x = s.pop(); s.push(s.pop() / x);}
	|	'*' {s.push(s.pop() * s.pop());}
	|	'^' {double x = s.pop(); s.push(Math.pow(s.pop(), x));}
	|	'+' {s.push(s.pop() + s.pop());};
WS	:	(' ' | '\t'){skip()};
NEWLINE	:	'\r'? '\n';

```

### java_code_2.txt
```java
import java.util.LinkedList;

public class RPN{
	public static void main(String[] args) {
		evalRPN("3 4 2 * 1 5 - 2 3 ^ ^ / +");
	}

	private static void evalRPN(String expr){
		LinkedList<Double> stack = new LinkedList<Double>();
		System.out.println("Input\tOperation\tStack after");
		for (String token : expr.split("\\s")){
			System.out.print(token + "\t");
			if (token.equals("*")) {
				System.out.print("Operate\t\t");
				double secondOperand = stack.pop();
				double firstOperand = stack.pop();
				stack.push(firstOperand * secondOperand);
			} else if (token.equals("/")) {
				System.out.print("Operate\t\t");
				double secondOperand = stack.pop();
				double firstOperand = stack.pop();
				stack.push(firstOperand / secondOperand);
			} else if (token.equals("-")) {
				System.out.print("Operate\t\t");
				double secondOperand = stack.pop();
				double firstOperand = stack.pop();
				stack.push(firstOperand - secondOperand);
			} else if (token.equals("+")) {
				System.out.print("Operate\t\t");
				double secondOperand = stack.pop();
				double firstOperand = stack.pop();
				stack.push(firstOperand + secondOperand);
			} else if (token.equals("^")) {
				System.out.print("Operate\t\t");
				double secondOperand = stack.pop();
				double firstOperand = stack.pop();
				stack.push(Math.pow(firstOperand, secondOperand));
			} else {
				System.out.print("Push\t\t");
				try {
					stack.push(Double.parseDouble(token+""));
				} catch (NumberFormatException e) {
    					System.out.println("\nError: invalid token " + token);
    					return;
				}
			}
			System.out.println(stack);
		}
		if (stack.size() > 1) {
			System.out.println("Error, too many operands: " + stack);
			return;
		}
		System.out.println("Final answer: " + stack.pop());
	}
}

```

## Python Code
### python_code_1.txt
```python
def op_pow(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a ** b )
def op_mul(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a * b )
def op_div(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a / b )
def op_add(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a + b )
def op_sub(stack):
    b = stack.pop(); a = stack.pop()
    stack.append( a - b )
def op_num(stack, num):
    stack.append( num )
    
ops = {
 '^': op_pow,
 '*': op_mul,
 '/': op_div,
 '+': op_add,
 '-': op_sub,
 }

def get_input(inp = None):
    'Inputs an expression and returns list of tokens'
    
    if inp is None:
        inp = input('expression: ')
    tokens = inp.strip().split()
    return tokens

def rpn_calc(tokens):
    stack = []
    table = ['TOKEN,ACTION,STACK'.split(',')]
    for token in tokens:
        if token in ops:
            action = 'Apply op to top of stack'
            ops[token](stack)
            table.append( (token, action, ' '.join(str(s) for s in stack)) )
        else:
            action = 'Push num onto top of stack'
            op_num(stack, eval(token))
            table.append( (token, action, ' '.join(str(s) for s in stack)) )
    return table

if __name__ == '__main__':
    rpn = '3 4 2 * 1 5 - 2 3 ^ ^ / +'
    print( 'For RPN expression: %r\n' % rpn )
    rp = rpn_calc(get_input(rpn))
    maxcolwidths = [max(len(y) for y in x) for x in zip(*rp)]
    row = rp[0]
    print( ' '.join('{cell:^{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))
    for row in rp[1:]:
        print( ' '.join('{cell:<{width}}'.format(width=width, cell=cell) for (width, cell) in zip(maxcolwidths, row)))

    print('\n The final output value is: %r' % rp[-1][2])

```

### python_code_2.txt
```python
a=[]
b={'+': lambda x,y: y+x, '-': lambda x,y: y-x, '*': lambda x,y: y*x,'/': lambda x,y:y/x,'^': lambda x,y:y**x}
for c in '3 4 2 * 1 5 - 2 3 ^ ^ / +'.split():
    if c in b: a.append(b[c](a.pop(),a.pop()))
    else: a.append(float(c))
    print c, a

```

