import _PyPacwar
import numpy
import random
import time


# Example Python module in C for Pacwar
def main():

    # rand_shit = []
    random.seed(time.time)
    # for _ in range(50):
    #     rand_shit.append(random.randint(0,3))
    rand_idx_to_flip = []
    for _ in range(5):
        rand_idx_to_flip.append(random.randint(0,49))
    ones = [1] * 50
    for idx_to_flip in rand_idx_to_flip:
        # ones[idx_to_flip] = random.randint(0,3)
        ones[idx_to_flip] = 0

    threes = [3] * 50
    og_ones = [1]*50
    
    print("Example Python module in C for Pacwar")
    print("all ones versus all threes ...")
    (rounds, c1, c2) = _PyPacwar.battle(ones, og_ones)
    print("Number of rounds:", rounds)
    print("Ones PAC-mites remaining:", c1)
    print("Threes PAC-mites remaining:", c2)

    print(ones)

if __name__ == "__main__":
    main()
