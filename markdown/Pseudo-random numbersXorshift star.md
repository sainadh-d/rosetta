# Pseudo-random numbers/Xorshift star

## Task Link
[Rosetta Code - Pseudo-random numbers/Xorshift star](https://rosettacode.org/wiki/Pseudo-random_numbers/Xorshift_star)

## Java Code
### java_code_1.txt
```java
public class XorShiftStar {
    private static final long MAGIC = Long.parseUnsignedLong("2545F4914F6CDD1D", 16);
    private long state;

    public void seed(long num) {
        state = num;
    }

    public int nextInt() {
        long x;
        int answer;

        x = state;
        x = x ^ (x >>> 12);
        x = x ^ (x << 25);
        x = x ^ (x >>> 27);
        state = x;
        answer = (int) ((x * MAGIC) >> 32);

        return answer;
    }

    public float nextFloat() {
        return (float) Integer.toUnsignedLong(nextInt()) / (1L << 32);
    }

    public static void main(String[] args) {
        var rng = new XorShiftStar();
        rng.seed(1234567);
        System.out.println(Integer.toUnsignedString(rng.nextInt()));
        System.out.println(Integer.toUnsignedString(rng.nextInt()));
        System.out.println(Integer.toUnsignedString(rng.nextInt()));
        System.out.println(Integer.toUnsignedString(rng.nextInt()));
        System.out.println(Integer.toUnsignedString(rng.nextInt()));
        System.out.println();

        int[] counts = {0, 0, 0, 0, 0};
        rng.seed(987654321);
        for (int i = 0; i < 100_000; i++) {
            int j = (int) Math.floor(rng.nextFloat() * 5.0);
            counts[j]++;
        }
        for (int i = 0; i < counts.length; i++) {
            System.out.printf("%d: %d\n", i, counts[i]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
mask64 = (1 << 64) - 1
mask32 = (1 << 32) - 1
const = 0x2545F4914F6CDD1D



class Xorshift_star():
    
    def __init__(self, seed=0):
        self.state = seed & mask64

    def seed(self, num):
        self.state =  num & mask64
    
    def next_int(self):
        "return random int between 0 and 2**32"
        x = self.state
        x = (x ^ (x >> 12)) & mask64
        x = (x ^ (x << 25)) & mask64
        x = (x ^ (x >> 27)) & mask64
        self.state = x
        answer = (((x * const) & mask64) >> 32) & mask32 
        return answer
    
    def  next_float(self):
        "return random float between 0 and 1"
        return self.next_int() / (1 << 32)
    

if __name__ == '__main__':
    random_gen = Xorshift_star()
    random_gen.seed(1234567)
    for i in range(5):
        print(random_gen.next_int())
        
    random_gen.seed(987654321)
    hist = {i:0 for i in range(5)}
    for i in range(100_000):
        hist[int(random_gen.next_float() *5)] += 1
    print(hist)

```

