# Draw a cuboid

## Task Link
[Rosetta Code - Draw a cuboid](https://rosettacode.org/wiki/Draw_a_cuboid)

## Java Code
### java_code_1.txt
```java
import java.awt.*;
import java.awt.event.*;
import static java.lang.Math.*;
import javax.swing.*;

public class Cuboid extends JPanel {
    double[][] nodes = {{-1, -1, -1}, {-1, -1, 1}, {-1, 1, -1}, {-1, 1, 1},
    {1, -1, -1}, {1, -1, 1}, {1, 1, -1}, {1, 1, 1}};

    int[][] edges = {{0, 1}, {1, 3}, {3, 2}, {2, 0}, {4, 5}, {5, 7}, {7, 6},
    {6, 4}, {0, 4}, {1, 5}, {2, 6}, {3, 7}};

    int mouseX, prevMouseX, mouseY, prevMouseY;

    public Cuboid() {
        setPreferredSize(new Dimension(640, 640));
        setBackground(Color.white);

        scale(80, 120, 160);
        rotateCube(PI / 5, PI / 9);

        addMouseListener(new MouseAdapter() {
            @Override
            public void mousePressed(MouseEvent e) {
                mouseX = e.getX();
                mouseY = e.getY();
            }
        });

        addMouseMotionListener(new MouseAdapter() {
            @Override
            public void mouseDragged(MouseEvent e) {
                prevMouseX = mouseX;
                prevMouseY = mouseY;
                mouseX = e.getX();
                mouseY = e.getY();

                double incrX = (mouseX - prevMouseX) * 0.01;
                double incrY = (mouseY - prevMouseY) * 0.01;

                rotateCube(incrX, incrY);
                repaint();
            }
        });
    }

    private void scale(double sx, double sy, double sz) {
        for (double[] node : nodes) {
            node[0] *= sx;
            node[1] *= sy;
            node[2] *= sz;
        }
    }

    private void rotateCube(double angleX, double angleY) {
        double sinX = sin(angleX);
        double cosX = cos(angleX);

        double sinY = sin(angleY);
        double cosY = cos(angleY);

        for (double[] node : nodes) {
            double x = node[0];
            double y = node[1];
            double z = node[2];

            node[0] = x * cosX - z * sinX;
            node[2] = z * cosX + x * sinX;

            z = node[2];

            node[1] = y * cosY - z * sinY;
            node[2] = z * cosY + y * sinY;
        }
    }

    void drawCube(Graphics2D g) {
        g.translate(getWidth() / 2, getHeight() / 2);

        for (int[] edge : edges) {
            double[] xy1 = nodes[edge[0]];
            double[] xy2 = nodes[edge[1]];
            g.drawLine((int) round(xy1[0]), (int) round(xy1[1]),
                    (int) round(xy2[0]), (int) round(xy2[1]));
        }

        for (double[] node : nodes) {
            g.fillOval((int) round(node[0]) - 4, (int) round(node[1]) - 4, 8, 8);
        }
    }

    @Override
    public void paintComponent(Graphics gg) {
        super.paintComponent(gg);
        Graphics2D g = (Graphics2D) gg;
        g.setRenderingHint(RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON);

        drawCube(g);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            JFrame f = new JFrame();
            f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
            f.setTitle("Cuboid");
            f.setResizable(false);
            f.add(new Cuboid(), BorderLayout.CENTER);
            f.pack();
            f.setLocationRelativeTo(null);
            f.setVisible(true);
        });
    }
}

```

## Python Code
### python_code_1.txt
```python
def _pr(t, x, y, z):
    txt = '\n'.join(''.join(t[(n,m)] for n in range(3+x+z)).rstrip()
                    for m in reversed(range(3+y+z)))
    return txt
		
def cuboid(x,y,z):
    t = {(n,m):' ' for n in range(3+x+z) for m in range(3+y+z)}
    xrow = ['+'] + ['%i' % (i % 10) for i in range(x)] + ['+']
    for i,ch in enumerate(xrow):
        t[(i,0)] = t[(i,1+y)] = t[(1+z+i,2+y+z)] = ch
    if _debug: print(_pr(t, x, y, z))
    ycol = ['+'] + ['%i' % (j % 10) for j in range(y)] + ['+']
    for j,ch in enumerate(ycol):
        t[(0,j)] = t[(x+1,j)] = t[(2+x+z,1+z+j)] = ch
    zdepth = ['+'] + ['%i' % (k % 10) for k in range(z)] + ['+']
    if _debug: print(_pr(t, x, y, z))
    for k,ch in enumerate(zdepth):
        t[(k,1+y+k)] = t[(1+x+k,1+y+k)] = t[(1+x+k,k)] = ch
	
    return _pr(t, x, y, z)


_debug = False
if __name__ == '__main__':
    for dim in ((2,3,4), (3,4,2), (4,2,3)):
        print("CUBOID%r" % (dim,), cuboid(*dim), sep='\n')

```

### python_code_2.txt
```python
from visual import *
mybox = box(pos=(0,0,0), length=4, height=2, width=3, axis=(-0.1,-0.1,0.1) ) 
scene.title = "VPython: cuboid"

```

### python_code_3.txt
```python
from __future__ import print_function, division
from visual import *
import itertools

title = "VPython: Draw a cuboid"
scene.title = title
print( "%s\n" % title )

msg = """
Drag with right mousebutton to rotate view.
Drag up+down with middle mousebutton to zoom.
Left mouseclick to show info.

Press x,X, y,Y, z,Z to rotate the box in single steps.
Press b, c,o,m to change background, color, opacity, material.
Press r,R to rotate, d,a for demo, automatic,  space to stop.
Press h to show this help,  ESC or q to quit.
"""

#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+...

## Rotate one step per keypress:

def rotX(obj, a) :
    obj.rotate( angle=a, axis=(1,0,0) )
def rotY(obj, a) :
    obj.rotate( angle=a, axis=(0,1,0) )
def rotZ(obj, a) :
    obj.rotate( angle=a, axis=(0,0,1) )

## Selection of background-colors:

bg_list = [color.gray(0.2), color.gray(0.4), color.gray(0.7), color.gray(0.9)]
bg = itertools.cycle(bg_list)
def backgr() :
    b = next(bg)
    print("BackgroundColor=",b)
    scene.background = b

## Selection of colors:

col_list = [color.white, color.red,  color.orange, color.yellow,  
            color.green, color.blue, color.cyan,   color.magenta, 
            color.black]
col = itertools.cycle(col_list)
#c = col.next()
#c = next(col)
def paint(obj) :
    c = next(col)
    print("Color=",c)
    obj.color = c

## Selection of opacity / transparancy :

opa_list = [1.0, 0.7, 0.5, 0.2]
opa = itertools.cycle(opa_list)
def solid(obj) :
    o = next(opa)
    print("opacity =",o)
    obj.opacity = o

## Selection of materials:

mName_list = ["None",
              "wood",
              "rough",
              "bricks",
              "glass",
              "earth",
              "plastic",
              "ice",
              "diffuse",
              "marble" ]
mat_list  = [ None,
              materials.wood,
              materials.rough,
              materials.bricks,
              materials.glass,
              materials.earth,
              materials.plastic,
              materials.ice,
              materials.diffuse,
              materials.marble ]
mName = itertools.cycle(mName_list)
mat   = itertools.cycle(mat_list)
def surface(obj) :
    mM = next(mat)
    mN = next(mName)
    print("Material:", mN)
    obj.material = mM
    obj.mat      = mN

## Selection for rotation-angle & axis :

rotAng_list = [ 0.0, 0.005, 0.0, -0.005 ]
rotDir_list = [ (1,0,0), (0,1,0), (0,0,1) ]

rotAng = itertools.cycle(rotAng_list)
rotDir = itertools.cycle(rotDir_list)

rotAn = next(rotAng)     # rotAn = 0.005
rotAx = next(rotDir)     # rotAx = (1,0,0)

def rotAngle() :
    global rotAn
    rotAn = next(rotAng)
    print("RotateAngle=",rotAn)

def rotAxis() :
    global rotAx
    rotAx = next(rotDir)
    print("RotateAxis=",rotAx)

## List of keypresses for demo:

#demoC_list = [ "h", "c", "a", "o", "m", "b" ]
demoCmd_list = "rcbr"+"robr"+"rmR_r?"
demoCmd = itertools.cycle(demoCmd_list)
def demoStep() :
    k = next(demoCmd)
    print("Demo:",k)
    cmd(k)

#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+...

def objCount():
    n=0
    for obj in scene.objects:
        n=n+1
    return n
            
def objInfo(obj) :
    print( "\nObject:", obj )
    print( "Pos:",  obj.pos,   "Size:", obj.size )
    print( "Axis:", obj.axis,  "Up:",   obj.up )
    print( "Color", obj.color, obj.opacity )
    print( "Mat:",  obj.mat,   obj.material )

def sceneInfo(sc) :
    print( "\nScene:",  sc )
    print( ".width x height:",   sc.width, "x", sc.height )
    print( ".range:",   sc.range, ".scale:", sc.scale )
    print( ".center:",  sc.center )    # Camera
    print( ".forward:", sc.forward, ".fov:", sc.fov )
    print( "Mouse:",    sc.mouse.camera, "ray:", sc.mouse.ray )
    print( ".ambient:", sc.ambient )
    print( "Lights:",   sc.lights  )    # distant_light
    print( "objects:", objCount(), scene.objects )
    
#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+...

scene.width  = 600
scene.height = 400
scene.range  = 4
#scene.autocenter = True
#scene.background = color.gray(0.2)
scene.background = next(bg)

autoDemo = -1

print( msg )


## Create cuboid (aka "box") :

# c = box()     # using default-values --> cube
# c = box(pos=(0,0,0), length=4, height=2, width=3, axis=(-0.1,-0.1,0.1) )
##c  = box(pos =( 0.0, 0.0, 0.0 ),
##         size=( 4, 2, 3 ),            # L,H,W
##         axis=( 1.0, 0.0, 0.0 ),
##         up  =( 0.0, 1.0, 0.0 ),
##         color   = color.orange,
##         opacity = 1.0,
##         material= materials.marble
##         )
c  = box(pos =( 0.0, 0.0, 0.0 ),
         size=( 4, 2, 3 ),            # L,H,W
         axis=( 1.0, 0.0, 0.0 ),
         up  =( 0.0, 1.0, 0.0 )
         )
print("Box:", c)
paint(c)     # c.color    = color.red
solid(c)     # c.opacity  = 1.0
surface(c)   # c.material = materials.marble

rotX(c,0.4)         # rotate box, to bring three faces into view
rotY(c,0.6)

#sceneInfo(scene)
#objInfo(c)
print("\nPress 'a' to start auto-running demo.")

#...+....1....+....2....+....3....+....4....+....5....+....6....+....7....+...


## Processing of input:

cCount = 0
def click():
    global cCount
    cCount=cCount+1
    sceneInfo(scene)
    objInfo(c)
scene.bind( 'click', click )

def keyInput():
    key = scene.kb.getkey()
    print( 'Key: "%s"' % key )

    if ( (key == 'esc') or (key == 'q') ) :
        print( "Bye!" )
        exit(0)
    else :
        cmd(key)
scene.bind('keydown', keyInput)

def cmd(key):
    global autoDemo
    if (key == 'h') :  print( msg )
    if (key == '?') :  print( msg )
    if (key == 's') :  sceneInfo(scene)
    if (key == 'i') :  objInfo(c)

    if (key == 'x') :  rotX(c, 0.1)
    if (key == 'X') :  rotX(c,-0.1)
    if (key == 'y') :  rotY(c, 0.1)
    if (key == 'Y') :  rotY(c,-0.1)
    if (key == 'z') :  rotZ(c, 0.1)
    if (key == 'Z') :  rotZ(c,-0.1)

    if (key == 'c') :  paint(c)
    if (key == 'o') :  solid(c)
    if (key == 'm') :  surface(c)

    if (key == 'b') :  backgr()
    if (key == 'r') :  rotAngle()
    if (key == 'R') :  rotAxis()
    if (key == 'd') :  demoStep()
    if (key == 'a') :  autoDemo = -autoDemo
    if (key == 'A') :  autoDemo = -autoDemo
    if (key == ' ') :  stop()

def stop() :
    global autoDemo, rotAn
    autoDemo = -1
    while rotAn <> 0 :
      rotAngle() 
    print("**Stop**")
      
r=100
t=0
while True:                 # Animation-loop
    rate(50)
    t = t+1
    if rotAn != 0 :
        c.rotate( angle=rotAn, axis=rotAx )

    if t>=r :
        t=0
        if autoDemo>0 :
            demoStep()

```

