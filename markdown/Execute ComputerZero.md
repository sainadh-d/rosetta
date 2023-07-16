# Execute Computer/Zero

## Task Link
[Rosetta Code - Execute Computer/Zero](https://rosettacode.org/wiki/Execute_Computer/Zero)

## Java Code
## Python Code
### python_code_1.txt
```python
import static java.lang.Math.floorMod;
import static java.lang.Math.min;
import static java.util.stream.Collectors.toMap;

import java.util.AbstractMap.SimpleEntry;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;
import java.util.stream.Stream;

public class ComputerZero {

    private static final int MEM = 32;

    private static final int NOP = 0;
    private static final int LDA = 1;
    private static final int STA = 2;
    private static final int ADD = 3;
    private static final int SUB = 4;
    private static final int BRZ = 5;
    private static final int JMP = 6;
    private static final int STP = 7;

    private static final Map<String, Integer> OPCODES = Stream.of(
            new SimpleEntry<>("NOP", NOP),
            new SimpleEntry<>("LDA", LDA),
            new SimpleEntry<>("STA", STA),
            new SimpleEntry<>("ADD", ADD),
            new SimpleEntry<>("SUB", SUB),
            new SimpleEntry<>("BRZ", BRZ),
            new SimpleEntry<>("JMP", JMP),
            new SimpleEntry<>("STP", STP))
            .collect(toMap(SimpleEntry::getKey, SimpleEntry::getValue));

    private static final Pattern RE_INSTRUCTION = Pattern.compile(
            "\\s*" +
                    "(?:(?<label>\\w+):)?" +
                    "\\s*" +
                    String.format("(?<opcode>%s)?", String.join("|", OPCODES.keySet())) +
                    "\\s*" +
                    "(?<argument>\\w+)?" +
                    "\\s*" +
                    "(?:;(?<comment>.+))?");

    public static class ComputerZeroException extends RuntimeException {
        public ComputerZeroException(String msg) {
            super(msg);
        }
    }

    private static class Instruction {
        String opcode;
        String argument;

        public Instruction(String opcode, String argument) {
            this.opcode = opcode;
            this.argument = argument;
        }
    }

    private static class Assembly {
        public Iterable<Instruction> instructions;
        public Map<String, Integer> labels;

        public Assembly(Iterable<Instruction> instructions, Map<String, Integer> labels) {
            this.instructions = instructions;
            this.labels = labels;
        }
    }

    public static Assembly parse(String assembly) {
        ArrayList<Instruction> instructions = new ArrayList<Instruction>();
        HashMap<String, Integer> labels = new HashMap<String, Integer>();
        int lineNumber = 0;

        for (String line : assembly.split("\\R")) {
            Matcher matcher = RE_INSTRUCTION.matcher(line);

            if (!matcher.matches()) {
                throw new ComputerZeroException(String.format("%s %d", line, lineNumber));
            }

            if (matcher.group("label") != null) {
                labels.put(matcher.group("label"), lineNumber);
            }

            instructions.add(new Instruction(matcher.group("opcode"), matcher.group("argument")));
            lineNumber++;
        }

        return new Assembly(instructions, labels);
    }

    public static Integer[] compile(Assembly assembly) {
        ArrayList<Integer> bytecode = new ArrayList<Integer>();

        for (Instruction instruction : assembly.instructions) {
            int argument;
            if (instruction.argument == null) {
                argument = 0;
            } else if (instruction.argument.matches("\\d+")) {
                argument = Integer.parseInt(instruction.argument);
            } else {
                argument = assembly.labels.getOrDefault(instruction.argument, 0);
            }

            if (instruction.opcode != null) {
                bytecode.add(OPCODES.get(instruction.opcode) << 5 | argument);
            } else {
                bytecode.add(argument);
            }
        }

        return bytecode.toArray(new Integer[0]);
    }

    public static int run(Integer[] bytecode) {
        int accumulator = 0;
        int instruction_pointer = 0;
        Integer[] memory = new Integer[MEM];
        Arrays.fill(memory, 0);
        System.arraycopy(bytecode, 0, memory, 0, min(MEM, bytecode.length));

        vm: while (instruction_pointer < MEM) {
            int operation = memory[instruction_pointer] >> 5;
            int argument = memory[instruction_pointer] & 0b11111;
            instruction_pointer++;

            switch (operation) {
                case NOP:
                    continue;
                case LDA:
                    accumulator = memory[argument];
                    break;
                case STA:
                    memory[argument] = accumulator;
                    break;
                case ADD:
                    accumulator = floorMod(accumulator + memory[argument], 256);
                    break;
                case SUB:
                    accumulator = floorMod(accumulator - memory[argument], 256);
                    break;
                case BRZ:
                    if (accumulator == 0) {
                        instruction_pointer = argument;
                    }
                    break;
                case JMP:
                    instruction_pointer = argument;
                    break;
                case STP:
                    break vm;
                default:
                    throw new ComputerZeroException(
                            String.format("error: %d %d", operation, argument));
            }

        }

        return accumulator;
    }

    public static int run(String source) {
        return run(compile(parse(source)));
    }

    public static final List<String> TEST_CASES = Arrays.asList(
            String.join("\n",
                    "        LDA   x",
                    "        ADD   y       ; accumulator = x + y",
                    "        STP",
                    "x:            2",
                    "y:            2"),
            String.join("\n",
                    "loop:   LDA   prodt",
                    "        ADD   x",
                    "        STA   prodt",
                    "        LDA   y",
                    "        SUB   one",
                    "        STA   y",
                    "        BRZ   done",
                    "        JMP   loop",
                    "done:   LDA   prodt   ; to display it",
                    "        STP",
                    "x:            8",
                    "y:            7",
                    "prodt:        0",
                    "one:          1"),
            String.join("\n",
                    "loop:   LDA   n",
                    "        STA   temp",
                    "        ADD   m",
                    "        STA   n",
                    "        LDA   temp",
                    "        STA   m",
                    "        LDA   count",
                    "        SUB   one",
                    "        BRZ   done",
                    "        STA   count",
                    "        JMP   loop",
                    "done:   LDA   n       ; to display it",
                    "        STP",
                    "m:            1",
                    "n:            1",
                    "temp:         0",
                    "count:        8       ; valid range: 1-11",
                    "one:          1"),
            String.join("\n",
                    "start:  LDA   load",
                    "        ADD   car     ; head of list",
                    "        STA   ldcar",
                    "        ADD   one",
                    "        STA   ldcdr   ; next CONS cell",
                    "ldcar:  NOP",
                    "        STA   value",
                    "ldcdr:  NOP",
                    "        BRZ   done    ; 0 stands for NIL",
                    "        STA   car",
                    "        JMP   start",
                    "done:   LDA   value   ; CAR of last CONS",
                    "        STP",
                    "load:   LDA   0",
                    "value:        0",
                    "car:          28",
                    "one:          1",
                    "                    ; order of CONS cells",
                    "                    ; in memory",
                    "                    ; does not matter",
                    "              6",
                    "              0       ; 0 stands for NIL",
                    "              2       ; (CADR ls)",
                    "              26      ; (CDDR ls) -- etc.",
                    "              5",
                    "              20",
                    "              3",
                    "              30",
                    "              1       ; value of (CAR ls)",
                    "              22      ; points to (CDR ls)",
                    "              4",
                    "              24"),
            String.join("\n",
                    "p:            0       ; NOP in first round",
                    "c:            0",
                    "start:  STP           ; wait for p's move",
                    "pmove:  NOP",
                    "        LDA   pmove",
                    "        SUB   cmove",
                    "        BRZ   same",
                    "        LDA   pmove",
                    "        STA   cmove   ; tit for tat",
                    "        BRZ   cdeft",
                    "        LDA   c       ; p defected, c did not",
                    "        ADD   three",
                    "        STA   c",
                    "        JMP   start",
                    "cdeft:  LDA   p",
                    "        ADD   three",
                    "        STA   p",
                    "        JMP   start",
                    "same:   LDA   pmove",
                    "        STA   cmove   ; tit for tat",
                    "        LDA   p",
                    "        ADD   one",
                    "        ADD   pmove",
                    "        STA   p",
                    "        LDA   c",
                    "        ADD   one",
                    "        ADD   pmove",
                    "        STA   c",
                    "        JMP   start",
                    "cmove:        0       ; co-operate initially",
                    "one:          1",
                    "three:        3            "),
            String.join("\n",
                    "LDA  3",
                    "SUB  4",
                    "STP  0",
                    "     0",
                    "     255"),
            String.join("\n",
                    "LDA  3",
                    "SUB  4",
                    "STP  0",
                    "     0",
                    "     1"),
            String.join("\n",
                    "LDA  3",
                    "ADD  4",
                    "STP  0",
                    "     1",
                    "     255")

    );

    public static void main(String[] args) {
        for (String source : TEST_CASES) {
            System.out.println(run(source));
        }
    }
}

```

### python_code_2.txt
```python
"""Computer/zero Assembly emulator. Requires Python >= 3.7"""

import re

from typing import Dict
from typing import Iterable
from typing import List
from typing import NamedTuple
from typing import Optional
from typing import Tuple


NOP = 0b000
LDA = 0b001
STA = 0b010
ADD = 0b011
SUB = 0b100
BRZ = 0b101
JMP = 0b110
STP = 0b111

OPCODES = {
    "NOP": NOP,
    "LDA": LDA,
    "STA": STA,
    "ADD": ADD,
    "SUB": SUB,
    "BRZ": BRZ,
    "JMP": JMP,
    "STP": STP,
}

RE_INSTRUCTION = re.compile(
    r"\s*"
    r"(?:(?P<label>\w+):)?"
    r"\s*"
    rf"(?P<opcode>{'|'.join(OPCODES)})?"
    r"\s*"
    r"(?P<argument>\w+)?"
    r"\s*"
    r"(?:;(?P<comment>[\w\s]+))?"
)


class AssemblySyntaxError(Exception):
    pass


class Instruction(NamedTuple):
    label: Optional[str]
    opcode: Optional[str]
    argument: Optional[str]
    comment: Optional[str]


def parse(assembly: str) -> Tuple[List[Instruction], Dict[str, int]]:
    instructions: List[Instruction] = []
    labels: Dict[str, int] = {}
    linenum: int = 0

    for line in assembly.split("\n"):
        match = RE_INSTRUCTION.match(line)

        if not match:
            raise AssemblySyntaxError(f"{line}: {linenum}")

        instructions.append(Instruction(**match.groupdict()))
        label = match.group(1)
        if label:
            labels[label] = linenum

        linenum += 1

    return instructions, labels


def compile(instructions: List[Instruction], labels: Dict[str, int]) -> Iterable[int]:
    for instruction in instructions:
        if instruction.argument is None:
            argument = 0
        elif instruction.argument.isnumeric():
            argument = int(instruction.argument)
        else:
            argument = labels[instruction.argument]

        if instruction.opcode:
            yield OPCODES[instruction.opcode] << 5 | argument
        else:
            yield argument


def run(bytecode: bytes) -> int:
    accumulator = 0
    program_counter = 0
    memory = list(bytecode)[:32] + [0 for _ in range(32 - len(bytecode))]

    while program_counter < 32:
        operation = memory[program_counter] >> 5
        argument = memory[program_counter] & 0b11111
        program_counter += 1

        if operation == NOP:
            continue
        elif operation == LDA:
            accumulator = memory[argument]
        elif operation == STA:
            memory[argument] = accumulator
        elif operation == ADD:
            accumulator = (accumulator + memory[argument]) % 256
        elif operation == SUB:
            accumulator = (accumulator - memory[argument]) % 256
        elif operation == BRZ:
            if accumulator == 0:
                program_counter = argument
        elif operation == JMP:
            program_counter = argument
        elif operation == STP:
            break
        else:
            raise Exception(f"error: {operation} {argument}")

    return accumulator


SAMPLES = [
    """\
            LDA   x
            ADD   y       ; accumulator = x + y
            STP
    x:            2
    y:            2
    """,
    """\
    loop:   LDA   prodt
            ADD   x
            STA   prodt
            LDA   y
            SUB   one
            STA   y
            BRZ   done
            JMP   loop
    done:   LDA   prodt   ; to display it
            STP
    x:            8
    y:            7
    prodt:        0
    one:          1
    """,
    """\
    loop:   LDA   n
            STA   temp
            ADD   m
            STA   n
            LDA   temp
            STA   m
            LDA   count
            SUB   one
            BRZ   done
            STA   count
            JMP   loop
    done:   LDA   n       ; to display it
            STP
    m:            1
    n:            1
    temp:         0
    count:        8       ; valid range: 1-11
    one:          1
    """,
    """\
    start:  LDA   load
            ADD   car     ; head of list
            STA   ldcar
            ADD   one
            STA   ldcdr   ; next CONS cell
    ldcar:  NOP
            STA   value
    ldcdr:  NOP
            BRZ   done    ; 0 stands for NIL
            STA   car
            JMP   start
    done:   LDA   value   ; CAR of last CONS
            STP
    load:   LDA   0
    value:        0
    car:          28
    one:          1
                        ; order of CONS cells
                        ; in memory
                        ; does not matter
                6
                0       ; 0 stands for NIL
                2       ; (CADR ls)
                26      ; (CDDR ls) -- etc.
                5
                20
                3
                30
                1       ; value of (CAR ls)
                22      ; points to (CDR ls)
                4
                24
    """,
    """\
    p:            0       ; NOP in first round
    c:            0
    start:  STP           ; wait for p's move
    pmove:  NOP
            LDA   pmove
            SUB   cmove
            BRZ   same
            LDA   pmove
            STA   cmove   ; tit for tat
            BRZ   cdeft
            LDA   c       ; p defected, c did not
            ADD   three
            STA   c
            JMP   start
    cdeft:  LDA   p
            ADD   three
            STA   p
            JMP   start
    same:   LDA   pmove
            STA   cmove   ; tit for tat
            LDA   p
            ADD   one
            ADD   pmove
            STA   p
            LDA   c
            ADD   one
            ADD   pmove
            STA   c
            JMP   start
    cmove:        0       ; co-operate initially
    one:          1
    three:        3
    """,
    """\
    LDA  3
    SUB  4
    STP  0
         0
         255
    """,
    """\
    LDA  3
    SUB  4
    STP  0
         0
         1
    """,
    """\
    LDA  3
    ADD  4
    STP  0
         1
         255
    """,
]


def main() -> None:
    for sample in SAMPLES:
        instructions, labels = parse(sample)
        bytecode = bytes(compile(instructions, labels))
        result = run(bytecode)
        print(result)


if __name__ == "__main__":
    main()

```

