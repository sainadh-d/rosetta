# UPC

## Task Link
[Rosetta Code - UPC](https://rosettacode.org/wiki/UPC)

## Java Code
### java_code_1.txt
```java
import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.function.Consumer;
import java.util.function.Function;
import java.util.stream.Collectors;

public class UPC {
    private static final int SEVEN = 7;

    private static final Map<String, Integer> LEFT_DIGITS = Map.of(
        "   ## #", 0,
        "  ##  #", 1,
        "  #  ##", 2,
        " #### #", 3,
        " #   ##", 4,
        " ##   #", 5,
        " # ####", 6,
        " ### ##", 7,
        " ## ###", 8,
        "   # ##", 9
    );

    private static final Map<String, Integer> RIGHT_DIGITS = LEFT_DIGITS.entrySet()
        .stream()
        .collect(Collectors.toMap(
            entry -> entry.getKey()
                .replace(' ', 's')
                .replace('#', ' ')
                .replace('s', '#'),
            Map.Entry::getValue
        ));

    private static final String END_SENTINEL = "# #";
    private static final String MID_SENTINEL = " # # ";

    private static void decodeUPC(String input) {
        Function<String, Map.Entry<Boolean, List<Integer>>> decode = (String candidate) -> {
            int pos = 0;
            var part = candidate.substring(pos, pos + END_SENTINEL.length());

            List<Integer> output = new ArrayList<>();
            if (END_SENTINEL.equals(part)) {
                pos += END_SENTINEL.length();
            } else {
                return Map.entry(false, output);
            }

            for (int i = 1; i < SEVEN; i++) {
                part = candidate.substring(pos, pos + SEVEN);
                pos += SEVEN;

                if (LEFT_DIGITS.containsKey(part)) {
                    output.add(LEFT_DIGITS.get(part));
                } else {
                    return Map.entry(false, output);
                }
            }

            part = candidate.substring(pos, pos + MID_SENTINEL.length());
            if (MID_SENTINEL.equals(part)) {
                pos += MID_SENTINEL.length();
            } else {
                return Map.entry(false, output);
            }

            for (int i = 1; i < SEVEN; i++) {
                part = candidate.substring(pos, pos + SEVEN);
                pos += SEVEN;

                if (RIGHT_DIGITS.containsKey(part)) {
                    output.add(RIGHT_DIGITS.get(part));
                } else {
                    return Map.entry(false, output);
                }
            }

            part = candidate.substring(pos, pos + END_SENTINEL.length());
            if (!END_SENTINEL.equals(part)) {
                return Map.entry(false, output);
            }

            int sum = 0;
            for (int i = 0; i < output.size(); i++) {
                if (i % 2 == 0) {
                    sum += 3 * output.get(i);
                } else {
                    sum += output.get(i);
                }
            }
            return Map.entry(sum % 10 == 0, output);
        };

        Consumer<List<Integer>> printList = list -> {
            var it = list.iterator();
            System.out.print('[');
            if (it.hasNext()) {
                System.out.print(it.next());
            }
            while (it.hasNext()) {
                System.out.print(", ");
                System.out.print(it.next());
            }
            System.out.print(']');
        };

        var candidate = input.trim();
        var out = decode.apply(candidate);
        if (out.getKey()) {
            printList.accept(out.getValue());
            System.out.println();
        } else {
            StringBuilder builder = new StringBuilder(candidate);
            builder.reverse();
            out = decode.apply(builder.toString());
            if (out.getKey()) {
                printList.accept(out.getValue());
                System.out.println(" Upside down");
            } else if (out.getValue().size() == 12) {
                System.out.println("Invalid checksum");
            } else {
                System.out.println("Invalid digit(s)");
            }
        }
    }

    public static void main(String[] args) {
        var barcodes = List.of(
            "         # #   # ##  #  ## #   ## ### ## ### ## #### # # # ## ##  #   #  ##  ## ###  # ##  ## ### #  # #       ",
            "        # # #   ##   ## # #### #   # ## #   ## #   ## # # # ###  # ###  ##  ## ###  # #  ### ###  # # #         ",
            "         # #    # # #  ###  #   #    # #  #   #    # # # # ## #   ## #   ## #   ##   # # #### ### ## # #         ",
            "       # # ##  ## ##  ##   #  #   #  # ###  # ##  ## # # #   ## ##  #  ### ## ## #   # #### ## #   # #        ",
            "         # # ### ## #   ## ## ###  ##  # ##   #   # ## # # ### #  ## ##  #    # ### #  ## ##  #      # #          ",
            "          # #  #   # ##  ##  #   #   #  # ##  ##  #   # # # # #### #  ##  # #### #### # #  ##  # #### # #         ",
            "         # #  #  ##  ##  # #   ## ##   # ### ## ##   # # # #  #   #   #  #  ### # #    ###  # #  #   # #        ",
            "        # # #    # ##  ##   #  # ##  ##  ### #   #  # # # ### ## ## ### ## ### ### ## #  ##  ### ## # #         ",
            "         # # ### ##   ## # # #### #   ## # #### # #### # # #   #  # ###  #    # ###  # #    # ###  # # #       ",
            "        # # # #### ##   # #### # #   ## ## ### #### # # # #  ### # ###  ###  # # ###  #    # #  ### # #         "
        );
        barcodes.forEach(UPC::decodeUPC);
    }
}

```

## Python Code
### python_code_1.txt
```python
"""UPC-A barcode reader. Requires Python =>3.6"""
import itertools
import re

RE_BARCODE = re.compile(
    r"^(?P<s_quiet> +)"  # quiet zone
    r"(?P<s_guard># #)"  # start guard
    r"(?P<left>[ #]{42})"  # left digits
    r"(?P<m_guard> # # )"  # middle guard
    r"(?P<right>[ #]{42})"  # right digits
    r"(?P<e_guard># #)"  # end guard
    r"(?P<e_quiet> +)$"  # quiet zone
)

LEFT_DIGITS = {
    (0, 0, 0, 1, 1, 0, 1): 0,
    (0, 0, 1, 1, 0, 0, 1): 1,
    (0, 0, 1, 0, 0, 1, 1): 2,
    (0, 1, 1, 1, 1, 0, 1): 3,
    (0, 1, 0, 0, 0, 1, 1): 4,
    (0, 1, 1, 0, 0, 0, 1): 5,
    (0, 1, 0, 1, 1, 1, 1): 6,
    (0, 1, 1, 1, 0, 1, 1): 7,
    (0, 1, 1, 0, 1, 1, 1): 8,
    (0, 0, 0, 1, 0, 1, 1): 9,
}

RIGHT_DIGITS = {
    (1, 1, 1, 0, 0, 1, 0): 0,
    (1, 1, 0, 0, 1, 1, 0): 1,
    (1, 1, 0, 1, 1, 0, 0): 2,
    (1, 0, 0, 0, 0, 1, 0): 3,
    (1, 0, 1, 1, 1, 0, 0): 4,
    (1, 0, 0, 1, 1, 1, 0): 5,
    (1, 0, 1, 0, 0, 0, 0): 6,
    (1, 0, 0, 0, 1, 0, 0): 7,
    (1, 0, 0, 1, 0, 0, 0): 8,
    (1, 1, 1, 0, 1, 0, 0): 9,
}


MODULES = {
    " ": 0,
    "#": 1,
}

DIGITS_PER_SIDE = 6
MODULES_PER_DIGIT = 7


class ParityError(Exception):
    """Exception raised when a parity error is found."""


class ChecksumError(Exception):
    """Exception raised when check digit does not match."""


def group(iterable, n):
    """Chunk the iterable into groups of size ``n``."""
    args = [iter(iterable)] * n
    return tuple(itertools.zip_longest(*args))


def parse(barcode):
    """Return the 12 digits represented by the given barcode. Raises a
    ParityError if any digit fails the parity check."""
    match = RE_BARCODE.match(barcode)

    # Translate bars and spaces to 1s and 0s so we can do arithmetic
    # with them. Group "modules" into chunks of 7 as we go.
    left = group((MODULES[c] for c in match.group("left")), MODULES_PER_DIGIT)
    right = group((MODULES[c] for c in match.group("right")), MODULES_PER_DIGIT)

    # Parity check
    left, right = check_parity(left, right)

    # Lookup digits
    return tuple(
        itertools.chain(
            (LEFT_DIGITS[d] for d in left),
            (RIGHT_DIGITS[d] for d in right),
        )
    )


def check_parity(left, right):
    """Check left and right parity. Flip left and right if the barcode
    was scanned upside down."""
    # When reading from left to right, each digit on the left should
    # have odd parity, and each digit on the right should have even
    # parity.
    left_parity = sum(sum(d) % 2 for d in left)
    right_parity = sum(sum(d) % 2 for d in right)

    # Use left and right parity to check if the barcode was scanned
    # upside down. Flip it if it was.
    if left_parity == 0 and right_parity == DIGITS_PER_SIDE:
        _left = tuple(tuple(reversed(d)) for d in reversed(right))
        right = tuple(tuple(reversed(d)) for d in reversed(left))
        left = _left
    elif left_parity != DIGITS_PER_SIDE or right_parity != 0:
        # Error condition. Mixed parity.
        error = tuple(
            itertools.chain(
                (LEFT_DIGITS.get(d, "_") for d in left),
                (RIGHT_DIGITS.get(d, "_") for d in right),
            )
        )
        raise ParityError(" ".join(str(d) for d in error))

    return left, right


def checksum(digits):
    """Return the check digit for the given digits. Raises a
    ChecksumError if the check digit does not match."""
    odds = (digits[i] for i in range(0, 11, 2))
    evens = (digits[i] for i in range(1, 10, 2))

    check_digit = (sum(odds) * 3 + sum(evens)) % 10

    if check_digit != 0:
        check_digit = 10 - check_digit

    if digits[-1] != check_digit:
        raise ChecksumError(str(check_digit))

    return check_digit


def main():
    barcodes = [
        "         # #   # ##  #  ## #   ## ### ## ### ## #### # # # ## ##  #   #  ##  ## ###  # ##  ## ### #  # #       ",
        "        # # #   ##   ## # #### #   # ## #   ## #   ## # # # ###  # ###  ##  ## ###  # #  ### ###  # # #         ",
        "         # #    # # #  ###  #   #    # #  #   #    # # # # ## #   ## #   ## #   ##   # # #### ### ## # #         ",
        "       # # ##  ## ##  ##   #  #   #  # ###  # ##  ## # # #   ## ##  #  ### ## ## #   # #### ## #   # #        ",
        "         # # ### ## #   ## ## ###  ##  # ##   #   # ## # # ### #  ## ##  #    # ### #  ## ##  #      # #          ",
        "          # #  #   # ##  ##  #   #   #  # ##  ##  #   # # # # #### #  ##  # #### #### # #  ##  # #### # #         ",
        "         # #  #  ##  ##  # #   ## ##   # ### ## ##   # # # #  #   #   #  #  ### # #    ###  # #  #   # #        ",
        "        # # #    # ##  ##   #  # ##  ##  ### #   #  # # # ### ## ## ### ## ### ### ## #  ##  ### ## # #         ",
        "         # # ### ##   ## # # #### #   ## # #### # #### # # #   #  # ###  #    # ###  # #    # ###  # # #       ",
        "        # # # #### ##   # #### # #   ## ## ### #### # # # #  ### # ###  ###  # # ###  #    # #  ### # #         ",
        "        # # # #### ##   # #### # #   ## ## ### #### # # # #  ### # ###  ###  # # ###  ## ##  #  ### # #         ",
    ]

    for barcode in barcodes:
        try:
            digits = parse(barcode)
        except ParityError as err:
            print(f"{err} parity error!")
            continue

        try:
            check_digit = checksum(digits)
        except ChecksumError as err:
            print(f"{' '.join(str(d) for d in digits)} checksum error! ({err})")
            continue

        print(f"{' '.join(str(d) for d in digits)}")


if __name__ == "__main__":
    main()

```

