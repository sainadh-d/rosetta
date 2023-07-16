# Kaprekar numbers

## Task Link
[Rosetta Code - Kaprekar numbers](https://rosettacode.org/wiki/Kaprekar_numbers)

## Java Code
### java_code_1.txt
```java
public class Kaprekar {
    private static String[] splitAt(String str, int idx){
        String[] ans = new String[2];
        ans[0] = str.substring(0, idx);
        if(ans[0].equals("")) ans[0] = "0"; //parsing "" throws an exception
        ans[1] = str.substring(idx);
        return ans;
    }
        
    public static void main(String[] args){
        int count = 0;
        int base = (args.length > 0) ? Integer.parseInt(args[0]) : 10;
        for(long i = 1; i <= 1000000; i++){
            String sqrStr = Long.toString(i * i, base);
            for(int j = 0; j < sqrStr.length() / 2 + 1; j++){
                String[] parts = splitAt(sqrStr, j);
                long firstNum = Long.parseLong(parts[0], base);
                long secNum = Long.parseLong(parts[1], base);
                //if the right part is all zeroes, then it will be forever, so break
                if(secNum == 0) break;
                if(firstNum + secNum == i){
                    System.out.println(i + "\t" + Long.toString(i, base) +
                            "\t" + sqrStr + "\t" + parts[0] + " + " + parts[1]);
                    count++;
                    break;
                }
            }
        }
        System.out.println(count + " Kaprekar numbers < 1000000 (base 10) in base "+base);
    }
}

```

## Python Code
### python_code_1.txt
```python
>>> def k(n):
	n2 = str(n**2)
	for i in range(len(n2)):
		a, b = int(n2[:i] or 0), int(n2[i:])
		if b and a + b == n:
			return n
			#return (n, (n2[:i], n2[i:]))

		
>>> [x for x in range(1,10000) if k(x)]
[1, 9, 45, 55, 99, 297, 703, 999, 2223, 2728, 4879, 4950, 5050, 5292, 7272, 7777, 9999]
>>> len([x for x in range(1,1000000) if k(x)])
54
>>>

```

### python_code_2.txt
```python
def encode(n, base):
    result = ""
    while n:
        n, d = divmod(n, base)
        if d < 10:
            result += str(d)
        else:
            result += chr(d - 10 + ord("a"))
    return result[::-1]
def Kaprekar(n, base):
    if n == '1':
        return True
    sq = encode((int(n, base)**2), base)
    for i in range(1,len(sq)):
        if (int(sq[:i], base) + int(sq[i:], base) == int(n, base)) and (int(sq[:i], base) > 0) and (int(sq[i:], base)>0):
            return True
    return False
def Find(m, n, base):
    return [encode(i, base) for i in range(m,n+1) if Kaprekar(encode(i, base), base)]

m = int(raw_input('Where to start?\n'))
n = int(raw_input('Where to stop?\n'))
base = int(raw_input('Enter base:'))
KNumbers = Find(m, n, base)
for i in KNumbers:
    print i
print 'The number of Kaprekar Numbers found are',
print len(KNumbers)
raw_input()

```

### python_code_3.txt
```python
Base = 10
N = 6
Paddy_cnt = 1
for n in range(N):
  for V in CastOut(Base,Start=Base**n,End=Base**(n+1)):
    for B in range(n+1,n*2+2):
      x,y = divmod(V*V,Base**B)
      if V == x+y and 0<y:
        print('{1}: {0}'.format(V, Paddy_cnt))
        Paddy_cnt += 1
        break

```

### python_code_4.txt
```python
Base = 16
N = 4
Paddy_cnt = 1
for V in CastOut(Base,Start=1,End=Base**N):
  for B in range(1,N*2-1):
    x,y = divmod(V*V,Base**B)
    if V == x+y and 0<y:
      print('{1}: {0:x}'.format(V, Paddy_cnt))
      Paddy_cnt += 1
      break

```

