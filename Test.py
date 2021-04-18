from ProofOfStake import ProofOfStake
from Lot import Lot
import string
import random

def getRandomString(length):
    letters = string.ascii_lowercase
    resultString = ''.join(random.choice(letters) for i in range(length))
    return resultString

bobStake = random.randint(0,100)
aliceStake = random.randint(0,100)

if __name__ == '__main__':
    pos = ProofOfStake()
    pos.update('bob', bobStake)
    pos.update('alice', aliceStake)

    bobWins = 0
    aliceWins = 0

    for i in range(100):
        forger = pos.forger(getRandomString(i))
        if forger == 'bob':
            bobWins += 1
        elif forger == 'alice':
            aliceWins += 1

    print('bob won: ' + str(bobWins) + ' times with ' + str(bobStake) + ' coins')
    print('alice won: ' + str(aliceWins) + ' times with ' + str(aliceStake) + ' coins')