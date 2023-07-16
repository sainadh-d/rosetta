# Pseudo-random numbers/PCG32

## Task Link
[Rosetta Code - Pseudo-random numbers/PCG32](https://rosettacode.org/wiki/Pseudo-random_numbers/PCG32)

## Java Code
### java_code_1.txt
```java
public class PCG32 {
    private static final long N = 6364136223846793005L;

    private long state = 0x853c49e6748fea9bL;
    private long inc = 0xda3e39cb94b95bdbL;

    public void seed(long seedState, long seedSequence) {
        state = 0;
        inc = (seedSequence << 1) | 1;
        nextInt();
        state = state + seedState;
        nextInt();
    }

    public int nextInt() {
        long old = state;
        state = old * N + inc;
        int shifted = (int) (((old >>> 18) ^ old) >>> 27);
        int rot = (int) (old >>> 59);
        return (shifted >>> rot) | (shifted << ((~rot + 1) & 31));
    }

    public double nextFloat() {
        var u = Integer.toUnsignedLong(nextInt());
        return (double) u / (1L << 32);
    }

    public static void main(String[] args) {
        var r = new PCG32();

        r.seed(42, 54);
        System.out.println(Integer.toUnsignedString(r.nextInt()));
        System.out.println(Integer.toUnsignedString(r.nextInt()));
        System.out.println(Integer.toUnsignedString(r.nextInt()));
        System.out.println(Integer.toUnsignedString(r.nextInt()));
        System.out.println(Integer.toUnsignedString(r.nextInt()));
        System.out.println();

        int[] counts = {0, 0, 0, 0, 0};
        r.seed(987654321, 1);
        for (int i = 0; i < 100_000; i++) {
            int j = (int) Math.floor(r.nextFloat() * 5.0);
            counts[j]++;
        }

        System.out.println("The counts for 100,000 repetitions are:");
        for (int i = 0; i < counts.length; i++) {
            System.out.printf("  %d : %d\n", i, counts[i]);
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
mask64 = (1 << 64) - 1
mask32 = (1 << 32) - 1
CONST = 6364136223846793005


class PCG32():
    
    def __init__(self, seed_state=None, seed_sequence=None):
        if all(type(x) == int for x in (seed_state, seed_sequence)):
            self.seed(seed_state, seed_sequence)
        else:
            self.state = self.inc = 0
    
    def seed(self, seed_state, seed_sequence):
        self.state = 0
        self.inc = ((seed_sequence << 1) | 1) & mask64
        self.next_int()
        self.state = (self.state + seed_state)
        self.next_int()
        
    def next_int(self):
        "return random 32 bit unsigned int"
        old = self.state
        self.state = ((old * CONST) + self.inc) & mask64
        xorshifted = (((old >> 18) ^ old) >> 27) & mask32
        rot = (old >> 59) & mask32
        answer = (xorshifted >> rot) | (xorshifted << ((-rot) & 31))
        answer = answer &mask32
        
        return answer
    
    def  next_float(self):
        "return random float between 0 and 1"
        return self.next_int() / (1 << 32)
    

if __name__ == '__main__':
    random_gen = PCG32()
    random_gen.seed(42, 54)
    for i in range(5):
        print(random_gen.next_int())
        
    random_gen.seed(987654321, 1)
    hist = {i:0 for i in range(5)}
    for i in range(100_000):
        hist[int(random_gen.next_float() *5)] += 1
    print(hist)

```

### python_code_2.txt
```python
def pcg32(seed_state=None, seed_sequence=None, as_int=True):
    def next_int():
        "return random 32 bit unsigned int"
        nonlocal state, inc

        state, xorshifted, rot = (((state * CONST) + inc) & mask64,
                                  (((state >> 18) ^ state) >> 27) & mask32,
                                  (state >> 59) & mask32)
        answer = (((xorshifted >> rot) | (xorshifted << ((-rot) & 31)))
                  & mask32)
        return answer

    # Seed
    state = inc = 0
    if all(type(x) == int for x in (seed_state, seed_sequence)):
        inc = ((seed_sequence << 1) | 1) & mask64
        next_int()
        state += seed_state
        next_int()

    while True:
        yield next_int() if as_int else next_int() / (1 << 32)


if  __name__ == '__main__':
    from itertools import islice

    for i in islice(pcg32(42, 54), 5):
        print(i)
    hist = {i:0 for i in range(5)}
    for i in islice(pcg32(987654321, 1, as_int=False), 100_000):
        hist[int(i * 5)] += 1
    print(hist)

```

