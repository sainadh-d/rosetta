# Constrained random points on a circle

## Task Link
[Rosetta Code - Constrained random points on a circle](https://rosettacode.org/wiki/Constrained_random_points_on_a_circle)

## Java Code
### java_code_1.txt
```java
import java.util.Random;

public class FuzzyCircle {
	static final Random rnd = new Random();
	public static void main(String[] args){
		char[][] field = new char[31][31];
		for(int i = 0; i < field.length; i++){
			for(int j = 0; j < field[i].length; j++){
				field[i][j] = ' ';
			}
		}
		int pointsInDisc = 0;
		while(pointsInDisc < 100){
			int x = rnd.nextInt(31) - 15;
			int y = rnd.nextInt(31) - 15;
			double dist = Math.hypot(x, y);
			if(dist >= 10 && dist <= 15 && field[x + 15][y + 15] == ' '){
				field[x + 15][y + 15] = 'X';
				pointsInDisc++;
			}
		}
		for(char[] row:field){
			for(char space:row){
				System.out.print(space);
			}
			System.out.println();
		}
	}
}

```

## Python Code
### python_code_1.txt
```python
>>> from collections import defaultdict
>>> from random import choice
>>> world = defaultdict(int)
>>> possiblepoints = [(x,y) for x in range(-15,16)
		  for y in range(-15,16)
		  if 10 <= abs(x+y*1j) <= 15]
>>> for i in range(100): world[choice(possiblepoints)] += 1

>>> for x in range(-15,16):
	print(''.join(str(min([9, world[(x,y)]])) if world[(x,y)] else ' '
			  for y in range(-15,16)))

	
                               
             1     1           
          1 1                  
      11 1     1  1     1      
     111  1     1211           
      1   2    1 1    11       
      1  11         21         
     1   1            11  1    
   1  2                1 1     
                               
 1  2                          
   1 1                      1  
   1 1                         
   2                      11   
  1                         1  
                         1     
                               
                               
  1                          1 
                         1     
                         2     
                            1  
     1                  1 1    
      1                2   1   
   1   3            11  2      
    11   1    1      1   2     
            1   1    2         
        1  1                   
         1      1     1        
          2 2   1              
               1

```

### python_code_2.txt
```python
>>> for i in range(1000): world[choice(possiblepoints)] += 1

>>> for x in range(-15,16):
	print(''.join(str(min([9, world[(x,y)]])) if world[(x,y)] else ' '
			  for y in range(-15,16)))

	
               2               
          41341421333          
        5133333131253 1        
      5231514 14214721 24      
     326 21222143234122322     
    54235153132123344125 22    
   32331432         2422 33    
   5453135           4144344   
  132595               323123  
  4 6353               432224  
 5 4323                 3 5313 
 23214                   41433 
 42454                   33342 
 332 4                   34314 
 142 1                   35 53 
124211                   53131 
 22221                   152 4 
 22213                   34562 
 654 4                   4 212 
 24354                   52232 
 544222                 283323 
  411123               453325  
  251321               124332  
   2124134           2443226   
   2 113315         64324334   
    2412452 324 32121132363    
      4222434324635 5433       
      3113333123432112633      
        2131181233  424        
          47414232164          
               4

```

