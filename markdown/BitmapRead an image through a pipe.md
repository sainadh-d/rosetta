# Bitmap/Read an image through a pipe

## Task Link
[Rosetta Code - Bitmap/Read an image through a pipe](https://rosettacode.org/wiki/Bitmap/Read_an_image_through_a_pipe)

## Java Code
## Python Code
### python_code_1.txt
```python
"""
Adapted from https://stackoverflow.com/questions/26937143/ppm-to-jpeg-jpg-conversion-for-python-3-4-1
Requires pillow-5.3.0 with Python 3.7.1 32-bit on Windows.
Sample ppm graphics files from http://www.cs.cornell.edu/courses/cs664/2003fa/images/
"""

from PIL import Image

# boxes_1.jpg is the jpg version of boxes_1.ppm

im = Image.open("boxes_1.jpg")
im.save("boxes_1v2.ppm")

```

