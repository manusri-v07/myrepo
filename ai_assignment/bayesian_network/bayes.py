from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create model
model = DiscreteBayesianNetwork([
    ('Rain', 'Traffic'),
    ('Traffic', 'Late')
])

# Define probabilities

cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7], [0.3]]  # No rain, Rain
)

cpd_traffic = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.8, 0.2],  # No traffic
        [0.2, 0.8]   # Traffic
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

cpd_late = TabularCPD(
    variable='Late',
    variable_card=2,
    values=[
        [0.9, 0.3],  # Not late
        [0.1, 0.7]   # Late
    ],
    evidence=['Traffic'],
    evidence_card=[2]
)

# Add CPDs
model.add_cpds(cpd_rain, cpd_traffic, cpd_late)

# Check model
print("Model is valid:", model.check_model())

# Inference
inference = VariableElimination(model)

# Query: Probability of being late if it is raining
result = inference.query(variables=['Late'], evidence={'Rain': 1})

print("\nProbability of being late given Rain:")
print(result)
