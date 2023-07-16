# User input/Graphical

## Task Link
[Rosetta Code - User input/Graphical](https://rosettacode.org/wiki/User_input/Graphical)

## Java Code
### java_code_1.txt
```java
import javax.swing.*;

public class GetInputSwing {
    public static void main(String[] args) throws Exception {
        int number = Integer.parseInt(
                JOptionPane.showInputDialog ("Enter an Integer"));
        String string = JOptionPane.showInputDialog ("Enter a String");
    }
}

```

### java_code_2.txt
```java
import javax.swing.JOptionPane;

int number = int(JOptionPane.showInputDialog ("Enter an Integer"));
println(number);
                
String string = JOptionPane.showInputDialog ("Enter a String");
println(string);

```

## Python Code
### python_code_1.txt
```python
from javax.swing import JOptionPane

def to_int(n, default=0):
    try:
        return int(n)
    except ValueError:
        return default

number = to_int(JOptionPane.showInputDialog ("Enter an Integer")) 
println(number)

a_string = JOptionPane.showInputDialog ("Enter a String")
println(a_string)

```

### python_code_2.txt
```python
import Tkinter,tkSimpleDialog

root = Tkinter.Tk()
root.withdraw()

number = tkSimpleDialog.askinteger("Integer", "Enter a Number")
string = tkSimpleDialog.askstring("String", "Enter a String")

```

### python_code_3.txt
```python
import tkinter
import tkinter.simpledialog as tks
 
root = tkinter.Tk()
root.withdraw()
 
number = tks.askinteger("Integer", "Enter a Number")
string = tks.askstring("String", "Enter a String")

tkinter.messagebox.showinfo("Results", f"Your input:\n {number} {string}")

```

