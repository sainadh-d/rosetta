# Blum integer

## Task Link
[Rosetta Code - Blum integer](https://rosettacode.org/wiki/Blum_integer)

## Java Code
### java_code_1.txt
```java
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <iostream>
#include <vector>

bool is_prime_type_3(const int32_t number) {
	if ( number < 2 ) return false;
	if ( number % 2 == 0 ) return false;
	if ( number % 3 == 0 ) return number == 3;

	for ( int divisor = 5; divisor * divisor <= number; divisor += 2 ) {
		if ( number % divisor == 0 ) { return false; }
	}

	return number % 4 == 3;
}

int32_t least_prime_factor(const int32_t number) {
	if ( number == 1 ) { return 1; }
    if ( number % 3 == 0 ) { return 3; }
    if ( number % 5 == 0 ) { return 5; }

    for ( int divisor = 7; divisor * divisor <= number; divisor += 2 ) {
		if ( number % divisor == 0 ) { return divisor; }
	}

	return number;
}

int main() {
	int32_t blums[50];
	int32_t blum_count = 0;
	int32_t last_digit_counts[10] = {};
	int32_t number = 1;

	while ( blum_count < 400'000 ) {
		const int32_t prime = least_prime_factor(number);
		if ( prime % 4 == 3 ) {
			const int32_t quotient = number / prime;
			if ( quotient != prime && is_prime_type_3(quotient) ) {
				if ( blum_count < 50 ) {
					blums[blum_count] = number;
				}
				last_digit_counts[number % 10] += 1;
				blum_count += 1;
				if ( blum_count == 50 ) {
					std::cout << "The first 50 Blum integers:" << std::endl;
					for ( int32_t i = 0; i < 50; ++i ) {
						std::cout << std::setw(3) << blums[i] << ( ( i % 10 == 9 ) ? "\n" : " " );
					}
					std::cout << std::endl;
				} else if ( blum_count == 26'828 || blum_count % 100'000 == 0 ) {
					std::cout << "The " << std::setw(6) << blum_count << "th Blum integer is: "
						<< std::setw(7) << number << std::endl;
					if ( blum_count == 400'000 ) {
						std::cout << "\nPercent distribution of the first 400000 Blum integers:" << std::endl;
						for ( const int32_t& i : { 1, 3, 7, 9 } ) {
							std::cout << "    " << std::setw(6) << std::setprecision(5)
								<< (double) last_digit_counts[i] / 4'000 << "% end in " << i << std::endl;
						}
					}
				}
			}
		}
		number += ( number % 5 == 3 ) ? 4 : 2;
	}
}

```

### java_code_2.txt
```java
import java.util.HashMap;
import java.util.Map;

public final class BlumInteger {

	public static void main(String[] aArgs) {
		int[] blums = new int[50];
		int blumCount = 0;
		Map<Integer, Integer> lastDigitCounts = new HashMap<Integer, Integer>();
		int number = 1;
		
		while ( blumCount < 400_000 ) {			
			final int prime = leastPrimeFactor(number);
			if ( prime % 4 == 3 ) {
				final int quotient = number / prime;
				if ( quotient != prime && isPrimeType3(quotient) ) {
					if ( blumCount < 50 ) {
						blums[blumCount] = number;
					}
					lastDigitCounts.merge(number % 10, 1, Integer::sum);
					blumCount += 1;
					if ( blumCount == 50 ) {
						System.out.println("The first 50 Blum integers:");
						for ( int i = 0; i < 50; i++ ) {
							System.out.print(String.format("%3d", blums[i]));
							System.out.print(( i % 10 == 9 ) ? System.lineSeparator() : " ");
						}
						System.out.println();
					} else if ( blumCount == 26_828 || blumCount % 100_000 == 0 ) {
						System.out.println(String.format("%s%6d%s%7d",
							"The ", blumCount, "th Blum integer is: ", number));
						if ( blumCount == 400_000 ) {
							System.out.println();
							System.out.println("Percent distribution of the first 400000 Blum integers:");
							for ( int key : lastDigitCounts.keySet() ) {
		            			System.out.println(String.format("%s%6.3f%s%d",
		            				"    ", (double) lastDigitCounts.get(key) / 4_000, "% end in ", key));
							}
						}
					}
				}
			}
			number += ( number % 5 == 3 ) ? 4 : 2;
		}
	}
	
	private static boolean isPrimeType3(int aNumber) {
		if ( aNumber < 2 ) { return false; }
		if ( aNumber % 2 == 0 ) { return false; }
		if ( aNumber % 3 == 0 ) { return aNumber == 3; }

		for ( int divisor = 5; divisor * divisor <= aNumber; divisor += 2 ) {
			if ( aNumber % divisor == 0 ) { return false; }
		}		
		return aNumber % 4 == 3;
	}

	private static int leastPrimeFactor(int aNumber) {
		if ( aNumber == 1 ) { return 1; }
	    if ( aNumber % 3 == 0 ) { return 3; }
	    if ( aNumber % 5 == 0 ) { return 5; }
	    
	    for ( int divisor = 7; divisor * divisor <= aNumber; divisor += 2 ) {
	    	if ( aNumber % divisor == 0 ) { return divisor; }
	    }	
		return aNumber;
	}

}

```

## Python Code
### python_code_1.txt
```python
''' python example for task rosettacode.org/wiki/Blum_integer '''

from sympy import factorint


def generate_blum():
    ''' Generate the Blum integers in series '''
    for candidate in range(1, 10_000_000_000):
        fexp = factorint(candidate).items()
        if len(fexp) == 2 and sum(p[1] == 1 and p[0] % 4 == 3 for p in fexp) == 2:
            yield candidate


print('First 50 Blum integers:')
lastdigitsums = [0, 0, 0, 0]

for idx, blum in enumerate(generate_blum()):
    if idx < 50:
        print(f'{blum: 4}', end='\n' if (idx + 1) % 10 == 0 else '')
    elif idx + 1 in [26_828, 100_000, 200_000, 300_000, 400_000]:
        print(f'\nThe {idx+1:,}th Blum number is {blum:,}.')

    j = blum % 10
    lastdigitsums[0] += j == 1
    lastdigitsums[1] += j == 3
    lastdigitsums[2] += j == 7
    lastdigitsums[3] += j == 9

    if idx + 1 == 400_000:
        print('\n% distribution of the first 400,000 Blum integers is:')
        for k, dig in enumerate([1, 3, 7, 9]):
            print(f'{lastdigitsums[k]/4000:>8.5}% end in {dig}')

        break

```

