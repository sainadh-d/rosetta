# Apply a digital filter (direct form II transposed)

## Task Link
[Rosetta Code - Apply a digital filter (direct form II transposed)](https://rosettacode.org/wiki/Apply_a_digital_filter_(direct_form_II_transposed))

## Java Code
### java_code_1.txt
```java
public class DigitalFilter {
    private static double[] filter(double[] a, double[] b, double[] signal) {
        double[] result = new double[signal.length];
        for (int i = 0; i < signal.length; ++i) {
            double tmp = 0.0;
            for (int j = 0; j < b.length; ++j) {
                if (i - j < 0) continue;
                tmp += b[j] * signal[i - j];
            }
            for (int j = 1; j < a.length; ++j) {
                if (i - j < 0) continue;
                tmp -= a[j] * result[i - j];
            }
            tmp /= a[0];
            result[i] = tmp;
        }
        return result;
    }

    public static void main(String[] args) {
        double[] a = new double[]{1.00000000, -2.77555756e-16, 3.33333333e-01, -1.85037171e-17};
        double[] b = new double[]{0.16666667, 0.5, 0.5, 0.16666667};

        double[] signal = new double[]{
            -0.917843918645, 0.141984778794, 1.20536903482, 0.190286794412,
            -0.662370894973, -1.00700480494, -0.404707073677, 0.800482325044,
            0.743500089861, 1.01090520172, 0.741527555207, 0.277841675195,
            0.400833448236, -0.2085993586, -0.172842103641, -0.134316096293,
            0.0259303398477, 0.490105989562, 0.549391221511, 0.9047198589
        };

        double[] result = filter(a, b, signal);
        for (int i = 0; i < result.length; ++i) {
            System.out.printf("% .8f", result[i]);
            System.out.print((i + 1) % 5 != 0 ? ", " : "\n");
        }
    }
}

```

## Python Code
### python_code_1.txt
```python
#!/bin/python
from __future__ import print_function
from scipy import signal
import matplotlib.pyplot as plt

if __name__=="__main__":
	sig = [-0.917843918645,0.141984778794,1.20536903482,0.190286794412,-0.662370894973,-1.00700480494,
		-0.404707073677,0.800482325044,0.743500089861,1.01090520172,0.741527555207,
		0.277841675195,0.400833448236,-0.2085993586,-0.172842103641,-0.134316096293,
		0.0259303398477,0.490105989562,0.549391221511,0.9047198589]

	#Create an order 3 lowpass butterworth filter
	#Generated using b, a = signal.butter(3, 0.5)
	a = [1.00000000, -2.77555756e-16, 3.33333333e-01, -1.85037171e-17]
	b = [0.16666667, 0.5, 0.5, 0.16666667]

	#Apply the filter to signal
	filt = signal.lfilter(b, a, sig)
	print (filt)

	plt.plot(sig, 'b')
	plt.plot(filt, 'r--')
	plt.show()

```

