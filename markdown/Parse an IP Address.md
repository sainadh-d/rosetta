# Parse an IP Address

## Task Link
[Rosetta Code - Parse an IP Address](https://rosettacode.org/wiki/Parse_an_IP_Address)

## Java Code
### java_code_1.txt
```java
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class ParseIPAddress {

    public static void main(String[] args) {
        String [] tests = new String[] {"192.168.0.1", "127.0.0.1", "256.0.0.1", "127.0.0.1:80", "::1", "[::1]:80", "[32e::12f]:80", "2605:2700:0:3::4713:93e3", "[2605:2700:0:3::4713:93e3]:80", "2001:db8:85a3:0:0:8a2e:370:7334"};
        System.out.printf("%-40s %-32s   %s%n", "Test Case", "Hex Address", "Port");
        for ( String ip : tests ) {
            try {
                String [] parsed = parseIP(ip);
                System.out.printf("%-40s %-32s   %s%n", ip, parsed[0], parsed[1]);
            }
            catch (IllegalArgumentException e) {
                System.out.printf("%-40s Invalid address:  %s%n", ip, e.getMessage());
            }
        }
    }
    
    private static final Pattern IPV4_PAT = Pattern.compile("^(\\d+)\\.(\\d+)\\.(\\d+)\\.(\\d+)(?::(\\d+)){0,1}$");
    private static final Pattern IPV6_DOUBL_COL_PAT = Pattern.compile("^\\[{0,1}([0-9a-f:]*)::([0-9a-f:]*)(?:\\]:(\\d+)){0,1}$");
    private static String ipv6Pattern;
    static {
        ipv6Pattern = "^\\[{0,1}";
        for ( int i = 1 ; i <= 7 ; i ++ ) {
            ipv6Pattern += "([0-9a-f]+):";
        }
        ipv6Pattern += "([0-9a-f]+)(?:\\]:(\\d+)){0,1}$";
    }
    private static final Pattern IPV6_PAT = Pattern.compile(ipv6Pattern);
    
    private static String[] parseIP(String ip) {
        String hex = "";
        String port = "";
        
        //  IPV4
        Matcher ipv4Matcher = IPV4_PAT.matcher(ip);
        if ( ipv4Matcher.matches() ) {
            for ( int i = 1 ; i <= 4 ; i++ ) {
                hex += toHex4(ipv4Matcher.group(i));
            }
            if ( ipv4Matcher.group(5) != null ) {
                port = ipv4Matcher.group(5);
            }
            return new String[] {hex, port};
        }
        
        //  IPV6, double colon        
        Matcher ipv6DoubleColonMatcher = IPV6_DOUBL_COL_PAT.matcher(ip);
        if ( ipv6DoubleColonMatcher.matches() ) {
            String p1 = ipv6DoubleColonMatcher.group(1);
            if ( p1.isEmpty() ) {
                p1 = "0";
            }
            String p2 = ipv6DoubleColonMatcher.group(2);
            if ( p2.isEmpty() ) {
                p2 = "0";
            }
            ip =  p1 + getZero(8 - numCount(p1) - numCount(p2)) + p2;
            if ( ipv6DoubleColonMatcher.group(3) != null ) {
                ip = "[" + ip + "]:" + ipv6DoubleColonMatcher.group(3);
            }
        }
        
        //  IPV6
        Matcher ipv6Matcher = IPV6_PAT.matcher(ip);
        if ( ipv6Matcher.matches() ) {
            for ( int i = 1 ; i <= 8 ; i++ ) {
                hex += String.format("%4s", toHex6(ipv6Matcher.group(i))).replace(" ", "0");
            }
            if ( ipv6Matcher.group(9) != null ) {
                port = ipv6Matcher.group(9);
            }
            return new String[] {hex, port};
        }
        
        throw new IllegalArgumentException("ERROR 103: Unknown address: " + ip);
    }
    
    private static int numCount(String s) {
        return s.split(":").length;
    }
    
    private static String getZero(int count) {
        StringBuilder sb = new StringBuilder();
        sb.append(":");
        while ( count > 0 ) {
            sb.append("0:");
            count--;
        }
        return sb.toString();
    }

    private static String toHex4(String s) {
        int val = Integer.parseInt(s);
        if ( val < 0 || val > 255 ) {
            throw new IllegalArgumentException("ERROR 101:  Invalid value : " + s);
        }
        return String.format("%2s", Integer.toHexString(val)).replace(" ", "0");
    }

    private static String toHex6(String s) {
        int val = Integer.parseInt(s, 16);
        if ( val < 0 || val > 65536 ) {
            throw new IllegalArgumentException("ERROR 102:  Invalid hex value : " + s);
        }
        return s;
    }

}

```

## Python Code
### python_code_1.txt
```python
from ipaddress import ip_address
from urllib.parse import urlparse

tests = [
    "127.0.0.1",
    "127.0.0.1:80",
    "::1",
    "[::1]:80",
    "::192.168.0.1",
    "2605:2700:0:3::4713:93e3",
    "[2605:2700:0:3::4713:93e3]:80" ]

def parse_ip_port(netloc):
    try:
        ip = ip_address(netloc)
        port = None
    except ValueError:
        parsed = urlparse('//{}'.format(netloc))
        ip = ip_address(parsed.hostname)
        port = parsed.port
    return ip, port

for address in tests:
    ip, port = parse_ip_port(address)
    hex_ip = {4:'{:08X}', 6:'{:032X}'}[ip.version].format(int(ip))
    print("{:39s}  {:>32s}  IPv{}  port={}".format(
        str(ip), hex_ip, ip.version, port ))

```

### python_code_2.txt
```python
import string
from pyparsing import * # import antigravity

tests="""#
127.0.0.1                       # The "localhost" IPv4 address
127.0.0.1:80                    # The "localhost" IPv4 address, with a specified port (80)
::1                             # The "localhost" IPv6 address
[::1]:80                        # The "localhost" IPv6 address, with a specified port (80)
2605:2700:0:3::4713:93e3        # Rosetta Code's primary server's public IPv6 address
[2605:2700:0:3::4713:93e3]:80   # Rosetta Code's primary server's public IPv6 address, +port (80)
2001:db8:85a3:0:0:8a2e:370:7334 # doc, IPv6 for 555-1234
2001:db8:85a3::8a2e:370:7334    # doc
[2001:db8:85a3:8d3:1319:8a2e:370:7348]:443 # doc +port
192.168.0.1                     # private
::ffff:192.168.0.1              # private transitional
::ffff:71.19.147.227            # Rosetta Code's transitional
[::ffff:71.19.147.227]:80       # Rosetta Code's transitional +port
::                              # unspecified
256.0.0.0                       # invalid, octet > 255 (currently not detected)
g::1                            # invalid
0000                                    Bad address
0000:0000                               Bad address
0000:0000:0000:0000:0000:0000:0000:0000 Good address
0000:0000:0000::0000:0000               Good Address
0000::0000::0000:0000                   Bad address
ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff Good address
ffff:ffff:ffff:fffg:ffff:ffff:ffff:ffff Bad address
fff:ffff:ffff:ffff:ffff:ffff:ffff:ffff  Good address
fff:ffff:0:ffff:ffff:ffff:ffff:ffff     Good address
"""

def print_args(args):
  print "print_args:", args

def join(args):
  args[0]="".join(args)
  del args[1:]

def replace(val):
  def lambda_replace(args):
    args[0]=val
    del args[1:]
  return lambda_replace

def atoi(args): args[0]=string.atoi(args[0])
def itohex2(args): args[0]="%02x"%args[0]

def hextoi(args): args[0]=string.atoi(args[0], 16)
def itohex4(args): args[0]="%04x"%args[0]

def assert_in_range(lwb, upb):
  def range_check(args):
    return # turn range checking off
    if args[0] < lwb:
      raise ValueError,"value %d < %d"%(args[0], lwb)
    if args[0] > upb:
      raise ValueError,"value %d > %d"%(args[0], upb)
  return range_check

dot = Literal(".").suppress()("dot"); colon = Literal(":").suppress()("colon")
octet = Word(nums).setParseAction(atoi,assert_in_range(0,255),itohex2)("octet");

port = Word(nums).setParseAction(atoi,assert_in_range(0,256*256-1))("port")
ipv4 = (octet + (dot+octet)*3)("addr")
ipv4.setParseAction(join) #,hextoi)

ipv4_port = ipv4+colon.suppress()+port

a2f = "abcdef"
hex = oneOf(" ".join(nums+a2f));

hexet = (hex*(0,4))("hexet")
hexet.setParseAction(join, hextoi, itohex4)

max=8; stop=max+1

xXXXX_etc = [None, hexet]; xXXXX_etc.extend([hexet + (colon+hexet)*n for n in range(1,max)])
x0000_etc = [ Literal("::").setParseAction(replace("0000"*num_x0000s)) for num_x0000s in range(stop) ]

ipv6=xXXXX_etc[-1]+x0000_etc[0] | xXXXX_etc[-1]

# Build a table of rules for IPv6, in particular the double colon
for num_prefix in range(max-1, -1, -1):
  for num_x0000s in range(0,stop-num_prefix):
    x0000 = x0000_etc[num_x0000s]
    num_suffix=max-num_prefix-num_x0000s
    if num_prefix:
      if num_suffix: pat = xXXXX_etc[num_prefix]+x0000+xXXXX_etc[num_suffix]
      else:          pat = xXXXX_etc[num_prefix]+x0000
    elif num_suffix: pat =                       x0000+xXXXX_etc[num_suffix]
    else: pat=x0000
    ipv6 = ipv6 | pat

ipv6.setParseAction(join) # ,hextoi)
ipv6_port = Literal("[").suppress() + ipv6 + Literal("]").suppress()+colon+port

ipv6_transitional = (Literal("::ffff:").setParseAction(replace("0"*20+"ffff"))+ipv4).setParseAction(join)
ipv6_transitional_port = Literal("[").suppress() + ipv6_transitional + Literal("]").suppress()+colon+port

ip_fmt = (
           (ipv4_port|ipv4)("ipv4") |
           (ipv6_transitional_port|ipv6_transitional|ipv6_port|ipv6)("ipv6")
         ) + LineEnd()

class IPAddr(object):
  def __init__(self, string):
    self.service = dict(zip(("address","port"), ip_fmt.parseString(string)[:]))
  def __getitem__(self, key): return self.service[key]
  def __contains__(self, key): return key in self.service
  def __repr__(self): return `self.service` # "".join(self.service)
  address=property(lambda self: self.service["address"])
  port=property(lambda self: self.service["port"])
  is_service=property(lambda self: "port" in self.service)
  version=property(lambda self: {False:4, True:6}[len(self.address)>8])

for test in tests.splitlines():
  if not test.startswith("#"):
    ip_str, desc = test.split(None,1)
    print ip_str,"=>",
    try:
      ip=IPAddr(ip_str)
      print ip, "IP Version:",ip.version,"- Address is OK!",
    except (ParseException,ValueError), details: print "Bad! IP address syntax error detected:",details,
    print "- Actually:",desc

```

