
def explain(observations, kb, explanation=set()):

    if observations:

        o = observations[0]

        if o in kb['assumables']:

            return explain(observations[1:], kb, explanations|{o})

        else:

            bodies = kb['rules'][o]

            explanations = []

            for body in bodies:

                explanations += explain(body + observations[1:], kb, explanation)

            return explanations

    return [explanation]

def get_minimal_explanation(explanations):

    not_minimal = []

    for i in range(len(explanations)):

        for j in range(len(explanations)) and i != j:

            if explanations[i].issubset(explanations[j]):

                not_minimal.append(j)

    minimal = [explanations[i] for i in range(len(explanations)) if i not in not_minimal]

    return minimal