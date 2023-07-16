# Long multiplication

## Task Link
[Rosetta Code - Long multiplication](https://rosettacode.org/wiki/Long_multiplication)

## Java Code
### java_code_1.txt
```java
public class LongMult {

	private static byte[] stringToDigits(String num) {
		byte[] result = new byte[num.length()];
		for (int i = 0; i < num.length(); i++) {
			char c = num.charAt(i);
			if (c < '0' || c > '9') {
				throw new IllegalArgumentException("Invalid digit " + c
						+ " found at position " + i);
			}
			result[num.length() - 1 - i] = (byte) (c - '0');
		}
		return result;
	}

	public static String longMult(String num1, String num2) {
		byte[] left = stringToDigits(num1);
		byte[] right = stringToDigits(num2);
		byte[] result = new byte[left.length + right.length];
		for (int rightPos = 0; rightPos < right.length; rightPos++) {
			byte rightDigit = right[rightPos];
			byte temp = 0;
			for (int leftPos = 0; leftPos < left.length; leftPos++) {
				temp += result[leftPos + rightPos];
				temp += rightDigit * left[leftPos];
				result[leftPos + rightPos] = (byte) (temp % 10);
				temp /= 10;
			}
			int destPos = rightPos + left.length;
			while (temp != 0) {
				temp += result[destPos] & 0xFFFFFFFFL;
				result[destPos] = (byte) (temp % 10);
				temp /= 10;
				destPos++;
			}
		}
		StringBuilder stringResultBuilder = new StringBuilder(result.length);
		for (int i = result.length - 1; i >= 0; i--) {
			byte digit = result[i];
			if (digit != 0 || stringResultBuilder.length() > 0) {
				stringResultBuilder.append((char) (digit + '0'));
			}
		}
		return stringResultBuilder.toString();
	}

	public static void main(String[] args) {
		System.out.println(longMult("18446744073709551616",
				"18446744073709551616"));
	}
}

```

### java_code_2.txt
```java
import java.util.Arrays;

public class LongMultBinary {

	/**
	 * A very basic arbitrary-precision integer class. It only handles
	 * non-negative numbers and doesn't implement any arithmetic not necessary
	 * for the task at hand.
	 */
	public static class MyLongNum implements Cloneable {

		/*
		 * The actual bits of the integer, with the least significant place
		 * first. The biggest native integer type of Java is the 64-bit long,
		 * but since we need to be able to store the result of two digits
		 * multiplied, we have to use the second biggest native type, the 32-bit
		 * int. All numeric types are signed in Java, but we don't want to waste
		 * the sign bit, so we need to take extra care while doing arithmetic to
		 * ensure unsigned semantics.
		 */
		private int[] digits;

		/*
		 * The number of digits actually used in the digits array. Since arrays
		 * cannot be resized in Java, we are better off remembering the logical
		 * size ourselves, instead of reallocating and copying every time we need to shrink.
		 */
		private int digitsUsed;

		@Override
		public MyLongNum clone() {
			try {
				MyLongNum clone = (MyLongNum) super.clone();
				clone.digits = clone.digits.clone();
				return clone;
			} catch (CloneNotSupportedException e) {
				throw new Error("Object.clone() threw exception", e);
			}
		}

		private void resize(int newLength) {
			if (digits.length < newLength) {
				digits = Arrays.copyOf(digits, newLength);
			}
		}

		private void adjustDigitsUsed() {
			while (digitsUsed > 0 && digits[digitsUsed - 1] == 0) {
				digitsUsed--;
			}
		}

		/**
		 * "Short" multiplication by one digit. Used to convert strings to long numbers.
		 */
		public void multiply(int multiplier) {
			if (multiplier < 0) {
				throw new IllegalArgumentException(
						"Signed arithmetic isn't supported");
			}
			resize(digitsUsed + 1);
			long temp = 0;
			for (int i = 0; i < digitsUsed; i++) {
				temp += (digits[i] & 0xFFFFFFFFL) * multiplier;
				digits[i] = (int) temp; // store the low 32 bits
				temp >>>= 32;
			}
			digits[digitsUsed] = (int) temp;
			digitsUsed++;
			adjustDigitsUsed();
		}

		/**
		 * "Short" addition (adding a one-digit number). Used to convert strings to long numbers.
		 */
		public void add(int addend) {
			if (addend < 0) {
				throw new IllegalArgumentException(
						"Signed arithmetic isn't supported");
			}
			long temp = addend;
			for (int i = 0; i < digitsUsed && temp != 0; i++) {
				temp += (digits[i] & 0xFFFFFFFFL);
				digits[i] = (int) temp; // store the low 32 bits
				temp >>>= 32;
			}
			if (temp != 0) {
				resize(digitsUsed + 1);
				digits[digitsUsed] = (int) temp;
				digitsUsed++;
			}
		}

		/**
		 * "Short" division (dividing by a one-digit number). Used to convert numbers to strings.
		 * @param divisor The digit to divide by.
		 * @return The remainder of the division.
		 */
		public int divide(int divisor) {
			if (divisor < 0) {
				throw new IllegalArgumentException(
						"Signed arithmetic isn't supported");
			}
			int remainder = 0;
			for (int i = digitsUsed - 1; i >= 0; i--) {
				long twoDigits = (((long) remainder << 32) | (digits[i] & 0xFFFFFFFFL));
				remainder = (int) (twoDigits % divisor);
				digits[i] = (int) (twoDigits / divisor);
			}
			adjustDigitsUsed();
			return remainder;
		}

		public MyLongNum(String value) {
			// each of our 32-bit digits can store at least 9 decimal digit's worth
			this.digits = new int[value.length() / 9 + 1]; 
			this.digitsUsed = 0;
			// To lower the number of bignum operations, handle nine digits at a time.
			for (int i = 0; i < value.length(); i+=9) {
				String chunk = value.substring(i, Math.min(i+9, value.length()));
				int multiplier = 1;
				int addend = 0;
				for (int j=0; j<chunk.length(); j++) {
					char c = chunk.charAt(j);
					if (c < '0' || c > '9') {
						throw new IllegalArgumentException("Invalid digit " + c
								+ " found in input");
					}
					multiplier *= 10;
					addend *= 10;
					addend += c - '0';
				}
				multiply(multiplier);
				add(addend);
			}
		}

		@Override
		public String toString() {
			if (digitsUsed == 0) {
				return "0";
			}
			MyLongNum dummy = this.clone();
			StringBuilder resultBuilder = new StringBuilder(digitsUsed * 9);
			while (dummy.digitsUsed > 0) {
				// To limit the number of bignum divisions, handle nine digits at a time.
				int decimalDigits = dummy.divide(1000000000);
				for (int i=0; i<9; i++) {
					resultBuilder.append((char) (decimalDigits % 10 + '0'));
					decimalDigits /= 10;
				}
			}
			// Trim any leading zeros we may have created.
			while (resultBuilder.charAt(resultBuilder.length()-1) == '0') {
				resultBuilder.deleteCharAt(resultBuilder.length()-1);
			}
			return resultBuilder.reverse().toString();
		}

		/**
		 * Long multiplication.
		 */
		public void multiply(MyLongNum multiplier) {
			MyLongNum left, right;
			// Make sure the shorter number is on the right-hand side to make things a bit more efficient.
			if (this.digitsUsed > multiplier.digitsUsed) {
				left = this;
				right = multiplier;
			} else {
				left = multiplier;
				right = this;
			}
			int[] newDigits = new int[left.digitsUsed + right.digitsUsed];
			for (int rightPos = 0; rightPos < right.digitsUsed; rightPos++) {
				long rightDigit = right.digits[rightPos] & 0xFFFFFFFFL;
				long temp = 0;
				for (int leftPos = 0; leftPos < left.digitsUsed; leftPos++) {
					temp += (newDigits[leftPos + rightPos] & 0xFFFFFFFFL);
					temp += rightDigit * (left.digits[leftPos] & 0xFFFFFFFFL);
					newDigits[leftPos + rightPos] = (int) temp;
					temp >>>= 32;
				}
				// Roll forward any carry we may have.
				int destPos = rightPos + digitsUsed;
				while (temp != 0) {
					temp += (newDigits[destPos] & 0xFFFFFFFFL);
					newDigits[destPos] = (int) temp;
					temp >>>= 32;
					destPos++;
				}
			}
			this.digits = newDigits;
			this.digitsUsed = newDigits.length;
			adjustDigitsUsed();
		}
	}

	public static void main(String[] args) {
		MyLongNum one = new MyLongNum("18446744073709551616");
		MyLongNum two = one.clone();
		one.multiply(two);
		System.out.println(one);
	}

}

```

## Python Code
### python_code_1.txt
```python
#!/usr/bin/env python
print 2**64*2**64

```

### python_code_2.txt
```python
#!/usr/bin/env python

def add_with_carry(result, addend, addendpos):
    while True:
        while len(result) < addendpos + 1:
            result.append(0)
        addend_result = str(int(addend) + int(result[addendpos]))
        addend_digits = list(addend_result)
        result[addendpos] = addend_digits.pop()

        if not addend_digits:
            break
        addend = addend_digits.pop()
        addendpos += 1

def longhand_multiplication(multiplicand, multiplier):
    result = []
    for multiplicand_offset, multiplicand_digit in enumerate(reversed(multiplicand)):
        for multiplier_offset, multiplier_digit in enumerate(reversed(multiplier), start=multiplicand_offset):
            multiplication_result = str(int(multiplicand_digit) * int(multiplier_digit))

            for addend_offset, result_digit_addend in enumerate(reversed(multiplication_result), start=multiplier_offset):
                add_with_carry(result, result_digit_addend, addend_offset)

    result.reverse()

    return ''.join(result)

if __name__ == "__main__":
    sixtyfour = "18446744073709551616"

    onetwentyeight = longhand_multiplication(sixtyfour, sixtyfour)
    print(onetwentyeight)

```

### python_code_3.txt
```python
'''Long multiplication'''

from functools import reduce


def longmult(x, y):
    '''Long multiplication.'''
    return reduce(
        digitSum,
        polymul(digits(x), digits(y)), 0
    )


def digitSum(a, x):
    '''Left to right decimal digit summing.'''
    return a * 10 + x


def polymul(xs, ys):
    '''List of specific products.'''
    return map(
        lambda *vs: sum(filter(None, vs)),
        *[
            [0] * i + zs for i, zs in
            enumerate(mult_table(xs, ys))
        ]
    )


def mult_table(xs, ys):
    '''Rows of all products.'''
    return [[x * y for x in xs] for y in ys]


def digits(x):
    '''Digits of x as a list of integers.'''
    return [int(c) for c in str(x)]


if __name__ == '__main__':
    print(
        longmult(2 ** 64, 2 ** 64)
    )

```

