# Conjugate transpose

## Task Link
[Rosetta Code - Conjugate transpose](https://rosettacode.org/wiki/Conjugate_transpose)

## Java Code
### java_code_1.txt
```java
import java.util.Arrays;
import java.util.List;

public final class ConjugateTranspose {

	public static void main(String[] aArgs) {		
		ComplexMatrix one = new ComplexMatrix( new Complex[][] { { new Complex(0, 4), new Complex(-1, 1) },
											                     { new Complex(1, -1), new Complex(0, 4) } } );		

		ComplexMatrix two = new ComplexMatrix(
			new Complex[][] { { new Complex(1, 0), new Complex(1, 1), new Complex(0, 2) },
			     			  { new Complex(1, -1), new Complex(5, 0), new Complex(-3, 0) },
							  { new Complex(0, -2), new Complex(-3, 0), new Complex(0, 0) } } );

		final double term = 1.0 / Math.sqrt(2.0);
		ComplexMatrix three = new ComplexMatrix( new Complex[][] { { new Complex(term, 0), new Complex(term, 0) },
																   { new Complex(0, term), new Complex(0, -term) } } );
		
		List<ComplexMatrix> matricies = List.of( one, two, three );
		for ( ComplexMatrix matrix : matricies ) {
			System.out.println("Matrix:");
			matrix.display();
			System.out.println("Conjugate transpose:");
			matrix.conjugateTranspose().display();
			System.out.println("Hermitian: " + matrix.isHermitian());
			System.out.println("Normal: " + matrix.isNormal());
			System.out.println("Unitary: " + matrix.isUnitary() + System.lineSeparator());
		}
	}

}

final class ComplexMatrix {
	
	public ComplexMatrix(Complex[][] aData) {
		rowCount = aData.length;
        colCount = aData[0].length;
        data = Arrays.stream(aData).map( row -> Arrays.copyOf(row, row.length) ).toArray(Complex[][]::new);
	}  
	
	public ComplexMatrix multiply(ComplexMatrix aOther) {
        if ( colCount != aOther.rowCount ) { 
        	throw new RuntimeException("Incompatible matrix dimensions.");
        }        
        Complex[][] newData = new Complex[rowCount][aOther.colCount];
        Arrays.stream(newData).forEach( row -> Arrays.fill(row, new Complex(0, 0)) );
        for ( int row = 0; row < rowCount; row++ ) {
            for ( int col = 0; col < aOther.colCount; col++ ) {
                for ( int k = 0; k < colCount; k++ ) {
                    newData[row][col] = newData[row][col].add(data[row][k].multiply(aOther.data[k][col]));
                }
            }
        }
        return new ComplexMatrix(newData);
    }     

    public ComplexMatrix conjugateTranspose() {
    	if ( rowCount != colCount ) {
    		throw new IllegalArgumentException("Only applicable to a square matrix");
    	}    	
    	Complex[][] newData = new Complex[colCount][rowCount];
        for ( int row = 0; row < rowCount; row++ ) {
            for ( int col = 0; col < colCount; col++ ) {
                newData[col][row] = data[row][col].conjugate();
            }
        }
        return new ComplexMatrix(newData);
    }
    
    public static ComplexMatrix identity(int aSize) {
    	Complex[][] data = new Complex[aSize][aSize];
        for ( int row = 0; row < aSize; row++ ) {
        	for ( int col = 0; col < aSize; col++ ) {
        		data[row][col] = ( row == col ) ? new Complex(1, 0) : new Complex(0, 0);
        	}
        }
        return new ComplexMatrix(data);
    }
    
    public boolean equals(ComplexMatrix aOther) {    	
        if ( aOther.rowCount != rowCount || aOther.colCount != colCount ) {
        	return false;
        }        
        for ( int row = 0; row < rowCount; row++ ) {
            for ( int col = 0; col < colCount; col++ ) {
            	if ( data[row][col].subtract(aOther.data[row][col]).modulus() > EPSILON ) {
                	return false;
                }
            }
        }
        return true;
    }      
    
    public void display() {
        for ( int row = 0; row < rowCount; row++ ) {
        	System.out.print("[");
            for ( int col = 0; col < colCount - 1; col++ ) { 
                System.out.print(data[row][col] + ", ");
            }
            System.out.println(data[row][colCount - 1] + " ]");
        }
    }
   
    public boolean isHermitian() {
    	return equals(conjugateTranspose());
    }
    
    public boolean isNormal() {
    	ComplexMatrix conjugateTranspose = conjugateTranspose();
    	return multiply(conjugateTranspose).equals(conjugateTranspose.multiply(this));
    }
    
    public boolean isUnitary() {
    	ComplexMatrix conjugateTranspose = conjugateTranspose();
    	return multiply(conjugateTranspose).equals(identity(rowCount)) &&
    		   conjugateTranspose.multiply(this).equals(identity(rowCount));
    }    
    
    private final int rowCount;
    private final int colCount;
    private final Complex[][] data;
    
    private static final double EPSILON = 0.000_000_000_001;
	
}

final class Complex {
	
	public Complex(double aReal, double aImag) {
		real = aReal;
		imag = aImag;
	}		
	
	public Complex add(Complex aOther) {
		return new Complex(real + aOther.real, imag + aOther.imag);
	}
	
	public Complex multiply(Complex aOther) {
		return new Complex(real * aOther.real - imag * aOther.imag, real * aOther.imag + imag * aOther.real);
	}
	
	public Complex negate() {
		return new Complex(-real, -imag);
	}
	
	public Complex subtract(Complex aOther) {
		return this.add(aOther.negate());
	}
	
	public Complex conjugate() {
		return new Complex(real, -imag);
	}
		
	public double modulus() {
		return Math.hypot(real, imag);
	}
	
	public boolean equals(Complex aOther) {
		return real == aOther.real && imag == aOther.imag;
	}
	
	@Override
	public String toString() {
		String prefix = ( real < 0.0 ) ? "" : " ";
		String realPart = prefix + String.format("%.3f", real);
		String sign = ( imag < 0.0 ) ? " - " : " + ";
		return realPart + sign + String.format("%.3f", Math.abs(imag)) + "i";
	}
	
	private final double real;
	private final double imag;
	
}

```

## Python Code
### python_code_1.txt
```python
def conjugate_transpose(m):
    return tuple(tuple(n.conjugate() for n in row) for row in zip(*m))

def mmul( ma, mb):
    return tuple(tuple(sum( ea*eb for ea,eb in zip(a,b)) for b in zip(*mb)) for a in ma)

def mi(size):
    'Complex Identity matrix'
    sz = range(size)
    m = [[0 + 0j for i in sz] for j in sz]
    for i in range(size):
        m[i][i] = 1 + 0j
    return tuple(tuple(row) for row in m)

def __allsame(vector):
    first, rest = vector[0], vector[1:]
    return all(i == first for i in rest)

def __allnearsame(vector, eps=1e-14):
    first, rest = vector[0], vector[1:]
    return all(abs(first.real - i.real) < eps and abs(first.imag - i.imag) < eps
               for i in rest)

def isequal(matrices, eps=1e-14):
    'Check any number of matrices for equality within eps'
    x = [len(m) for m in matrices]
    if not __allsame(x): return False
    y = [len(m[0]) for m in matrices]
    if not __allsame(y): return False
    for s in range(x[0]):
        for t in range(y[0]):
            if not __allnearsame([m[s][t] for m in matrices], eps): return False
    return True
    

def ishermitian(m, ct):
    return isequal([m, ct])

def isnormal(m, ct):
    return isequal([mmul(m, ct), mmul(ct, m)])

def isunitary(m, ct):
    mct, ctm = mmul(m, ct), mmul(ct, m)
    mctx, mcty, cmx, ctmy = len(mct), len(mct[0]), len(ctm), len(ctm[0])
    ident = mi(mctx)
    return isequal([mct, ctm, ident])

def printm(comment, m):
    print(comment)
    fields = [['%g%+gj' % (f.real, f.imag) for f in row] for row in m]
    width = max(max(len(f) for f in row) for row in fields)
    lines = (', '.join('%*s' % (width, f) for f in row) for row in fields)
    print('\n'.join(lines))

if __name__ == '__main__':
    for matrix in [
            ((( 3.000+0.000j), (+2.000+1.000j)), 
            (( 2.000-1.000j), (+1.000+0.000j))),

            ((( 1.000+0.000j), (+1.000+0.000j), (+0.000+0.000j)), 
            (( 0.000+0.000j), (+1.000+0.000j), (+1.000+0.000j)), 
            (( 1.000+0.000j), (+0.000+0.000j), (+1.000+0.000j))),

            ((( 2**0.5/2+0.000j), (+2**0.5/2+0.000j), (+0.000+0.000j)), 
            (( 0.000+2**0.5/2j), (+0.000-2**0.5/2j), (+0.000+0.000j)), 
            (( 0.000+0.000j), (+0.000+0.000j), (+0.000+1.000j)))]:
        printm('\nMatrix:', matrix)
        ct = conjugate_transpose(matrix)
        printm('Its conjugate transpose:', ct)
        print('Hermitian? %s.' % ishermitian(matrix, ct))
        print('Normal?    %s.' % isnormal(matrix, ct))
        print('Unitary?   %s.' % isunitary(matrix, ct))

```

