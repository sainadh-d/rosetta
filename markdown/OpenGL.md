# OpenGL

## Task Link
[Rosetta Code - OpenGL](https://rosettacode.org/wiki/OpenGL)

## Java Code
### java_code_1.txt
```java
import org.lwjgl.LWJGLException;
import org.lwjgl.opengl.Display;
import org.lwjgl.opengl.DisplayMode;
import static org.lwjgl.opengl.GL11.*;


public class OpenGlExample {

	public void run() throws LWJGLException {
		Display.setDisplayMode(new DisplayMode(640, 480));
		Display.create();
		
		glMatrixMode(GL_PROJECTION);
		glLoadIdentity();
		glOrtho(-30, 30, -30, 30, -30, 30);
		glMatrixMode(GL_MODELVIEW);
		
		while(!Display.isCloseRequested()) {
			render();
			
			Display.update();
		}
		
		Display.destroy();
	}
	
	public void render() {
		
		glClearColor(0.3f, 0.3f, 0.3f, 0.0f);
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
		
		glShadeModel(GL_SMOOTH);
		
		glLoadIdentity();
		glTranslatef(-15.0f, -15.0f, 0.0f);
		
		glBegin(GL_TRIANGLES);
		glColor3f(1.0f, 0.0f, 0.0f);
		glVertex2f(0.0f, 0.0f);
		glColor3f(0.0f, 1.0f, 0.0f);
		glVertex2f(30f, 0.0f);
		glColor3f(0.0f, 0.0f, 1.0f);
		glVertex2f(0.0f, 30.0f);
		glEnd();
		
	}
	
	public static void main(String[] args) {
		OpenGlExample openGlExmpl = new OpenGlExample();
		try {
			openGlExmpl.run();
		} catch(LWJGLException e) {
			System.err.println(e);
		}
	}
	
}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
#-*- coding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLUT import *

def paint():
    glClearColor(0.3,0.3,0.3,0.0)
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

    glShadeModel(GL_SMOOTH)

    glLoadIdentity()
    glTranslatef(-15.0, -15.0, 0.0)

    glBegin(GL_TRIANGLES)
    glColor3f(1.0, 0.0, 0.0)
    glVertex2f(0.0, 0.0)
    glColor3f(0.0, 1.0, 0.0)
    glVertex2f(30.0, 0.0)
    glColor3f(0.0, 0.0, 1.0)
    glVertex2f(0.0, 30.0)
    glEnd()

    glFlush()

def reshape(width, height):
    glViewport(0, 0, width, height)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-30.0, 30.0, -30.0, 30.0, -30.0, 30.0)
    glMatrixMode(GL_MODELVIEW)

if __name__ == '__main__':
    glutInit(1, 1)
    glutInitWindowSize(640, 480)
    glutCreateWindow("Triangle")

    glutDisplayFunc(paint)
    glutReshapeFunc(reshape)

    glutMainLoop()

```

