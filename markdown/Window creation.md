# Window creation

## Task Link
[Rosetta Code - Window creation](https://rosettacode.org/wiki/Window_creation)

## Java Code
### java_code_1.txt
```java
import javax.swing.JFrame;

public class Main {
     public static void main(String[] args) throws Exception {
         JFrame w = new JFrame("Title");
         w.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
         w.setSize(800,600);
         w.setVisible(true);
     }
}

```

### java_code_2.txt
```java
size(1000,1000);

```

## Python Code
### python_code_1.txt
```python
  import Tkinter
  
  w = Tkinter.Tk()
  w.mainloop()

```

### python_code_2.txt
```python
import tkinter
 
w = tkinter.Tk()
w.mainloop()

```

### python_code_3.txt
```python
  from wxPython.wx import *
  
  class MyApp(wxApp):
    def OnInit(self):
      frame = wxFrame(NULL, -1, "Hello from wxPython")
      frame.Show(true)
      self.SetTopWindow(frame)
      return true
  
  app = MyApp(0)
  app.MainLoop()

```

### python_code_4.txt
```python
  import win32ui
  from pywin.mfc.dialog import Dialog
  
  d = Dialog(win32ui.IDD_SIMPLE_INPUT)
  d.CreateWindow()

```

### python_code_5.txt
```python
  import gtk
  
  window = gtk.Window()
  window.show()
  gtk.main()

```

### python_code_6.txt
```python
  from PyQt4.QtGui import *

  app = QApplication([])
  win = QWidget()
  win.show()

  app.exec_()

```

