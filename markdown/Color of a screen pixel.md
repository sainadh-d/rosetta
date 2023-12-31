# Color of a screen pixel

## Task Link
[Rosetta Code - Color of a screen pixel](https://rosettacode.org/wiki/Color_of_a_screen_pixel)

## Java Code
### java_code_1.txt
```java
public static Color getColorAt(int x, int y){
   return new Robot().getPixelColor(x, y);
}

```

## Python Code
### python_code_1.txt
```python
def get_pixel_colour(i_x, i_y):
	import win32gui
	i_desktop_window_id = win32gui.GetDesktopWindow()
	i_desktop_window_dc = win32gui.GetWindowDC(i_desktop_window_id)
	long_colour = win32gui.GetPixel(i_desktop_window_dc, i_x, i_y)
	i_colour = int(long_colour)
	win32gui.ReleaseDC(i_desktop_window_id,i_desktop_window_dc)
	return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)

print (get_pixel_colour(0, 0))

```

### python_code_2.txt
```python
def get_pixel_colour(i_x, i_y):
	import PIL.ImageGrab
	return PIL.ImageGrab.grab().load()[i_x, i_y]

print (get_pixel_colour(0, 0))

```

### python_code_3.txt
```python
def get_pixel_colour(i_x, i_y):
	import PIL.Image # python-imaging
	import PIL.ImageStat # python-imaging
	import Xlib.display # python-xlib
	o_x_root = Xlib.display.Display().screen().root
	o_x_image = o_x_root.get_image(i_x, i_y, 1, 1, Xlib.X.ZPixmap, 0xffffffff)
	o_pil_image_rgb = PIL.Image.fromstring("RGB", (1, 1), o_x_image.data, "raw", "BGRX")
	lf_colour = PIL.ImageStat.Stat(o_pil_image_rgb).mean
	return tuple(map(int, lf_colour))

print (get_pixel_colour(0, 0))

```

### python_code_4.txt
```python
def get_pixel_colour(i_x, i_y):
	import gtk # python-gtk2
	o_gdk_pixbuf = gtk.gdk.Pixbuf(gtk.gdk.COLORSPACE_RGB, False, 8, 1, 1)
	o_gdk_pixbuf.get_from_drawable(gtk.gdk.get_default_root_window(), gtk.gdk.colormap_get_system(), i_x, i_y, 0, 0, 1, 1)
	return tuple(o_gdk_pixbuf.get_pixels_array().tolist()[0][0])

print (get_pixel_colour(0, 0))

```

### python_code_5.txt
```python
def get_pixel_colour(i_x, i_y):
	import PyQt4.QtGui # python-qt4
	app = PyQt4.QtGui.QApplication([])
	long_qdesktop_id = PyQt4.QtGui.QApplication.desktop().winId()
	long_colour = PyQt4.QtGui.QPixmap.grabWindow(long_qdesktop_id, i_x, i_y, 1, 1).toImage().pixel(0, 0)
	i_colour = int(long_colour)
	return ((i_colour >> 16) & 0xff), ((i_colour >> 8) & 0xff), (i_colour & 0xff)

print (get_pixel_colour(0, 0))

```

