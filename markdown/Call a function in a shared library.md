# Call a function in a shared library

## Task Link
[Rosetta Code - Call a function in a shared library](https://rosettacode.org/wiki/Call_a_function_in_a_shared_library)

## Java Code
### java_code_1.txt
```java
/* TrySort.java */

import java.util.Collections;
import java.util.Random;

public class TrySort {
    static boolean useC;
    static {
	try {
	    System.loadLibrary("TrySort");
	    useC = true;
	} catch(UnsatisfiedLinkError e) {
	    useC = false;
	}
    }
    
    static native void sortInC(int[] ary);
    
    static class IntList extends java.util.AbstractList<Integer> {
	int[] ary;
	IntList(int[] ary) { this.ary = ary; }
	public Integer get(int i) { return ary[i]; }
	public Integer set(int i, Integer j) {
	    Integer o = ary[i]; ary[i] = j; return o;
	}
	public int size() { return ary.length; }
    }

    static class ReverseAbsCmp
	implements java.util.Comparator<Integer>
    {
	public int compare(Integer pa, Integer pb) {
	    /* Order from highest to lowest absolute value. */
	    int a = pa > 0 ? -pa : pa;
	    int b = pb > 0 ? -pb : pb;
	    return a < b ? -1 : a > b ? 1 : 0;
	}
    }
    
    static void sortInJava(int[] ary) {
	Collections.sort(new IntList(ary), new ReverseAbsCmp());
    }

    public static void main(String[] args) {
	/* Create an array of random integers. */
	int[] ary = new int[1000000];
	Random rng = new Random();
	for (int i = 0; i < ary.length; i++)
	    ary[i] = rng.nextInt();

	/* Do the reverse sort. */
	if (useC) {
	    System.out.print("Sorting in C...  ");
	    sortInC(ary);
	} else {
	    System.out.print
		("Missing library for C!  Sorting in Java...  ");
	    sortInJava(ary);
	}

	for (int i = 0; i < ary.length - 1; i++) {
	    int a = ary[i];
	    int b = ary[i + 1];
	    if ((a > 0 ? -a : a) > (b > 0 ? -b : b)) {
		System.out.println("*BUG IN SORT*");
		System.exit(1);
	    }
	}
	System.out.println("ok");
    }
}

```

### java_code_2.txt
```java
import com.sun.jna.Library;
import com.sun.jna.Native;

public class LoadLibJNA{
   private interface YourSharedLibraryName extends Library{
      //put shared library functions here with no definition
      public void sharedLibraryfunction();
   }

   public static void main(String[] args){
      YourSharedLibraryName lib = (YourSharedLibraryName)Native.loadLibrary("sharedLibrary",//as in "sharedLibrary.dll"
                                                                          YourSharedLibraryName.class);
      lib.sharedLibraryFunction();
   }
}

```

## Python Code
### python_code_1.txt
```python
import ctypes
  
user32_dll = ctypes.cdll.LoadLibrary('User32.dll')
print user32_dll.GetDoubleClickTime()

```

### python_code_2.txt
```python
>>> import ctypes
>>> # libc = ctypes.cdll.msvcrt # Windows
>>> # libc = ctypes.CDLL('libc.dylib') # Mac
>>> libc = ctypes.CDLL('libc.so') # Linux and most other *nix
>>> libc.printf(b'hi there, %s\n', b'world')
hi there, world.
17

```

### python_code_3.txt
```python
>>> from cffi import FFI
>>> ffi = FFI()
>>> ffi.cdef("""
...     int printf(const char *format, ...);   // copy-pasted from the man page
... """)
>>> C = ffi.dlopen(None)                     # loads the entire C namespace
>>> arg = ffi.new("char[]", b"world")         # equivalent to C code: char arg[] = "world";
>>> C.printf(b"hi there, %s.\n", arg)         # call printf
hi there, world.
17

```

