# S-expressions

## Task Link
[Rosetta Code - S-expressions](https://rosettacode.org/wiki/S-expressions)

## Java Code
### java_code_1.txt
```java
package jfkbits;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.Reader;
import java.io.StreamTokenizer;
import java.io.StringReader;
import java.util.Iterator;

public class LispTokenizer implements Iterator<Token>
{
    // Instance variables have default access to allow unit tests access.
    StreamTokenizer m_tokenizer;
    IOException m_ioexn;

    /** Constructs a tokenizer that scans input from the given string.
     * @param src A string containing S-expressions.
     */
    public LispTokenizer(String src)
    {
        this(new StringReader(src));
    }

    /** Constructs a tokenizer that scans input from the given Reader.
     * @param r Reader for the character input source
     */
    public LispTokenizer(Reader r)
    {
        if(r == null)
            r = new StringReader("");
        BufferedReader buffrdr = new BufferedReader(r);
        m_tokenizer = new StreamTokenizer(buffrdr);
        m_tokenizer.resetSyntax(); // We don't like the default settings

        m_tokenizer.whitespaceChars(0, ' ');
        m_tokenizer.wordChars(' '+1,255);
        m_tokenizer.ordinaryChar('(');
        m_tokenizer.ordinaryChar(')');
        m_tokenizer.ordinaryChar('\'');
        m_tokenizer.commentChar(';');
        m_tokenizer.quoteChar('"');
    }

    public Token peekToken()
    {	
        if(m_ioexn != null)
            return null;
        try
        {
            m_tokenizer.nextToken();
        }
        catch(IOException e)
        {
            m_ioexn = e;
            return null;
        }
        if(m_tokenizer.ttype == StreamTokenizer.TT_EOF)
            return null;
        Token token = new Token(m_tokenizer);
        m_tokenizer.pushBack();
        return token;
    }

    public boolean hasNext()
    {
        if(m_ioexn != null)
            return false;
        try
        {
            m_tokenizer.nextToken();
        }
        catch(IOException e)
        {
            m_ioexn = e;
            return false;
        }
        if(m_tokenizer.ttype == StreamTokenizer.TT_EOF)
            return false;
        m_tokenizer.pushBack();
        return true;
    }

    /** Return the most recently caught IOException, if any,
     * 
     * @return
     */
    public IOException getIOException()
    {
        return m_ioexn;
    }

    public Token next()
    {
        try
        {
            m_tokenizer.nextToken();
        }
        catch(IOException e)
        {
            m_ioexn = e;
            return null;
        }

        Token token = new Token(m_tokenizer);
        return token;
    }

    public void remove()
    {
    }
}

```

### java_code_2.txt
```java
package jfkbits;
import java.io.StreamTokenizer;

public class Token
{
    public static final int SYMBOL = StreamTokenizer.TT_WORD;
    public int type;
    public String text;
    public int line;

    public Token(StreamTokenizer tzr)
    {
        this.type = tzr.ttype;
        this.text = tzr.sval;
        this.line = tzr.lineno();
    }

    public String toString()
    {
        switch(this.type)
        {
            case SYMBOL:
            case '"':
                return this.text;
            default:
                return String.valueOf((char)this.type);
        }
    }
}

```

### java_code_3.txt
```java
package jfkbits;

import jfkbits.LispParser.Expr;

public class Atom implements Expr
{
    String name;
    public String toString()
    {
        return name;
    }
    public Atom(String text)
    {
        name = text;
    }

}

```

### java_code_4.txt
```java
package jfkbits;

public class StringAtom extends Atom
{
    public String toString()
    {
        // StreamTokenizer hardcodes escaping with \, and doesn't allow \n inside words
        String escaped = name.replace("\\", "\\\\").replace("\n", "\\n").replace("\r", "\\r").replace("\"", "\\\"");
        return "\""+escaped+"\"";
    }

    public StringAtom(String text)
    {
        super(text);
    }
    public String getValue()
    {
        return name;
    }
}

```

### java_code_5.txt
```java
package jfkbits;

import java.util.AbstractCollection;
import java.util.Arrays;
import java.util.Iterator;
import java.util.ArrayList;

import jfkbits.LispParser.Expr;

public class ExprList extends ArrayList<Expr> implements Expr
{
    ExprList parent = null;
    int indent =1;

    public int getIndent()
    {
        if (parent != null)
        {
            return parent.getIndent()+indent;
        }
        else return 0;
    }

    public void setIndent(int indent)
    {
        this.indent = indent;
    }



    public void setParent(ExprList parent)
    {
        this.parent = parent;
    }

    public String toString()
    {
        String indent = "";
        if (parent != null && parent.get(0) != this)
        {
            indent = "\n";
            char[] chars = new char[getIndent()];
            Arrays.fill(chars, ' ');
            indent += new String(chars);		
        }

        String output = indent+"(";
        for(Iterator<Expr> it=this.iterator(); it.hasNext(); ) 
        {
            Expr expr = it.next();
            output += expr.toString();
            if (it.hasNext())
                output += " ";
        }
        output += ")";
        return output;
    }

    @Override
    public synchronized boolean add(Expr e)
    {
        if (e instanceof ExprList)
        {
            ((ExprList) e).setParent(this);
            if (size() != 0 && get(0) instanceof Atom)
                ((ExprList) e).setIndent(2);
        }
        return super.add(e);
    }

}

```

### java_code_6.txt
```java
package jfkbits;


public class LispParser
{
    LispTokenizer tokenizer;

    public LispParser(LispTokenizer input)
    {
        tokenizer=input;
    }

    public class ParseException extends Exception
    {

    }

    public interface Expr
    {
        // abstract parent for Atom and ExprList
    }

    public Expr parseExpr() throws ParseException
    {
        Token token = tokenizer.next();
        switch(token.type)
        {
            case '(': return parseExprList(token);
            case '"': return new StringAtom(token.text);
            default: return new Atom(token.text);
        }
    }


    protected ExprList parseExprList(Token openParen) throws ParseException
    {
        ExprList acc = new ExprList();
        while(tokenizer.peekToken().type != ')')
        {
            Expr element = parseExpr();
            acc.add(element);
        }
        Token closeParen = tokenizer.next();
        return acc;
    }

}

```

### java_code_7.txt
```java
import jfkbits.ExprList;
import jfkbits.LispParser;
import jfkbits.LispParser.ParseException;
import jfkbits.LispTokenizer;

public class LispParserDemo
{
    public static void main(String args[])
    {

        LispTokenizer tzr = new LispTokenizer(
            "((data \"quoted data\" 123 4.5)\n (data (!@# (4.5) \"(more\" \"data)\")))");
        LispParser parser = new LispParser(tzr);

        try
        {
            Expr result = parser.parseExpr();
            System.out.println(result);
        }
        catch (ParseException e1)
        {
            // TODO Auto-generated catch block
            e1.printStackTrace();
        }
    }	
}

```

## Python Code
### python_code_1.txt
```python
import re

dbg = False

term_regex = r'''(?mx)
    \s*(?:
        (?P<brackl>\()|
        (?P<brackr>\))|
        (?P<num>\-?\d+\.\d+|\-?\d+)|
        (?P<sq>"[^"]*")|
        (?P<s>[^(^)\s]+)
       )'''

def parse_sexp(sexp):
    stack = []
    out = []
    if dbg: print("%-6s %-14s %-44s %-s" % tuple("term value out stack".split()))
    for termtypes in re.finditer(term_regex, sexp):
        term, value = [(t,v) for t,v in termtypes.groupdict().items() if v][0]
        if dbg: print("%-7s %-14s %-44r %-r" % (term, value, out, stack))
        if   term == 'brackl':
            stack.append(out)
            out = []
        elif term == 'brackr':
            assert stack, "Trouble with nesting of brackets"
            tmpout, out = out, stack.pop(-1)
            out.append(tmpout)
        elif term == 'num':
            v = float(value)
            if v.is_integer(): v = int(v)
            out.append(v)
        elif term == 'sq':
            out.append(value[1:-1])
        elif term == 's':
            out.append(value)
        else:
            raise NotImplementedError("Error: %r" % (term, value))
    assert not stack, "Trouble with nesting of brackets"
    return out[0]

def print_sexp(exp):
    out = ''
    if type(exp) == type([]):
        out += '(' + ' '.join(print_sexp(x) for x in exp) + ')'
    elif type(exp) == type('') and re.search(r'[\s()]', exp):
        out += '"%s"' % repr(exp)[1:-1].replace('"', '\"')
    else:
        out += '%s' % exp
    return out
        
    
if __name__ == '__main__':
    sexp = ''' ( ( data "quoted data" 123 4.5)
         (data (123 (4.5) "(more" "data)")))'''

    print('Input S-expression: %r' % (sexp, ))
    parsed = parse_sexp(sexp)
    print("\nParsed to Python:", parsed)

    print("\nThen back to: '%s'" % print_sexp(parsed))

```

### python_code_2.txt
```python
>>> from pprint import pprint as pp
>>> x = [[(t,v) for t,v in  termtypes.groupdict().items() if v][0] for termtypes in re.finditer(term_regex, sexp)]
>>> pp(x)
[('brackl', '('),
 ('brackl', '('),
 ('s', 'data'),
 ('sq', '"quoted data"'),
 ('num', '123'),
 ('num', '4.5'),
 ('brackr', ')'),
 ('brackl', '('),
 ('s', 'data'),
 ('brackl', '('),
 ('num', '123'),
 ('brackl', '('),
 ('num', '4.5'),
 ('brackr', ')'),
 ('sq', '"(more"'),
 ('sq', '"data)"'),
 ('brackr', ')'),
 ('brackr', ')'),
 ('brackr', ')')]
>>>

```

### python_code_3.txt
```python
'''S-expressions'''

from itertools import chain, repeat
import re


def main():
    '''Sample s-expression parsed, diagrammed,
       and reserialized from the parse tree.
    '''
    expr = "((data \"quoted data\" 123 4.5)\n" + (
        "  (data (!@# (4.5) \"(more\" \"data)\")))"
    )
    parse = parseExpr(tokenized(expr))[0]
    print(
        drawForest([
            fmapTree(str)(tree) for tree
            in forestFromExprs(parse)
        ])
    )
    print(
        f'\nReserialized from parse:\n\n{serialized(parse)}'
    )


# ----------------- S-EXPRESSION PARSER ------------------

# parseExpr :: [String] -> ([Expr], [String]
def parseExpr(tokens):
    '''A tuple of a nested list with any
       unparsed tokens that remain.
    '''
    return until(finished)(parseToken)(
        ([], tokens)
    )


# finished :: ([Expr], [String]) -> Bool
def finished(xr):
    '''True if no tokens remain,
       or the next token is a closing bracket.
    '''
    r = xr[1]
    return (not r) or (r[0] == ")")


# parseToken :: ([Expr], [String]) -> ([Expr], [String])
def parseToken(xsr):
    '''A tuple of an expanded expression list
       and a reduced token list.
    '''
    xs, r = xsr
    h, *t = r
    if "(" == h:
        expr, rest = parseExpr(t)
        return xs + [expr], rest[1:]
    else:
        return (xs, t) if ")" == h else (
            xs + [atom(h)], t
        )

# --------------------- ATOM PARSER ----------------------

# atom :: String -> Expr
def atom(s):
    '''A Symbol, String, Float, or Int derived from s.
       Symbol is represented as a dict with a 'name' key.
    '''
    def n(k):
        return float(k) if '.' in k else int(k)

    return s if '"' == s[0] else (
        n(s) if s.replace('.', '', 1).isdigit() else {
            "name": s
        }
    )


# --------------------- TOKENIZATION ---------------------

# tokenized :: String -> [String]
def tokenized(s):
    '''A list of the tokens in s.
    '''
    return list(chain.from_iterable(map(
        lambda token: [token] if '"' == token[0] else (
            x for x in re.split(
                r'\s+',
                re.sub(r"([()])", r" \1 ", token)
            ) if x
        ) if token else [], (
            x if (0 == i % 2) else f'"{x}"'
            for (i, x) in enumerate(s.split('"'))
        )
    )))


# -------------------- SERIALIZATION ---------------------

# serialized :: Expr -> String
def serialized(e):
    '''An s-expression written out from the parse tree.
    '''
    k = typename(e)

    return str(e) if k in ['int', 'float', 'str'] else (
        (
            f'({" ".join([serialized(x) for x in e])})' if (
                (1 < len(e)) or ('list' != typename(e[0]))
            ) else serialized(e[0])
        ) if 'list' == k else (
            e.get("name") if 'dict' == k else "?"
        )
    )


# typename :: a -> String
def typename(x):
    '''Name property of the type of a value.'''
    return type(x).__name__


# ------------------- TREE DIAGRAMMING -------------------

# Node :: a -> [Tree a] -> Tree a
def Node(v):
    '''Constructor for a Tree node which connects a
       value of some kind to a list of zero or
       more child trees.
    '''
    return lambda xs: {'type': 'Tree', 'root': v, 'nest': xs}


# append :: [a] -> [a] -> [a]
def append(a, b):
    '''Concatenation.'''
    return a + b


# draw :: Tree a -> [String]
def draw(node):
    '''List of the lines of an ASCII
       diagram of a tree.
    '''
    def shift_(h, other, xs):
        return list(map(
            append,
            chain(
                [h], (
                    repeat(other, len(xs) - 1)
                )
            ),
            xs
        ))

    def drawSubTrees(xs):
        return (
            (
                ['|'] + shift_(
                    '├─ ', '│  ', draw(xs[0])
                ) + drawSubTrees(xs[1:])
            ) if 1 < len(xs) else ['|'] + shift_(
                '└─ ', '   ', draw(xs[0])
            )
        ) if xs else []

    return (root(node)).splitlines() + (
        drawSubTrees(nest(node))
    )


# drawForest :: [Tree String] -> String
def drawForest(trees):
    '''A simple unicode character representation of
       a list of trees.
    '''
    return '\n'.join(map(drawTree, trees))


# drawTree :: Tree a -> String
def drawTree(tree):
    '''ASCII diagram of a tree.'''
    return '\n'.join(draw(tree))


# fmapTree :: (a -> b) -> Tree a -> Tree b
def fmapTree(f):
    '''A new tree holding the results of
       an application of f to each root in
       the existing tree.
    '''
    def go(x):
        return Node(
            f(root(x))
        )([go(v) for v in nest(x)])
    return go


# forestFromExprs :: [Expr] -> [Tree Expr]
def forestFromExprs(es):
    '''A list of expressions rewritten as a forest.
    '''
    return [treeFromExpr(x) for x in es]


# nest :: Tree a -> [Tree a]
def nest(t):
    '''Accessor function for children of tree node.'''
    return t.get('nest')


# root :: Tree a -> a
def root(t):
    '''Accessor function for data of tree node.'''
    return t.get('root')


# treeFromExprs :: Expr -> Tree Expr
def treeFromExpr(e):
    '''An expression rewritten as a tree.
    '''
    return (
        Node({"name": "List"})(forestFromExprs(e))
    ) if type(e) is list else (
        Node(e)([])
    )


# ----------------------- GENERIC ------------------------

# until :: (a -> Bool) -> (a -> a) -> a -> a
def until(p):
    '''The result of repeatedly applying f until p holds.
       The initial seed value is x.
    '''
    def go(f):
        def loop(x):
            v = x
            while not p(v):
                v = f(v)
            return v
        return loop
    return go


# MAIN ---
if __name__ == '__main__':
    main()

```

