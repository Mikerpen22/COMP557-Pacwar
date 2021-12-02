import os
import random
import _PyPacwar

def read_genes(file):
    genes = []
    with open(file) as reader:
        while True:
            ln = reader.readline()
            if not ln:
                break
            genes.append(str_to_gene(ln))
    return genes

def write_gene(gene, score, file):
    with open('res_file', 'w') as writer:
        writer.write(gene, score)


def write_genes(genes, file):
    with open('res_file', 'w') as writer:
        for gene in genes:
            writer.write(gene_to_str(gene[0], gene[1]))


def init_winning_write(size):
    with open('winning.txt', 'w') as writer:
        for i in range(size):
            writer.write(gene_to_str(generate_rand_gene(), .0))

def read_winning():
    return read_genes("winning.txt")

def clear_winning():
    writer = open("winning.txt", "w")
    writer.truncate(0)

def gene_to_str(gene, score):
    return ''.join(str(i) + " " for i in gene) + str(score) + "\n"

def str_to_gene(s):
    print(s)
    s = s.split()
    gene = []
    for i in range(len(s)-1):
        gene.append(int(s[i]))
    score = float(s[-1])
    return gene, score

def generate_rand_gene():
    return [random.choice([0, 1, 2, 3]) for i in range(50)]


def create_random_champs(size):
    init_winning_write(size)


def og_score(gene_1, gene_2):
    # print(_PyPacwar.battle(gene_1, gene_2))
    rounds, g1_left, g2_left = _PyPacwar.battle(gene_1, gene_2)

    # g1 wins
    if g1_left > g2_left:
        if g2_left == 0:
            if rounds < 50:
                return 10
            elif rounds < 100:
                return 9
            elif rounds < 200:
                return 6
            elif rounds < 350:
                return 4
            elif rounds < 500:
                return 2
        else:
            return 1
    # g1 loses
    else:
        if rounds < 50:
            return 1
        elif rounds < 200:
            return 2
        elif rounds < 500:
            return 3
        else:
            return 0

def get_scores(pop):
    scores = []
    for gene_i, score_i in pop:
        score = pop_score(gene_i[0], pop)
        scores.append(score)
    return scores

## Calculate gene_i's avg og_score against the whole pop
def pop_score(gene_i, pop):
    og_scores_sum = []
    for gene_j, score in pop:
        s = og_score(gene_i, gene_j)
        og_scores_sum.append(s)
    avg_og_score = sum(og_scores_sum)/len(og_scores_sum)
    return avg_og_score


## Calculate gene_i's avg score against the winning group
def winning_pop_score(gene_i):
    og_scores = []
    winning_genes = read_genes('winningGenes.txt')
    for winning_gene, winning_g_score in winning_genes:
        og_score = og_score(gene_i, winning_gene)
        og_scores.append(og_score)
    return sum(og_scores)/(len(og_scores)*1.0)

# def aggregated_score(gene_i, pop):
#     return winning_pop_score()

# Take 2 genes in population and have it battle with each other
# keep the winning one => the function will return the winning population
def battling(pop):
    battles = [pop[i:i + 2] for i in range(0, len(pop), 2)]
    dominating_pop = []
    for battle in battles:
        rounds, g1_left, g2_left = _PyPacwar.battle(battle[0][0], battle[1][0])
        if g1_left > g2_left:
            dominating_pop.append((battle[0][0], .0))
        else:
            dominating_pop.append((battle[1][0], .0))
    return dominating_pop

def sort_genes_by_score(pop, scores):
    zipped = list(zip(pop, scores))
    zipped.sort(key=lambda x: x[1], reverse=True)
    genes = list(map(lambda x: (x[0][0], 0), zipped))
    return genes


def updateWinningGenes(pop):
    winning_genes = read_winning()
    winning_genes_updated = []
    scores_updated = []

    for gene_i, score_i in pop:
        for gene_j, score_j in winning_genes:
            if (gene_j, 0) not in winning_genes_updated:
                rounds, g_i_left, g_j_left = _PyPacwar.battle(gene_i, gene_j)
                gene_j_score = pop_score(gene_j, pop)
                winning_genes_updated.append((gene_j, 0))
                scores_updated.append(gene_j_score)

            if (gene_i, 0) not in winning_genes_updated:
                if g_i_left > g_j_left:
                        gene_i_score = pop_score(gene_i, pop)
                        winning_genes_updated.append((gene_i, 0))
                        scores_updated.append(gene_i_score)

    winning_genes_updated = sort_genes_by_score(winning_genes, scores_updated)[0:12]

    clear_winning()
    write_genes(winning_genes_updated, "champions.txt")
    print("Best Gene: ", winning_genes_updated[0][0], max(scores_updated))
    return winning_genes_updated
