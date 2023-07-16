# Galton box animation

## Task Link
[Rosetta Code - Galton box animation](https://rosettacode.org/wiki/Galton_box_animation)

## Java Code
### java_code_1.txt
```java
import java.util.Random;
import java.util.List;
import java.util.ArrayList;

public class GaltonBox {
    public static void main( final String[] args ) {
        new GaltonBox( 8, 200 ).run();
    }

    private final int        m_pinRows;
    private final int        m_startRow;
    private final Position[] m_balls;
    private final Random     m_random = new Random();

    public GaltonBox( final int pinRows, final int ballCount ) {
        m_pinRows  = pinRows;
        m_startRow = pinRows + 1;
        m_balls    = new Position[ ballCount ];

        for ( int ball = 0; ball < ballCount; ball++ )
            m_balls[ ball ] = new Position( m_startRow, 0, 'o' );
    }

    private static class Position {
        int  m_row;
        int  m_col;
        char m_char;

        Position( final int row, final int col, final char ch ) {
            m_row  = row;
            m_col  = col;
            m_char = ch;
        }
    }

    public void run() {
        for ( int ballsInPlay = m_balls.length; ballsInPlay > 0;  ) {
            ballsInPlay = dropBalls();
            print();
        }
    }

    private int dropBalls() {
        int ballsInPlay = 0;
        int ballToStart = -1;

        // Pick a ball to start dropping
        for ( int ball = 0; ball < m_balls.length; ball++ )
            if ( m_balls[ ball ].m_row == m_startRow )
                ballToStart = ball;

        // Drop balls that are already in play
        for ( int ball = 0; ball < m_balls.length; ball++ )
            if ( ball == ballToStart ) {
                m_balls[ ball ].m_row = m_pinRows;
                ballsInPlay++;
            }
            else if ( m_balls[ ball ].m_row > 0 && m_balls[ ball ].m_row != m_startRow ) {
                m_balls[ ball ].m_row -= 1;
                m_balls[ ball ].m_col += m_random.nextInt( 2 );
                if ( 0 != m_balls[ ball ].m_row )
                    ballsInPlay++;
            }

        return ballsInPlay;
    }

    private void print() {
        for ( int row = m_startRow; row --> 1;  ) {
            for ( int ball = 0; ball < m_balls.length; ball++ )
                if ( m_balls[ ball ].m_row == row )
                    printBall( m_balls[ ball ] );
            System.out.println();
            printPins( row );
        }
        printCollectors();
        System.out.println();
    }

    private static void printBall( final Position pos ) {
        for ( int col = pos.m_row + 1; col --> 0;  )
            System.out.print( ' ' );
        for ( int col = 0; col < pos.m_col; col++ )
            System.out.print( "  " );
        System.out.print( pos.m_char );
    }

    private void printPins( final int row ) {
        for ( int col = row + 1; col --> 0;  )
            System.out.print( ' ' );
        for ( int col = m_startRow - row; col --> 0;  )
            System.out.print( ". " );
        System.out.println();
    }

    private void printCollectors() {
        final List<List<Position>> collectors = new ArrayList<List<Position>>();

        for ( int col = 0; col < m_startRow; col++ ) {
            final List<Position> collector = new ArrayList<Position>();

            collectors.add( collector );
            for ( int ball = 0; ball < m_balls.length; ball++ )
                if ( m_balls[ ball ].m_row == 0 && m_balls[ ball ].m_col == col )
                    collector.add( m_balls[ ball ] );
        }

        for ( int row = 0, rows = longest( collectors ); row < rows; row++ ) {
            for ( int col = 0; col < m_startRow; col++ ) {
                final List<Position> collector = collectors.get( col );
                final int            pos       = row + collector.size() - rows;

                System.out.print( '|' );
                if ( pos >= 0 )
                    System.out.print( collector.get( pos ).m_char );
                else
                    System.out.print( ' ' );
            }
            System.out.println( '|' );
        }
    }

    private static final int longest( final List<List<Position>> collectors ) {
        int result = 0;

        for ( final List<Position> collector : collectors )
            result = Math.max( collector.size(), result );

        return result;
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/python

import sys, os
import random
import time

def print_there(x, y, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (x, y, text))
     sys.stdout.flush()


class Ball():
    def __init__(self):
        self.x = 0
        self.y = 0
        
    def update(self):
        self.x += random.randint(0,1)
        self.y += 1

    def fall(self):
        self.y +=1


class Board():
    def __init__(self, width, well_depth, N):
        self.balls = []
        self.fallen = [0] * (width + 1)
        self.width = width
        self.well_depth = well_depth
        self.N = N
        self.shift = 4
        
    def update(self):
        for ball in self.balls:
            if ball.y < self.width:
                ball.update()
            elif ball.y < self.width + self.well_depth - self.fallen[ball.x]:
                ball.fall()
            elif ball.y == self.width + self.well_depth - self.fallen[ball.x]:
                self.fallen[ball.x] += 1
            else:
                pass
                
    def balls_on_board(self):
        return len(self.balls) - sum(self.fallen)
                
    def add_ball(self):
        if(len(self.balls) <= self.N):
            self.balls.append(Ball())

    def print_board(self):
        for y in range(self.width + 1):
            for x in range(y):
                print_there( y + 1 ,self.width - y + 2*x + self.shift + 1, "#")
    def print_ball(self, ball):
        if ball.y <= self.width:
            x = self.width - ball.y + 2*ball.x + self.shift
        else:
            x = 2*ball.x + self.shift
        y = ball.y + 1
        print_there(y, x, "*")
         
    def print_all(self):
        print(chr(27) + "[2J")
        self.print_board();
        for ball in self.balls:
            self.print_ball(ball)


def main():
    board = Board(width = 15, well_depth = 5, N = 10)
    board.add_ball() #initialization
    while(board.balls_on_board() > 0):
         board.print_all()
         time.sleep(0.25)
         board.update()
         board.print_all()
         time.sleep(0.25)
         board.update()
         board.add_ball()


if __name__=="__main__":
    main()

```

