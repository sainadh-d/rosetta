# Two bullet roulette

## Task Link
[Rosetta Code - Two bullet roulette](https://rosettacode.org/wiki/Two_bullet_roulette)

## Java Code
### java_code_1.txt
```java
import java.util.BitSet;
import java.util.concurrent.ThreadLocalRandom;

public class TwoBulletRoulette {

	public static void main(String[] aArgs) {		
		Revolver handgun = new Revolver();
		final int simulationCount = 100_000;		
	
		for ( Situation situation : Situation.values() ) {
			double deaths = 0.0;
			for ( int i = 0; i < simulationCount; i++ ) {
				ResultState resultState = handgun.operateInMode(situation);
				if ( resultState == ResultState.DEAD) {
					deaths += 1.0;
				}
			}
			final double deathRate = ( deaths / simulationCount ) * 100;
			String percentage = String.format("%4.1f%%", deathRate);
			System.out.println("Situation " + situation + " produces " + percentage + " deaths");
		}
	}	
	
}

enum Situation { A, B, C, D }

enum ResultState { ALIVE, DEAD }

/**
 * Representation of a six cylinder revolving chamber pistol.
 */
class Revolver {
	
	public Revolver() {
		chambers = new BitSet(chamberCount);			
		random = ThreadLocalRandom.current();
	}	
	
	public ResultState operateInMode(Situation aSituation) {
		return switch ( aSituation ) {
			case A -> useSituationA();
			case B -> useSituationB();
			case C -> useSituationC();
			case D -> useSituationD();
		};
	}
	
	// PRIVATE //
	
	private void unload() {		
		chambers.clear();
	}
	
	private void load() {
		while ( chambers.get(loadingChamber) ) {
			rotateClockwise();
		}		
		chambers.set(loadingChamber);
		rotateClockwise();
	}	
	
	private void spin() {
		final int spins = random.nextInt(0, chamberCount);
		for ( int i = 0; i < spins; i++ ) {
			rotateClockwise();
		}
	}
	
	private boolean fire() {
		boolean fire = chambers.get(firingChamber);
		chambers.set(firingChamber, false);
		rotateClockwise();
		return fire;			
	}
	
	private void rotateClockwise() {		
		final boolean temp = chambers.get(chamberCount - 1);
		for ( int i = chamberCount - 2; i >= 0; i-- ) {
			chambers.set(i + 1, chambers.get(i));
		}
		chambers.set(firingChamber, temp);
	}
		
	private ResultState useSituationA() {
		unload();
		load();
		spin();
		load();
		spin();
		if ( fire() ) {
			return ResultState.DEAD;
		};
		spin();
		if ( fire() ) {
			return ResultState.DEAD;
		};
		
		return ResultState.ALIVE;
	}
	
	private ResultState useSituationB() {
		unload();
		load();
		spin();
		load();
		spin();
		if ( fire() ) {
			return ResultState.DEAD;
		};
		if ( fire() ) {
			return ResultState.DEAD;
		};
		
		return ResultState.ALIVE;
	}
	
	private ResultState useSituationC() {
		unload();
		load();
		load();
		spin();
		if ( fire() ) {
			return ResultState.DEAD;
		};
		spin();
		if ( fire() ) {
			return ResultState.DEAD;
		};
		
		return ResultState.ALIVE;
	}
	
	private ResultState useSituationD() {
		unload();
		load();
		load();
		spin();
		if ( fire() ) {
			return ResultState.DEAD;
		};
		if ( fire() ) {
			return ResultState.DEAD;
		};
		
		return ResultState.ALIVE;
	}	
	
	private BitSet chambers;
	private ThreadLocalRandom random;
	
	private final int firingChamber = 0;
	private final int loadingChamber = 1;
	private final int chamberCount = 6;
	
}

```

## Python Code
### python_code_1.txt
```python
""" Russian roulette problem """
import numpy as np

class Revolver:
    """ simulates 6-shot revolving cylinger pistol """

    def __init__(self):
        """ start unloaded """
        self.cylinder = np.array([False] * 6)

    def unload(self):
        """ empty all chambers of cylinder """
        self.cylinder[:] = False

    def load(self):
        """ load a chamber (advance til empty if full already), then advance once """
        while self.cylinder[1]:
            self.cylinder[:] = np.roll(self.cylinder, 1)
        self.cylinder[1] = True

    def spin(self):
        """ spin cylinder, randomizing position of chamber to be fired """
        self.cylinder[:] = np.roll(self.cylinder, np.random.randint(1, high=7))

    def fire(self):
        """ pull trigger of revolver, return True if fired, False if did not fire """
        shot = self.cylinder[0]
        self.cylinder[:] = np.roll(self.cylinder, 1)
        return shot

    def LSLSFSF(self):
        """ load, spin, load, spin, fire, spin, fire """
        self.unload()
        self.load()
        self.spin()
        self.load()
        self.spin()
        if self.fire():
            return True
        self.spin()
        if self.fire():
            return True
        return False

    def LSLSFF(self):
        """ load, spin, load, spin, fire, fire """
        self.unload()
        self.load()
        self.spin()
        self.load()
        self.spin()
        if self.fire():
            return True
        if self.fire():
            return True
        return False

    def LLSFSF(self):
        """ load, load, spin, fire, spin, fire """
        self.unload()
        self.load()
        self.load()
        self.spin()
        if self.fire():
            return True
        self.spin()
        if self.fire():
            return True
        return False

    def LLSFF(self):
        """ load, load, spin, fire, fire """
        self.unload()
        self.load()
        self.load()
        self.spin()
        if self.fire():
            return True
        if self.fire():
            return True
        return False


if __name__ == '__main__':

    REV = Revolver()
    TESTCOUNT = 100000
    for (name, method) in [['load, spin, load, spin, fire, spin, fire', REV.LSLSFSF],
                           ['load, spin, load, spin, fire, fire', REV.LSLSFF],
                           ['load, load, spin, fire, spin, fire', REV.LLSFSF],
                           ['load, load, spin, fire, fire', REV.LLSFF]]:

        percentage = 100 * sum([method() for _ in range(TESTCOUNT)]) / TESTCOUNT
        print("Method", name, "produces", percentage, "per cent deaths.")

```

