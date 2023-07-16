# Vector products

## Task Link
[Rosetta Code - Vector products](https://rosettacode.org/wiki/Vector_products)

## Java Code
### java_code_1.txt
```java
public class VectorProds{
    public static class Vector3D<T extends Number>{
        private T a, b, c;

        public Vector3D(T a, T b, T c){
            this.a = a;
            this.b = b;
            this.c = c;
        }

        public double dot(Vector3D<?> vec){
            return (a.doubleValue() * vec.a.doubleValue() +
                    b.doubleValue() * vec.b.doubleValue() +
                    c.doubleValue() * vec.c.doubleValue());
        }

        public Vector3D<Double> cross(Vector3D<?> vec){
            Double newA = b.doubleValue()*vec.c.doubleValue() - c.doubleValue()*vec.b.doubleValue();
            Double newB = c.doubleValue()*vec.a.doubleValue() - a.doubleValue()*vec.c.doubleValue();
            Double newC = a.doubleValue()*vec.b.doubleValue() - b.doubleValue()*vec.a.doubleValue();
            return new Vector3D<Double>(newA, newB, newC);
        }

        public double scalTrip(Vector3D<?> vecB, Vector3D<?> vecC){
            return this.dot(vecB.cross(vecC));
        }

        public Vector3D<Double> vecTrip(Vector3D<?> vecB, Vector3D<?> vecC){
            return this.cross(vecB.cross(vecC));
        }

        @Override
        public String toString(){
            return "<" + a.toString() + ", " + b.toString() + ", " + c.toString() + ">";
        }
    }

    public static void main(String[] args){
        Vector3D<Integer> a = new Vector3D<Integer>(3, 4, 5);
        Vector3D<Integer> b = new Vector3D<Integer>(4, 3, 5);
        Vector3D<Integer> c = new Vector3D<Integer>(-5, -12, -13);

        System.out.println(a.dot(b));
        System.out.println(a.cross(b));
        System.out.println(a.scalTrip(b, c));
        System.out.println(a.vecTrip(b, c));
    }
}

```

## Python Code
### python_code_1.txt
```python
def crossp(a, b):
    '''Cross product of two 3D vectors'''
    assert len(a) == len(b) == 3, 'For 3D vectors only'
    a1, a2, a3 = a
    b1, b2, b3 = b
    return (a2*b3 - a3*b2, a3*b1 - a1*b3, a1*b2 - a2*b1)
 
def dotp(a,b):
    '''Dot product of two eqi-dimensioned vectors'''
    assert len(a) == len(b), 'Vector sizes must match'
    return sum(aterm * bterm for aterm,bterm in zip(a, b))
 
def scalartriplep(a, b, c):
    '''Scalar triple product of three vectors: "a . (b x c)"'''
    return dotp(a, crossp(b, c))
 
def vectortriplep(a, b, c):
    '''Vector triple product of three vectors: "a x (b x c)"'''
    return crossp(a, crossp(b, c))
 
if __name__ == '__main__':
    a, b, c = (3, 4, 5), (4, 3, 5), (-5, -12, -13)
    print("a = %r;  b = %r;  c = %r" % (a, b, c))
    print("a . b = %r" % dotp(a,b))
    print("a x b = %r"  % (crossp(a,b),))
    print("a . (b x c) = %r" % scalartriplep(a, b, c))
    print("a x (b x c) = %r" % (vectortriplep(a, b, c),))

```

