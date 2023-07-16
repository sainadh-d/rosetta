# Tic-tac-toe

## Task Link
[Rosetta Code - Tic-tac-toe](https://rosettacode.org/wiki/Tic-tac-toe)

## Java Code
### java_code_1.txt
```java
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Hashtable;

public class TicTacToe
{
	public static void main(String[] args)
	{
		TicTacToe now=new TicTacToe();
		now.startMatch();
	}
	
	private int[][] marks;
	private int[][] wins;
	private int[] weights;
	private char[][] grid;
	private final int knotcount=3;
	private final int crosscount=4;
	private final int totalcount=5;
	private final int playerid=0;
	private final int compid=1;
	private final int truceid=2;
	private final int playingid=3;
	private String movesPlayer;
	private byte override;
	private char[][] overridegrid={{'o','o','o'},{'o','o','o'},{'o','o','o'}};
	private char[][] numpad={{'7','8','9'},{'4','5','6'},{'1','2','3'}};
	private Hashtable<Integer,Integer> crossbank;
	private Hashtable<Integer,Integer> knotbank;
	
	public void startMatch()
	{
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		System.out.print("Start?(y/n):");
		char choice='y';
		try
		{
			choice=br.readLine().charAt(0);
		}
		catch(Exception e)
		{
			System.out.println(e.getMessage());
		}
		if(choice=='n'||choice=='N')
		{
			return;
		}
		
		System.out.println("Use a standard numpad as an entry grid, as so:\n ");
		display(numpad);
		System.out.println("Begin");
		int playerscore=0;
		int compscore=0;
		do
		{
			int result=startGame();
			if(result==playerid)
				playerscore++;
			else if(result==compid)
				compscore++;
			System.out.println("Score: Player-"+playerscore+" AI-"+compscore);
			System.out.print("Another?(y/n):");
			try
			{
				choice=br.readLine().charAt(0);
			}
			catch(Exception e)
			{
				System.out.println(e.getMessage());
			}
			
		}while(choice!='n'||choice=='N');
		
		System.out.println("Game over.");
	}
	private void put(int cell,int player)
	{
		int i=-1,j=-1;;
		switch(cell)
		{
		case 1:i=2;j=0;break;
		case 2:i=2;j=1;break;
		case 3:i=2;j=2;break;
		case 4:i=1;j=0;break;
		case 5:i=1;j=1;break;
		case 6:i=1;j=2;break;
		case 7:i=0;j=0;break;
		case 8:i=0;j=1;break;
		case 9:i=0;j=2;break;
		default:display(overridegrid);return;
		}
		char mark='x';
		if(player==0)
			mark='o';
		grid[i][j]=mark;
		display(grid);
	}
	private int startGame()
	{
		init();
		display(grid);
		int status=playingid;
		while(status==playingid)
		{
			put(playerMove(),0);
			if(override==1)
			{
				System.out.println("O wins.");
				return playerid;
			}
			status=checkForWin();
			if(status!=playingid)
				break;
			try{Thread.sleep(1000);}catch(Exception e){System.out.print(e.getMessage());}
			put(compMove(),1);
			status=checkForWin();
		}
		return status;
	}
	private void init()
	{
		movesPlayer="";
		override=0;
		marks=new int[8][6];
		wins=new int[][]	//new int[8][3];
		{	
				{7,8,9},
				{4,5,6},
				{1,2,3},
				{7,4,1},
				{8,5,2},
				{9,6,3},
				{7,5,3},
				{9,5,1}
		};
		weights=new int[]{3,2,3,2,4,2,3,2,3};
		grid=new char[][]{{' ',' ',' '},{' ',' ',' '},{' ',' ',' '}};
		crossbank=new Hashtable<Integer,Integer>();
		knotbank=new Hashtable<Integer,Integer>();
	}
	private void mark(int m,int player)
	{
		for(int i=0;i<wins.length;i++)
			for(int j=0;j<wins[i].length;j++)
				if(wins[i][j]==m)
				{
					marks[i][j]=1;
					if(player==playerid)
						marks[i][knotcount]++;
					else
						marks[i][crosscount]++;
					marks[i][totalcount]++;
				}
	}
	private void fixWeights()
	{
		for(int i=0;i<3;i++)
			for(int j=0;j<3;j++)
				if(marks[i][j]==1)
					if(weights[wins[i][j]-1]!=Integer.MIN_VALUE)
						weights[wins[i][j]-1]=Integer.MIN_VALUE;
		
		for(int i=0;i<8;i++)
		{
			if(marks[i][totalcount]!=2)
				continue;
			if(marks[i][crosscount]==2)
			{
				int p=i,q=-1;
				if(marks[i][0]==0)
					q=0;
				else if(marks[i][1]==0)
					q=1;
				else if(marks[i][2]==0)
					q=2;
				
				if(weights[wins[p][q]-1]!=Integer.MIN_VALUE)
				{
					weights[wins[p][q]-1]=6;
				}
			}
			if(marks[i][knotcount]==2)
			{
				int p=i,q=-1;
				if(marks[i][0]==0)
					q=0;
				else if(marks[i][1]==0)
					q=1;
				else if(marks[i][2]==0)
					q=2;
				
				if(weights[wins[p][q]-1]!=Integer.MIN_VALUE)
				{
					weights[wins[p][q]-1]=5;
				}
			}
		}
	}
	private int compMove()
	{
		int cell=move();
		System.out.println("Computer plays: "+cell);
		//weights[cell-1]=Integer.MIN_VALUE;
		return cell;
	}
	private int move()
	{
		int max=Integer.MIN_VALUE;
		int cell=0;
		for(int i=0;i<weights.length;i++)
			if(weights[i]>max)
			{
				max=weights[i];
				cell=i+1;
			}
		
		//This section ensures the computer never loses
		//Remove it for a fair match
		//Dirty kluge
		if(movesPlayer.equals("76")||movesPlayer.equals("67"))
			cell=9;
		else if(movesPlayer.equals("92")||movesPlayer.equals("29"))
			cell=3;
		else if (movesPlayer.equals("18")||movesPlayer.equals("81"))
			cell=7;
		else if(movesPlayer.equals("73")||movesPlayer.equals("37"))
			cell=4*((int)(Math.random()*2)+1);
		else if(movesPlayer.equals("19")||movesPlayer.equals("91"))
			cell=4+2*(int)(Math.pow(-1, (int)(Math.random()*2)));
		
		mark(cell,1);
		fixWeights();
		crossbank.put(cell, 0);
		return cell;
	}
	private int playerMove()
	{
		System.out.print("What's your move?: ");
		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
		int cell=0;
		int okay=0;
		while(okay==0)
		{
			try
			{
				cell=Integer.parseInt(br.readLine());
			}
			catch(Exception e)
			{
				System.out.println(e.getMessage());
			}
			if(cell==7494)
			{
				override=1;
				return -1;
			}
			if((cell<1||cell>9)||weights[cell-1]==Integer.MIN_VALUE)
				System.out.print("Invalid move. Try again:");
			else
				okay=1;
		}
		playerMoved(cell);
		System.out.println();
		return cell;
	}
	private void playerMoved(int cell)
	{
		movesPlayer+=cell;
		mark(cell,0);
		fixWeights();
		knotbank.put(cell, 0);
	}
	private int checkForWin()
	{
		int crossflag=0,knotflag=0;
		for(int i=0;i<wins.length;i++)
		{
			if(crossbank.containsKey(wins[i][0]))
				if(crossbank.containsKey(wins[i][1]))
					if(crossbank.containsKey(wins[i][2]))
					{
						crossflag=1;
						break;
					}
			if(knotbank.containsKey(wins[i][0]))
				if(knotbank.containsKey(wins[i][1]))
					if(knotbank.containsKey(wins[i][2]))
					{
						knotflag=1;
						break;
					}
		}
		if(knotflag==1)
		{
			display(grid);
			System.out.println("O wins.");
			return playerid;
		}
		else if(crossflag==1)
		{
			display(grid);
			System.out.println("X wins.");
			return compid;
		}
		
		for(int i=0;i<weights.length;i++)
			if(weights[i]!=Integer.MIN_VALUE)
				return playingid;
		System.out.println("Truce");
		
		return truceid;
	}
	private void display(char[][] grid)
	{
		for(int i=0;i<3;i++)
		{
			System.out.println("\n-------");
			System.out.print("|");
			for(int j=0;j<3;j++)
				System.out.print(grid[i][j]+"|");
		}
		System.out.println("\n-------");
	}
}

```

### java_code_2.txt
```java
import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.logging.Logger;
/**

* TicTacToe Application
* @author Steve Robinson
* @version 1.0
*/
class TicTacToeFrame extends JFrame
{
 JButton [][] buttons= new JButton[3][3];
 JTextField statusBar;
 GamePanel panel;
 Integer turn;
 GameListener listener=new GameListener();
 Integer count;
 public TicTacToeFrame()
 {
setLayout(new BorderLayout());
  panel=new GamePanel();
  add(panel,BorderLayout.CENTER);
  statusBar=new JTextField("Player1's Turn");
  statusBar.setEditable(false);
  add(statusBar,BorderLayout.SOUTH);
  setTitle("Tic Tac Toe!");
  setVisible(true);
  setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
  setBounds(400,400,300,300);
 }
 class GamePanel extends JPanel
 {
  public GamePanel()
  {
   setLayout(new GridLayout(3,3));
   turn =1;
   count=0;
   for(int i=0;i<3;i++)
    for(int j=0;j<3;j++)   {
     buttons[i][j]=new JButton();
     buttons[i][j].putClientProperty("INDEX", new Integer[]{i,j});
     buttons[i][j].putClientProperty("OWNER", null);
     buttons[i][j].addActionListener(listener);
     add(buttons[i][j]);
    }
  }
 }
 class GameListener implements ActionListener
 {
  public void actionPerformed(ActionEvent e)
  {
   count++;
   JButton b=(JButton)e.getSource();
   Integer[]index=(Integer[]) b.getClientProperty("INDEX");
   //System.out.println(turn); //turn                  //   //System.out.println("["+index[0]+"]"+"["+index[1]+"]");         //
   b.putClientProperty("OWNER", turn);
   Icon ico=new ImageIcon(turn.toString()+".gif");
   b.setIcon(ico);
   b.setEnabled(false);
   boolean result=checkVictoryCondition(index);
   if(result)
   {
    JOptionPane.showMessageDialog(null, "Player "+turn.toString()+" Wins");
    initComponents();
   }
   else
   {
    if(turn==1)
    {
     turn=2;
     statusBar.setText("Player2's Turn");
    }
    else
    {
     turn=1;
     statusBar.setText("Player1's Turn");
    }
   }
   if(count==9)
   {
    JOptionPane.showMessageDialog(null, "Match is a draw!");
    initComponents();
   }
  }
  Integer getOwner(JButton b)
  {
   return (Integer)b.getClientProperty("OWNER");
  }
  //PrintButtonMap for Diagnostics
  void printbuttonMap(Integer [][]bMap)
  {
   for(int i=0;i    for(int j=0;j     System.out.print(bMap[i][j]+" ");
    System.out.println("");
   }
  }
  boolean checkVictoryCondition(Integer [] index)
  {
   /*Integer[][]buttonMap=new Integer[][] {

     { getOwner(buttons[0][0]),getOwner(buttons[0][1]),getOwner(buttons[0][2])},

     { getOwner(buttons[1][0]),getOwner(buttons[1][1]),getOwner(buttons[1][2])},

     { getOwner(buttons[2][0]),getOwner(buttons[2][1]),getOwner(buttons[2][2])}
   };
   printbuttonMap(buttonMap); */
   Integer a=index[0];
                Integer b=index[1];
   int i;
   //check row
   for(i=0;i<3;i++)  {
    if(getOwner(buttons[a][i])!=getOwner(buttons[a][b]))
     break;
   }
   if(i==3)
    return true;
   //check column
   for(i=0;i<3;i++)  {
    if(getOwner(buttons[i][b])!=getOwner(buttons[a][b]))
     break;
   }
   if(i==3)
    return true;
   //check diagonal
   if((a==2&&b==2)||(a==0&&b==0)||(a==1&&b==1)||(a==0&&b==2)||(a==2&&b==0))
   {
    //left diagonal
    for(i=0;i     if(getOwner(buttons[i][i])!=getOwner(buttons[a][b]))
      break;
    if(i==3)
     return true;
    //right diagonal
    if((getOwner(buttons[0][2])==getOwner(buttons[a][b]))&&(getOwner(buttons[1][1])==getOwner(buttons[a][b]))&&(getOwner(buttons[2][0])==getOwner(buttons[a][b])))
     return true;
    }
   return false;
  }
 }
 void initComponents()
 {
  for(int i=0;i<3;i++)  
   for(int j=0;j<3;j++)  {
    buttons[i][j].putClientProperty("INDEX", new Integer[]{i,j});
    buttons[i][j].putClientProperty("OWNER",null);
    buttons[i][j].setIcon(null);
    buttons[i][j].setEnabled(true);
    turn=1;
    count=0;
    statusBar.setText("Player1's Turn");
   }
 }
}
class TicTacToe {
 public static void main(String[] args) {
  EventQueue.invokeLater(new Runnable(){
   public void run()
   {
    TicTacToeFrame frame=new TicTacToeFrame();
   }
  });
 }
}

```

### java_code_3.txt
```java
import javax.swing.*;
import java.awt.event.*;
import java.awt.*;


//Make sure the name of the class is the same as the .java file name.
//If you change the class name you should change the class object name in runGUI method
public class ticTacToeCallum implements ActionListener {
 
  static JFrame frame;          
  static JPanel contentPane;    
  static JLabel lblEnterFirstPlayerName, lblEnterSecondPlayerName, lblFirstPlayerScore, lblSecondPlayerScore;    
  static JButton btnButton1, btnButton2, btnButton3, btnButton4, btnButton5, btnButton6, btnButton7, btnButton8, btnButton9, btnClearBoard, btnClearAll, btnCloseGame;     
  static JTextField txtEnterFirstPlayerName, txtEnterSecondPlayerName;  
  static Icon imgicon = new ImageIcon("saveIcon.JPG");

  Font buttonFont = new Font("Arial", Font.PLAIN, 20);
  
  
  //to adjust the frame size change the values in pixels
  static int width = 600;
  static int length = 400;
  static int firstPlayerScore = 0;
  static int secondPlayerScore = 0;
  static int playerTurn = 1;
  static int roundComplete = 0;
  static int button1 = 1, button2 = 1, button3 = 1, button4 = 1, button5 = 1, button6 = 1, button7 = 1, button8 = 1, button9 = 1; // 1 is true, 0 is false
  

  public ticTacToeCallum(){
	  
    frame = new JFrame("Tic Tac Toe ^_^");
    frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    
    contentPane = new JPanel();
    contentPane.setLayout(new GridLayout(6, 3, 10, 10));
    contentPane.setBorder(BorderFactory.createEmptyBorder(20, 20, 20, 20));
   
    btnButton1 = new JButton("");
    btnButton1.setFont(buttonFont);
    btnButton1.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton1.setIcon(imgicon);
    btnButton1.setActionCommand("CLICK1");    
    btnButton1.addActionListener(this);  
    contentPane.add(btnButton1);
    
    btnButton2 = new JButton("");
    btnButton2.setFont(buttonFont);
    btnButton2.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton2.setIcon(imgicon);
    btnButton2.setActionCommand("CLICK2");    
    btnButton2.addActionListener(this);      
    contentPane.add(btnButton2);
    
    btnButton3 = new JButton(""); 
    btnButton3.setFont(buttonFont);
    btnButton3.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton3.setIcon(imgicon);
    btnButton3.setActionCommand("CLICK3");    
    btnButton3.addActionListener(this);      
    contentPane.add(btnButton3);
    
    btnButton4 = new JButton("");
    btnButton4.setFont(buttonFont);
    btnButton4.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton4.setIcon(imgicon);
    btnButton4.setActionCommand("CLICK4");    
    btnButton4.addActionListener(this);      
    contentPane.add(btnButton4);
    
    btnButton5 = new JButton(""); 
    btnButton5.setFont(buttonFont);
    btnButton5.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton5.setIcon(imgicon);
    btnButton5.setActionCommand("CLICK5");    
    btnButton5.addActionListener(this);      
    contentPane.add(btnButton5);
    
    btnButton6 = new JButton(""); 
    btnButton6.setFont(buttonFont);
    btnButton6.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton6.setIcon(imgicon);
    btnButton6.setActionCommand("CLICK6");    
    btnButton6.addActionListener(this);      
    contentPane.add(btnButton6);
    
    btnButton7 = new JButton(""); 
    btnButton7.setFont(buttonFont);
    btnButton7.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton7.setIcon(imgicon);
    btnButton7.setActionCommand("CLICK7");    
    btnButton7.addActionListener(this);      
    contentPane.add(btnButton7);
    
    btnButton8 = new JButton(""); 
    btnButton8.setFont(buttonFont);
    btnButton8.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton8.setIcon(imgicon);
    btnButton8.setActionCommand("CLICK8");    
    btnButton8.addActionListener(this);      
    contentPane.add(btnButton8);
    
    btnButton9 = new JButton("");
    btnButton9.setFont(buttonFont);
    btnButton9.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnButton9.setIcon(imgicon);
    btnButton9.setActionCommand("CLICK9");    
    btnButton9.addActionListener(this);      
    contentPane.add(btnButton9);
    
    lblEnterFirstPlayerName = new JLabel("Enter First Player's Name");
    contentPane.add(lblEnterFirstPlayerName);
    
    txtEnterFirstPlayerName = new JTextField("");
    contentPane.add(txtEnterFirstPlayerName);
    
    lblFirstPlayerScore = new JLabel("Score: " + firstPlayerScore);
    contentPane.add(lblFirstPlayerScore);
    
    lblEnterSecondPlayerName = new JLabel("Enter Second Player's Name");
    contentPane.add(lblEnterSecondPlayerName);
    
    txtEnterSecondPlayerName = new JTextField("");
    contentPane.add(txtEnterSecondPlayerName);
    
    lblSecondPlayerScore = new JLabel("Score: " + secondPlayerScore);
    contentPane.add(lblSecondPlayerScore);
    
    btnClearBoard = new JButton("Clear Board");  
    btnClearBoard.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnClearBoard.setIcon(imgicon);
    btnClearBoard.setActionCommand("CLICKClearBoard");    
    btnClearBoard.addActionListener(this);      
    contentPane.add(btnClearBoard);
    
    btnClearAll = new JButton("Clear All");  
    btnClearAll.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnClearAll.setIcon(imgicon);
    btnClearAll.setActionCommand("CLICKClearAll");    
    btnClearAll.addActionListener(this);      
    contentPane.add(btnClearAll);
    
    btnCloseGame = new JButton("Close Game"); 
    btnCloseGame.setAlignmentX(JButton.CENTER_ALIGNMENT);
    btnCloseGame.setIcon(imgicon);
    btnCloseGame.setActionCommand("CLICKCloseGame");    
    btnCloseGame.addActionListener(this);      
    contentPane.add(btnCloseGame);
    
    frame.setContentPane(contentPane);
    frame.pack();
    frame.setSize(width,length);
    frame.setVisible(true);

  }

  public void actionPerformed(ActionEvent event) {
    String eventName = event.getActionCommand();
     if (eventName.equals("CLICK1")) {
    	 if (button1 == 1){
    		 if (playerTurn == 1){
    			 btnButton1.setForeground(Color.RED);
    			 btnButton1.setText("X");
   	  			 playerTurn = 2;
    			 button1 = 0;
    		 } else if (playerTurn == 2) {
    			 btnButton1.setForeground(Color.GREEN);
    			 btnButton1.setText("O");
    			 playerTurn = 1;
    			 button1 = 0;
    		 }
    	 }
      } else if (eventName.equals ("CLICK2")) {
    	  if (button2 == 1){	
    	  	if (playerTurn == 1){
    	  		btnButton2.setForeground(Color.RED);
    	  		btnButton2.setText("X");
  	  			playerTurn = 2;
    	  		button2 = 0;
    	  	} else if (playerTurn == 2) {
    	  		btnButton2.setForeground(Color.GREEN);
    	  		btnButton2.setText("O");
    	  		playerTurn = 1;
    	  		button2 = 0;
    	  	}
    	  }	
      }	else if (eventName.equals ("CLICK3")) {
    	  if (button3 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton3.setForeground(Color.RED);
      	  		btnButton3.setText("X");
  	  			playerTurn = 2;
      	  		button3 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton3.setForeground(Color.GREEN);
      	  		btnButton3.setText("O");
      	  		playerTurn = 1;
      	  		button3 = 0;
      	  	}
      	  }
      }	else if (eventName.equals ("CLICK4")) {
    	  if (button4 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton4.setForeground(Color.RED);
      	  		btnButton4.setText("X");
  	  			playerTurn = 2;
      	  		button4 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton4.setForeground(Color.GREEN);
      	  		btnButton4.setText("O");
      	  		playerTurn = 1;
      	  		button4 = 0;
      	  	}
      	  }
      }	else if (eventName.equals ("CLICK5")) {
    	  if (button5 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton5.setForeground(Color.RED);
  	  			btnButton5.setText("X");
  	  			playerTurn = 2;
  	  			button5 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton5.setForeground(Color.GREEN);
  	  			btnButton5.setText("O");
  	  			playerTurn = 1;
  	  			button5 = 0;
      	  	}
      	  }
      } else if (eventName.equals ("CLICK6")) {
    	  if (button6 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton6.setForeground(Color.RED);
  	  			btnButton6.setText("X");
  	  			playerTurn = 2;
  	  			button6 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton6.setForeground(Color.GREEN);
  	  			btnButton6.setText("O");
  	  			playerTurn = 1;
  	  			button6 = 0;
      	  	}
      	  }
      } else if (eventName.equals ("CLICK7")) {
    	  if (button7 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton7.setForeground(Color.RED);
  	  			btnButton7.setText("X");
  	  			playerTurn = 2;
  	  			button7 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton7.setForeground(Color.GREEN);
  	  			btnButton7.setText("O");
  	  			playerTurn = 1;
  	  			button7 = 0;
      	  	}
      	  }
      } else if (eventName.equals ("CLICK8")) {
    	  if (button8 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton8.setForeground(Color.RED);
  	  			btnButton8.setText("X");
  	  			playerTurn = 2;
  	  			button8 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton8.setForeground(Color.GREEN);
  	  			btnButton8.setText("O");
  	  			playerTurn = 1;
  	  			button8 = 0;
      	  	}
      	  }
      } else if (eventName.equals ("CLICK9")) {
    	  if (button9 == 1){	
      	  	if (playerTurn == 1){
      	  		btnButton9.setForeground(Color.RED);
  	  			btnButton9.setText("X");
  	  			playerTurn = 2;
  	  			button9 = 0;
      	  	} else if (playerTurn == 2) {
      	  		btnButton9.setForeground(Color.GREEN);
  	  			btnButton9.setText("O");
  	  			playerTurn = 1;
  	  			button9 = 0;
      	  	}
      	  }
      } else if (eventName.equals ("CLICKClearBoard")) {
          
    	  btnButton1.setText("");
          btnButton2.setText("");
          btnButton3.setText("");
          btnButton4.setText("");
          btnButton5.setText("");
          btnButton6.setText("");
          btnButton7.setText("");
          btnButton8.setText("");
          btnButton9.setText("");
          
          button1 = 1;
          button2 = 1;
          button3 = 1;
          button4 = 1;
          button5 = 1;
          button6 = 1;
          button7 = 1;
          button8 = 1;
          button9 = 1;
          
          playerTurn = 1;
          
          roundComplete = 0;
          
      } else if (eventName.equals ("CLICKClearAll")) {
    	  
    	  btnButton1.setText("");
          btnButton2.setText("");
          btnButton3.setText("");
          btnButton4.setText("");
          btnButton5.setText("");
          btnButton6.setText("");
          btnButton7.setText("");
          btnButton8.setText("");
          btnButton9.setText("");
          
          firstPlayerScore = 0;
          lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
          secondPlayerScore = 0;
          lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
          
          txtEnterFirstPlayerName.setText("");
          txtEnterSecondPlayerName.setText("");
          
          button1 = 1;
          button2 = 1;
          button3 = 1;
          button4 = 1;
          button5 = 1;
          button6 = 1;
          button7 = 1;
          button8 = 1;
          button9 = 1;
         
          playerTurn = 1;
          
          roundComplete = 0;
          
      } else if (eventName.equals ("CLICKCloseGame")) {
    	  System.exit(0);
      }  
     score();
    }
  
  
  public static void score(){
	  if (roundComplete == 0){
	  if (btnButton1.getText().equals(btnButton2.getText())  && btnButton1.getText().equals(btnButton3.getText())){
	    	if (btnButton1.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton1.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton1.getText().equals(btnButton4.getText())  && btnButton1.getText().equals(btnButton7.getText())){
	    	if (btnButton1.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton1.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton1.getText().equals(btnButton5.getText())  && btnButton1.getText().equals(btnButton9.getText())){
	    	if (btnButton1.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton1.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton7.getText().equals(btnButton8.getText())  && btnButton7.getText().equals(btnButton9.getText())){
	    	if (btnButton7.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton7.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton7.getText().equals(btnButton5.getText())  && btnButton7.getText().equals(btnButton3.getText())){
	    	if (btnButton7.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton7.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton3.getText().equals(btnButton6.getText())  && btnButton3.getText().equals(btnButton9.getText())){
	    	if (btnButton3.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton3.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton4.getText().equals(btnButton5.getText())  && btnButton4.getText().equals(btnButton6.getText())){
	    	if (btnButton4.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton4.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	    if (btnButton2.getText().equals(btnButton5.getText())  && btnButton2.getText().equals(btnButton8.getText())){
	    	if (btnButton2.getText().equals("X")){
	    		firstPlayerScore += 1;
	    		lblFirstPlayerScore.setText("Score: " + firstPlayerScore);
	    		roundComplete = 1;
	    	} else if (btnButton2.getText().equals("O")){
	    		secondPlayerScore += 1;
	    		lblSecondPlayerScore.setText("Score: " + secondPlayerScore);
	    		roundComplete = 1;
	    	}
	    }
	  }
	    if (roundComplete == 1){
	    	button1 = 0;
	    	button2 = 0;
	    	button3 = 0;
	    	button4 = 0;
	    	button5 = 0;
	    	button6 = 0;
	    	button7 = 0;
	    	button8 = 0;
	    	button9 = 0;
	    }
  }
  
  /**
   * Create and show the GUI.
   */
  private static void runGUI() {
    ticTacToeCallum        greeting     = new ticTacToeCallum();
  }
  
  
  
  //Do not change this method
  public static void main(String[] args) {
    /* Methods that create and show a GUI should be run from an event-dispatching thread */
    javax.swing.SwingUtilities.invokeLater(new Runnable() {
      public void run() {
        runGUI();
      }
    });
  }
}

```

### java_code_4.txt
```java
import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class TicTacToe {
        private static int turnNumber = 0;
        private static final JPanel panel = new JPanel();
        private static final JTextField ta = new JTextField("Player A's Turn (X)");
        private static final JButton r1c1 = new JButton("");
        private static final JButton r1c2 = new JButton("");
        private static final JButton r1c3 = new JButton("");
        private static final JButton r2c1 = new JButton("");
        private static final JButton r2c2 = new JButton("");
        private static final JButton r2c3 = new JButton("");
        private static final JButton r3c1 = new JButton("");
        private static final JButton r3c2 = new JButton("");
        private static final JButton r3c3 = new JButton("");
        private static final JButton restart = new JButton("New Game");
        private static final JPanel startMain = new JPanel();

    public static void main(String[]args){
        JFrame frame = new JFrame("Tic Tac Toe");
        frame.setSize(600,650);
        ta.setEditable(false);
        restart.addActionListener(e -> {
            enableAll();
            ta.setText("Player A's Turn (X)");
        });
        r1c1.setSize(67,67);
        r1c1.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r1c1.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r1c1.setText("O");
                r1c1.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r1c1.setText("X");
                r1c1.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r1c2.setSize(67,67);
        r1c2.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r1c2.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r1c2.setText("O");
                r1c2.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r1c2.setText("X");
                r1c2.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r1c3.setSize(67,67);
        r1c3.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r1c3.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r1c3.setText("O");
                r1c3.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r1c3.setText("X");
                r1c3.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r2c1.setSize(67,67);
        r2c1.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r2c1.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r2c1.setText("O");
                r2c1.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r2c1.setText("X");
                r2c1.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r2c2.setSize(67,67);
        r2c2.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r2c2.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r2c2.setText("O");
                r2c2.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r2c2.setText("X");
                r2c2.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r2c3.setSize(67,67);
        r2c3.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r2c3.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r2c3.setText("O");
                r2c3.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r2c3.setText("X");
                r2c3.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r3c1.setSize(67,67);
        r3c1.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r3c1.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r3c1.setText("O");
                r3c1.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r3c1.setText("X");
                r3c1.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r3c2.setSize(67,67);
        r3c2.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r3c2.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r3c2.setText("O");
                r3c2.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r3c2.setText("X");
                r3c2.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        r3c3.setSize(67,67);
        r3c3.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        r3c3.addActionListener(e -> {
            turnNumber++;
            if(turnNumber % 2 == 0){
                r3c3.setText("O");
                r3c3.setEnabled(false);
                ta.setText("Player A's Turn (X)");
            }else{
                r3c3.setText("X");
                r3c3.setEnabled(false);
                ta.setText("Player B's Turn (O)");
            }
            checkWin();
        });
        panel.setLayout(new GridLayout(3,3));

        panel.add(r1c1);
        panel.add(r1c2);
        panel.add(r1c3);
        panel.add(r2c1);
        panel.add(r2c2);
        panel.add(r2c3);
        panel.add(r3c1);
        panel.add(r3c2);
        panel.add(r3c3);
        startMain.setLayout(new GridLayout(5,5));
        JButton start = new JButton("Start");
        JLabel main = new JLabel("Tic Tac Toe", SwingConstants.CENTER);
        main.setFont(new Font("Trebuchet MS", Font.PLAIN, 70));
        main.setSize(400,400);
        startMain.add(main);
        startMain.add(start);
        frame.add(startMain);
        frame.setVisible(true);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        start.addActionListener(e -> {
            startMain.setVisible(false);
            frame.add(restart, BorderLayout.PAGE_START);
            frame.add(ta, BorderLayout.PAGE_END);
            frame.add(panel, BorderLayout.CENTER);
        });
    }
    public static void checkWin(){
        if(r1c1.getText().equals("X") && r1c2.getText().equals("X") && r1c3.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r1c1.getText().equals("O") && r1c2.getText().equals("O") && r1c3.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r1c1.getText().equals("X") && r2c2.getText().equals("X") && r3c3.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r1c1.getText().equals("O") && r2c2.getText().equals("O") && r3c3.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r1c1.getText().equals("X") && r2c1.getText().equals("X") && r3c1.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r1c1.getText().equals("O") && r2c1.getText().equals("O") && r3c1.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r2c1.getText().equals("X") && r2c2.getText().equals("X") && r2c3.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r2c1.getText().equals("O") && r2c2.getText().equals("O") && r2c3.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r1c2.getText().equals("X") && r2c2.getText().equals("X") && r3c2.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r1c2.getText().equals("O") && r2c2.getText().equals("O") && r3c2.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r1c3.getText().equals("X") && r2c3.getText().equals("X") && r3c3.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r1c3.getText().equals("O") && r2c3.getText().equals("O") && r3c3.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r3c1.getText().equals("X") && r3c2.getText().equals("X") && r3c3.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r3c1.getText().equals("O") && r3c2.getText().equals("O") && r3c3.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(r3c1.getText().equals("X") && r2c2.getText().equals("X") && r1c3.getText().equals("X")){
            ta.setText("Player A Won! (X)");
            disableAll();
        }else if(r3c1.getText().equals("O") && r2c2.getText().equals("O") && r1c3.getText().equals("O")){
            ta.setText("Player B Won! (O)");
            disableAll();
        }else if(!r1c1.isEnabled() && !r1c2.isEnabled() && !r1c3.isEnabled() && !r2c1.isEnabled() && !r2c2.isEnabled() && !r2c3.isEnabled() && !r3c1.isEnabled() && !r3c2.isEnabled() && !r3c3.isEnabled()){
            ta.setText("Draw!");
            disableAll();
        }
    }
    public static void disableAll(){
        r1c1.setEnabled(false);
        r1c2.setEnabled(false);
        r1c3.setEnabled(false);
        r2c1.setEnabled(false);
        r2c2.setEnabled(false);
        r2c3.setEnabled(false);
        r3c1.setEnabled(false);
        r3c2.setEnabled(false);
        r3c3.setEnabled(false);
    }

    public static void enableAll(){
        turnNumber = 0;
        r1c1.setEnabled(true);
        r1c2.setEnabled(true);
        r1c3.setEnabled(true);
        r2c1.setEnabled(true);
        r2c2.setEnabled(true);
        r2c3.setEnabled(true);
        r3c1.setEnabled(true);
        r3c2.setEnabled(true);
        r3c3.setEnabled(true);
        r1c1.setText("");
        r1c2.setText("");
        r1c3.setText("");
        r2c1.setText("");
        r2c2.setText("");
        r2c3.setText("");
        r3c1.setText("");
        r3c2.setText("");
        r3c3.setText("");
        panel.setEnabled(true);
    }
}

```

## Python Code
### python_code_1.txt
```python
'''
    Tic-tac-toe game player.
    Input the index of where you wish to place your mark at your turn.
'''

import random

board = list('123456789')
wins = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

def printboard():
    print('\n'.join(' '.join(board[x:x+3]) for x in(0,3,6)))

def score():
    for w in wins:
        b = board[w[0]]
        if b in 'XO' and all (board[i] == b for i in w):
            return b, [i+1 for i in w]
    return None, None

def finished():
    return all (b in 'XO' for b in board)

def space():
    return [ b for b in board if b not in 'XO']

def my_turn(xo):
    options = space()
    choice = random.choice(options)
    board[int(choice)-1] = xo
    return choice

def your_turn(xo):
    options = space()
    while True:
        choice = input(" Put your %s in any of these positions: %s "
                       % (xo, ''.join(options))).strip()
        if choice in options:
            break
        print( "Whoops I don't understand the input" )
    board[int(choice)-1] = xo
    return choice

def me(xo='X'):
    printboard()
    print('I go at', my_turn(xo))
    return score()
    assert not s[0], "\n%s wins across %s" % s

def you(xo='O'):
    printboard()
    # Call my_turn(xo) below for it to play itself
    print('You went at', your_turn(xo))
    return score()
    assert not s[0], "\n%s wins across %s" % s


print(__doc__)
while not finished():
    s = me('X')
    if s[0]:
        printboard()
        print("\n%s wins across %s" % s)
        break
    if not finished():
        s = you('O')
        if s[0]:
            printboard()
            print("\n%s wins across %s" % s)
            break
else:
    print('\nA draw')

```

### python_code_2.txt
```python
'''
    Tic-tac-toe game player.
    Input the index of where you wish to place your mark at your turn.
'''

import random

board = list('123456789')
wins = ((0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6))

def printboard():
    print('\n-+-+-\n'.join('|'.join(board[x:x+3]) for x in(0,3,6)))

def score(board=board):
    for w in wins:
        b = board[w[0]]
        if b in 'XO' and all (board[i] == b for i in w):
            return b, [i+1 for i in w]
    return None

def finished():
    return all (b in 'XO' for b in board)

def space(board=board):
    return [ b for b in board if b not in 'XO']

def my_turn(xo, board):
    options = space()
    choice = random.choice(options)
    board[int(choice)-1] = xo
    return choice

def my_better_turn(xo, board):
    'Will return a next winning move or block your winning move if possible'
    ox = 'O' if xo =='X' else 'X'
    oneblock = None
    options  = [int(s)-1 for s in space(board)]
    for choice in options:
        brd = board[:]
        brd[choice] = xo
        if score(brd):
            break
        if oneblock is None:
            brd[choice] = ox
            if score(brd):
                oneblock = choice
    else:
        choice = oneblock if oneblock is not None else random.choice(options)
    board[choice] = xo
    return choice+1

def your_turn(xo, board):
    options = space()
    while True:
        choice = input("\nPut your %s in any of these positions: %s "
                       % (xo, ''.join(options))).strip()
        if choice in options:
            break
        print( "Whoops I don't understand the input" )
    board[int(choice)-1] = xo
    return choice

def me(xo='X'):
    printboard()
    print('\nI go at', my_better_turn(xo, board))
    return score()

def you(xo='O'):
    printboard()
    # Call my_turn(xo, board) below for it to play itself
    print('\nYou went at', your_turn(xo, board))
    return score()


print(__doc__)
while not finished():
    s = me('X')
    if s:
        printboard()
        print("\n%s wins along %s" % s)
        break
    if not finished():
        s = you('O')
        if s:
            printboard()
            print("\n%s wins along %s" % s)
            break
else:
    print('\nA draw')

```

