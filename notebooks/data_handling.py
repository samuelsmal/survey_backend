# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import json
import numpy as np

# <codecell>

ls ../data/additional_data/

# <codecell>

user_id = "1613"

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

from datetime import datetime

answers['timestamp'] = answers['timestamp'].apply(lambda x: datetime.utcfromtimestamp(x / 1000).strftime('%Y-%m-%d %H:%M:%S'))

# <codecell>

answers
