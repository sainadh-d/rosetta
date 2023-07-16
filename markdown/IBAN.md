# IBAN

## Task Link
[Rosetta Code - IBAN](https://rosettacode.org/wiki/IBAN)

## Java Code
### java_code_1.txt
```java
import java.math.BigInteger;
import java.util.*;

public class IBAN {
    private static final String DEFSTRS = ""
            + "AL28 AD24 AT20 AZ28 BE16 BH22 BA20 BR29 BG22 "
            + "HR21 CY28 CZ24 DK18 DO28 EE20 FO18 FI18 FR27 GE22 DE22 GI23 "
            + "GL18 GT28 HU28 IS26 IE22 IL23 IT27 KZ20 KW30 LV21 LB28 LI21 "
            + "LT20 LU20 MK19 MT31 MR27 MU30 MC27 MD24 ME22 NL18 NO15 PK24 "
            + "PS29 PL28 PT25 RO24 SM27 SA24 RS22 SK24 SI19 ES24 SE24 CH21 "
            + "TN24 TR26 AE23 GB22 VG24 GR27 CR21";
    private static final Map<String, Integer> DEFINITIONS = new HashMap<>();

    static {
        for (String definition : DEFSTRS.split(" "))
            DEFINITIONS.put(definition.substring(0, 2), Integer.parseInt(definition.substring(2)));
    }

    public static void main(String[] args) {
        String[] ibans = {
                "GB82 WEST 1234 5698 7654 32",
                "GB82 TEST 1234 5698 7654 32",
                "GB81 WEST 1234 5698 7654 32",
                "SA03 8000 0000 6080 1016 7519",
                "CH93 0076 2011 6238 5295 7",
                "XX00 0000",
                "",
                "DE",
                "DE13 äöü_ 1234 1234 1234 12"};
        for (String iban : ibans)
            System.out.printf("%s is %s.%n", iban, validateIBAN(iban) ? "valid" : "not valid");
    }

    static boolean validateIBAN(String iban) {
        iban = iban.replaceAll("\\s", "").toUpperCase(Locale.ROOT);

        int len = iban.length();
        if (len < 4 || !iban.matches("[0-9A-Z]+") || DEFINITIONS.getOrDefault(iban.substring(0, 2), 0) != len)
            return false;

        iban = iban.substring(4) + iban.substring(0, 4);

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < len; i++)
            sb.append(Character.digit(iban.charAt(i), 36));

        BigInteger bigInt = new BigInteger(sb.toString());

        return bigInt.mod(BigInteger.valueOf(97)).intValue() == 1;
    }
}

```

## Python Code
### python_code_1.txt
```python
import re

_country2length = dict(
    AL=28, AD=24, AT=20, AZ=28, BE=16, BH=22, BA=20, BR=29,
    BG=22, CR=21, HR=21, CY=28, CZ=24, DK=18, DO=28, EE=20,
    FO=18, FI=18, FR=27, GE=22, DE=22, GI=23, GR=27, GL=18,
    GT=28, HU=28, IS=26, IE=22, IL=23, IT=27, KZ=20, KW=30,
    LV=21, LB=28, LI=21, LT=20, LU=20, MK=19, MT=31, MR=27,
    MU=30, MC=27, MD=24, ME=22, NL=18, NO=15, PK=24, PS=29,
    PL=28, PT=25, RO=24, SM=27, SA=24, RS=22, SK=24, SI=19,
    ES=24, SE=24, CH=21, TN=24, TR=26, AE=23, GB=22, VG=24 )

def valid_iban(iban):
    # Ensure upper alphanumeric input.
    iban = iban.replace(' ','').replace('\t','')
    if not re.match(r'^[\dA-Z]+$', iban): 
        return False
    # Validate country code against expected length.
    if len(iban) != _country2length[iban[:2]]:
        return False
    # Shift and convert.
    iban = iban[4:] + iban[:4]
    digits = int(''.join(str(int(ch, 36)) for ch in iban)) #BASE 36: 0..9,A..Z -> 0..35
    return digits % 97 == 1

if __name__ == '__main__':
    for account in ["GB82 WEST 1234 5698 7654 32", "GB82 TEST 1234 5698 7654 32"]:
        print('%s validation is: %s' % (account, valid_iban(account)))

```

