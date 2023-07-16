# Compiler/syntax analyzer

## Task Link
[Rosetta Code - Compiler/syntax analyzer](https://rosettacode.org/wiki/Compiler/syntax_analyzer)

## Java Code
### java_code_1.txt
```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.StringTokenizer;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Parser {
	private List<Token> source;
	private Token token;
	private int position;

	static class Node {
		public NodeType nt;
		public Node left, right;
		public String value;

		Node() {
			this.nt = null;
			this.left = null;
			this.right = null;
			this.value = null;
		}
		Node(NodeType node_type, Node left, Node right, String value) {
			this.nt = node_type;
			this.left = left;
			this.right = right;
			this.value = value;
		}
		public static Node make_node(NodeType nodetype, Node left, Node right) {
			return new Node(nodetype, left, right, "");
		}
		public static Node make_node(NodeType nodetype, Node left) {
			return new Node(nodetype, left, null, "");
		}
		public static Node make_leaf(NodeType nodetype, String value) {
			return new Node(nodetype, null, null, value);
		}
	}

	static class Token {
		public TokenType tokentype;
		public String value;
		public int line;
		public int pos;

		Token(TokenType token, String value, int line, int pos) {
			this.tokentype = token; this.value = value; this.line = line; this.pos = pos;
		}
		@Override
		public String toString() {
			return String.format("%5d  %5d %-15s %s", this.line, this.pos, this.tokentype, this.value);
		}
	}

	static enum TokenType {
		End_of_input(false, false, false, -1, NodeType.nd_None),
		Op_multiply(false, true, false, 13, NodeType.nd_Mul),
		Op_divide(false, true, false, 13, NodeType.nd_Div),
		Op_mod(false, true, false, 13, NodeType.nd_Mod),
		Op_add(false, true, false, 12, NodeType.nd_Add),
		Op_subtract(false, true, false, 12, NodeType.nd_Sub),
		Op_negate(false, false, true, 14, NodeType.nd_Negate),
		Op_not(false, false, true, 14, NodeType.nd_Not),
		Op_less(false, true, false, 10, NodeType.nd_Lss),
		Op_lessequal(false, true, false, 10, NodeType.nd_Leq),
		Op_greater(false, true, false, 10, NodeType.nd_Gtr),
		Op_greaterequal(false, true, false, 10, NodeType.nd_Geq),
		Op_equal(false, true, true, 9, NodeType.nd_Eql),
		Op_notequal(false, true, false, 9, NodeType.nd_Neq),
		Op_assign(false, false, false, -1, NodeType.nd_Assign),
		Op_and(false, true, false, 5, NodeType.nd_And),
		Op_or(false, true, false, 4, NodeType.nd_Or),
		Keyword_if(false, false, false, -1, NodeType.nd_If),
		Keyword_else(false, false, false, -1, NodeType.nd_None),
		Keyword_while(false, false, false, -1, NodeType.nd_While),
		Keyword_print(false, false, false, -1, NodeType.nd_None),
		Keyword_putc(false, false, false, -1, NodeType.nd_None),
		LeftParen(false, false, false, -1, NodeType.nd_None),
		RightParen(false, false, false, -1, NodeType.nd_None),
		LeftBrace(false, false, false, -1, NodeType.nd_None),
		RightBrace(false, false, false, -1, NodeType.nd_None),
		Semicolon(false, false, false, -1, NodeType.nd_None),
		Comma(false, false, false, -1, NodeType.nd_None),
		Identifier(false, false, false, -1, NodeType.nd_Ident),
		Integer(false, false, false, -1, NodeType.nd_Integer),
		String(false, false, false, -1, NodeType.nd_String);

		private final int precedence;
		private final boolean right_assoc;
		private final boolean is_binary;
		private final boolean is_unary;
		private final NodeType node_type;

		TokenType(boolean right_assoc, boolean is_binary, boolean is_unary, int precedence, NodeType node) {
			this.right_assoc = right_assoc;
			this.is_binary = is_binary;
			this.is_unary = is_unary;
			this.precedence = precedence;
			this.node_type = node;
		}
		boolean isRightAssoc() { return this.right_assoc; }
		boolean isBinary() { return this.is_binary; }
		boolean isUnary() { return this.is_unary; }
		int getPrecedence() { return this.precedence; }
		NodeType getNodeType() { return this.node_type; }
	}
	static enum NodeType {
		nd_None(""), nd_Ident("Identifier"), nd_String("String"), nd_Integer("Integer"), nd_Sequence("Sequence"), nd_If("If"),
		nd_Prtc("Prtc"), nd_Prts("Prts"), nd_Prti("Prti"), nd_While("While"),
		nd_Assign("Assign"), nd_Negate("Negate"), nd_Not("Not"), nd_Mul("Multiply"), nd_Div("Divide"), nd_Mod("Mod"), nd_Add("Add"),
		nd_Sub("Subtract"), nd_Lss("Less"), nd_Leq("LessEqual"),
		nd_Gtr("Greater"), nd_Geq("GreaterEqual"), nd_Eql("Equal"), nd_Neq("NotEqual"), nd_And("And"), nd_Or("Or");

		private final String name;

		NodeType(String name) {
			this.name = name;
		}

		@Override
		public String toString() { return this.name; }
	}
	static void error(int line, int pos, String msg) {
		if (line > 0 && pos > 0) {
			System.out.printf("%s in line %d, pos %d\n", msg, line, pos);
		} else {
			System.out.println(msg);
		}
		System.exit(1);
	}
	Parser(List<Token> source) {
		this.source = source;
		this.token = null;
		this.position = 0;
	}
	Token getNextToken() {
		this.token = this.source.get(this.position++);
		return this.token;
	}
	Node expr(int p) {
		Node result = null, node;
		TokenType op;
		int q;

		if (this.token.tokentype == TokenType.LeftParen) {
			result = paren_expr();
		} else if (this.token.tokentype == TokenType.Op_add || this.token.tokentype == TokenType.Op_subtract) {
			op = (this.token.tokentype == TokenType.Op_subtract) ? TokenType.Op_negate : TokenType.Op_add;
			getNextToken();
			node = expr(TokenType.Op_negate.getPrecedence());
			result = (op == TokenType.Op_negate) ? Node.make_node(NodeType.nd_Negate, node) : node;
		} else if (this.token.tokentype == TokenType.Op_not) {
			getNextToken();
			result = Node.make_node(NodeType.nd_Not, expr(TokenType.Op_not.getPrecedence()));
		} else if (this.token.tokentype == TokenType.Identifier) {
			result = Node.make_leaf(NodeType.nd_Ident, this.token.value);
			getNextToken();
		} else if (this.token.tokentype == TokenType.Integer) {
			result = Node.make_leaf(NodeType.nd_Integer, this.token.value);
			getNextToken();
		} else {
			error(this.token.line, this.token.pos, "Expecting a primary, found: " + this.token.tokentype);
		}

		while (this.token.tokentype.isBinary() && this.token.tokentype.getPrecedence() >= p) {
			op = this.token.tokentype;
			getNextToken();
			q = op.getPrecedence();
			if (!op.isRightAssoc()) {
				q++;
			}
			node = expr(q);
			result = Node.make_node(op.getNodeType(), result, node);
		}
		return result;
	}
	Node paren_expr() {
		expect("paren_expr", TokenType.LeftParen);
		Node node = expr(0);
		expect("paren_expr", TokenType.RightParen);
		return node;
	}
	void expect(String msg, TokenType s) {
		if (this.token.tokentype == s) {
			getNextToken();
			return;
		}
		error(this.token.line, this.token.pos, msg + ": Expecting '" + s + "', found: '" + this.token.tokentype + "'");
	}
	Node stmt() {
		Node s, s2, t = null, e, v;
		if (this.token.tokentype == TokenType.Keyword_if) {
			getNextToken();
			e = paren_expr();
			s = stmt();
			s2 = null;
			if (this.token.tokentype == TokenType.Keyword_else) {
				getNextToken();
				s2 = stmt();
			}
			t = Node.make_node(NodeType.nd_If, e, Node.make_node(NodeType.nd_If, s, s2));
		} else if (this.token.tokentype == TokenType.Keyword_putc) {
			getNextToken();
			e = paren_expr();
			t = Node.make_node(NodeType.nd_Prtc, e);
			expect("Putc", TokenType.Semicolon);
		} else if (this.token.tokentype == TokenType.Keyword_print) {
			getNextToken();
			expect("Print", TokenType.LeftParen);
			while (true) {
				if (this.token.tokentype == TokenType.String) {
					e = Node.make_node(NodeType.nd_Prts, Node.make_leaf(NodeType.nd_String, this.token.value));
					getNextToken();
				} else {
					e = Node.make_node(NodeType.nd_Prti, expr(0), null);
				}
				t = Node.make_node(NodeType.nd_Sequence, t, e);
				if (this.token.tokentype != TokenType.Comma) {
					break;
				}
				getNextToken();
			}
			expect("Print", TokenType.RightParen);
			expect("Print", TokenType.Semicolon);
		} else if (this.token.tokentype == TokenType.Semicolon) {
			getNextToken();
		} else if (this.token.tokentype == TokenType.Identifier) {
			v = Node.make_leaf(NodeType.nd_Ident, this.token.value);
			getNextToken();
			expect("assign", TokenType.Op_assign);
			e = expr(0);
			t = Node.make_node(NodeType.nd_Assign, v, e);
			expect("assign", TokenType.Semicolon);
		} else if (this.token.tokentype == TokenType.Keyword_while) {
			getNextToken();
			e = paren_expr();
			s = stmt();
			t = Node.make_node(NodeType.nd_While, e, s);
		} else if (this.token.tokentype == TokenType.LeftBrace) {
			getNextToken();
			while (this.token.tokentype != TokenType.RightBrace && this.token.tokentype != TokenType.End_of_input) {
				t = Node.make_node(NodeType.nd_Sequence, t, stmt());
			}
			expect("LBrace", TokenType.RightBrace);
		} else if (this.token.tokentype == TokenType.End_of_input) {
		} else {
			error(this.token.line, this.token.pos, "Expecting start of statement, found: " + this.token.tokentype);
		}
		return t;
	}
	Node parse() {
		Node t = null;
		getNextToken();
		while (this.token.tokentype != TokenType.End_of_input) {
			t = Node.make_node(NodeType.nd_Sequence, t, stmt());
		}
		return t;
	}
	void printAST(Node t) {
		int i = 0;
		if (t == null) {
			System.out.println(";");
		} else {
			System.out.printf("%-14s", t.nt);
			if (t.nt == NodeType.nd_Ident || t.nt == NodeType.nd_Integer || t.nt == NodeType.nd_String) {
				System.out.println(" " + t.value);
			} else {
				System.out.println();
				printAST(t.left);
				printAST(t.right);
			}
		}
	}
	public static void main(String[] args) {
		if (args.length > 0) {
			try {
				String value, token;
				int line, pos;
				Token t;
				boolean found;
				List<Token> list = new ArrayList<>();
				Map<String, TokenType> str_to_tokens = new HashMap<>();

				str_to_tokens.put("End_of_input", TokenType.End_of_input);
				str_to_tokens.put("Op_multiply", TokenType.Op_multiply);
				str_to_tokens.put("Op_divide", TokenType.Op_divide);
				str_to_tokens.put("Op_mod", TokenType.Op_mod);
				str_to_tokens.put("Op_add", TokenType.Op_add);
				str_to_tokens.put("Op_subtract", TokenType.Op_subtract);
				str_to_tokens.put("Op_negate", TokenType.Op_negate);
				str_to_tokens.put("Op_not", TokenType.Op_not);
				str_to_tokens.put("Op_less", TokenType.Op_less);
				str_to_tokens.put("Op_lessequal", TokenType.Op_lessequal);
				str_to_tokens.put("Op_greater", TokenType.Op_greater);
				str_to_tokens.put("Op_greaterequal", TokenType.Op_greaterequal);
				str_to_tokens.put("Op_equal", TokenType.Op_equal);
				str_to_tokens.put("Op_notequal", TokenType.Op_notequal);
				str_to_tokens.put("Op_assign", TokenType.Op_assign);
				str_to_tokens.put("Op_and", TokenType.Op_and);
				str_to_tokens.put("Op_or", TokenType.Op_or);
				str_to_tokens.put("Keyword_if", TokenType.Keyword_if);
				str_to_tokens.put("Keyword_else", TokenType.Keyword_else);
				str_to_tokens.put("Keyword_while", TokenType.Keyword_while);
				str_to_tokens.put("Keyword_print", TokenType.Keyword_print);
				str_to_tokens.put("Keyword_putc", TokenType.Keyword_putc);
				str_to_tokens.put("LeftParen", TokenType.LeftParen);
				str_to_tokens.put("RightParen", TokenType.RightParen);
				str_to_tokens.put("LeftBrace", TokenType.LeftBrace);
				str_to_tokens.put("RightBrace", TokenType.RightBrace);
				str_to_tokens.put("Semicolon", TokenType.Semicolon);
				str_to_tokens.put("Comma", TokenType.Comma);
				str_to_tokens.put("Identifier", TokenType.Identifier);
				str_to_tokens.put("Integer", TokenType.Integer);
				str_to_tokens.put("String", TokenType.String);

				Scanner s = new Scanner(new File(args[0]));
				String source = " ";
				while (s.hasNext()) {
					String str = s.nextLine();
					StringTokenizer st = new StringTokenizer(str);
					line = Integer.parseInt(st.nextToken());
					pos = Integer.parseInt(st.nextToken());
					token = st.nextToken();
					value = "";
					while (st.hasMoreTokens()) {
						value += st.nextToken() + " ";
					}
					found = false;
					if (str_to_tokens.containsKey(token)) {
						found = true;
						list.add(new Token(str_to_tokens.get(token), value, line, pos));
					}
					if (found == false) {
						throw new Exception("Token not found: '" + token + "'");
					}
				}
				Parser p = new Parser(list);
				p.printAST(p.parse());
			} catch (FileNotFoundException e) {
				error(-1, -1, "Exception: " + e.getMessage());
			} catch (Exception e) {
				error(-1, -1, "Exception: " + e.getMessage());
			}
		} else {
			error(-1, -1, "No args");
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
def expr(p)
    if tok is "("
        x = paren_expr()
    elif tok in ["-", "+", "!"]
        gettok()
        y = expr(precedence of operator)
        if operator was "+"
            x = y
        else
            x = make_node(operator, y)
    elif tok is an Identifier
        x = make_leaf(Identifier, variable name)
        gettok()
    elif tok is an Integer constant
        x = make_leaf(Integer, integer value)
        gettok()
    else
        error()

    while tok is a binary operator and precedence of tok >= p
        save_tok = tok
        gettok()
        q = precedence of save_tok
        if save_tok is not right associative
            q += 1
        x = make_node(Operator save_tok represents, x, expr(q))

    return x

def paren_expr()
    expect("(")
    x = expr(0)
    expect(")")
    return x

def stmt()
    t = NULL
    if accept("if")
        e = paren_expr()
        s = stmt()
        t = make_node(If, e, make_node(If, s, accept("else") ? stmt() : NULL))
    elif accept("putc")
        t = make_node(Prtc, paren_expr())
        expect(";")
    elif accept("print")
        expect("(")
        repeat
            if tok is a string
                e = make_node(Prts, make_leaf(String, the string))
                gettok()
            else
                e = make_node(Prti, expr(0))

            t = make_node(Sequence, t, e)
        until not accept(",")
        expect(")")
        expect(";")
    elif tok is ";"
        gettok()
    elif tok is an Identifier
        v = make_leaf(Identifier, variable name)
        gettok()
        expect("=")
        t = make_node(Assign, v, expr(0))
        expect(";")
    elif accept("while")
        e = paren_expr()
        t = make_node(While, e, stmt()
    elif accept("{")
        while tok not equal "}" and tok not equal end-of-file
            t = make_node(Sequence, t, stmt())
        expect("}")
    elif tok is end-of-file
        pass
    else
        error()
    return t

def parse()
    t = NULL
    gettok()
    repeat
        t = make_node(Sequence, t, stmt())
    until tok is end-of-file
    return t

```

### python_code_2.txt
```python
def prt_ast(t)
    if t == NULL
        print(";\n")
    else
        print(t.node_type)
        if t.node_type in [Identifier, Integer, String]     # leaf node
            print the value of the Ident, Integer or String, "\n"
        else
            print("\n")
            prt_ast(t.left)
            prt_ast(t.right)

```

### python_code_3.txt
```python
def load_ast()
    line = readline()
    # Each line has at least one token
    line_list = tokenize the line, respecting double quotes

    text = line_list[0] # first token is always the node type

    if text == ";"   # a terminal node
        return NULL

    node_type = text # could convert to internal form if desired

    # A line with two tokens is a leaf node
    # Leaf nodes are: Identifier, Integer, String
    # The 2nd token is the value
    if len(line_list) > 1
        return make_leaf(node_type, line_list[1])

    left = load_ast()
    right = load_ast()
    return make_node(node_type, left, right)

```

### python_code_4.txt
```python
from __future__ import print_function
import sys, shlex, operator

tk_EOI, tk_Mul, tk_Div, tk_Mod, tk_Add, tk_Sub, tk_Negate, tk_Not, tk_Lss, tk_Leq, tk_Gtr, \
tk_Geq, tk_Eql, tk_Neq, tk_Assign, tk_And, tk_Or, tk_If, tk_Else, tk_While, tk_Print,      \
tk_Putc, tk_Lparen, tk_Rparen, tk_Lbrace, tk_Rbrace, tk_Semi, tk_Comma, tk_Ident,          \
tk_Integer, tk_String = range(31)

nd_Ident, nd_String, nd_Integer, nd_Sequence, nd_If, nd_Prtc, nd_Prts, nd_Prti, nd_While, \
nd_Assign, nd_Negate, nd_Not, nd_Mul, nd_Div, nd_Mod, nd_Add, nd_Sub, nd_Lss, nd_Leq,     \
nd_Gtr, nd_Geq, nd_Eql, nd_Neq, nd_And, nd_Or = range(25)

# must have same order as above
Tokens = [
    ["EOI"             , False, False, False, -1, -1        ],
    ["*"               , False, True,  False, 13, nd_Mul    ],
    ["/"               , False, True,  False, 13, nd_Div    ],
    ["%"               , False, True,  False, 13, nd_Mod    ],
    ["+"               , False, True,  False, 12, nd_Add    ],
    ["-"               , False, True,  False, 12, nd_Sub    ],
    ["-"               , False, False, True,  14, nd_Negate ],
    ["!"               , False, False, True,  14, nd_Not    ],
    ["<"               , False, True,  False, 10, nd_Lss    ],
    ["<="              , False, True,  False, 10, nd_Leq    ],
    [">"               , False, True,  False, 10, nd_Gtr    ],
    [">="              , False, True,  False, 10, nd_Geq    ],
    ["=="              , False, True,  False,  9, nd_Eql    ],
    ["!="              , False, True,  False,  9, nd_Neq    ],
    ["="               , False, False, False, -1, nd_Assign ],
    ["&&"              , False, True,  False,  5, nd_And    ],
    ["||"              , False, True,  False,  4, nd_Or     ],
    ["if"              , False, False, False, -1, nd_If     ],
    ["else"            , False, False, False, -1, -1        ],
    ["while"           , False, False, False, -1, nd_While  ],
    ["print"           , False, False, False, -1, -1        ],
    ["putc"            , False, False, False, -1, -1        ],
    ["("               , False, False, False, -1, -1        ],
    [")"               , False, False, False, -1, -1        ],
    ["{"               , False, False, False, -1, -1        ],
    ["}"               , False, False, False, -1, -1        ],
    [";"               , False, False, False, -1, -1        ],
    [","               , False, False, False, -1, -1        ],
    ["Ident"           , False, False, False, -1, nd_Ident  ],
    ["Integer literal" , False, False, False, -1, nd_Integer],
    ["String literal"  , False, False, False, -1, nd_String ]
    ]

all_syms = {"End_of_input"   : tk_EOI,     "Op_multiply"    : tk_Mul,
            "Op_divide"      : tk_Div,     "Op_mod"         : tk_Mod,
            "Op_add"         : tk_Add,     "Op_subtract"    : tk_Sub,
            "Op_negate"      : tk_Negate,  "Op_not"         : tk_Not,
            "Op_less"        : tk_Lss,     "Op_lessequal"   : tk_Leq,
            "Op_greater"     : tk_Gtr,     "Op_greaterequal": tk_Geq,
            "Op_equal"       : tk_Eql,     "Op_notequal"    : tk_Neq,
            "Op_assign"      : tk_Assign,  "Op_and"         : tk_And,
            "Op_or"          : tk_Or,      "Keyword_if"     : tk_If,
            "Keyword_else"   : tk_Else,    "Keyword_while"  : tk_While,
            "Keyword_print"  : tk_Print,   "Keyword_putc"   : tk_Putc,
            "LeftParen"      : tk_Lparen,  "RightParen"     : tk_Rparen,
            "LeftBrace"      : tk_Lbrace,  "RightBrace"     : tk_Rbrace,
            "Semicolon"      : tk_Semi,    "Comma"          : tk_Comma,
            "Identifier"     : tk_Ident,   "Integer"        : tk_Integer,
            "String"         : tk_String}

Display_nodes = ["Identifier", "String", "Integer", "Sequence", "If", "Prtc", "Prts",
    "Prti", "While", "Assign", "Negate", "Not", "Multiply", "Divide", "Mod", "Add",
    "Subtract", "Less", "LessEqual", "Greater", "GreaterEqual", "Equal", "NotEqual",
    "And", "Or"]

TK_NAME         = 0
TK_RIGHT_ASSOC  = 1
TK_IS_BINARY    = 2
TK_IS_UNARY     = 3
TK_PRECEDENCE   = 4
TK_NODE         = 5

input_file = None
err_line   = None
err_col    = None
tok        = None
tok_text   = None

#*** show error and exit
def error(msg):
    print("(%d, %d) %s" % (int(err_line), int(err_col), msg))
    exit(1)

#***
def gettok():
    global err_line, err_col, tok, tok_text, tok_other
    line = input_file.readline()
    if len(line) == 0:
        error("empty line")

    line_list = shlex.split(line, False, False)
    # line col Ident var_name
    # 0    1   2     3

    err_line = line_list[0]
    err_col  = line_list[1]
    tok_text = line_list[2]

    tok = all_syms.get(tok_text)
    if tok == None:
        error("Unknown token %s" % (tok_text))

    tok_other = None
    if tok in [tk_Integer, tk_Ident, tk_String]:
        tok_other = line_list[3]

class Node:
    def __init__(self, node_type, left = None, right = None, value = None):
        self.node_type  = node_type
        self.left  = left
        self.right = right
        self.value = value

#***
def make_node(oper, left, right = None):
    return Node(oper, left, right)

#***
def make_leaf(oper, n):
    return Node(oper, value = n)

#***
def expect(msg, s):
    if tok == s:
        gettok()
        return
    error("%s: Expecting '%s', found '%s'" % (msg, Tokens[s][TK_NAME], Tokens[tok][TK_NAME]))

#***
def expr(p):
    x = None

    if tok == tk_Lparen:
        x = paren_expr()
    elif tok in [tk_Sub, tk_Add]:
        op = (tk_Negate if tok == tk_Sub else tk_Add)
        gettok()
        node = expr(Tokens[tk_Negate][TK_PRECEDENCE])
        x = (make_node(nd_Negate, node) if op == tk_Negate else node)
    elif tok == tk_Not:
        gettok()
        x = make_node(nd_Not, expr(Tokens[tk_Not][TK_PRECEDENCE]))
    elif tok == tk_Ident:
        x = make_leaf(nd_Ident, tok_other)
        gettok()
    elif tok == tk_Integer:
        x = make_leaf(nd_Integer, tok_other)
        gettok()
    else:
        error("Expecting a primary, found: %s" % (Tokens[tok][TK_NAME]))

    while Tokens[tok][TK_IS_BINARY] and Tokens[tok][TK_PRECEDENCE] >= p:
        op = tok
        gettok()
        q = Tokens[op][TK_PRECEDENCE]
        if not Tokens[op][TK_RIGHT_ASSOC]:
            q += 1

        node = expr(q)
        x = make_node(Tokens[op][TK_NODE], x, node)

    return x

#***
def paren_expr():
    expect("paren_expr", tk_Lparen)
    node = expr(0)
    expect("paren_expr", tk_Rparen)
    return node

#***
def stmt():
    t = None

    if tok == tk_If:
        gettok()
        e = paren_expr()
        s = stmt()
        s2 = None
        if tok == tk_Else:
            gettok()
            s2 = stmt()
        t = make_node(nd_If, e, make_node(nd_If, s, s2))
    elif tok == tk_Putc:
        gettok()
        e = paren_expr()
        t = make_node(nd_Prtc, e)
        expect("Putc", tk_Semi)
    elif tok == tk_Print:
        gettok()
        expect("Print", tk_Lparen)
        while True:
            if tok == tk_String:
                e = make_node(nd_Prts, make_leaf(nd_String, tok_other))
                gettok()
            else:
                e = make_node(nd_Prti, expr(0))

            t = make_node(nd_Sequence, t, e)
            if tok != tk_Comma:
                break
            gettok()
        expect("Print", tk_Rparen)
        expect("Print", tk_Semi)
    elif tok == tk_Semi:
        gettok()
    elif tok == tk_Ident:
        v = make_leaf(nd_Ident, tok_other)
        gettok()
        expect("assign", tk_Assign)
        e = expr(0)
        t = make_node(nd_Assign, v, e)
        expect("assign", tk_Semi)
    elif tok == tk_While:
        gettok()
        e = paren_expr()
        s = stmt()
        t = make_node(nd_While, e, s)
    elif tok == tk_Lbrace:
        gettok()
        while tok != tk_Rbrace and tok != tk_EOI:
            t = make_node(nd_Sequence, t, stmt())
        expect("Lbrace", tk_Rbrace)
    elif tok == tk_EOI:
        pass
    else:
        error("Expecting start of statement, found: %s" % (Tokens[tok][TK_NAME]))

    return t

#***
def parse():
    t = None
    gettok()
    while True:
        t = make_node(nd_Sequence, t, stmt())
        if tok == tk_EOI or t == None:
            break
    return t

def prt_ast(t):
    if t == None:
        print(";")
    else:
        print("%-14s" % (Display_nodes[t.node_type]), end='')
        if t.node_type in [nd_Ident, nd_Integer]:
            print("%s" % (t.value))
        elif t.node_type == nd_String:
            print("%s" %(t.value))
        else:
            print("")
            prt_ast(t.left)
            prt_ast(t.right)

#*** main driver
input_file = sys.stdin
if len(sys.argv) > 1:
    try:
        input_file = open(sys.argv[1], "r", 4096)
    except IOError as e:
        error(0, 0, "Can't open %s" % sys.argv[1])
t = parse()
prt_ast(t)

```

