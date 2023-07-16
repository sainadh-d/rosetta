# Compiler/AST interpreter

## Task Link
[Rosetta Code - Compiler/AST interpreter](https://rosettacode.org/wiki/Compiler/AST_interpreter)

## Java Code
### java_code_1.txt
```java
import java.util.Scanner;
import java.io.File;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

class Interpreter {
	static Map<String, Integer> globals = new HashMap<>();
	static Scanner s;
	static List<Node> list = new ArrayList<>();
	static Map<String, NodeType> str_to_nodes = new HashMap<>();

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
	static enum NodeType {
		nd_None(";"), nd_Ident("Identifier"), nd_String("String"), nd_Integer("Integer"),
		nd_Sequence("Sequence"), nd_If("If"),
		nd_Prtc("Prtc"), nd_Prts("Prts"), nd_Prti("Prti"), nd_While("While"),
		nd_Assign("Assign"), nd_Negate("Negate"), nd_Not("Not"), nd_Mul("Multiply"), nd_Div("Divide"),
		nd_Mod("Mod"), nd_Add("Add"),
		nd_Sub("Subtract"), nd_Lss("Less"), nd_Leq("LessEqual"),
		nd_Gtr("Greater"), nd_Geq("GreaterEqual"), nd_Eql("Equal"), nd_Neq("NotEqual"), nd_And("And"), nd_Or("Or");
		
		private final String name;
		
		NodeType(String name) {	this.name = name; }
		
		@Override
		public String toString() { return this.name; }
	}
	static String str(String s) {
		String result = "";
		int i = 0;
		s = s.replace("\"", "");
		while (i < s.length()) {
			if (s.charAt(i) == '\\' && i + 1 < s.length()) {
				if (s.charAt(i + 1) == 'n') {
					result += '\n';
					i += 2;
				} else if (s.charAt(i) == '\\') {
					result += '\\';
					i += 2;
				} 
			} else {
				result += s.charAt(i);
				i++;
			}
		}
		return result;
	}
	static boolean itob(int i) {
		return i != 0;
	}
	static int btoi(boolean b) {
		return b ? 1 : 0;
	}
	static int fetch_var(String name) {
		int result;
		if (globals.containsKey(name)) {
			result = globals.get(name);
		} else {
			globals.put(name, 0);
			result = 0;
		}
		return result;		
	}
	static Integer interpret(Node n) throws Exception {
		if (n == null) {
			return 0;
		}
		switch (n.nt) {
			case nd_Integer:
				return Integer.parseInt(n.value);
			case nd_Ident:
				return fetch_var(n.value);
			case nd_String:
				return 1;//n.value;
			case nd_Assign:
				globals.put(n.left.value, interpret(n.right));
				return 0;
			case nd_Add:
				return interpret(n.left) + interpret(n.right);
			case nd_Sub:
				return interpret(n.left) - interpret(n.right);
			case nd_Mul:
				return interpret(n.left) * interpret(n.right);
			case nd_Div:
				return interpret(n.left) / interpret(n.right);
			case nd_Mod:
				return interpret(n.left) % interpret(n.right);
			case nd_Lss:
				return btoi(interpret(n.left) < interpret(n.right));
			case nd_Leq:
				return btoi(interpret(n.left) <= interpret(n.right));
			case nd_Gtr:
				return btoi(interpret(n.left) > interpret(n.right));
			case nd_Geq:
				return btoi(interpret(n.left) >= interpret(n.right));
			case nd_Eql:
				return btoi(interpret(n.left) == interpret(n.right));
			case nd_Neq:
				return btoi(interpret(n.left) != interpret(n.right));
			case nd_And:
				return btoi(itob(interpret(n.left)) && itob(interpret(n.right)));
			case nd_Or:
				return btoi(itob(interpret(n.left)) || itob(interpret(n.right)));
			case nd_Not:
				if (interpret(n.left) == 0) {
					return 1;
				} else {
					return 0;
				}
			case nd_Negate:
				return -interpret(n.left);
			case nd_If:
				if (interpret(n.left) != 0) {
					interpret(n.right.left);
				} else {
					interpret(n.right.right);
				}
				return 0;
			case nd_While:
				while (interpret(n.left) != 0) {
					interpret(n.right);
				}
				return 0;
			case nd_Prtc:
				System.out.printf("%c", interpret(n.left));
				return 0;
			case nd_Prti:
				System.out.printf("%d", interpret(n.left));
				return 0;
			case nd_Prts:
				System.out.print(str(n.left.value));//interpret(n.left));
				return 0;
			case nd_Sequence:
				interpret(n.left);
				interpret(n.right);
				return 0;
			default:
				throw new Exception("Error: '" + n.nt + "' found, expecting operator");
		}
	}
	static Node load_ast() throws Exception {
		String command, value;
		String line;
		Node left, right;
		
		while (s.hasNext()) {
			line = s.nextLine();
			value = null;
			if (line.length() > 16) {
				command = line.substring(0, 15).trim();
				value = line.substring(15).trim();
			} else {
				command = line.trim();
			}
			if (command.equals(";")) {
				return null;
			}
			if (!str_to_nodes.containsKey(command)) {
				throw new Exception("Command not found: '" + command + "'");
			}
			if (value != null) {
				return Node.make_leaf(str_to_nodes.get(command), value);
			}
			left = load_ast(); right = load_ast();
			return Node.make_node(str_to_nodes.get(command), left, right);
		}
		return null; // for the compiler, not needed
	}
	public static void main(String[] args) {
		Node n;

		str_to_nodes.put(";", NodeType.nd_None);
		str_to_nodes.put("Sequence", NodeType.nd_Sequence);
		str_to_nodes.put("Identifier", NodeType.nd_Ident);
		str_to_nodes.put("String", NodeType.nd_String);
		str_to_nodes.put("Integer", NodeType.nd_Integer);
		str_to_nodes.put("If", NodeType.nd_If);
		str_to_nodes.put("While", NodeType.nd_While);
		str_to_nodes.put("Prtc", NodeType.nd_Prtc);
		str_to_nodes.put("Prts", NodeType.nd_Prts);
		str_to_nodes.put("Prti", NodeType.nd_Prti);
		str_to_nodes.put("Assign", NodeType.nd_Assign);
		str_to_nodes.put("Negate", NodeType.nd_Negate);
		str_to_nodes.put("Not", NodeType.nd_Not);
		str_to_nodes.put("Multiply", NodeType.nd_Mul);
		str_to_nodes.put("Divide", NodeType.nd_Div);
		str_to_nodes.put("Mod", NodeType.nd_Mod);
		str_to_nodes.put("Add", NodeType.nd_Add);
		str_to_nodes.put("Subtract", NodeType.nd_Sub);
		str_to_nodes.put("Less", NodeType.nd_Lss);
		str_to_nodes.put("LessEqual", NodeType.nd_Leq);
		str_to_nodes.put("Greater", NodeType.nd_Gtr);
		str_to_nodes.put("GreaterEqual", NodeType.nd_Geq);
		str_to_nodes.put("Equal", NodeType.nd_Eql);
		str_to_nodes.put("NotEqual", NodeType.nd_Neq);
		str_to_nodes.put("And", NodeType.nd_And);
		str_to_nodes.put("Or", NodeType.nd_Or);
		
		if (args.length > 0) {
			try {
				s = new Scanner(new File(args[0]));
				n = load_ast();
				interpret(n);
			} catch (Exception e) {
				System.out.println("Ex: "+e.getMessage());
			}
		}
	}
}

```

## Python Code
### python_code_1.txt
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

### python_code_2.txt
```python
interp(x)
    if x == NULL return NULL
    elif x.node_type == Integer return x.value converted to an integer
    elif x.node_type == Ident   return the current value of variable x.value
    elif x.node_type == String  return x.value
    elif x.node_type == Assign
                    globals[x.left.value] = interp(x.right)
                    return NULL
    elif x.node_type is a binary operator return interp(x.left) operator interp(x.right)
    elif x.node_type is a unary operator, return return operator interp(x.left)
    elif x.node_type ==  If
                    if (interp(x.left)) then interp(x.right.left)
                    else interp(x.right.right)
                    return NULL
    elif x.node_type == While
                    while (interp(x.left)) do interp(x.right)
                    return NULL
    elif x.node_type == Prtc
                    print interp(x.left) as a character, no newline
                    return NULL
    elif x.node_type == Prti
                    print interp(x.left) as an integer, no newline
                    return NULL
    elif x.node_type == Prts
                    print interp(x.left) as a string, respecting newlines ("\n")
                    return NULL
    elif x.node_type == Sequence
                    interp(x.left)
                    interp(x.right)
                    return NULL
    else
        error("unknown node type")

```

### python_code_3.txt
```python
from __future__ import print_function
import sys, shlex, operator

nd_Ident, nd_String, nd_Integer, nd_Sequence, nd_If, nd_Prtc, nd_Prts, nd_Prti, nd_While, \
nd_Assign, nd_Negate, nd_Not, nd_Mul, nd_Div, nd_Mod, nd_Add, nd_Sub, nd_Lss, nd_Leq,     \
nd_Gtr, nd_Geq, nd_Eql, nd_Neq, nd_And, nd_Or = range(25)

all_syms = {
    "Identifier"  : nd_Ident,    "String"      : nd_String,
    "Integer"     : nd_Integer,  "Sequence"    : nd_Sequence,
    "If"          : nd_If,       "Prtc"        : nd_Prtc,
    "Prts"        : nd_Prts,     "Prti"        : nd_Prti,
    "While"       : nd_While,    "Assign"      : nd_Assign,
    "Negate"      : nd_Negate,   "Not"         : nd_Not,
    "Multiply"    : nd_Mul,      "Divide"      : nd_Div,
    "Mod"         : nd_Mod,      "Add"         : nd_Add,
    "Subtract"    : nd_Sub,      "Less"        : nd_Lss,
    "LessEqual"   : nd_Leq,      "Greater"     : nd_Gtr,
    "GreaterEqual": nd_Geq,      "Equal"       : nd_Eql,
    "NotEqual"    : nd_Neq,      "And"         : nd_And,
    "Or"          : nd_Or}

input_file  = None
globals     = {}

#*** show error and exit
def error(msg):
    print("%s" % (msg))
    exit(1)

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
def fetch_var(var_name):
    n = globals.get(var_name, None)
    if n == None:
        globals[var_name] = n = 0
    return n

#***
def interp(x):
    global globals

    if x == None: return None
    elif x.node_type == nd_Integer: return int(x.value)
    elif x.node_type == nd_Ident:   return fetch_var(x.value)
    elif x.node_type == nd_String:  return x.value

    elif x.node_type == nd_Assign:
                    globals[x.left.value] = interp(x.right)
                    return None
    elif x.node_type == nd_Add:     return interp(x.left) +   interp(x.right)
    elif x.node_type == nd_Sub:     return interp(x.left) -   interp(x.right)
    elif x.node_type == nd_Mul:     return interp(x.left) *   interp(x.right)
    # use C like division semantics
    # another way: abs(x) / abs(y) * cmp(x, 0) * cmp(y, 0)
    elif x.node_type == nd_Div:     return int(float(interp(x.left)) / interp(x.right))
    elif x.node_type == nd_Mod:     return int(float(interp(x.left)) % interp(x.right))
    elif x.node_type == nd_Lss:     return interp(x.left) <   interp(x.right)
    elif x.node_type == nd_Gtr:     return interp(x.left) >   interp(x.right)
    elif x.node_type == nd_Leq:     return interp(x.left) <=  interp(x.right)
    elif x.node_type == nd_Geq:     return interp(x.left) >=  interp(x.right)
    elif x.node_type == nd_Eql:     return interp(x.left) ==  interp(x.right)
    elif x.node_type == nd_Neq:     return interp(x.left) !=  interp(x.right)
    elif x.node_type == nd_And:     return interp(x.left) and interp(x.right)
    elif x.node_type == nd_Or:      return interp(x.left) or  interp(x.right)
    elif x.node_type == nd_Negate:  return -interp(x.left)
    elif x.node_type == nd_Not:     return not interp(x.left)

    elif x.node_type ==  nd_If:
                    if (interp(x.left)):
                        interp(x.right.left)
                    else:
                        interp(x.right.right)
                    return None

    elif x.node_type == nd_While:
                    while (interp(x.left)):
                        interp(x.right)
                    return None

    elif x.node_type == nd_Prtc:
                    print("%c" % (interp(x.left)), end='')
                    return None

    elif x.node_type == nd_Prti:
                    print("%d" % (interp(x.left)), end='')
                    return None

    elif x.node_type == nd_Prts:
                    print(interp(x.left), end='')
                    return None

    elif x.node_type == nd_Sequence:
                    interp(x.left)
                    interp(x.right)
                    return None
    else:
        error("error in code generator - found %d, expecting operator" % (x.node_type))

def str_trans(srce):
    dest = ""
    i = 0
    srce = srce[1:-1]
    while i < len(srce):
        if srce[i] == '\\' and i + 1 < len(srce):
            if srce[i + 1] == 'n':
                dest += '\n'
                i += 2
            elif srce[i + 1] == '\\':
                dest += '\\'
                i += 2
        else:
            dest += srce[i]
            i += 1

    return dest

def load_ast():
    line = input_file.readline()
    line_list = shlex.split(line, False, False)

    text = line_list[0]

    value = None
    if len(line_list) > 1:
        value = line_list[1]
        if value.isdigit():
            value = int(value)

    if text == ";":
        return None
    node_type = all_syms[text]
    if value != None:
        if node_type == nd_String:
            value = str_trans(value)

        return make_leaf(node_type, value)
    left = load_ast()
    right = load_ast()
    return make_node(node_type, left, right)

#*** main driver
input_file = sys.stdin
if len(sys.argv) > 1:
    try:
        input_file = open(sys.argv[1], "r", 4096)
    except IOError as e:
        error(0, 0, "Can't open %s" % sys.argv[1])

n = load_ast()
interp(n)

```

