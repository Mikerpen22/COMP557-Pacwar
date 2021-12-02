import numpy
import random
import _PyPacwar
import helper


def generate_gene():
    return [random.choice([0, 1, 2, 3]) for i in range(50)]

def generate_pop(pop_size):
    gen = []
    for i in range(pop_size):
        # gen[i]: [[0,2,0,0,1,1,1....], score]
        gen.append([generate_gene(), 0])
    return gen

def crossover(pop, prob):
    firstGroup = pop[0:10]
    # print(pop)
    for gene_i, score_i in pop:
        for i in range(50):
            if random.random() < prob:
                gene_j = random.choice(firstGroup)[0]
                gene_i = gene_i[0:24] + gene_j[24:]
                gene_j = gene_j[0:24] + gene_i[24:]
    return pop

def mutate(pop, prob):
    for gene_i, score_i in pop:
        for pos in range(50):
            if random.random() < prob:
                choices = [0, 1, 2, 3]
                choices.remove(gene_i[pos])
                gene_i[pos] = random.choice(choices)
    return pop


def sort_pop_by_score(pop, scores):
    zipped = list(zip(pop, scores))
    zipped.sort(key=lambda x: x[1], reverse=True)
    genes = []
    genes = list(map(lambda x:(x[0][0], 0), zipped))
    return genes


def main():
    # parameters we use
    numOfPopulations = 100
    iterations = 50
    winning_group_size = 10
    pop_size = pow(2, 12)
    mutate_prop = 0.02
    crossover_prop = 0.2
    helper.init_winning_write(winning_group_size)

    for i in range(numOfPopulations):
        ## Generate population
        pop = generate_pop(pop_size)

        ## Halving the size everytime
        for j in range(12):
            pop = helper.battling(pop)

        # Run GA
        for itr in range(iterations):
            print(f"---itr {itr} ---")
            scores = helper.get_scores(pop)
            pop = sort_pop_by_score(pop, scores)
            print(pop)
            crossover(pop, crossover_prop)
            mutate(pop, mutate_prop)
        print("...checking champions")

        helper.updateWinningGenes(pop)


if __name__ == "__main__":
    main()


