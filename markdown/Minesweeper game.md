# Minesweeper game

## Task Link
[Rosetta Code - Minesweeper game](https://rosettacode.org/wiki/Minesweeper_game)

## Java Code
### java_code_1.txt
```java
--------------------------------- START of Main.java ---------------------------------
//By xykmz. Enjoy!

import java.util.Scanner;

public class Main {

    static int intErrorTrap (int x, int y){
        
        int max, min;
        
        if (x < y) {
            min = x;
            max = y;
        } else {
            min = y;
            max = x;
        }
        
        int input;
        boolean loopEnd;
        
        do {
            
            System.out.println("Please enter an integer between " + min + " to " + max + ".");
            Scanner userInput = new Scanner(System.in); //Player inputs a guess
            
            try 
            {
                input = userInput.nextInt();
                
                if(input > max) //Input is too high
                {
                    loopEnd = false;
                    System.out.println("Input is invalid.");
                    return -1;
                }
                
                else if(input < min) //Input is too low
                {
                    loopEnd = false;
                    System.out.println("Input is invalid.");
                    return -1;
                }
                
                else //Input is within acceptable range
                {
                    loopEnd = true;
                    System.out.println(input + " is a valid input.");
                    return input;
    
                }
            }
            
            catch (Exception e)
            {
                loopEnd = false;
                userInput.next();
                System.out.println("Input is invalid.");
                return 0;
            }
        
        } while (loopEnd == false);
    }
    
    
    public static void main(String[] args) {
      
    	System.out.println ("Enter width.");
    	int x = intErrorTrap (0,60);
    	
    	System.out.println ("Enter height.");
    	int y = intErrorTrap (0,30);
    	
    	System.out.println ("Enter difficulty.");
    	int d = intErrorTrap (0,100);
 
        new Minesweeper(x, y, d); //Suggested: (60, 30, 15)
    }

}


//--------------------------------- END of Main.java ---------------------------------

//--------------------------------- START of Cell.java ---------------------------------



public class Cell{ //This entire class is quite self-explanatory. All we're really doing is setting booleans.
	
    private boolean isMine, isFlagged, isCovered;
    private int number;
 
    public Cell(){
        isMine = false;
        isFlagged = false;
        isCovered = true;
        number = 0;
    }
 
    public void flag(){
        isFlagged = true;
    }
 
    public void unflag(){
        isFlagged = false;
    }
    
    public void setMine(){
        isMine = true;
    }
 
    public boolean isMine(){
        return isMine;
    }
    
    public void reveal(){
        isCovered = false;
    }
 
    public void setNumber(int i){ //Set the number of the cell
        number = i;
    }
    
    public int getNumber(){ //Request the program for the number of the cell
        return number;
    }
 
    public boolean isFlagged(){
        return isFlagged;
    }
 
    public boolean isCovered(){
        return isCovered;
    }
 

}

//--------------------------------- END of Cell.java ---------------------------------

//--------------------------------- START of Board.java ---------------------------------

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JPanel;
 
public class Board extends JPanel{
	
    private static final long serialVersionUID = 1L; //Guarantees consistent serialVersionUID value across different java compiler implementations,
    												 //Auto-generated value might screw things up
   
    private Minesweeper mine;
    private Cell[][] cells;
 
 
    public void paintComponent(Graphics g){
    	
        cells = mine.getCells();
 
        for (int i = 0; i < mine.getx(); i++){
        	
            for (int j = 0; j < mine.gety(); j++){
            	
                Cell current = cells[i][j];
 
                
                //Flagged cells
                if (current.isFlagged()){
                	
                    if (current.isMine() && mine.isFinished()){
                    	
                        g.setColor(Color.ORANGE); //Let's the player know which mines they got right when the game is finished.
                        g.fillRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                        g.setColor(Color.BLACK);
 
                        g.drawLine(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                        g.drawLine(i * 20, j * 20 + 20, i * 20 + 20, j * 20);
                    }
                    else if (mine.isFinished()){ //Shows cells that the player incorrectly identified as mines.
                        g.setColor(Color.YELLOW);
                        g.fillRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                        g.setColor(Color.BLACK);
                    }
                    else{
                        g.setColor(Color.GREEN); //Flagging a mine.
                        g.fillRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                        g.setColor(Color.BLACK);
                    }
                }
                
                //Unflagged cells
                else if (current.isCovered()){ //Covered cells
                    g.setColor(Color.DARK_GRAY);
                    g.fillRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                    g.setColor(Color.BLACK);
                }
                else if (current.isMine()){ //Incorrect cells are shown when the game is over.=
                    g.setColor(Color.RED);
                    g.fillRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                    g.setColor(Color.BLACK);
                    g.drawLine(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                    g.drawLine(i * 20, j * 20 + 20, i * 20 + 20, j * 20);
                }
                else{ //Empty cells or numbered cells
                    g.setColor(Color.LIGHT_GRAY);
                    g.fillRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
                    g.setColor(Color.BLACK);
                }
                
                //The following part is very self explanatory - drawing the numbers.
                //Not very interesting work.
                //Not a fun time.
                //Rating: 0/10. Would not recommend.
                
                if (!current.isCovered()){
                    if (current.getNumber() == 1){
                        g.drawLine(i * 20 + 13, j * 20 + 5, i * 20 + 13, j * 20 + 9);    //3
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                    }
                    else if (current.getNumber() == 2){
                        g.drawLine(i * 20 + 8, j * 20 + 4, i * 20 + 12, j * 20 + 4);    //2
                        g.drawLine(i * 20 + 13, j * 20 + 5, i * 20 + 13, j * 20 + 9);    //3
                        g.drawLine(i * 20 + 8, j * 20 + 10, i * 20 + 12, j * 20 + 10);    //4
                        g.drawLine(i * 20 + 7, j * 20 + 11, i * 20 + 7, j * 20 + 15);    //5
                        g.drawLine(i * 20 + 8, j * 20 + 16, i * 20 + 12, j * 20 + 16);    //7
                    }
                    else if (current.getNumber() == 3){
                        g.drawLine(i * 20 + 8, j * 20 + 4, i * 20 + 12, j * 20 + 4);    //2
                        g.drawLine(i * 20 + 13, j * 20 + 5, i * 20 + 13, j * 20 + 9);    //3
                        g.drawLine(i * 20 + 8, j * 20 + 10, i * 20 + 12, j * 20 + 10);    //4
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                        g.drawLine(i * 20 + 8, j * 20 + 16, i * 20 + 12, j * 20 + 16);    //7
                    }
                    else if (current.getNumber() == 4){
                        g.drawLine(i * 20 + 7, j * 20 + 5, i * 20 + 7, j * 20 + 9);        //1
                        g.drawLine(i * 20 + 13, j * 20 + 5, i * 20 + 13, j * 20 + 9);    //3
                        g.drawLine(i * 20 + 8, j * 20 + 10, i * 20 + 12, j * 20 + 10);    //4
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                    }
                    else if (current.getNumber() == 5){
                        g.drawLine(i * 20 + 7, j * 20 + 5, i * 20 + 7, j * 20 + 9);        //1
                        g.drawLine(i * 20 + 8, j * 20 + 4, i * 20 + 12, j * 20 + 4);    //2
                        g.drawLine(i * 20 + 8, j * 20 + 10, i * 20 + 12, j * 20 + 10);    //4
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                        g.drawLine(i * 20 + 8, j * 20 + 16, i * 20 + 12, j * 20 + 16);    //7
                    }
                    else if (current.getNumber() == 6){
                        g.drawLine(i * 20 + 7, j * 20 + 5, i * 20 + 7, j * 20 + 9);        //1
                        g.drawLine(i * 20 + 8, j * 20 + 4, i * 20 + 12, j * 20 + 4);    //2
                        g.drawLine(i * 20 + 8, j * 20 + 10, i * 20 + 12, j * 20 + 10);    //4
                        g.drawLine(i * 20 + 7, j * 20 + 11, i * 20 + 7, j * 20 + 15);    //5
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                        g.drawLine(i * 20 + 8, j * 20 + 16, i * 20 + 12, j * 20 + 16);    //7
                    }
                    else if (current.getNumber() == 7){
                        g.drawLine(i * 20 + 8, j * 20 + 4, i * 20 + 12, j * 20 + 4);    //2
                        g.drawLine(i * 20 + 13, j * 20 + 5, i * 20 + 13, j * 20 + 9);    //3
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                    }
                    else if (current.getNumber() == 8){
                        g.drawLine(i * 20 + 7, j * 20 + 5, i * 20 + 7, j * 20 + 9);        //1
                        g.drawLine(i * 20 + 8, j * 20 + 4, i * 20 + 12, j * 20 + 4);    //2
                        g.drawLine(i * 20 + 13, j * 20 + 5, i * 20 + 13, j * 20 + 9);    //3
                        g.drawLine(i * 20 + 8, j * 20 + 10, i * 20 + 12, j * 20 + 10);    //4
                        g.drawLine(i * 20 + 7, j * 20 + 11, i * 20 + 7, j * 20 + 15);    //5
                        g.drawLine(i * 20 + 13, j * 20 + 11, i * 20 + 13, j * 20 + 15);    //6
                        g.drawLine(i * 20 + 8, j * 20 + 16, i * 20 + 12, j * 20 + 16);    //7
                    }
                }
                g.setColor(Color.BLACK);
                g.drawRect(i * 20, j * 20, i * 20 + 20, j * 20 + 20);
            }
        }
    }
    
    public Board(Minesweeper m){ //Creating a new game so we can draw a board for it
        mine = m;
        cells = mine.getCells();
 
        addMouseListener(new Actions(mine));
 
        setPreferredSize(new Dimension(mine.getx() * 20, mine.gety() * 20));
    }
    
}

//--------------------------------- END of Board.java ---------------------------------

//--------------------------------- START of Actions.java ---------------------------------

import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
 
public class Actions implements ActionListener, MouseListener{
	
    private Minesweeper mine;
    
    //These following four are not important. We simply tell the machine to pay no mind when mouse is pressed, released, etc.
    //If these weren't here the computer would freak out and panic over what to do because no instructions were given.
 
    public void mouseEntered(MouseEvent e){
    	 
    }
 
    public void mouseExited(MouseEvent e){
 
    }
 
    public void mousePressed(MouseEvent e){
 
    }
 
    public void mouseReleased(MouseEvent e){
 
    }
    
    //Where the fun begins
    
    public Actions(Minesweeper m){
    	
        mine = m;
    }
 
    //Any time an action is performed, redraw the board and keep it up to date.
    public void actionPerformed(ActionEvent e){
    	
        mine.reset();
 
        mine.refresh();
    }
 
    //Mouse clicky clicky
    public void mouseClicked(MouseEvent e){
    	
    	//Left click - opens mine
        if (e.getButton() == 1)
        {
            int x = e.getX() / 20;
            int y = e.getY() / 20;
 
            mine.select(x, y);
        }

        //Right click - marks mine
        if (e.getButton() == 3)
        {
            int x = e.getX() / 20;
            int y = e.getY() / 20;
 
            mine.mark(x, y);
        }
        
        
        mine.refresh(); //Gotta keep it fresh
    }
 
 
}

//--------------------------------- END of Actions.java ---------------------------------

//--------------------------------- START of Minesweeper.java ---------------------------------

import java.awt.BorderLayout;
import java.util.Random;
import javax.swing.JButton;
import javax.swing.JFrame;
import javax.swing.JOptionPane;

public class Minesweeper extends JFrame
{
    private static final long serialVersionUID = 1L;
    private int width, height;
    private int difficulty;
    private Cell[][] cells;
    private Board board;
    private JButton reset;
    private boolean finished;
 
    
    public void select(int x, int y){ //Select a mine on the board
    	
        if (cells[x][y].isFlagged()) //Is the mine flagged?
        	return;
        
        cells[x][y].reveal(); //Reveal the cell
        resetMarks(); //Reset marks and redraw board
        refresh();
 
        if (cells[x][y].isMine()) //If a mine is revealed, you lose.
        {
            lose();
        }
        else if (won()) //If the game has been won, you win. Hahahahahaha.
        {
            win();
        }
    }
    
    private void setNumbers(){ //For each cell, count the amount of mines in surrounding squares.
    	                       //Because the board is modeled as a 2D array, this is relatively easy - simply check the surrounding addresses for mines.
    						   //If there's a mine, add to the count.
    	
        for (int i = 0; i < width; i++){
        	
            for (int j = 0; j < height; j++){
            	
                int count = 0;
 
                if (i > 0 &&  j > 0 && cells[i - 1][j - 1].isMine()) 
                	count++;
                
                if (j > 0 && cells[i][j - 1].isMine()) 
                	count++;
                
                if (i < width - 1 && j > 0 && cells[i + 1][j - 1].isMine()) 
                	count++;
 
                if (i > 0 && cells[i - 1][j].isMine()) 
                	count++;
                
                if (i < width - 1 && cells[i + 1][j].isMine()) 
                	count++;
 
                if (i > 0 && j < height - 1 && cells[i - 1][j + 1].isMine()) 
                	count++;
                
                if (j < height - 1 && cells[i] [j + 1].isMine()) 
                	count++;
                
                if (i < width - 1 && j < height - 1 && cells[i + 1][j + 1].isMine()) 
                	count++;
 
                cells[i][j].setNumber(count);
                
 
                if (cells[i][j].isMine())
                    cells[i][j].setNumber(-1);
                
 
                if (cells[i][j].getNumber() == 0)
                    cells[i][j].reveal();
                
            }
        }
 
        for (int i = 0; i < width; i++){ //This is for the beginning of the game.
        	                             //If the 8 cells around certain cell have no mines beside them (hence getNumber() = 0) beside them, this cell is empty.  
        	
            for (int j = 0; j < height; j++){
            	
                if (i > 0 && j > 0 && cells[i - 1][j - 1].getNumber() == 0) 
                	cells[i][j].reveal();
                
                if (j > 0 && cells[i][j - 1].getNumber() == 0) 
                	cells[i][j].reveal();
                
                if (i < width - 1 && j > 0 && cells[i + 1][j - 1].getNumber() == 0) 
                	cells[i][j].reveal();
 
                if (i > 0 && cells[i - 1][j].getNumber() == 0) 
                	cells[i][j].reveal();
                
                if (i < width - 1 && cells[i + 1][j].getNumber() == 0) 
                	cells[i][j].reveal();
 
                if (i > 0 && j < height - 1 && cells[i - 1][j + 1].getNumber() == 0) 
                	cells[i][j].reveal();
                
                if (j < height - 1 && cells[i][j + 1].getNumber() == 0) 
                	cells[i][j].reveal();
                
                if (i < width - 1 && j < height - 1 && cells[i + 1][j + 1].getNumber() == 0) 
                	cells[i][j].reveal();
            }
        }
    }
    
    public void mark(int x, int y){ //When a player wants to flag/unflag a cell
    	
        if (cells[x][y].isFlagged()) //If the cell is already flagged, unflag it.
        	cells[x][y].unflag();
        
        else if (cells[x][y].isCovered()) //If the cell has nothing on it and is covered, flag it.
        	cells[x][y].flag();
 
        resetMarks();
    }
 
    private void resetMarks(){ //If a cell is not covered, then it cannot be flagged.
    	                       //Every time a player does something, this should be called to redraw the board.
    	
        for (int i = 0; i < width; i++){
            for (int j = 0; j < height; j++){
            	
                if (!cells[i][j].isCovered()) 
                	cells[i][j].unflag();
                
            }
        }
    }
    
    public void reset(){ //Reset the positions of the mines on the board
    	                 //If randomly generated number from 0 to 100 is less than the chosen difficulty, a mine is placed down.
    	                 //This will somewhat accurately reflect the mine percentage that the user requested - the more cells, the more accurate.
    	
        Random random = new Random();
        finished = false;
 
        for (int i = 0; i < width; i++)  {
            for (int j = 0; j < height; j++)   {
            	
                Cell c = new Cell();
                cells[i][j] = c;
                int r = random.nextInt(100);
 
                if (r < difficulty)
                {
                    cells[i][j].setMine(); //Put down a mine.
                }
                
            }
        }
        setNumbers(); //Set the numbers after mines have been put down.
    }
 
    public int getx() {
        return width;
    }
 
    public int gety() {
        return height;
    }
 
    public Cell[][] getCells() {
        return cells;
    }

 
    public void refresh(){ //Refresh the drawing of the board
        board.repaint();
    }
 
    private void win(){ //Winning a game
        finished = true;
        for (int i = 0; i < width; i++)
        {
            for (int j = 0; j < height; j++)
            {
                cells[i][j].reveal();//Reveal all cells
                
                if (!cells[i][j].isMine()) 
                	cells[i][j].unflag();
            }
        }
 
        refresh();
        JOptionPane.showMessageDialog(null, "Congratulations! You won!"); //Tell the user they won. They probably deserve to know.
        reset();
    }
    
    private void lose(){ //Losing a game...basically the same as above.
        finished = true;
        for (int i = 0; i < width; i++)
        {
            for (int j = 0; j < height; j++)
            {
                if (!cells[i][j].isCovered()) 
                	cells[i][j].unflag();
                
                cells[i][j].reveal();
            }
        }
        refresh();
        JOptionPane.showMessageDialog(null, "GAME OVER."); //Dialogue window letting the user know that they lost.
        reset();
    }
 
 
    private boolean won(){ //Check if the game has been won
        for (int i = 0; i < width; i++){
            for (int j = 0; j < height; j++){
            	
                if (cells[i][j].isCovered() && !cells[i][j].isMine())
                {
                    return false;
                }
            }
        }
 
        return true; 
    } 
 
 
    public boolean isFinished(){ //Extremely self-explanatory.
        return finished;
    }
    
    public Minesweeper(int x, int y, int d){
    	
        width = x; //Width of the board
        height = y; //Height of the board
        difficulty = d; //Percentage of mines in the board
        cells = new Cell[width][height];
 
        reset(); //Set mines on the board
 
        board = new Board(this); //Create new board
        reset = new JButton("Reset"); //Reset button
 
        add(board, BorderLayout.CENTER); //Put board in the center
        add(reset, BorderLayout.SOUTH); //IT'S A BUTTON! AND IT WORKS! VERY COOL
 
        reset.addActionListener(new Actions(this)); //ActionListener to watch for mouse actions
 
        //GUI window settings
        setTitle("Minesweeper");
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setResizable(false);
        pack();
        setVisible(true);
    }
    
}


//--------------------------------- END of Minesweeper.java ---------------------------------

```

## Python Code
### python_code_1.txt
```python
'''
Minesweeper game.

    There is an n by m grid that has a random number of between 20% to 60%
    of randomly hidden mines that need to be found. 

    Positions in the grid are modified by entering their coordinates
    where the first coordinate is horizontal in the grid and the second
    vertical. The top left of the grid is position 1,1; the bottom right is
    at n,m.

    * The total number of mines to be found is shown at the beginning of the
    game.
    * Each mine occupies a single grid point, and its position is initially
    unknown to the player
    * The grid is shown as a rectangle of characters between moves.
    * You are initially shown all grids as obscured, by a single dot '.'
    * You may mark what you think is the position of a mine which will show
    as a '?'
    * You can mark what you think is free space by entering its coordinates.
    :*  If the point is free space then it is cleared, as are any adjacent
    points that are also free space- this is repeated recursively for
    subsequent adjacent free points unless that point is marked as a mine
    or is a mine.
    ::*   Points marked as a mine show as a '?'.
    ::*   Other free points show as an integer count of the number of adjacent
    true mines in its immediate neighbourhood, or as a single space ' ' if the
    free point is not adjacent to any true mines.
    * Of course you loose if you try to clear space that starts on a mine.
    * You win when you have correctly identified all mines.


    When prompted you may:
        Toggle where you think a mine is at position x, y:
          m <x> <y>
        Clear the grid starting at position x, y (and print the result):
          c <x> <y>
        Print the grid so far:
          p
        Resign
          r
    Resigning will first show the grid with an 'N' for unfound true mines, a
    'Y' for found true mines and a '?' for where you marked clear space as a
    mine 
      
'''


gridsize  = (6, 4)
minerange = (0.2, 0.6)


try:
    raw_input
except:
    raw_input = input
    
import random
from itertools import product
from pprint import pprint as pp


def gridandmines(gridsize=gridsize, minerange=minerange):
    xgrid, ygrid = gridsize
    minmines, maxmines = minerange
    minecount = xgrid * ygrid    
    minecount = random.randint(int(minecount*minmines), int(minecount*maxmines))
    grid = set(product(range(xgrid), range(ygrid)))
    mines = set(random.sample(grid, minecount))
    show = {xy:'.' for xy in grid}
    return grid, mines, show

def printgrid(show, gridsize=gridsize):
    xgrid, ygrid = gridsize
    grid = '\n'.join(''.join(show[(x,y)] for x in range(xgrid))
                     for y in range(ygrid))
    print( grid )

def resign(showgrid, mines, markedmines):
    for m in mines:
        showgrid[m] = 'Y' if m in markedmines else 'N'

def clear(x,y, showgrid, grid, mines, markedmines):
    if showgrid[(x, y)] == '.':
        xychar = str(sum(1
                         for xx in (x-1, x, x+1)
                         for yy in (y-1, y, y+1)
                         if (xx, yy) in mines ))
        if xychar == '0': xychar = '.'
        showgrid[(x,y)] = xychar
        for xx in (x-1, x, x+1):
            for yy in (y-1, y, y+1):
                xxyy = (xx, yy)
                if ( xxyy != (x, y)
                     and xxyy in grid
                     and xxyy not in mines | markedmines ):
                    clear(xx, yy, showgrid, grid, mines, markedmines)

if __name__ == '__main__':
    grid, mines, showgrid = gridandmines()
    markedmines = set([])
    print( __doc__ )
    print( '\nThere are %i true mines of fixed position in the grid\n' % len(mines) )
    printgrid(showgrid)
    while markedmines != mines:
        inp = raw_input('m x y/c x y/p/r: ').strip().split()
        if inp:
            if inp[0] == 'm':
                x, y = [int(i)-1 for i in inp[1:3]]
                if (x,y) in markedmines:
                    markedmines.remove((x,y))
                    showgrid[(x,y)] = '.'
                else:
                    markedmines.add((x,y))
                    showgrid[(x,y)] = '?'
            elif inp[0] == 'p':
                printgrid(showgrid)
            elif inp[0] == 'c':
                x, y = [int(i)-1 for i in inp[1:3]]
                if (x,y) in mines | markedmines:
                    print( '\nKLABOOM!! You hit a mine.\n' )
                    resign(showgrid, mines, markedmines)
                    printgrid(showgrid)
                    break
                clear(x,y, showgrid, grid, mines, markedmines)
                printgrid(showgrid)
            elif inp[0] == 'r':
                print( '\nResigning!\n' )
                resign(showgrid, mines, markedmines)
                printgrid(showgrid)
                break
    
    print( '\nYou got %i and missed %i of the %i mines'
           % (len(mines.intersection(markedmines)),
              len(markedmines.difference(mines)),
              len(mines)) )

```

