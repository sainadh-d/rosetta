# 100 prisoners

## Task Link
[Rosetta Code - 100 prisoners](https://rosettacode.org/wiki/100_prisoners)

## Java Code
### java_code_1.txt
```java
import java.util.Collections;
import java.util.List;
import java.util.Objects;
import java.util.function.Function;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class Main {
    private static boolean playOptimal(int n) {
        List<Integer> secretList = IntStream.range(0, n).boxed().collect(Collectors.toList());
        Collections.shuffle(secretList);

        prisoner:
        for (int i = 0; i < secretList.size(); ++i) {
            int prev = i;
            for (int j = 0; j < secretList.size() / 2; ++j) {
                if (secretList.get(prev) == i) {
                    continue prisoner;
                }
                prev = secretList.get(prev);
            }
            return false;
        }
        return true;
    }

    private static boolean playRandom(int n) {
        List<Integer> secretList = IntStream.range(0, n).boxed().collect(Collectors.toList());
        Collections.shuffle(secretList);

        prisoner:
        for (Integer i : secretList) {
            List<Integer> trialList = IntStream.range(0, n).boxed().collect(Collectors.toList());
            Collections.shuffle(trialList);

            for (int j = 0; j < trialList.size() / 2; ++j) {
                if (Objects.equals(trialList.get(j), i)) {
                    continue prisoner;
                }
            }

            return false;
        }
        return true;
    }

    private static double exec(int n, int p, Function<Integer, Boolean> play) {
        int succ = 0;
        for (int i = 0; i < n; ++i) {
            if (play.apply(p)) {
                succ++;
            }
        }
        return (succ * 100.0) / n;
    }

    public static void main(String[] args) {
        final int n = 100_000;
        final int p = 100;
        System.out.printf("# of executions: %d\n", n);
        System.out.printf("Optimal play success rate: %f%%\n", exec(n, p, Main::playOptimal));
        System.out.printf("Random play success rate: %f%%\n", exec(n, p, Main::playRandom));
    }
}

```

## Python Code
### python_code_1.txt
```python
import random

def play_random(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    sampler = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        found = False
        for prisoner in range(100):
            found = False
            for reveal in random.sample(sampler, 50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %

def play_optimal(n):
    # using 0-99 instead of ranges 1-100
    pardoned = 0
    in_drawer = list(range(100))
    for _round in range(n):
        random.shuffle(in_drawer)
        for prisoner in range(100):
            reveal = prisoner
            found = False
            for go in range(50):
                card = in_drawer[reveal]
                if card == prisoner:
                    found = True
                    break
                reveal = card
            if not found:
                break
        if found:
            pardoned += 1
    return pardoned / n * 100   # %

if __name__ == '__main__':
    n = 100_000
    print(" Simulation count:", n)
    print(f" Random play wins: {play_random(n):4.1f}% of simulations")
    print(f"Optimal play wins: {play_optimal(n):4.1f}% of simulations")

```

### python_code_2.txt
```python
# http://rosettacode.org/wiki/100_prisoners

import random


def main():
    NUM_DRAWERS = 10
    NUM_REPETITIONS = int(1E5)

    print('{:15}: {:5} ({})'.format('approach', 'wins', 'ratio'))
    for approach in PrisionersGame.approaches:
        num_victories = 0
        for _ in range(NUM_REPETITIONS):
            game = PrisionersGame(NUM_DRAWERS)
            num_victories += PrisionersGame.victory(game.play(approach))

        print('{:15}: {:5} ({:.2%})'.format(
            approach.__name__, num_victories, num_victories / NUM_REPETITIONS))


class PrisionersGame:
    """docstring for PrisionersGame"""
    def __init__(self, num_drawers):
        assert num_drawers % 2 == 0
        self.num_drawers = num_drawers
        self.max_attempts = int(self.num_drawers / 2)
        self.drawer_ids = list(range(1, num_drawers + 1))
        shuffled = self.drawer_ids[:]
        random.shuffle(shuffled)
        self.drawers = dict(zip(self.drawer_ids, shuffled))

    def play_naive(self, player_number):
        """ Randomly open drawers """
        for attempt in range(self.max_attempts):
            if self.drawers[random.choice(self.drawer_ids)] == player_number:
                return True

        return False

    def play_naive_mem(self, player_number):
        """ Randomly open drawers but avoiding repetitions """
        not_attemped = self.drawer_ids[:]
        for attempt in range(self.max_attempts):
            guess = random.choice(not_attemped)
            not_attemped.remove(guess)

            if self.drawers[guess] == player_number:
                return True

        return False

    def play_optimum(self, player_number):
        """ Open the drawer that matches the player number and then open the drawer
        with the revealed number.
        """
        prev_attempt = player_number
        for attempt in range(self.max_attempts):
            if self.drawers[prev_attempt] == player_number:
                return True
            else:
                prev_attempt = self.drawers[prev_attempt]

        return False

    @classmethod
    def victory(csl, results):
        """Defines a victory of a game: all players won"""
        return all(results)

    approaches = [play_naive, play_naive_mem, play_optimum]

    def play(self, approach):
        """Plays this game and returns a list of booleans with
        True if a player one, False otherwise"""
        return [approach(self, player) for player in self.drawer_ids]


if __name__ == '__main__':
    main()

```

### python_code_3.txt
```python
'''100 Prisoners'''

from random import randint, sample


# allChainedPathsAreShort :: Int -> IO (0|1)
def allChainedPathsAreShort(n):
    '''1 if none of the index-chasing cycles in a shuffled
       sample of [1..n] cards are longer than half the
       sample size. Otherwise, 0.
    '''
    limit = n // 2
    xs = range(1, 1 + n)
    shuffled = sample(xs, k=n)

    # A cycle of boxes, drawn from a shuffled
    # sample, which includes the given target.
    def cycleIncluding(target):
        boxChain = [target]
        v = shuffled[target - 1]
        while v != target:
            boxChain.append(v)
            v = shuffled[v - 1]
        return boxChain

    # Nothing if the target list is empty, or if the cycle which contains the
    # first target is larger than half the sample size.
    # Otherwise, just a cycle of enchained boxes containing the first target
    # in the list, tupled with the residue of any remaining targets which
    # fall outside that cycle.
    def boxCycle(targets):
        if targets:
            boxChain = cycleIncluding(targets[0])
            return Just((
                difference(targets[1:])(boxChain),
                boxChain
            )) if limit >= len(boxChain) else Nothing()
        else:
            return Nothing()

    # No cycles longer than half of total box count ?
    return int(n == sum(map(len, unfoldr(boxCycle)(xs))))


# randomTrialResult :: RandomIO (0|1) -> Int -> (0|1)
def randomTrialResult(coin):
    '''1 if every one of the prisoners finds their ticket
       in an arbitrary half of the sample. Otherwise 0.
    '''
    return lambda n: int(all(
        coin(x) for x in range(1, 1 + n)
    ))


# TEST ----------------------------------------------------
# main :: IO ()
def main():
    '''Two sampling techniques constrasted with 100 drawers
       and 100 prisoners, over 100,000 trial runs.
    '''
    halfOfDrawers = randomRInt(0)(1)

    def optimalDrawerSampling(x):
        return allChainedPathsAreShort(x)

    def randomDrawerSampling(x):
        return randomTrialResult(halfOfDrawers)(x)

    # kSamplesWithNBoxes :: Int -> Int -> String
    def kSamplesWithNBoxes(k):
        tests = range(1, 1 + k)
        return lambda n: '\n\n' + fTable(
            str(k) + ' tests of optimal vs random drawer-sampling ' +
            'with ' + str(n) + ' boxes: \n'
        )(fName)(lambda r: '{:.2%}'.format(r))(
            lambda f: sum(f(n) for x in tests) / k
        )([
            optimalDrawerSampling,
            randomDrawerSampling,
        ])

    print(kSamplesWithNBoxes(10000)(10))

    print(kSamplesWithNBoxes(10000)(100))

    print(kSamplesWithNBoxes(100000)(100))


# ------------------------DISPLAY--------------------------

# fTable :: String -> (a -> String) ->
# (b -> String) -> (a -> b) -> [a] -> String
def fTable(s):
    '''Heading -> x display function -> fx display function ->
       f -> xs -> tabular string.
    '''
    def go(xShow, fxShow, f, xs):
        ys = [xShow(x) for x in xs]
        w = max(map(len, ys))
        return s + '\n' + '\n'.join(map(
            lambda x, y: y.rjust(w, ' ') + ' -> ' + fxShow(f(x)),
            xs, ys
        ))
    return lambda xShow: lambda fxShow: lambda f: lambda xs: go(
        xShow, fxShow, f, xs
    )


# fname :: (a -> b) -> String
def fName(f):
    '''Name bound to the given function.'''
    return f.__name__


# ------------------------GENERIC -------------------------

# Just :: a -> Maybe a
def Just(x):
    '''Constructor for an inhabited Maybe (option type) value.
       Wrapper containing the result of a computation.
    '''
    return {'type': 'Maybe', 'Nothing': False, 'Just': x}


# Nothing :: Maybe a
def Nothing():
    '''Constructor for an empty Maybe (option type) value.
       Empty wrapper returned where a computation is not possible.
    '''
    return {'type': 'Maybe', 'Nothing': True}


# difference :: Eq a => [a] -> [a] -> [a]
def difference(xs):
    '''All elements of xs, except any also found in ys.'''
    return lambda ys: list(set(xs) - set(ys))


# randomRInt :: Int -> Int -> IO () -> Int
def randomRInt(m):
    '''The return value of randomRInt is itself
       a function. The returned function, whenever
       called, yields a a new pseudo-random integer
       in the range [m..n].
    '''
    return lambda n: lambda _: randint(m, n)


# unfoldr(lambda x: Just((x, x - 1)) if 0 != x else Nothing())(10)
# -> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
# unfoldr :: (b -> Maybe (a, b)) -> b -> [a]
def unfoldr(f):
    '''Dual to reduce or foldr.
       Where catamorphism reduces a list to a summary value,
       the anamorphic unfoldr builds a list from a seed value.
       As long as f returns Just(a, b), a is prepended to the list,
       and the residual b is used as the argument for the next
       application of f.
       When f returns Nothing, the completed list is returned.
    '''
    def go(v):
        xr = v, v
        xs = []
        while True:
            mb = f(xr[0])
            if mb.get('Nothing'):
                return xs
            else:
                xr = mb.get('Just')
                xs.append(xr[1])
        return xs
    return lambda x: go(x)


# MAIN ---
if __name__ == '__main__':
    main()

```

