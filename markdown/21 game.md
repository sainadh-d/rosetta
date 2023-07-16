# 21 game

## Task Link
[Rosetta Code - 21 game](https://rosettacode.org/wiki/21_game)

## Java Code
### java_code_1.txt
```java
import java.util.Random;
import java.util.Scanner;

public class TwentyOneGame {

    public static void main(String[] args) {
        new TwentyOneGame().run(true, 21, new int[] {1, 2, 3});
    }
    
    public void run(boolean computerPlay, int max, int[] valid) {
        String comma = "";
        for ( int i = 0 ; i < valid.length ; i++ ) {
            comma += valid[i];
            if ( i < valid.length - 2 && valid.length >= 3 ) {
                comma += ", ";
            }
            if ( i == valid.length - 2 ) {
                comma += " or ";
            }
        }
        System.out.printf("The %d game.%nEach player chooses to add %s to a running total.%n" + 
                "The player whose turn it is when the total reaches %d will win the game.%n" + 
                "Winner of the game starts the next game.  Enter q to quit.%n%n", max, comma, max);
        int cGames = 0;
        int hGames = 0;
        boolean anotherGame = true;
        try (Scanner scanner = new Scanner(System.in);) {
            while ( anotherGame ) {
                Random r = new Random();
                int round = 0;
                int total = 0;
                System.out.printf("Start game %d%n", hGames + cGames + 1);
                DONE:
                    while ( true ) {
                        round++;
                        System.out.printf("ROUND %d:%n%n", round);
                        for ( int play = 0 ; play < 2 ; play++ ) {
                            if ( computerPlay ) {
                                int guess = 0;
                                //  try find one equal
                                for ( int test : valid ) {
                                    if ( total + test == max ) {
                                        guess = test;
                                        break;
                                    }
                                }
                                //  try find one greater than
                                if ( guess == 0 ) {
                                    for ( int test : valid ) {
                                        if ( total + test >= max ) {
                                            guess = test;
                                            break;
                                        }
                                    }
                                }
                                if ( guess == 0 ) {
                                    guess = valid[r.nextInt(valid.length)];
                                }
                                total += guess;
                                System.out.printf("The computer chooses %d%n", guess);
                                System.out.printf("Running total is now %d%n%n", total);
                                if ( total >= max ) {
                                    break DONE;
                                }
                            }
                            else {
                                while ( true ) {
                                    System.out.printf("Your choice among %s: ", comma);
                                    String line = scanner.nextLine();
                                    if ( line.matches("^[qQ].*") ) {
                                        System.out.printf("Computer wins %d game%s, human wins %d game%s.  One game incomplete.%nQuitting.%n", cGames, cGames == 1 ? "" : "s", hGames, hGames == 1 ? "" : "s");
                                        return;
                                    }
                                    try {
                                        int input = Integer.parseInt(line);
                                        boolean inputOk = false;
                                        for ( int test : valid ) {
                                            if ( input == test ) {
                                                inputOk = true;
                                                break;
                                            }
                                        }
                                        if ( inputOk ) {
                                            total += input;
                                            System.out.printf("Running total is now %d%n%n", total);
                                            if ( total >= max ) {
                                                break DONE;
                                            }
                                            break;
                                        }
                                        else {
                                            System.out.printf("Invalid input - must be a number among %s.  Try again.%n", comma);
                                        }
                                    }
                                    catch (NumberFormatException e) {
                                        System.out.printf("Invalid input - must be a number among %s.  Try again.%n", comma);
                                    }
                                }
                            }
                            computerPlay = !computerPlay;
                        }
                    }
                String win;
                if ( computerPlay ) {
                    win = "Computer wins!!";
                    cGames++;
                }
                else {
                    win = "You win and probably had help from another computer!!";
                    hGames++;
                }
                System.out.printf("%s%n", win);
                System.out.printf("Computer wins %d game%s, human wins %d game%s%n%n", cGames, cGames == 1 ? "" : "s", hGames, hGames == 1 ? "" : "s");
                while ( true ) {
                    System.out.printf("Another game (y/n)? ");
                    String line = scanner.nextLine();
                    if ( line.matches("^[yY]$") ) {
                        //  OK
                        System.out.printf("%n");
                        break;
                    }
                    else if ( line.matches("^[nN]$") ) {
                        anotherGame = false;
                        System.out.printf("Quitting.%n");
                        break;
                    }
                    else {
                        System.out.printf("Invalid input - must be a y or n.  Try again.%n");
                    }
                }
            }
        }
    }

}

```

## Python Code
### python_code_1.txt
```python
from random import randint
def start():
	game_count=0
	print("Enter q to quit at any time.\nThe computer will choose first.\nRunning total is now {}".format(game_count))
	roundno=1
	while game_count<21:
		print("\nROUND {}: \n".format(roundno))
		t = select_count(game_count)
		game_count = game_count+t
		print("Running total is now {}\n".format(game_count))
		if game_count>=21:
			print("So, commiserations, the computer has won!")
			return 0
		t = request_count()
		if not t:
			print('OK,quitting the game')
			return -1
		game_count = game_count+t
		print("Running total is now {}\n".format(game_count))
		if game_count>=21:
			print("So, congratulations, you've won!")
			return 1
		roundno+=1

def select_count(game_count):
	'''selects a random number if the game_count is less than 18. otherwise chooses the winning number'''
	if game_count<18:
		t= randint(1,3)
	else:
		t = 21-game_count
	print("The computer chooses {}".format(t))
	return t

def request_count():
	'''request user input between 1,2 and 3. It will continue till either quit(q) or one of those numbers is requested.'''
	t=""
	while True:
		try:
			t = raw_input('Your choice 1 to 3 :')
			if int(t) in [1,2,3]:
				return int(t)
			else:
				print("Out of range, try again")
		except:
			if t=="q":
				return None
			else:
				print("Invalid Entry, try again")

c=0
m=0
r=True
while r:
	o = start()
	if o==-1:
		break
	else:
		c+=1 if o==0 else 0
		m+=1 if o==1 else 0
	print("Computer wins {0} game, human wins {1} games".format(c,m))
	t = raw_input("Another game?(press y to continue):")
	r = (t=="y")

```

### python_code_2.txt
```python
''' Python 3.6.5 code using Tkinter graphical user interface.
    Starting player chosen randomly. ''' 
from tkinter import *
from tkinter import messagebox
import random

# ************************************************

class Game:
    def __init__(self, gw):
        self.window = gw
        self.won = 0
        self.lost = 0
        self.score = 0
        self.puter_turn = None
        self.var123 = IntVar()
        self.varsub = IntVar()

        # top frame:
        self.top_fr = Frame(gw,
                            width=600,
                            height=100,
                            bg='dodger blue')
        self.top_fr.pack(fill=X)

        self.hdg = Label(self.top_fr,
                         text='  21 Game  ',
                         font='arial 22 bold',
                         fg='navy',
                         bg='lemon chiffon')
        self.hdg.place(relx=0.5, rely=0.5,
                       anchor=CENTER)

        self.play_btn = Button(self.top_fr,
                               text='Play\nGame',
                               bd=5,
                               bg='navy',
                               fg='lemon chiffon',
                               font='arial 12 bold',
                               command=self.play_game)
        self.play_btn.place(relx=0.92, rely=0.5,
                            anchor=E)

        self.quit_btn = Button(self.top_fr,
                               text='Quit\nGame',
                               bd=5,
                               bg='navy',
                               fg='lemon chiffon',
                               font='arial 12 bold',
                               command=self.quit_game)
        self.quit_btn.place(relx=0.07, rely=0.5,
                            anchor=W)

        # bottom frame:
        self.btm_fr = Frame(gw,
                            width=600,
                            height=500,
                            bg='lemon chiffon')
        self.btm_fr.pack(fill=X)

        self.msg = Label(self.btm_fr,
                         text="(Click 'Play' or 'Quit')",
                         font='arial 16 bold',
                         fg='navy',
                         bg='lemon chiffon')
        self.msg.place(relx=0.5, rely=0.1,
                       anchor=CENTER)

        self.hdg = Label(self.btm_fr,
                         text="Scoreboard",
                         font='arial 16 bold',
                         fg='navy',
                         bg='lemon chiffon')
        self.hdg.place(relx=0.5, rely=0.2,
                       anchor=CENTER)

        self.score_msg = Label(self.btm_fr,
                               text="0",
                               font='arial 16 bold',
                               fg='navy',
                               bg='dodger blue',
                               width=8)
        
        self.score_msg.place(relx=0.5, rely=0.27,
                             anchor=CENTER)

        self.ch_fr = LabelFrame(self.btm_fr,
                                text='Choose a number',
                                bg='dodger blue',
                                fg='navy',
                                bd=8,
                                relief=RIDGE,
                                font='arial 16 bold')
        self.ch_fr.place(relx=0.5, rely=0.5,
                         anchor=CENTER)

        self.radio1 = Radiobutton(self.ch_fr,
                                  text='1',
                                  state='disabled',
                                  font='arial 16 bold',
                                  fg='navy',
                                  bg='dodger blue',
                                  variable=self.var123,
                                  value=1)
        self.radio1.pack()

        self.radio2 = Radiobutton(self.ch_fr,
                                  text='2',
                                  state='disabled',
                                  font='arial 16 bold',
                                  fg='navy', 
                                  bg='dodger blue',
                                  variable=self.var123,
                                  value=2)
        self.radio2.pack()

        self.radio3 = Radiobutton(self.ch_fr,
                                  text='3',
                                  state='disabled',
                                  font='arial 16 bold ',
                                  fg='navy', 
                                  bg='dodger blue',
                                  variable=self.var123,
                                  value=3)
        self.radio3.pack()

        self.submit_btn = Button(self.btm_fr,
                                 text='SUBMIT',
                                 state='disabled',
                                 bd=5,
                                 bg='navy',
                                 fg='lemon chiffon',
                                 font='arial 12 bold',
                                 command=self.submit)
        self.submit_btn.place(relx=0.5, rely=0.75,
                              anchor=CENTER)

        self.won_lbl = Label(self.btm_fr,
                             text="Won: 0",
                             font='arial 16 bold',
                             fg='navy',
                             bg='lemon chiffon')
        self.won_lbl.place(relx=0.85, rely=0.88,
                           anchor=W)

        self.lost_lbl = Label(self.btm_fr,
                              text="Lost: 0",
                              font='arial 16 bold',
                              fg='navy',
                              bg='lemon chiffon')
        self.lost_lbl.place(relx=0.85, rely=0.93,
                            anchor=W)

    # play one game:    
    def play_game(self):
        self.play_btn.config(state='disabled')
        # pick who goes first randomly:
        self.puter_turn = random.choice([True, False])
        self.score = 0
        self.score_msg.config(text=self.score)
        if not self.puter_turn:
            m = 'your turn'
            self.msg.config(text=m)
        # alternate turns until 21 is reached:
        while self.score != 21:
            if self.puter_turn:
                self.puter_plays()
            else:
                self.user_plays()
            self.puter_turn = not self.puter_turn
        self.play_btn.config(state='normal')
        return

    # computer picks a number:
    def puter_plays(self):
        if self.score == 20:
            x = 1
        elif self.score == 19:
                x = random.choice([1, 2])
        else:
            x = random.choice([1, 2, 3])
        self.score += x
        self.score_msg.config(text=self.score)
        if self.score == 21:
            m = 'Computer won!'
            self.lost += 1
            self.lost_lbl.config(text='Lost: ' + str(self.lost))
        else:
            m = 'Computer chose ' + str(x) + ', your turn'
        self.msg.config(text=m)
        return

    # user picks a number:
    def user_plays(self):
        self.set_user_state('normal')
        while True:
            # wait for submit button to be pressed:
            self.submit_btn.wait_variable(self.varsub)
            x = self.var123.get()
            if x + self.score > 21:
                m = 'Score cannot exceed 21, try again'
                messagebox.showerror('Error', m)
            elif x not in (1,2,3):
                m = 'No selection made'
                messagebox.showerror('Error', m)
            else:
                break
        self.score += x
        if self.score == 21:
            m = 'You won!'
            self.msg.config(text=m)
            self.score_msg.config(text=self.score)
            self.won += 1
            self.won_lbl.config(text='Won: ' + str(self.won))
        # reset and disable radio buttons:   
        self.var123.set(0)  
        self.set_user_state('disabled')                     
        return

    # set radio buttons to 'disabled' or 'normal':
    def set_user_state(self, state):
        self.radio1.config(state=state)
        self.radio2.config(state=state)
        self.radio3.config(state=state)
        self.submit_btn.config(state=state)
        return
        
                            
    def quit_game(self):
        self.window.destroy()

    # indicate that submit button was pressed:
    def submit(self):
        self.varsub.set(0)

# ************************************************

root = Tk()
root.title('21 Game')
root.geometry('600x600+100+50')
root.resizable(False, False)
g = Game(root)
root.mainloop()

```

