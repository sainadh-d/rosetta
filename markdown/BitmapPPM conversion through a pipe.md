# Bitmap/PPM conversion through a pipe

## Task Link
[Rosetta Code - Bitmap/PPM conversion through a pipe](https://rosettacode.org/wiki/Bitmap/PPM_conversion_through_a_pipe)

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

im = Image.open("boxes_1.ppm")
im.save("boxes_1.jpg")

```

