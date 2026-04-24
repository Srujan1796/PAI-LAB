states = ['Rainy', 'Sunny']
obs = ['walk', 'shop', 'clean']

pi = {'Rainy': 0.6, 'Sunny': 0.4}

A = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

B = {
    'Rainy': {'walk': 0.1, 'shop': 0.4, 'clean': 0.5},
    'Sunny': {'walk': 0.6, 'shop': 0.3, 'clean': 0.1}
}

O = ['walk', 'shop', 'clean']  # observation sequence

# Forward Algorithm
alpha = [{s: pi[s]*B[s][O[0]] for s in states}]

for t in range(1, len(O)):
    alpha.append({
        s: sum(alpha[t-1][sp]*A[sp][s] for sp in states)*B[s][O[t]]
        for s in states
    })

print("P(O) =", sum(alpha[-1].values()))
