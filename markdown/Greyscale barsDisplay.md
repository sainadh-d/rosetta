# Greyscale bars/Display

## Task Link
[Rosetta Code - Greyscale bars/Display](https://rosettacode.org/wiki/Greyscale_bars/Display)

## Java Code
### java_code_1.txt
```java
import javax.swing.* ;
import java.awt.* ;

public class Greybars extends JFrame {
   private int width ;
   private int height ;

   public Greybars( )  {
      super( "grey bars example!" ) ;
      width = 640 ;
      height = 320 ;
      setSize( width , height ) ;
      setDefaultCloseOperation( JFrame.EXIT_ON_CLOSE ) ;
      setVisible( true ) ;
    }

    public void paint ( Graphics g ) {
      int run = 0 ;
      double colorcomp = 0.0 ; //component of the color
      for ( int columncount = 8 ; columncount < 128 ; columncount *= 2 ) {
	 double colorgap = 255.0 / (columncount - 1) ; //by this gap we change the background color
	 int columnwidth = width / columncount ;
	 int columnheight = height / 4 ;
	 if ( run % 2 == 0 ) //switches color directions with every for loop
	    colorcomp = 0.0 ;
	 else {
	    colorcomp = 255.0 ;
	    colorgap *= -1.0 ;
	 }
	 int ystart = 0 + columnheight * run ;
	 int xstart = 0 ;
	 for ( int i = 0 ; i < columncount ; i++ ) {
            int icolor = (int)Math.round(colorcomp) ; //round to nearer integer
	    Color nextColor = new Color( icolor , icolor, icolor ) ;
	    g.setColor( nextColor ) ;
	    g.fillRect( xstart , ystart , columnwidth , columnheight ) ;
	    xstart += columnwidth ;
	    colorcomp += colorgap ;
	 }
	 run++ ;
      }
    }

    public static void main( String[ ] args ) {
       Greybars gb = new Greybars( ) ;
    }
}

```

### java_code_2.txt
```java
//Aamrun, 3rd July 2022

void drawPanel(int startColour,int endColour,int bars,int startY){
  int rectWidth = width / bars,rectHeight = height / 4, startX = 0,increment;
  
  increment = (endColour - startColour)/(bars-1);
    
  for(int i = 0;i < bars;i++){
    fill(startColour + i*increment);
    rect(startX + i*rectWidth,startY,rectWidth,rectHeight);
  }
}

void setup(){
  size(1280,960);
  
  drawPanel(0,255,8,0);
  drawPanel(255,0,16,height/4);
  drawPanel(0,255,32,height/2);
  drawPanel(255,0,64,3*height/4);
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
#four gray scaled stripes 8:16:32:64 in Python 2.7.1

from livewires import *

horiz=640; vert=480; pruh=vert/4; dpp=255.0
begin_graphics(width=horiz,height=vert,title="Gray stripes",background=Colour.black)

def ty_pruhy(each):
	hiy=each[0]*pruh; loy=hiy-pruh
	krok=horiz/each[1]; piecol=255.0/(each[1]-1)
	for x in xrange(0,each[1]):
		barva=Colour(piecol*x/dpp,piecol*x/dpp,piecol*x/dpp ); set_colour(barva)
		if each[2]:
			box(x*krok,hiy,x*krok+krok,loy,filled=1)
		else:
			box(horiz-x*krok,hiy,horiz-((x+1)*krok),loy,filled=1)

# main
source=[[4,8,True],[3,16,False],[2,32,True],[1,64,False]]
for each in source:
	ty_pruhy(each)

while keys_pressed() != [' ']: # press spacebar to close window
	pass

```

