# Pascal's triangle/Puzzle

## Task Link
[Rosetta Code - Pascal's triangle/Puzzle](https://rosettacode.org/wiki/Pascal%27s_triangle/Puzzle)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class PascalsTrianglePuzzle {

    public static void main(String[] args) {
        Matrix mat = new Matrix(Arrays.asList(1d, 0d, 0d, 0d, 0d, 0d, 0d, 0d, -1d, 0d, 0d), 
                                Arrays.asList(0d, 1d, 0d, 0d, 0d, 0d, 0d, 0d, 0d, -1d, 0d),
                                Arrays.asList(0d, 0d, 0d, 0d, 0d, 0d, 0d, 0d, -1d, 1d, -1d),
                                Arrays.asList(0d, 0d, 1d, 0d, 0d, 0d, 0d, 0d, 0d, -1d, 0d),
                                Arrays.asList(0d, 0d, 0d, 1d, 0d, 0d, 0d, 0d, 0d, 0d, -1d),
                                Arrays.asList(1d, 1d, 0d, 0d, 0d, 0d, 0d, 0d, 0d, 0d, 0d),
                                Arrays.asList(0d, 1d, 1d, 0d, -1d, 0d, 0d, 0d, 0d, 0d, 0d),
                                Arrays.asList(0d, 0d, 1d, 1d, 0d, -1d, 0d, 0d, 0d, 0d, 0d),
                                Arrays.asList(0d, 0d, 0d, 0d, -1d, 0d, 1d, 0d, 0d, 0d, 0d),
                                Arrays.asList(0d, 0d, 0d, 0d, 1d, 1d, 0d, -1d, 0d, 0d, 0d),
                                Arrays.asList(0d, 0d, 0d, 0d, 0d, 0d, 1d, 1d, 0d, 0d, 0d));
        List<Double> b = Arrays.asList(11d, 11d, 0d, 4d, 4d, 40d, 0d, 0d, 40d, 0d, 151d);
        List<Double> solution = cramersRule(mat, b);
        System.out.println("Solution = " + cramersRule(mat, b));
        System.out.printf("X = %.2f%n", solution.get(8));
        System.out.printf("Y = %.2f%n", solution.get(9));
        System.out.printf("Z = %.2f%n", solution.get(10));
    }
    
    private static List<Double> cramersRule(Matrix matrix, List<Double> b) {
        double denominator = matrix.determinant();
        List<Double> result = new ArrayList<>();
        for ( int i = 0 ; i < b.size() ; i++ ) {
            result.add(matrix.replaceColumn(b, i).determinant() / denominator);
        }
        return result;
    }
        
    private static class Matrix {
        
        private List<List<Double>> matrix;
        
        @Override
        public String toString() {
            return matrix.toString();
        }
        
        @SafeVarargs
        public Matrix(List<Double> ... lists) {
            matrix = new ArrayList<>();
            for ( List<Double> list : lists) {
                matrix.add(list);
            }
        }
        
        public Matrix(List<List<Double>> mat) {
            matrix = mat;
        }
        
        public double determinant() {
            if ( matrix.size() == 1 ) {
                return get(0, 0);
            }
            if ( matrix.size() == 2 ) {
                return get(0, 0) * get(1, 1) - get(0, 1) * get(1, 0);
            }
            double sum = 0;
            double sign = 1;
            for ( int i = 0 ; i < matrix.size() ; i++ ) {
                sum += sign * get(0, i) * coFactor(0, i).determinant();
                sign *= -1;
            }
            return sum;
        }
        
        private Matrix coFactor(int row, int col) {
            List<List<Double>> mat = new ArrayList<>();
            for ( int i = 0 ; i < matrix.size() ; i++ ) {
                if ( i == row ) {
                    continue;
                }
                List<Double> list = new ArrayList<>();
                for ( int j = 0 ; j < matrix.size() ; j++ ) {
                    if ( j == col ) {
                        continue;
                    }
                    list.add(get(i, j));
                }
                mat.add(list);
            }
            return new Matrix(mat);
        }

        private Matrix replaceColumn(List<Double> b, int column) {
            List<List<Double>> mat = new ArrayList<>();
            for ( int row = 0 ; row < matrix.size() ; row++ ) {
                List<Double> list = new ArrayList<>();
                for ( int col = 0 ; col < matrix.size() ; col++ ) {
                    double value = get(row, col);
                    if ( col == column ) {
                        value = b.get(row);
                    }
                    list.add(value);
                }
                mat.add(list);
            }
            return new Matrix(mat);
        }

        private double get(int row, int col) {
            return matrix.get(row).get(col);
        }
        
    }

}

```

## Python Code
### python_code_1.txt
```python
# Pyramid solver
#            [151]
#         [   ] [   ]
#      [ 40] [   ] [   ]
#   [   ] [   ] [   ] [   ]
#[ X ] [ 11] [ Y ] [ 4 ] [ Z ]
#  X -Y + Z = 0

def combine( snl, snr ):

	cl = {}
	if isinstance(snl, int):
		cl['1'] = snl
	elif isinstance(snl, string):
		cl[snl] = 1
	else:
		cl.update( snl)

	if isinstance(snr, int):
		n = cl.get('1', 0)
		cl['1'] = n + snr
	elif isinstance(snr, string):
		n = cl.get(snr, 0)
		cl[snr] = n + 1
	else:
		for k,v in snr.items():
			n = cl.get(k, 0)
			cl[k] = n+v
	return cl


def constrain(nsum, vn ):
	nn = {}
	nn.update(vn)
	n = nn.get('1', 0)
	nn['1'] = n - nsum
	return nn

def makeMatrix( constraints ):
	vmap = set()
	for c in constraints:
		vmap.update( c.keys())
	vmap.remove('1')
	nvars = len(vmap)
	vmap = sorted(vmap)		# sort here so output is in sorted order
	mtx = []
	for c in constraints:
		row = []
		for vv in vmap:
			row.append(float(c.get(vv, 0)))
		row.append(-float(c.get('1',0)))
		mtx.append(row)
	
	if len(constraints) == nvars:
		print 'System appears solvable'
	elif len(constraints) < nvars:
		print 'System is not solvable - needs more constraints.'
	return mtx, vmap


def SolvePyramid( vl, cnstr ):

	vl.reverse()
	constraints = [cnstr]
	lvls = len(vl)
	for lvln in range(1,lvls):
		lvd = vl[lvln]
		for k in range(lvls - lvln):
			sn = lvd[k]
			ll = vl[lvln-1]
			vn = combine(ll[k], ll[k+1])
			if sn is None:
				lvd[k] = vn
			else:
				constraints.append(constrain( sn, vn ))

	print 'Constraint Equations:'
	for cstr in constraints:
		fset = ('%d*%s'%(v,k) for k,v in cstr.items() )
		print ' + '.join(fset), ' = 0'

	mtx,vmap = makeMatrix(constraints)

	MtxSolve(mtx)

	d = len(vmap)
	for j in range(d):
		print vmap[j],'=', mtx[j][d]


def MtxSolve(mtx):
	# Simple Matrix solver...

	mDim = len(mtx)			# dimension---
	for j in range(mDim):
		rw0= mtx[j]
		f = 1.0/rw0[j]
		for k in range(j, mDim+1):
			rw0[k] *= f
		
		for l in range(1+j,mDim):
			rwl = mtx[l]
			f = -rwl[j]
			for k in range(j, mDim+1):
				rwl[k] += f * rw0[k]

	# backsolve part ---
	for j1 in range(1,mDim):
		j = mDim - j1
		rw0= mtx[j]
		for l in range(0, j):
			rwl = mtx[l]
			f = -rwl[j]
			rwl[j]    += f * rw0[j]
			rwl[mDim] += f * rw0[mDim]

	return mtx


p = [ [151], [None,None], [40,None,None], [None,None,None,None], ['X', 11, 'Y', 4, 'Z'] ]
addlConstraint = { 'X':1, 'Y':-1, 'Z':1, '1':0 }
SolvePyramid( p, addlConstraint)

```

### python_code_2.txt
```python
from csp import Problem

p = Problem()
pvars = "R2 R3 R5 R6 R7 R8 R9 R10 X Y Z".split()
# 0-151 is the possible finite range of the variables
p.addvars(pvars, xrange(152))
p.addrule("R7 == X + 11")
p.addrule("R8 == Y + 11")
p.addrule("R9 == Y + 4")
p.addrule("R10 == Z + 4")
p.addrule("R7 + R8 == 40")
p.addrule("R5 == R8 + R9")
p.addrule("R6 == R9 + R10")
p.addrule("R2 == 40 + R5")
p.addrule("R3 == R5 + R6")
p.addrule("R2 + R3 == 151")
p.addrule("Y == X + Z")
for sol in p.xsolutions():
    print [sol[k] for k in "XYZ"]

```

