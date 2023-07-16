# Hello world/Graphical

## Task Link
[Rosetta Code - Hello world/Graphical](https://rosettacode.org/wiki/Hello_world/Graphical)

## Java Code
### java_code_1.txt
```java
import javax.swing.*;
import java.awt.*;

public class OutputSwing {

    public static void main(String[] args) {

        SwingUtilities.invokeLater(new Runnable(){
            public void run() {
                JOptionPane.showMessageDialog (null, "Goodbye, World!"); // in alert box
                JFrame frame = new JFrame("Goodbye, World!");            // on title bar
                JTextArea text = new JTextArea("Goodbye, World!");       // in editable area
                JButton button = new JButton("Goodbye, World!");         // on button

                frame.setLayout(new FlowLayout());
                frame.add(button);
                frame.add(text);
                frame.pack();
                frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
                frame.setVisible(true);
            }
        });
    }
}

```

### java_code_2.txt
```java
import javax.swing.*;
import java.awt.*;

public class HelloWorld {
    public static void main(String[] args) {
        
        SwingUtilities.invokeLater(() -> {
            JOptionPane.showMessageDialog(null, "Goodbye, world!");
            JFrame frame = new JFrame("Goodbye, world!");
            JTextArea text = new JTextArea("Goodbye, world!");
            JButton button = new JButton("Goodbye, world!");

            frame.setLayout(new FlowLayout());
            frame.add(button);
            frame.add(text);
            frame.pack();
            frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            frame.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
import bpy

# select default cube
bpy.data.objects['Cube'].select_set(True)

# delete default cube
bpy.ops.object.delete(True)
  
# add text to Blender scene  
bpy.data.curves.new(type="FONT", name="Font Curve").body = "Hello World"
font_obj = bpy.data.objects.new(name="Font Object", object_data=bpy.data.curves["Font Curve"])
bpy.context.scene.collection.objects.link(font_obj)
        
# camera center to text
bpy.context.scene.camera.location = (2.5,0.3,10)

# camera orient angle to text
bpy.context.scene.camera.rotation_euler = (0,0,0)

# change 3D scene to view from the camera
area = next(area for area in bpy.context.screen.areas if area.type == 'VIEW_3D')
area.spaces[0].region_3d.view_perspective = 'CAMERA'

```

### python_code_2.txt
```python
import tkMessageBox

result = tkMessageBox.showinfo("Some Window Label", "Goodbye, World!")

```

### python_code_3.txt
```python
from tkinter import messagebox

result = messagebox.showinfo("Some Window Label", "Goodbye, World!")

```

### python_code_4.txt
```python
import PyQt4.QtGui
app = PyQt4.QtGui.QApplication([])
pb = PyQt4.QtGui.QPushButton('Hello World')
pb.connect(pb,PyQt4.QtCore.SIGNAL("clicked()"),pb.close)
pb.show()
exit(app.exec_())

```

### python_code_5.txt
```python
import pygtk
pygtk.require('2.0')
import gtk

window = gtk.Window()
window.set_title('Goodbye, World')
window.connect('delete-event', gtk.main_quit)
window.show_all()
gtk.main()

```

### python_code_6.txt
```python
# HelloWorld for VPython - HaJo Gurt - 2014-09-20
from visual import *

scene.title = "VPython Demo"
scene.background = color.gray(0.2)

scene.width  = 600
scene.height = 400
scene.range  = 4
#scene.autocenter = True

S = sphere(pos=(0,0,0), radius=1, material=materials.earth)
rot=0.005

txPos=(0, 1.2, 0)

from visual.text import *
# Old 3D text machinery (pre-Visual 5.3): numbers and uppercase letters only:
T1 = text(pos=txPos, string='HELLO', color=color.red, depth=0.3, justify='center')

import vis
# new text object, can render text from any font (default: "sans") :
T2 = vis.text(pos=txPos, text="Goodbye", color=color.green, depth=-0.3, align='center')
T2.visible=False

Lbl_w = label(pos=(0,0,0), text='World', color=color.cyan,
              xoffset=80, yoffset=-40)     # in screen-pixels

L1 = label(pos=(0,-1.5,0), text='Drag with right mousebutton to rotate view',   box=0)
L2 = label(pos=(0,-1.9,0), text='Drag up+down with middle mousebutton to zoom', box=0)
L3 = label(pos=(0,-2.3,0), text='Left-click to change', color=color.orange,     box=0)

print "Hello World"     # Console


cCount = 0
def change():
    global rot, cCount
    cCount=cCount+1
    print "change:", cCount
    rot=-rot
    if T1.visible:
        T1.visible=False
        T2.visible=True
    else:
        T1.visible=True
        T2.visible=False

scene.bind( 'click', change )
        
while True:
  rate(100)
  S.rotate( angle=rot, axis=(0,1,0) )

```

### python_code_7.txt
```python
import wx

app = wx.App(False)
frame = wx.Frame(None, wx.ID_ANY, "Hello, World")
frame.Show(True)
app.MainLoop()

```

### python_code_8.txt
```python
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label


class GoodByeApp(App):
    def build(self, *args, **kwargs):
        layout = FloatLayout()
        ppp = Popup(title='Goodbye, World!',
                    size_hint=(0.75, 0.75), opacity=0.8,
                    content=Label(font_size='50sp', text='Goodbye, World!'))
        btn = Button(text='Goodbye', size_hint=(0.3, 0.3),
                     pos_hint={'center': (0.5, 0.5)}, on_press=ppp.open)
        layout.add_widget(btn)
        return layout


GoodByeApp().run()

```

### python_code_9.txt
```python
from kivy.app import App
from kivy.lang.builder import Builder

kv = '''
#:import Factory kivy.factory.Factory

FloatLayout:
    Button:
        text: 'Goodbye'
        size_hint: (0.3, 0.3)
        pos_hint: {'center': (0.5, 0.5)}
        on_press: Factory.ThePopUp().open()

<ThePopUp@Popup>:
    title: 'Goodbye, World!'
    size_hint: (0.75, 0.75)
    opacity: 0.8
    Label:
        text: 'Goodbye, World!'
        font_size: '50sp'
'''


class GoodByeApp(App):
    def build(self, *args, **kwargs):
        return Builder.load_string(kv)


GoodByeApp().run()

```

