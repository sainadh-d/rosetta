# Simple windowed application

## Task Link
[Rosetta Code - Simple windowed application](https://rosettacode.org/wiki/Simple_windowed_application)

## Java Code
### java_code_1.txt
```java
import java.awt.BorderLayout;
import java.awt.Dimension;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JLabel;
import javax.swing.SwingUtilities;
public class Clicks extends JFrame{
	private long clicks = 0;

	public Clicks(){
		super("Clicks");//set window title
		JLabel label = new JLabel("There have been no clicks yet");
		JButton clicker = new JButton("click me");
		clicker.addActionListener(//listen to the button
			new ActionListener(){
				@Override
				public void actionPerformed(ActionEvent e) {
					label.setText("There have been " + (++clicks) + " clicks");//change the text
				}
			}
		);
		setLayout(new BorderLayout());//handles placement of components
		add(label,BorderLayout.CENTER);//add the label to the biggest section
		add(clicker,BorderLayout.SOUTH);//put the button underneath it
		label.setPreferredSize(new Dimension(300,100));//nice big label
		label.setHorizontalAlignment(JLabel.CENTER);//text not up against the side
		pack();//fix layout
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);//stop the program on "X"
		setVisible(true);//show it
	}
	public static void main(String[] args){
		SwingUtilities.invokeLater( //Swing UI updates should not happen on the main thread
			() -> new Clicks() //call the constructor where all the magic happens
		);
	}
}

```

### java_code_2.txt
```java
//Aamrun, 11th July 2022

int labelLeft = 100, labelTop = 100, labelWidth = 440, labelHeight = 100;

int labelTextLeft = 150, labelTextTop = 150;

int buttonLeft = 170, buttonTop = 230, buttonWidth = 300, buttonHeight = 100;

boolean hasBeenClicked = false;

int clicks = 0;


void setup(){
  size(640,480);
  fill(255);
  rect(labelLeft,labelTop,labelWidth,labelHeight);
  fill(0);
  textSize(30);
  text("There have been no clicks yet",labelTextLeft,labelTextTop);
  fill(#c0c0c0);
  rect(buttonLeft,buttonTop,buttonWidth,buttonHeight);
  fill(0);
  text("Click Me !", buttonLeft + 50,buttonTop + 50);
}

void mousePressed(){
  if(mouseX > buttonLeft && mouseX < buttonLeft + buttonWidth
      && mouseY > buttonTop && mouseY < buttonTop + buttonHeight){
        hasBeenClicked = true;
        clicks++;
      }
}

void draw(){
  if(hasBeenClicked == true){
    fill(255);
    rect(labelLeft,labelTop,labelWidth,labelHeight);
    fill(0);
    textSize(30);
    text("Clicks : " + str(clicks),labelTextLeft,labelTextTop);
  }
}

```

## Python Code
### python_code_1.txt
```python
from functools import partial
import tkinter as tk

def on_click(label: tk.Label,
             counter: tk.IntVar) -> None:
    counter.set(counter.get() + 1)
    label["text"] = f"Number of clicks: {counter.get()}"

def main():
    window = tk.Tk()
    window.geometry("200x50+100+100")
    label = tk.Label(master=window,
                     text="There have been no clicks yet")
    label.pack()
    counter = tk.IntVar()
    update_counter = partial(on_click,
                             label=label,
                             counter=counter)
    button = tk.Button(master=window,
                       text="click me",
                       command=update_counter)
    button.pack()
    window.mainloop()

if __name__ == '__main__':
    main()

```

### python_code_2.txt
```python
import tkinter as tk

class ClickCounter(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        tk.Pack.config(self)
        self.label = tk.Label(self, text='There have been no clicks yet')
        self.label.pack()
        self.button = tk.Button(self,
                                text='click me',
                                command=self.click)
        self.button.pack()
        self.count = 0

    def click(self):
        self.count += 1
        self.label['text'] = f'Number of clicks: {self.count}'


if __name__ == "__main__":
    ClickCounter().mainloop()

```

### python_code_3.txt
```python
from functools import partial
from itertools import count

from PyQt5.QtWidgets import (QApplication,
                             QLabel,
                             QPushButton,
                             QWidget)
from PyQt5.QtCore import QRect

LABEL_GEOMETRY = QRect(0, 15, 200, 25)
BUTTON_GEOMETRY = QRect(50, 50, 100, 25)


def on_click(_, label, counter=count(1)):
    label.setText(f"Number of clicks: {next(counter)}")


def main():
    application = QApplication([])
    window = QWidget()
    label = QLabel(text="There have been no clicks yet",
                   parent=window)
    label.setGeometry(LABEL_GEOMETRY)
    button = QPushButton(text="click me",
                         parent=window)
    button.setGeometry(BUTTON_GEOMETRY)
    update_counter = partial(on_click,
                             label=label)
    button.clicked.connect(update_counter)
    window.show()
    application.lastWindowClosed.connect(window.close)
    application.exec_()


if __name__ == '__main__':
    main()

```

### python_code_4.txt
```python
import wx


class ClickCounter(wx.Frame):
    def __init__(self):
        super().__init__(parent=None)
        self.count = 0
        self.button = wx.Button(parent=self,
                                label="Click me!")
        self.label = wx.StaticText(parent=self,
                                   label="There have been no clicks yet")
        self.Bind(event=wx.EVT_BUTTON,
                  handler=self.click,
                  source=self.button)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(window=self.button,
                       proportion=1,
                       flag=wx.EXPAND)
        self.sizer.Add(window=self.label,
                       proportion=1,
                       flag=wx.EXPAND)
        self.SetSizer(self.sizer)
        self.sizer.Fit(self)

    def click(self, _):
        self.count += 1
        self.label.SetLabel(f"Count: {self.count}")


if __name__ == '__main__':
    app = wx.App()
    frame = ClickCounter()
    frame.Show()
    app.MainLoop()

```

