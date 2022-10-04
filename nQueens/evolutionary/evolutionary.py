import numpy as np
import copy

# semelhante ao processo de selecao natural de darwin. Onde se tem uma determinada populacao, solucoes, que sofrem mutaccoes,
# troca de solucao a cada iteracao, e se reproduzem, se comparam as solucoes, permanecendo a mais adaptavel, a melhor solucao

# verifica conflito na coluna
def different_column_violations(sol):

    conflicts = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            if (i != j) and (sol[i] == sol[j]):
                conflicts += 1
                
    return conflicts

# verifica conflito na diagonal
def different_diagonal_violations(sol):

    conflicts = 0
    for i in range(len(sol)):
        for j in range(len(sol)):
            deltay = abs(sol[i]-sol[j])
            deltax = abs(i - j)
            if (deltay == deltax):
                conflicts += 1

    return conflicts

# objetivo
def obj(sol):
    return different_diagonal_violations(sol) + different_column_violations(sol)






# gera populacao inicial
def pop_init(k, n):
    # gera permutacoes
    return [np.random.permutation(n) for i in range(k)]

# estrtutura de vizinhanca de troca parar trocar mutacoes
def mutation(sol):

    neighbor = copy.copy(sol)

    idx1 = np.random.randint(0, len(sol))
    idx2 = np.random.randint(0, len(sol))

    neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

    return neighbor

# intersecao, cruzamento
def crossover(sol1, sol2):
    # vetor binario
    mask = np.random.randint(2, size=len(sol1))

    f1 = copy.copy(sol1)
    for i in range(len(sol1)):
        if mask[i] == 0:
            f1[i] = sol2[i]

    f2 = copy.copy(sol2)
    for i in range(len(sol2)):
        if mask[i] == 0:
            f2[i] = sol1[i]

    return f1, f2


def select_parent(pop):
    
    print(pop)
    
    
    return

def EA_nqueens(pop_size=10, n=8, gen_max=2):

    # Generate population
    pop = pop_init(pop_size, n)
    
    gen = 0  # Contador de geracoes

    while gen < gen_max:

        for i in pop:
            # Selecao para reproducao
            idx_P1 = select_parent(i)
            idx_P2 = select_parent(i)
            # Crossover
            #F1, F2 = crossover(pop[idx_P1], pop[idx_P2])
            # Mutacao + atualizacao da populacao
            #pop[idx_P1] = mutation(F1)
            #pop[idx_P2] = mutation(F2)

        gen += 1

    # Encontrar o melhor individuo da populacao

    #return best_ind
    return ''


if __name__ == '__main__':

    aux = EA_nqueens()

#    pop = pop_init(10, 8)
#    for p in pop:
#        print(p)

#    print('------------------')
#    print(pop[0])

#    print(mutation(pop[0]))

#    print('------------------')
#    print(pop[0])
#    print(pop[1])

#    f1, f2 = crossover(pop[0], pop[1])

#    print(f1)
#    print(f2)
