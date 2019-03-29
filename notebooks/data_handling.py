# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import json
import numpy as np

# <codecell>

user_id = "1010"

# <codecell>

with open(f'../data/answers/{user_id}.json', 'r') as f:
    #answers = pd.read_json(f)
    #answers = f.read()
    answers = json.load(f)
    
    
with open(f'../data/additional_data/{user_id}.json', 'r') as f:
    additional_data = json.load(f)

# <codecell>

from pandas.io.json import json_normalize    

# <codecell>

import pandas as pd

# <codecell>

answers['data'][:2]

# <codecell>

answers = pd.DataFrame(answers)
#answers['question_id'] = answers['data'].str

# <codecell>

answers[['question_id', 'answer', 'timestamp']] = pd.DataFrame(answers.data.values.tolist(), index=answers.index)

# <codecell>

answers

# <codecell>

json_normalize(answers[0], 'data', ['api_token'])

# <codecell>

answers

# <codecell>

answers = pd.DataFrame(answers)

# <codecell>



# <codecell>

additional_data

# <codecell>

ls ../data/additional_data/

# <codecell>

!rm ../data/answers/*
!rm ../data/additional_data/*

# <codecell>

cat ../data/additional_data/1010.json

# <codecell>

data

# <codecell>



# <codecell>

data[-1]

# <codecell>


