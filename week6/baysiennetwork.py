import pandas as pd
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.inference import VariableElimination

# Dataset
data = pd.DataFrame({
    'Rain': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No'],
    'TrafficJam': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No'],
    'ArriveLate': ['Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'Yes', 'No']
})

# Model
model = DiscreteBayesianNetwork([
    ('Rain', 'TrafficJam'),
    ('TrafficJam', 'ArriveLate')
])

# Train
model.fit(data, estimator=MaximumLikelihoodEstimator)

# Print CPDs
for cpd in model.get_cpds():
    print(cpd)
    print()

# Inference
inference = VariableElimination(model)

result = inference.query(
    variables=['ArriveLate'],
    evidence={'Rain': 'Yes'}
)

print("P(ArriveLate | Rain = Yes):")
print(result)
