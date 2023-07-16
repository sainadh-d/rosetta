# GUI enabling/disabling of controls

## Task Link
[Rosetta Code - GUI enabling/disabling of controls](https://rosettacode.org/wiki/GUI_enabling/disabling_of_controls)

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
import javax.swing.JPanel;
import javax.swing.JTextField;
import javax.swing.SwingUtilities;

public class Interact extends JFrame{
	final JTextField numberField;
	final JButton incButton, decButton;
	
	public Interact(){
		//stop the GUI threads when the user hits the X button
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); 
		
		numberField = new JTextField();
		incButton = new JButton("Increment");
		decButton = new JButton("Decrement");
		
		numberField.setText("0");//start at 0
		decButton.setEnabled(false);//we're already at 0
		
		//listen for button presses in the text field
		numberField.addKeyListener(new KeyListener(){
			@Override
			public void keyTyped(KeyEvent e) {
				//if the entered character is not a digit
				if(!Character.isDigit(e.getKeyChar())){
					//eat the event (i.e. stop it from being processed)
					e.consume();
				}else if(Character.isDigit(e.getKeyChar())){
					//This method is executed from the event thread and updating the GUI
					//from there doesn't always work. invokeLater will ensure that the
					//GUI is updated
					SwingUtilities.invokeLater(new Runnable() {
						@Override
						public void run() {
							String text = numberField.getText();
							if(text.isEmpty()){//default to 0 when all text is erased
								numberField.setText("0");
								decButton.setEnabled(false);
								incButton.setEnabled(true);
								return;
							}
							if(Long.valueOf(text) <= 0){
								decButton.setEnabled(false);
								incButton.setEnabled(true);
							}else if(Long.valueOf(text) >= 10){
								incButton.setEnabled(false);
								decButton.setEnabled(true);
							}else{
								incButton.setEnabled(true);
								decButton.setEnabled(true);
							}
						}
					});
				}
			}
			@Override
			public void keyReleased(KeyEvent e){}
			@Override
			public void keyPressed(KeyEvent e){
				//backspace and delete don't register in keyTyped because they don't
				//display a Unicode character, so they must be handled here
				if(e.getKeyCode() == KeyEvent.VK_BACK_SPACE ||
						e.getKeyCode() == KeyEvent.VK_DELETE){
					SwingUtilities.invokeLater(new Runnable() {
						@Override
						public void run() {
							String text = numberField.getText();
							if(text.isEmpty()){
								numberField.setText("0");
								decButton.setEnabled(false);
								incButton.setEnabled(true);
								return;
							}
							if(Long.valueOf(text) <= 0){
								decButton.setEnabled(false);
								incButton.setEnabled(true);
							}else if(Long.valueOf(text) >= 10){
								incButton.setEnabled(false);
								decButton.setEnabled(true);
							}else{
								incButton.setEnabled(true);
								decButton.setEnabled(true);
							}
						}
					});
				}
			}
		});
		
		//listen for button clicks on the increment button
		incButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent e) {
				String text = numberField.getText();
				numberField.setText((Long.valueOf(text) + 1) + "");
				if(Long.valueOf(text) + 1 >= 10){
					incButton.setEnabled(false);
				}
				
				if(Long.valueOf(text) + 1 > 0){
					decButton.setEnabled(true);
				}
			}
		});
		
		//listen for button clicks on the random button
		decButton.addActionListener(new ActionListener(){
			@Override
			public void actionPerformed(ActionEvent e) {
				String text = numberField.getText();
				numberField.setText((Long.valueOf(text) - 1) + "");
				if(Long.valueOf(text) - 1 <= 0){
					decButton.setEnabled(false);
				}
				
				if(Long.valueOf(text) - 1 < 10){
					incButton.setEnabled(true);
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
		buttonPanel.add(decButton);
		
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
import javafx.application.Application;
import javafx.beans.property.LongProperty;
import javafx.beans.property.SimpleLongProperty;
import javafx.scene.Scene;
import javafx.scene.control.Button;
import javafx.scene.control.TextField;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.stage.Stage;
import javafx.util.converter.NumberStringConverter;

public class InteractFX extends Application {

    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void start(Stage stage) throws Exception {

        TextField input = new TextField("0"){
            // only accept numbers as input
            @Override public void replaceText(int start, int end, String text) {
                if (text.matches("[0-9]*")) {
                    super.replaceText(start, end, text);
                }
            }

            // only accept numbers on copy+paste
            @Override public void replaceSelection(String text) {
                if (text.matches("[0-9]*")) {
                    super.replaceSelection(text);
                }
            }
        };

        // when the textfield is empty, replace text with "0"
        input.textProperty().addListener((observable, oldValue, newValue)->{
            if(newValue == null || newValue.trim().isEmpty()){
                input.setText("0");
            }
        });


        // get a bi-directional bound long-property of the input value
        LongProperty inputValue = new SimpleLongProperty();
        input.textProperty().bindBidirectional(inputValue, new NumberStringConverter());

        // textfield is disabled when the current value is other than "0"
        input.disableProperty().bind(inputValue.isNotEqualTo(0));


        Button increment = new Button("Increment");
        increment.setOnAction(event-> inputValue.set(inputValue.get() + 1));

        // incr-button is disabled when input is >= 10
        increment.disableProperty().bind(inputValue.greaterThanOrEqualTo(10));

        
        Button decrement = new Button("Decrement");
        decrement.setOnAction(event-> inputValue.set(inputValue.get() - 1));

        // decrement button is disabled when input is <=0
        decrement.disableProperty().bind(inputValue.lessThanOrEqualTo(0));


        // layout
        VBox root = new VBox();
        root.getChildren().add(input);
        HBox buttons = new HBox();
        buttons.getChildren().addAll(increment,decrement);
        root.getChildren().add(buttons);

        stage.setScene(new Scene(root));
        stage.sizeToScene();
        stage.show();
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python3

import tkinter as tk

class MyForm(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack(expand=True, fill="both", padx=10, pady=10)
        self.master.title("Controls")
        self.setupUI()

    def setupUI(self):
        self.value_entry = tk.Entry(self, justify=tk.CENTER)
        self.value_entry.grid(row=0, column=0, columnspan=2,
                              padx=5, pady=5, sticky="nesw")
        self.value_entry.insert('end', '0')
        self.value_entry.bind("<KeyPress-Return>", self.eventHandler)

        self.decre_btn = tk.Button(self, text="Decrement", state=tk.DISABLED)
        self.decre_btn.grid(row=1, column=0, padx=5, pady=5)
        self.decre_btn.bind("<Button-1>", self.eventHandler)

        self.incre_btn = tk.Button(self, text="Increment")
        self.incre_btn.grid(row=1, column=1, padx=5, pady=5)
        self.incre_btn.bind("<Button-1>", self.eventHandler)

    def eventHandler(self, event):
        value = int(self.value_entry.get())
        if event.widget == self.value_entry:
            if value > 10:
                self.value_entry.delete("0", "end")
                self.value_entry.insert("end", "0")
            elif value == 10:
                self.value_entry.config(state=tk.DISABLED)
                self.incre_btn.config(state=tk.DISABLED)
                self.decre_btn.config(state=tk.NORMAL)
            elif value == 0:
                self.value_entry.config(state=tk.NORMAL)
                self.incre_btn.config(state=tk.NORMAL)
                self.decre_btn.config(state=tk.DISABLED)
            elif (value > 0) and (value < 10):
                self.value_entry.config(state=tk.DISABLED)
                self.incre_btn.config(state=tk.NORMAL)
                self.decre_btn.config(state=tk.NORMAL)
        else:
            if event.widget == self.incre_btn:
                if (value >= 0) and (value < 10):
                    value += 1
                    self.value_entry.config(state=tk.NORMAL)
                    self.value_entry.delete("0", "end")
                    self.value_entry.insert("end", str(value))
                if value > 0:
                    self.decre_btn.config(state=tk.NORMAL)
                    self.value_entry.config(state=tk.DISABLED)
                if value == 10:
                    self.incre_btn.config(state=tk.DISABLED)
            elif event.widget == self.decre_btn:
                if (value > 0) and (value <= 10):
                    value -= 1
                    self.value_entry.config(state=tk.NORMAL)
                    self.value_entry.delete("0", "end")
                    self.value_entry.insert("end", str(value))
                    self.value_entry.config(state=tk.DISABLED)
                if (value) < 10:
                    self.incre_btn.config(state=tk.NORMAL)
                if (value) == 0:
                    self.decre_btn.config(state=tk.DISABLED)
                    self.value_entry.config(state=tk.NORMAL)

def main():
    app = MyForm()
    app.mainloop()

if __name__ == "__main__":
    main()

```

