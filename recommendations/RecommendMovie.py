# Gets recommendations for a person by using weighted aveage f every other users rating

from PearsonsCorrelationCoefficient_r import pearsons_r
from recommendationDataset import critics

totals = {}
SimSums = {}
def getRecommendation(prefs,person,similarity = pearsons_r):
    for other in prefs:
        # not comparing with recommend getable person
        if other == person:  continue
        sim = similarity(prefs, person, other)
        if sim <= 0: continue

        for item in prefs[other]:
            #only score movies the person haven't seen yet
            if item not in prefs[person] or prefs[person][item] == 0:
                #similarity * score
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim

                #sum of similarities

                SimSums.setdefault(item,0)
                SimSums[item] +=sim

#creating the normalized list

    rankings = [(total/SimSums[item],item) for item,total in totals.items()]

    # return the sorted list

    rankings.sort()
    rankings.reverse()
    return rankings




# calling getRecommendation() method

MoviesToWatch = getRecommendation(critics,'Toby')


for movies in MoviesToWatch:
    print(movies)





