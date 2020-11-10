#!/usr/bin/env python3

##### Calculation functions for main program #####

import random


def initial_velocity_generation():
    side = random.randint(0, 1)
    mag = random.randint(10, 40)
    if side == 0:
        mag = -1 * mag 
    return mag


def verify_distance(pos1, pos2):
    if pos2 - pos1 < 50:
        return 20 - (pos2 - pos1)
    else:
        return 0

def side_finder():
    return random.randint(1, 2)

def next_position(current_position, mag):
    return current_position + mag

def encounter_nextpos(factor, pos_e1, pos_e2):
    pass