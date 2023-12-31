# Parsing/RPN to infix conversion

## Task Link
[Rosetta Code - Parsing/RPN to infix conversion](https://rosettacode.org/wiki/Parsing/RPN_to_infix_conversion)

## Java Code
### java_code_1.txt
```java
import java.util.Stack;

public class PostfixToInfix {

    public static void main(String[] args) {
        for (String e : new String[]{"3 4 2 * 1 5 - 2 3 ^ ^ / +",
            "1 2 + 3 4 + ^ 5 6 + ^"}) {
            System.out.printf("Postfix : %s%n", e);
            System.out.printf("Infix : %s%n", postfixToInfix(e));
            System.out.println();
        }
    }

    static String postfixToInfix(final String postfix) {

        class Expression {
            final static String ops = "-+/*^";

            String op, ex;
            int prec = 3;

            Expression(String e) {
                ex = e;
            }

            Expression(String e1, String e2, String o) {
                ex = String.format("%s %s %s", e1, o, e2);
                op = o;
                prec = ops.indexOf(o) / 2;
            }

            @Override
            public String toString() {
                return ex;
            }
        }

        Stack<Expression> expr = new Stack<>();

        for (String token : postfix.split("\\s+")) {
            char c = token.charAt(0);
            int idx = Expression.ops.indexOf(c);
            if (idx != -1 && token.length() == 1) {

                Expression r = expr.pop();
                Expression l = expr.pop();

                int opPrec = idx / 2;

                if (l.prec < opPrec || (l.prec == opPrec && c == '^'))
                    l.ex = '(' + l.ex + ')';

                if (r.prec < opPrec || (r.prec == opPrec && c != '^'))
                    r.ex = '(' + r.ex + ')';

                expr.push(new Expression(l.ex, r.ex, token));
            } else {
                expr.push(new Expression(token));
            }
            System.out.printf("%s -> %s%n", token, expr);
        }
        return expr.peek().ex;
    }
}

```

## Python Code
### python_code_1.txt
```python
 
"""
>>> # EXAMPLE USAGE
>>> result = rpn_to_infix('3 4 2 * 1 5 - 2 3 ^ ^ / +', VERBOSE=True)
TOKEN  STACK
3      ['3']
4      ['3', '4']
2      ['3', '4', '2']
*      ['3', Node('2','*','4')]
1      ['3', Node('2','*','4'), '1']
5      ['3', Node('2','*','4'), '1', '5']
-      ['3', Node('2','*','4'), Node('5','-','1')]
2      ['3', Node('2','*','4'), Node('5','-','1'), '2']
3      ['3', Node('2','*','4'), Node('5','-','1'), '2', '3']
^      ['3', Node('2','*','4'), Node('5','-','1'), Node('3','^','2')]
^      ['3', Node('2','*','4'), Node(Node('3','^','2'),'^',Node('5','-','1'))]
/      ['3', Node(Node(Node('3','^','2'),'^',Node('5','-','1')),'/',Node('2','*','4'))]
+      [Node(Node(Node(Node('3','^','2'),'^',Node('5','-','1')),'/',Node('2','*','4')),'+','3')]
"""

prec_dict =  {'^':4, '*':3, '/':3, '+':2, '-':2}
assoc_dict = {'^':1, '*':0, '/':0, '+':0, '-':0}
 
class Node:
    def __init__(self,x,op,y=None):
        self.precedence = prec_dict[op]
        self.assocright = assoc_dict[op]
        self.op = op
        self.x,self.y = x,y
 
    def __str__(self):
        """
        Building an infix string that evaluates correctly is easy.
        Building an infix string that looks pretty and evaluates
        correctly requires more effort.
        """
        # easy case, Node is unary
        if self.y == None:
            return '%s(%s)'%(self.op,str(self.x))
 
        # determine left side string
        str_y = str(self.y)
        if  self.y < self or \
            (self.y == self and self.assocright) or \
            (str_y[0] is '-' and self.assocright):
 
            str_y = '(%s)'%str_y
        # determine right side string and operator
        str_x = str(self.x)
        str_op = self.op
        if self.op is '+' and not isinstance(self.x, Node) and str_x[0] is '-':
            str_x = str_x[1:]
            str_op = '-'
        elif self.op is '-' and not isinstance(self.x, Node) and str_x[0] is '-':
            str_x = str_x[1:]
            str_op = '+'
        elif self.x < self or \
             (self.x == self and not self.assocright and \
              getattr(self.x, 'op', 1) != getattr(self, 'op', 2)):
 
            str_x = '(%s)'%str_x
        return ' '.join([str_y, str_op, str_x])
 
    def __repr__(self):
        """
        >>> repr(Node('3','+','4')) == repr(eval(repr(Node('3','+','4'))))
        True
        """
        return 'Node(%s,%s,%s)'%(repr(self.x), repr(self.op), repr(self.y))
 
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.precedence < other.precedence
        return self.precedence < prec_dict.get(other,9)
 
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.precedence > other.precedence
        return self.precedence > prec_dict.get(other,9)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.precedence == other.precedence
        return self.precedence > prec_dict.get(other,9)
 
 
 
def rpn_to_infix(s, VERBOSE=False):
    """
    
    converts rpn notation to infix notation for string s
 
    """
    if VERBOSE : print('TOKEN  STACK')
 
    stack=[]
    for token in s.replace('^','^').split():
        if token in prec_dict:
            stack.append(Node(stack.pop(),token,stack.pop()))
        else:
            stack.append(token)
 
        # can't use \t in order to make global docstring pass doctest
        if VERBOSE : print(token+' '*(7-len(token))+repr(stack)) 
 
    return str(stack[0])
  
strTest = "3 4 2 * 1 5 - 2 3 ^ ^ / +"
strResult = rpn_to_infix(strTest, VERBOSE=False)
print ("Input: ",strTest)
print ("Output:",strResult)

print()

strTest = "1 2 + 3 4 + ^ 5 6 + ^"
strResult = rpn_to_infix(strTest, VERBOSE=False)
print ("Input: ",strTest)
print ("Output:",strResult)

```

