# Four bit adder

## Task Link
[Rosetta Code - Four bit adder](https://rosettacode.org/wiki/Four_bit_adder)

## Java Code
### java_code_1.txt
```java
public class GateLogic
{
  // Basic gate interfaces
  public interface OneInputGate
  {  boolean eval(boolean input);  }
  
  public interface TwoInputGate
  {  boolean eval(boolean input1, boolean input2);  }
  
  public interface MultiGate
  {  boolean[] eval(boolean... inputs);  }
  
  // Create NOT
  public static OneInputGate NOT = new OneInputGate() {
    public boolean eval(boolean input)
    {  return !input;  }
  };
  
  // Create AND
  public static TwoInputGate AND = new TwoInputGate() {
    public boolean eval(boolean input1, boolean input2)
    {  return input1 && input2;  }
  };
  
  // Create OR
  public static TwoInputGate OR = new TwoInputGate() {
    public boolean eval(boolean input1, boolean input2)
    {  return input1 || input2;  }
  };
  
  // Create XOR
  public static TwoInputGate XOR = new TwoInputGate() {
    public boolean eval(boolean input1, boolean input2)
    {
      return OR.eval(
               AND.eval(input1, NOT.eval(input2)),
               AND.eval(NOT.eval(input1), input2)
             );
    }
  };
  
  // Create HALF_ADDER
  public static MultiGate HALF_ADDER = new MultiGate() {
    public boolean[] eval(boolean... inputs)
    {
      if (inputs.length != 2)
        throw new IllegalArgumentException();
      return new boolean[] {
        XOR.eval(inputs[0], inputs[1]),  // Output bit
        AND.eval(inputs[0], inputs[1])   // Carry bit
      };
    }
  };
  
  // Create FULL_ADDER
  public static MultiGate FULL_ADDER = new MultiGate() {
    public boolean[] eval(boolean... inputs)
    {
      if (inputs.length != 3)
        throw new IllegalArgumentException();
      // Inputs: CarryIn, A, B
      // Outputs: S, CarryOut
      boolean[] haOutputs1 = HALF_ADDER.eval(inputs[0], inputs[1]);
      boolean[] haOutputs2 = HALF_ADDER.eval(haOutputs1[0], inputs[2]);
      return new boolean[] {
        haOutputs2[0],                         // Output bit
        OR.eval(haOutputs1[1], haOutputs2[1])  // Carry bit
      };
    }
  };
  
  public static MultiGate buildAdder(final int numBits)
  {
    return new MultiGate() {
      public boolean[] eval(boolean... inputs)
      {
        // Inputs: A0, A1, A2..., B0, B1, B2...
        if (inputs.length != (numBits << 1))
          throw new IllegalArgumentException();
        boolean[] outputs = new boolean[numBits + 1];
        boolean[] faInputs = new boolean[3];
        boolean[] faOutputs = null;
        for (int i = 0; i < numBits; i++)
        {
          faInputs[0] = (faOutputs == null) ? false : faOutputs[1];  // CarryIn
          faInputs[1] = inputs[i];                                   // Ai
          faInputs[2] = inputs[numBits + i];                         // Bi
          faOutputs = FULL_ADDER.eval(faInputs);
          outputs[i] = faOutputs[0];                                 // Si
        }
        if (faOutputs != null)
          outputs[numBits] = faOutputs[1];                           // CarryOut
        return outputs;
      }
    };
  }
  
  public static void main(String[] args)
  {
    int numBits = Integer.parseInt(args[0]);
    int firstNum = Integer.parseInt(args[1]);
    int secondNum = Integer.parseInt(args[2]);
    int maxNum = 1 << numBits;
    if ((firstNum < 0) || (firstNum >= maxNum))
    {
      System.out.println("First number is out of range");
      return;
    }
    if ((secondNum < 0) || (secondNum >= maxNum))
    {
      System.out.println("Second number is out of range");
      return;
    }
    
    MultiGate multiBitAdder = buildAdder(numBits);
    // Convert input numbers into array of bits
    boolean[] inputs = new boolean[numBits << 1];
    String firstNumDisplay = "";
    String secondNumDisplay = "";
    for (int i = 0; i < numBits; i++)
    {
      boolean firstBit = ((firstNum >>> i) & 1) == 1;
      boolean secondBit = ((secondNum >>> i) & 1) == 1;
      inputs[i] = firstBit;
      inputs[numBits + i] = secondBit;
      firstNumDisplay = (firstBit ? "1" : "0") + firstNumDisplay;
      secondNumDisplay = (secondBit ? "1" : "0") + secondNumDisplay;
    }
    
    boolean[] outputs = multiBitAdder.eval(inputs);
    int outputNum = 0;
    String outputNumDisplay = "";
    String outputCarryDisplay = null;
    for (int i = numBits; i >= 0; i--)
    {
      outputNum = (outputNum << 1) | (outputs[i] ? 1 : 0);
      if (i == numBits)
        outputCarryDisplay = outputs[i] ? "1" : "0";
      else
        outputNumDisplay += (outputs[i] ? "1" : "0");
    }
    System.out.println("numBits=" + numBits);
    System.out.println("A=" + firstNumDisplay + " (" + firstNum + "), B=" + secondNumDisplay + " (" + secondNum + "), S=" + outputCarryDisplay + " " + outputNumDisplay + " (" + outputNum + ")");
    return;
  }
  
}

```

## Python Code
### python_code_1.txt
```python
"""  
To run: 
    python3 Four_bit_adder_011.py
"""

from myhdl import *

#     define set of primitives 

@block
def NOTgate( a,  q ):   # define component name & interface
   """ q <- not(a) """
   @always_comb   # define asynchronous logic
   def NOTgateLogic():
      q.next = not a

   return NOTgateLogic   # return defined logic function, named 'NOTgate'


@block
def ANDgate( a, b,  q ):
   """ q <- a and b """
   @always_comb 
   def ANDgateLogic():
      q.next = a and b

   return ANDgateLogic


@block
def ORgate( a, b,  q ):
   """ q <- a or b """   
   @always_comb  
   def ORgateLogic():
      q.next = a or b

   return ORgateLogic


#     build components using defined primitive set

@block
def XORgate( a, b,  q ):
   """ q <- a xor b """   
   # define internal signals
   nota, notb, annotb, bnnota = [Signal(bool(0)) for i in range(4)]
   # name sub-components, and their interconnect 
   inv0 = NOTgate( a,  nota )
   inv1 = NOTgate( b,  notb )
   and2a = ANDgate( a, notb,  annotb )
   and2b = ANDgate( b, nota,  bnnota )
   or2a = ORgate( annotb, bnnota,  q )

   return inv0, inv1, and2a, and2b, or2a


@block
def HalfAdder( in_a, in_b,  summ, carry ):
   """ carry,sum is the sum of in_a, in_b """ 
   and2a =  ANDgate(in_a, in_b,  carry)
   xor2a =  XORgate(in_a, in_b,  summ)

   return and2a, xor2a


@block
def FullAdder( fa_c0, fa_a, fa_b,  fa_s, fa_c1 ):
   """ fa_c1,fa_s is the sum of fa_c0, fa_a, fa_b """

   ha1_s, ha1_c1, ha2_c1 = [Signal(bool(0)) for i in range(3)]

   HalfAdder01 = HalfAdder( fa_c0, fa_a,  ha1_s, ha1_c1 )
   HalfAdder02 = HalfAdder( ha1_s, fa_b,  fa_s,  ha2_c1 )
   or2a = ORgate(ha1_c1, ha2_c1,  fa_c1)

   return HalfAdder01, HalfAdder02, or2a


@block
def Adder4b( ina, inb,  cOut, sum4):
   ''' assemble 4 full adders ''' 

   cl = [Signal(bool()) for i in range(0,4)]  # carry signal list
   sl = [Signal(bool()) for i in range(4)]  # sum signal list

   HalfAdder0 = HalfAdder(        ina(0), inb(0),  sl[0], cl[1] )
   FullAdder1 = FullAdder( cl[1], ina(1), inb(1),  sl[1], cl[2] ) 
   FullAdder2 = FullAdder( cl[2], ina(2), inb(2),  sl[2], cl[3] ) 
   FullAdder3 = FullAdder( cl[3], ina(3), inb(3),  sl[3], cOut ) 

   sc = ConcatSignal(*reversed(sl))  # create internal bus for output list

   @always_comb
   def list2intbv():
      sum4.next = sc  # assign internal bus to actual output

   return HalfAdder0, FullAdder1, FullAdder2, FullAdder3, list2intbv


"""   define signals and code for testing
      -----------------------------------   """
t_co, t_s, t_a, t_b, dbug =  [Signal(bool(0)) for i in range(5)]
ina4, inb4, sum4 =  [Signal(intbv(0)[4:])  for i in range(3)]

from random import randrange 

@block
def Test_Adder4b():
   ''' Test Bench for Adder4b '''
   dut = Adder4b( ina4, inb4,  t_co, sum4 )

   @instance
   def check():
      print( "\n      b   a   |  c1    s   \n     -------------------" )
      for i in range(15):
         ina4.next, inb4.next = randrange(2**4), randrange(2**4)
         yield delay(5)
         print( "     %2d  %2d   |  %2d   %2d     " \
                % (ina4,inb4, t_co,sum4) )
         assert t_co * 16 + sum4 == ina4 + inb4  # test result
      print()

   return dut, check


"""   instantiate components and run test
      -----------------------------------   """

def main():
   simInst = Test_Adder4b()
   simInst.name = "mySimInst"
   simInst.config_sim(trace=True)  # waveform trace turned on
   simInst.run_sim(duration=None)

   inst = Adder4b( ina4, inb4,  t_co, sum4 )  #Multibit_Adder( a, b, s)
   inst.convert(hdl='VHDL')  # export VHDL
   inst.convert(hdl='Verilog')  # export Verilog

    
if __name__ == '__main__':
   main()

```

### python_code_2.txt
```python
def xor(a, b): return (a and not b) or (b and not a)

def ha(a, b): return xor(a, b), a and b     # sum, carry

def fa(a, b, ci):
    s0, c0 = ha(ci, a)
    s1, c1 = ha(s0, b)
    return s1, c0 or c1     # sum, carry

def fa4(a, b):
    width = 4
    ci = [None] * width
    co = [None] * width
    s  = [None] * width
    for i in range(width):
        s[i], co[i] = fa(a[i], b[i], co[i-1] if i else 0)
    return s, co[-1]

def int2bus(n, width=4):
    return [int(c) for c in "{0:0{1}b}".format(n, width)[::-1]]

def bus2int(b):
    return sum(1 << i for i, bit in enumerate(b) if bit)

def test_fa4():
    width = 4
    tot = [None] * (width + 1)
    for a in range(2**width):
        for b in range(2**width):
            tot[:width], tot[width] = fa4(int2bus(a), int2bus(b))
            assert a + b == bus2int(tot), "totals don't match: %i + %i != %s" % (a, b, tot)


if __name__ == '__main__':
   test_fa4()

```

