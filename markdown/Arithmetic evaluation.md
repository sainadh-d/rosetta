# Arithmetic evaluation

## Task Link
[Rosetta Code - Arithmetic evaluation](https://rosettacode.org/wiki/Arithmetic_evaluation)

## Java Code
### java_code_1.txt
```java
import java.util.Stack;

public class ArithmeticEvaluation {

    public interface Expression {
        BigRational eval();
    }

    public enum Parentheses {LEFT}

    public enum BinaryOperator {
        ADD('+', 1),
        SUB('-', 1),
        MUL('*', 2),
        DIV('/', 2);

        public final char symbol;
        public final int precedence;

        BinaryOperator(char symbol, int precedence) {
            this.symbol = symbol;
            this.precedence = precedence;
        }

        public BigRational eval(BigRational leftValue, BigRational rightValue) {
            switch (this) {
                case ADD:
                    return leftValue.add(rightValue);
                case SUB:
                    return leftValue.subtract(rightValue);
                case MUL:
                    return leftValue.multiply(rightValue);
                case DIV:
                    return leftValue.divide(rightValue);
            }
            throw new IllegalStateException();
        }

        public static BinaryOperator forSymbol(char symbol) {
            for (BinaryOperator operator : values()) {
                if (operator.symbol == symbol) {
                    return operator;
                }
            }
            throw new IllegalArgumentException(String.valueOf(symbol));
        }
    }

    public static class Number implements Expression {
        private final BigRational number;

        public Number(BigRational number) {
            this.number = number;
        }

        @Override
        public BigRational eval() {
            return number;
        }

        @Override
        public String toString() {
            return number.toString();
        }
    }

    public static class BinaryExpression implements Expression {
        public final Expression leftOperand;
        public final BinaryOperator operator;
        public final Expression rightOperand;

        public BinaryExpression(Expression leftOperand, BinaryOperator operator, Expression rightOperand) {
            this.leftOperand = leftOperand;
            this.operator = operator;
            this.rightOperand = rightOperand;
        }

        @Override
        public BigRational eval() {
            BigRational leftValue = leftOperand.eval();
            BigRational rightValue = rightOperand.eval();
            return operator.eval(leftValue, rightValue);
        }

        @Override
        public String toString() {
            return "(" + leftOperand + " " + operator.symbol + " " + rightOperand + ")";
        }
    }

    private static void createNewOperand(BinaryOperator operator, Stack<Expression> operands) {
        Expression rightOperand = operands.pop();
        Expression leftOperand = operands.pop();
        operands.push(new BinaryExpression(leftOperand, operator, rightOperand));
    }

    public static Expression parse(String input) {
        int curIndex = 0;
        boolean afterOperand = false;
        Stack<Expression> operands = new Stack<>();
        Stack<Object> operators = new Stack<>();
        while (curIndex < input.length()) {
            int startIndex = curIndex;
            char c = input.charAt(curIndex++);

            if (Character.isWhitespace(c))
                continue;

            if (afterOperand) {
                if (c == ')') {
                    Object operator;
                    while (!operators.isEmpty() && ((operator = operators.pop()) != Parentheses.LEFT))
                        createNewOperand((BinaryOperator) operator, operands);
                    continue;
                }
                afterOperand = false;
                BinaryOperator operator = BinaryOperator.forSymbol(c);
                while (!operators.isEmpty() && (operators.peek() != Parentheses.LEFT) && (((BinaryOperator) operators.peek()).precedence >= operator.precedence))
                    createNewOperand((BinaryOperator) operators.pop(), operands);
                operators.push(operator);
                continue;
            }

            if (c == '(') {
                operators.push(Parentheses.LEFT);
                continue;
            }

            afterOperand = true;
            while (curIndex < input.length()) {
                c = input.charAt(curIndex);
                if (((c < '0') || (c > '9')) && (c != '.'))
                    break;
                curIndex++;
            }
            operands.push(new Number(BigRational.valueOf(input.substring(startIndex, curIndex))));
        }

        while (!operators.isEmpty()) {
            Object operator = operators.pop();
            if (operator == Parentheses.LEFT)
                throw new IllegalArgumentException();
            createNewOperand((BinaryOperator) operator, operands);
        }

        Expression expression = operands.pop();
        if (!operands.isEmpty())
            throw new IllegalArgumentException();
        return expression;
    }

    public static void main(String[] args) {
        String[] testExpressions = {
                "2+3",
                "2+3/4",
                "2*3-4",
                "2*(3+4)+5/6",
                "2 * (3 + (4 * 5 + (6 * 7) * 8) - 9) * 10",
                "2*-3--4+-.25"};
        for (String testExpression : testExpressions) {
            Expression expression = parse(testExpression);
            System.out.printf("Input: \"%s\", AST: \"%s\", value=%s%n", testExpression, expression, expression.eval());
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
import operator

class AstNode(object):
   def __init__( self, opr, left, right ):
      self.opr = opr
      self.l = left
      self.r = right

   def eval(self):
      return self.opr(self.l.eval(), self.r.eval())

class LeafNode(object):
   def __init__( self, valStrg ):
      self.v = int(valStrg)

   def eval(self):
      return self.v

class Yaccer(object):
   def __init__(self):
      self.operstak = []
      self.nodestak =[]
      self.__dict__.update(self.state1)

   def v1( self, valStrg ):
      # Value String
      self.nodestak.append( LeafNode(valStrg))
      self.__dict__.update(self.state2)
      #print 'push', valStrg

   def o2( self, operchar ):
      # Operator character or open paren in state1
      def openParen(a,b):
         return 0		# function should not be called

      opDict= { '+': ( operator.add, 2, 2 ),
         '-': (operator.sub, 2, 2 ),
         '*': (operator.mul, 3, 3 ),
         '/': (operator.div, 3, 3 ),
         '^': ( pow,         4, 5 ),  # right associative exponentiation for grins
         '(': ( openParen,   0, 8 )
         }
      operPrecidence = opDict[operchar][2]
      self.redeuce(operPrecidence)

      self.operstak.append(opDict[operchar])
      self.__dict__.update(self.state1)
      # print 'pushop', operchar

   def syntaxErr(self, char ):
      # Open Parenthesis 
      print 'parse error - near operator "%s"' %char

   def pc2( self,operchar ):
      # Close Parenthesis
      # reduce node until matching open paren found 
      self.redeuce( 1 )
      if len(self.operstak)>0:
         self.operstak.pop()		# pop off open parenthesis
      else:
         print 'Error - no open parenthesis matches close parens.'
      self.__dict__.update(self.state2)

   def end(self):
      self.redeuce(0)
      return self.nodestak.pop()

   def redeuce(self, precidence):
      while len(self.operstak)>0:
         tailOper = self.operstak[-1]
         if tailOper[1] < precidence: break

         tailOper = self.operstak.pop()
         vrgt = self.nodestak.pop()
         vlft= self.nodestak.pop()
         self.nodestak.append( AstNode(tailOper[0], vlft, vrgt))
         # print 'reduce'

   state1 = { 'v': v1, 'o':syntaxErr, 'po':o2, 'pc':syntaxErr }
   state2 = { 'v': syntaxErr, 'o':o2, 'po':syntaxErr, 'pc':pc2 }


def Lex( exprssn, p ):
   bgn = None
   cp = -1
   for c in exprssn:
      cp += 1
      if c in '+-/*^()':         # throw in exponentiation (^)for grins
         if bgn is not None:
            p.v(p, exprssn[bgn:cp])
            bgn = None
         if c=='(': p.po(p, c)
         elif c==')':p.pc(p, c)
         else: p.o(p, c)
      elif c in ' \t':
         if bgn is not None:
            p.v(p, exprssn[bgn:cp])
            bgn = None
      elif c in '0123456789':
         if bgn is None:
            bgn = cp
      else:
         print 'Invalid character in expression'
         if bgn is not None:
            p.v(p, exprssn[bgn:cp])
            bgn = None
         
   if bgn is not None:
      p.v(p, exprssn[bgn:cp+1])
      bgn = None
   return p.end()


expr = raw_input("Expression:")
astTree = Lex( expr, Yaccer())
print expr, '=',astTree.eval()

```

### python_code_2.txt
```python
>>> import ast
>>> 
>>> expr="2 * (3 -1) + 2 * 5"
>>> node = ast.parse(expr, mode='eval')
>>> print(ast.dump(node).replace(',', ',\n'))
Expression(body=BinOp(left=BinOp(left=Num(n=2),
 op=Mult(),
 right=BinOp(left=Num(n=3),
 op=Sub(),
 right=Num(n=1))),
 op=Add(),
 right=BinOp(left=Num(n=2),
 op=Mult(),
 right=Num(n=5))))
>>> code_object = compile(node, filename='<string>', mode='eval')
>>> eval(code_object)
14
>>> # lets modify the AST by changing the 5 to a 6
>>> node.body.right.right.n
5
>>> node.body.right.right.n = 6
>>> code_object = compile(node, filename='<string>', mode='eval')
>>> eval(code_object)
16

```

