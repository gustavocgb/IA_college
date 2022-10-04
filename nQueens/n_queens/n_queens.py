import numpy as np

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


if __name__ == '__main__':

  #representacao das solucoes
  #[1,2,3,4,5,6,7,8,..,n]

  sol = list(range(8))

  sol1 = obj(sol)

  print(sol1)

    