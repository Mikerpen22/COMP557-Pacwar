import _PyPacwar
import numpy
import random
import time

def crossover():


def gen_random_genes(g):   
    # random.seed(1)
    rand_idx_to_flip = []
    for _ in range(10):
        rand_idx_to_flip.append(random.randint(0,49))
    for idx_to_flip in rand_idx_to_flip:
        # ones[idx_to_flip] = random.randint(0,3)
        g[idx_to_flip] = random.choice([0,1,2,3])
    return g

# Example Python module in C for Pacwar
def main():
    potential = []
    # random.seed(time.time)
    # rand_idx_to_flip = []
    # for _ in range(3):
    #     rand_idx_to_flip.append(random.randint(0,49))
    # ones = [1]*50
    # for idx_to_flip in rand_idx_to_flip:
    #     # ones[idx_to_flip] = random.randint(0,3)
    #     ones[idx_to_flip] = random.choice([0,2,3])

    threes = [3] * 50
    og_ones = [1] * 50

    # ones =[1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1]

    while(len(potential) < 1):
        ones = gen_random_genes([1]*50)
        print("Example Python module in C for Pacwar")
        print("all ones versus all threes ...")
        (rounds1, c11, c21) = _PyPacwar.battle(ones, og_ones)
        print("Number of rounds:", rounds1)
        print("Mod-Ones PAC-mites remaining:", c11)
        print("Ones PAC-mites remaining:", c21)

        (rounds2, c12, c22) = _PyPacwar.battle(ones, threes)
        print("Number of rounds:", rounds2)
        print("Mod-Ones PAC-mites remaining:", c12)
        print("Threes PAC-mites remaining:", c22)

        if(c21 == 0 and c22 == 0):
            potential.append(ones)
        else:
            ones=gen_random_genes(ones)




        # if c11 > c21 or c12 > c22:
        #     rand_idx_to_flip = []
        #     if rounds1 < 200 and rounds2 < 200:
        #         potential.append(ones)
        #     for _ in range(10):
        #         rand_idx_to_flip.append(random.randint(0,49))
        #     for idx_to_flip in rand_idx_to_flip:
        #         ones[idx_to_flip] = random.choice([0, 1, 2, 3])
        # else:
        #     ones = gen_random_genes()
        #     # rand_idx_to_flip = []
        #     # for _ in range(10):
        #     #     rand_idx_to_flip.append(random.randint(0,49))
        #     # for idx_to_flip in rand_idx_to_flip:
        #     #     ones[idx_to_flip] = random.choice([0])




        # print(ones)
    print(potential[0])
    cand = potential[0]
    cand[random.randint(0,49)] = random.choice([0,1,2,3])
    print("Example Python module in C for Pacwar")
    print(cand)
    print("all ones versus all threes ...")
    (rounds1, c11, c21) = _PyPacwar.battle(cand, og_ones)
    print("Number of rounds:", rounds1)
    print("Mod-Ones PAC-mites remaining:", c11)
    print("Ones PAC-mites remaining:", c21)
    
    (rounds2, c12, c22) = _PyPacwar.battle(cand, threes)
    print("Number of rounds:", rounds2)
    print("Mod-Ones PAC-mites remaining:", c12)
    print("Threes PAC-mites remaining:", c22)

if __name__ == "__main__":
    main()
