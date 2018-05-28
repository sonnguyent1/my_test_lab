#!/usr/bin/python
from recommendations import critics, sim_distance, sim_pearson, topMatches

if __name__ == '__main__':

    print topMatches(critics, 'Toby', n=3)
