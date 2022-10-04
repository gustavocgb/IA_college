import numpy as np
import copy
import matplotlib.pyplot as plt

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

# estrtutura de vizinhanca randomica
def rand_in_rand_position(sol):

  neighbor = copy.copy(sol)

  idx = np.random.randint(0, len(sol))
  value = np.random.randint(0, len(sol))

  neighbor[idx] = value

  return neighbor

# estrtutura de vizinhanca de troca
def swap(sol):

  neighbor = copy.copy(sol)

  idx1 = np.random.randint(0, len(sol))
  idx2 = np.random.randint(0, len(sol))

  # swap
  neighbor[idx1], neighbor[idx2] = neighbor[idx2], neighbor[idx1]

  return neighbor

# algoritmo de busca local, passando o maximo de iteracoes (maxit)
def local_search(sol, objective, get_neighbor, maxit=50):
  # primeira melhora

  c_vals = []
  best_val = objective(sol)
  it = 0
  while it <= maxit:
      n = get_neighbor(sol)
      n_val = objective(n)
      # se o n de conflitos do vizinhos for menor que o melhor valor registrado, sub sol atual 
      if n_val < best_val:
          sol = copy.copy(n)
          c_val = n_val
          best_val = n_val

      print(it, best_val)

      it += 1

      c_vals.append(c_val)

  return c_vals


if __name__ == '__main__':

  #representacao das solucoes
  #[1,2,3,4,5,6,7,8,..,n]

  sol = list(range(100))

  plot_sol = local_search(sol, obj, swap, maxit=1000)
  
  plt.plot(plot_sol)
  plt.show()

    