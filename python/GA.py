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
    numOfPopulations = 20   # Think of it as evolutions
    iterations = 50     # How many times you want the genes in population to battle each other
    winning_group_size = 10     # we want to keep track of the top 10 genes
    pop_size = pow(2, 13)       # size for a single population
    mutate_prop = 0.02          # mutation probability
    crossover_prop = 0.2        # crossover probability
    helper.init_winning_write(winning_group_size)   # randomly write 10 genes to the file for the program to start

    for i in range(numOfPopulations):
        ## Generate population
        pop = generate_pop(pop_size)

        ## Halving the size everytime
        for j in range(11):
            pop = helper.battling(pop)

        # Run GA
        for itr in range(iterations):
            print(f"---itr {itr} ---")
            scores = helper.get_scores(pop)
            pop = sort_pop_by_score(pop, scores)
            mutate(pop, mutate_prop)
            crossover(pop, crossover_prop)

        ## Update the top 10, write to file
        helper.updateWinningGenes(pop)


if __name__ == "__main__":
    main()



