"""
finding the best matches for a given person from the prefs dictionary
"""

from PearsonsCorrelationCoefficient_r import pearsons_r
from recommendationDataset import critics

def topmatches(prefs,person,n,similarity = pearsons_r):
    scores = [(similarity(prefs,person,other),other) for other in prefs if other != person]

    # sort the list to get the highest score on top of list

    scores.sort()
    scores.reverse()
    #for i in scores:
        #print(i)
    return scores[0:n]

#calling the topmatches method

result = topmatches(critics,'Toby',n=3)
for peoples in result:
    print(peoples)