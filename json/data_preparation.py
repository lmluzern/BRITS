import json
from random import randrange

MISSING_VALUE_PERCENTAGE = 25
GROUND_TRUTH_PERCENTAGE = 10

delta = 0.0
masks = 1
eval_masks = 0
data = {}
data['forward'] = []
firstIteration = True

file = open("airq_normal_first_column.txt", "r")

for v in file:
    value = float(v)
    eval = float(v)
    rand_m = randrange(100//MISSING_VALUE_PERCENTAGE)
    rand_g = randrange(100//GROUND_TRUTH_PERCENTAGE)
    
    if rand_m == 0:
        masks = 0
        eval_masks = 0
        value = 0.0
        eval = 0.0
        if not firstIteration:
            delta = delta + 1.0
    else:
        if rand_g == 0:
            masks = 0
            eval_masks = 1
            value = 0.0
            if not firstIteration:
                delta = delta + 1.0
        else:
            masks = 1
            eval_masks = 0
    
    data['forward'].append({
        'evals': [eval],
        'deltas': [delta],
        'forwards': [0.0],
        'masks': [masks],
        'values': [value],
        'eval_masks': [eval_masks],
    })
    
    firstIteration = False
    
    
data['backward'] = []

firstIteration = True
delta = 0.0
for e in reversed(data['forward']):
    newDict = e.copy()
    if not firstIteration and newDict['masks'][0] == 0:
        delta = delta - 1.0
    newDict['deltas'] = [delta]
    data['backward'].append(newDict)
    
    firstIteration = False

data['label'] = 0

with open('json_univariate', 'w') as outfile:
    json.dump(data, outfile)

print('finished')
