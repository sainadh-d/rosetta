# GUI component interaction

## Task Link
[Rosetta Code - GUI component interaction](https://rosettacode.org/wiki/GUI_component_interaction)

## Java Code
### java_code_1.txt
```java
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class Interact extends JFrame{
	final JTextField numberField;
	final JButton incButton, randButton;
	
	public Interact(){
		//stop the GUI threads when the user hits the X button
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
		
		numberField = new JTextField();
		incButton = new JButton("Increment");
		randButton = new JButton("Random");
		
		numberField.setText("0");//start at 0
		
		//listen for button presses in the text field
		numberField.addKeyListener(new KeyListener(){
			@Override
			public void keyTyped(KeyEvent e) {
				//if the entered character is not a digit
				if(!Character.isDigit(e.getKeyChar())){
					//eat the event (i.e. stop it from being processed)
					e.consume();
				}
			}
			@Override
			public void keyReleased(KeyEvent e){}
			@Override
			public void keyPressed(KeyEvent e){}
		});
		
		//listen for button clicks on the increment button
		incButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent e) {
				String text = numberField.getText();
				if(text.isEmpty()){
					numberField.setText("1");
				}else{
					numberField.setText((Long.valueOf(text) + 1) + "");
				}
			}
		});
		
		//listen for button clicks on the random button
		randButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent e) {
				//show a dialog and if they answer "Yes"
				if(JOptionPane.showConfirmDialog(null, "Are you sure?") ==
					JOptionPane.YES_OPTION){
					//set the text field text to a random positive long
					numberField.setText(Long.toString((long)(Math.random() 
							* Long.MAX_VALUE)));
				}
			}
		});
		
		//arrange the components in a grid with 2 rows and 1 column
		setLayout(new GridLayout(2, 1));
		
		//a secondary panel for arranging both buttons in one grid space in the window
		JPanel buttonPanel = new JPanel();
		
		//the buttons are in a grid with 1 row and 2 columns
		buttonPanel.setLayout(new GridLayout(1, 2));
		//add the buttons
		buttonPanel.add(incButton);
		buttonPanel.add(randButton);
		
		//put the number field on top of the buttons
		add(numberField);
		add(buttonPanel);
		//size the window appropriately
		pack();
		
	}

	public static void main(String[] args){
		new Interact().setVisible(true);
	}
}

```

### java_code_2.txt
```java
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

public interface FunctionalKeyListener extends KeyListener {
  @Override
  public default void keyPressed(KeyEvent event) {}
  @Override
  public default void keyTyped(KeyEvent event) {}
  @Override
  public default void keyReleased(KeyEvent event) {}

  @FunctionalInterface
  public static interface Pressed extends FunctionalKeyListener {
    @Override
    public void keyPressed(KeyEvent event);
  }

  @FunctionalInterface
  public static interface Typed extends FunctionalKeyListener {
    @Override
    public void keyTyped(KeyEvent event);
  }

  @FunctionalInterface
  public static interface Released extends FunctionalKeyListener {
    @Override
    public void keyReleased(KeyEvent event);
  }
}

```

### java_code_3.txt
```java
import java.awt.GridLayout;
import java.awt.event.ActionEvent;
import java.awt.event.KeyEvent;
import java.util.function.Consumer;
import java.util.function.Predicate;
import java.util.stream.Stream;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;
import javax.swing.JPanel;
import javax.swing.JTextField;

public interface Interact {
  public static final JFrame FRAME = new JFrame();
  public static final JTextField FIELD = new JTextField();
  public static final JPanel PANEL = new JPanel();
  
  public static void setDefaultCloseOperation(JFrame frame) {
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  }

  public static void setText(JTextField field) {
    field.setText("0");
  }

  public static void setEditable(JTextField field) {
    field.setEditable(false);
  }

  public static boolean isDigitKeyChar(KeyEvent event) {
    return !Character.isDigit(event.getKeyChar());
  }

  public static void keyTyped(KeyEvent event) {
    Stream.of(event)
      .parallel()
      .filter(Interact::isDigitKeyChar)
      .forEach(KeyEvent::consume)
    ;
  }

  public static void addKeyListener(JTextField field) {
    field.addKeyListener((FunctionalKeyListener.Typed) Interact::keyTyped);
  }

  public static String mapText(String text) {
    return text.isEmpty()
      ? "1"
      : String.valueOf(Long.valueOf(text) + 1)
    ;
  }

  public static void actionPerformedOnIncrementButton(ActionEvent event) {
    Stream.of(FIELD)
      .parallel()
      .map(JTextField::getText)
      .map(Interact::mapText)
      .forEach(FIELD::setText)
    ;
  }

  public static void addActionListenerToIncrementButton(JButton button) {
    button.addActionListener(Interact::actionPerformedOnIncrementButton);
  }

  public static void addIncrementButton(JPanel panel) {
    Stream.of("Increment")
      .parallel()
      .map(JButton::new)
      .peek(Interact::addActionListenerToIncrementButton)
      .forEach(panel::add)
    ;
  }

  public static int showConfirmDialog(String question) {
    return JOptionPane.showConfirmDialog(null, question);
  }

  public static void setFieldText(int integer) {
    FIELD.setText(
      String.valueOf(
        (long) (Math.random() * Long.MAX_VALUE))
      )
    ;
  }

  public static void actionPerformedOnRandomButton(ActionEvent event) {
    Stream.of("Are you sure?")
      .parallel()
      .map(Interact::showConfirmDialog)
      .filter(Predicate.isEqual(JOptionPane.YES_OPTION))
      .forEach(Interact::setFieldText)
    ;
  }

  public static void addActionListenerToRandomButton(JButton button) {
    button.addActionListener(Interact::actionPerformedOnRandomButton);
  }

  public static void addRandomButton(JPanel panel) {
    Stream.of("Random")
      .parallel()
      .map(JButton::new)
      .peek(Interact::addActionListenerToRandomButton)
      .forEach(panel::add)
    ;
  }

  public static void acceptField(Consumer<JTextField> consumer) {
    consumer.accept(FIELD);
  }

  public static void prepareField(JTextField field) {
    Stream.<Consumer<JTextField>>of(
      Interact::setEditable,
      Interact::setText,
      Interact::addKeyListener
    )
      .parallel()
      .forEach(Interact::acceptField)
    ;
  }

  public static void addField(JFrame frame) {
    Stream.of(FIELD)
      .parallel()
      .peek(Interact::prepareField)
      .forEach(frame::add)
    ;
  }

  public static void acceptPanel(Consumer<JPanel> consumer) {
    consumer.accept(PANEL);
  }

  public static void processPanel(JPanel panel) {
    Stream.<Consumer<JPanel>>of(
      Interact::setLayout,
      Interact::addIncrementButton,
      Interact::addRandomButton
    )
      .parallel()
      .forEach(Interact::acceptPanel)
    ;
  }

  public static void addPanel(JFrame frame) {
    Stream.of(PANEL)
      .parallel()
      .peek(Interact::processPanel)
      .forEach(frame::add)
    ;
  }

  public static void setLayout(JFrame frame) {
    frame.setLayout(new GridLayout(2, 1));
  }

  public static void setLayout(JPanel panel) {
    panel.setLayout(new GridLayout(1, 2));
  }

  public static void setVisible(JFrame frame) {
    frame.setVisible(true);
  }

  public static void acceptFrame(Consumer<JFrame> consumer) {
    consumer.accept(FRAME);
  }

  public static void processField(JFrame frame) {
    Stream.<Consumer<JFrame>>of(
      Interact::setDefaultCloseOperation,
      Interact::setLayout,
      Interact::addField,
      Interact::addPanel,
      Interact::setVisible
    )
      .parallel()
      .forEach(Interact::acceptFrame)
    ;
  }
  
  public static void main(String... arguments) {
    Stream.of(FRAME)
      .parallel()
      .peek(Interact::processField)
      .forEach(JFrame::pack)
    ;
  }
}

```

## Python Code
### python_code_1.txt
```python
import random, tkMessageBox
from Tkinter import *
window = Tk()
window.geometry("300x50+100+100")
options = { "padx":5, "pady":5}
s=StringVar()
s.set(1)
def increase():
    s.set(int(s.get())+1)
def rand():
    if tkMessageBox.askyesno("Confirmation", "Reset to random value ?"):
        s.set(random.randrange(0,5000))
def update(e):
    if not e.char.isdigit():
        tkMessageBox.showerror('Error', 'Invalid input !') 
        return "break"
e = Entry(text=s)
e.grid(column=0, row=0, **options)
e.bind('<Key>', update)
b1 = Button(text="Increase", command=increase, **options )
b1.grid(column=1, row=0, **options)
b2 = Button(text="Random", command=rand, **options)
b2.grid(column=2, row=0, **options)
mainloop()

```

### python_code_2.txt
```python
import random, tkinter.messagebox
from tkinter import *

window = Tk()
window.geometry("330x50+100+100")
options = { "padx":5, "pady":5}
s=StringVar()
s.set(1)

def increase():
    s.set(int(s.get())+1)
def rand():
    if messagebox.askyesno("Confirmation", "Reset to random value ?"):
        s.set(random.randrange(0,5000))
def update(e):
    if not e.char.isdigit():
        messagebox.showerror('Error', 'Invalid input !') 
        return "break"

e = Entry(text=s)
e.grid(column=0, row=0, **options)
e.bind('<Key>', update)

b1 = Button(text="Increase", command=increase, **options )
b1.grid(column=1, row=0, **options)
b2 = Button(text="Random", command=rand, **options)
b2.grid(column=2, row=0, **options)

mainloop()

```

### python_code_3.txt
```python
import random
from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.counter = 0
        self.contents = StringVar()
        self.contents.set(str(self.counter))
        self.pack(expand=True, fill='both', padx=10, pady=15)
        self.create_widgets()

    def increment(self, *args):
        self.counter += 1
        self.update_entry()

    def random(self):
        if tkMessageBox.askyesno("Confirmation", "Reset to random value ?"):
            self.counter = random.randint(0, 5000)
            self.update_entry()

    def entry_updated(self, event, *args):
        if not event.char:
            return 'break'
        if not event.char.isdigit():
            tkMessageBox.showerror('Error', 'Invalid input !')
            return 'break'
        self.counter = int('%s%s' % (self.contents.get(), event.char))

    def update_entry(self):
        self.contents.set(str(self.counter))
        self.entry['textvariable'] = self.contents

    def create_widgets(self):
        options = {'expand': True, 'fill': 'x', 'side': 'left', 'padx': 5}
        self.entry = Entry(self)
        self.entry.bind('<Key>', self.entry_updated)
        self.entry.pack(**options)
        self.update_entry()
        self.increment_button = Button(self, text='Increment', command=self.increment)
        self.increment_button.pack(**options)
        self.random_button = Button(self, text='Random', command=self.random)
        self.random_button.pack(**options)

if __name__ == '__main__':
    root = Tk()
    try:
        app = Application(master=root)
        app.master.title("Rosetta code")
        app.mainloop()
    except KeyboardInterrupt:
        root.destroy()

```

