# -*- coding: utf-8 -*-
# <nbformat>4</nbformat>

# <codecell>

import numpy as np

# <codecell>

__TASK_ORDER__ = [1,2,3,4]
__MUSIC_ORDER__ = ['relax', 'energy', 'nothing']
    
def generate_user_ids(n):
    '''Generate a list of n valid user ids.'''
    return [hex(2*i + 16)[-2:] + hex(i + 16)[-2:] for i in range(n)]

def shuffle(user_id):
    return int(user_id[-2:], 16) - 16

def shuffle_task(tasks):
    '''Returns shuffled task for specified user'''
    return np.random.permutation(tasks)

def shuffle_music(music_order):
    '''Returns shuffled music_order for specified user'''
    return np.random.permutation(music_order)

def user_task(user_id, tasks=__TASK_ORDER__, music_order=__MUSIC_ORDER__):
     # the last one is always self chosen
    return {user_id: {'questions': shuffle_task(tasks).tolist(), 'music_order': shuffle_music(music_order).tolist() + ['nothing']}}

# <codecell>

np.random.seed(42)
assignments = [user_task(i) for i in generate_user_ids(10)]

# <codecell>

list(a.values())

# <codecell>

def get_key(d):
    return list(d.keys())[0]

def get_vals(d):
    return list(d.values())[0]

import json
with open('../data/user_assigments.json', 'w') as f:
    json.dump({get_key(d): get_vals(d) for d in assignments}, f)

# <codecell>

ls ../data/

# <codecell>


