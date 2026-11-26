import json
from pathlib import Path

def source(name, index):
    nb=json.loads((Path(__file__).resolve().parents[1]/'notebooks'/f'{name}.ipynb').read_text())
    return ''.join(nb['cells'][index]['source'])

import numpy as np
x_train = np.array([[0.], [2.]])
x_test = np.array([[100.]])
ns = dict(x_train=x_train, x_test=x_test)
exec(source('crop-yield-prediction-model',36), ns)
assert np.allclose(ns['sc'].mean_, [1.])
assert np.allclose(ns['x_test'], [[99.]])

print('Targeted regression passed; no original-data performance claim.')
