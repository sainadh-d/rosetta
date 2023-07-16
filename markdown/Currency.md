# Currency

## Task Link
[Rosetta Code - Currency](https://rosettacode.org/wiki/Currency)

## Java Code
### java_code_1.txt
```java
import java.math.*;
import java.util.*;

public class Currency {
    final static String taxrate = "7.65";

    enum MenuItem {

        Hamburger("5.50"), Milkshake("2.86");

        private MenuItem(String p) {
            price = new BigDecimal(p);
        }

        public final BigDecimal price;
    }

    public static void main(String[] args) {
        Locale.setDefault(Locale.ENGLISH);

        MathContext mc = MathContext.DECIMAL128;

        Map<MenuItem, BigDecimal> order = new HashMap<>();
        order.put(MenuItem.Hamburger, new BigDecimal("4000000000000000"));
        order.put(MenuItem.Milkshake, new BigDecimal("2"));

        BigDecimal subtotal = BigDecimal.ZERO;
        for (MenuItem it : order.keySet())
            subtotal = subtotal.add(it.price.multiply(order.get(it), mc));

        BigDecimal tax = new BigDecimal(taxrate, mc);
        tax = tax.divide(new BigDecimal("100"), mc);
        tax = subtotal.multiply(tax, mc);

        System.out.printf("Subtotal: %20.2f%n", subtotal);
        System.out.printf("     Tax: %20.2f%n", tax);
        System.out.printf("   Total: %20.2f%n", subtotal.add(tax));
    }
}

```

## Python Code
### python_code_1.txt
```python
from decimal import Decimal as D
from collections import namedtuple

Item = namedtuple('Item', 'price, quant')

items = dict( hamburger=Item(D('5.50'), D('4000000000000000')),
              milkshake=Item(D('2.86'), D('2')) )
tax_rate = D('0.0765')

fmt = "%-10s %8s %18s %22s"
print(fmt % tuple('Item Price Quantity Extension'.upper().split()))

total_before_tax = 0
for item, (price, quant) in sorted(items.items()):
    ext = price * quant
    print(fmt % (item, price, quant, ext))
    total_before_tax += ext
print(fmt % ('', '', '', '--------------------'))
print(fmt % ('', '', 'subtotal', total_before_tax))

tax = (tax_rate * total_before_tax).quantize(D('0.00'))
print(fmt % ('', '', 'Tax', tax))

total = total_before_tax + tax
print(fmt % ('', '', '', '--------------------'))
print(fmt % ('', '', 'Total', total))

```

