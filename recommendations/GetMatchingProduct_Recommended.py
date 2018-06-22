from recommendationDataset import critics

def transformPrefs(prefs):
    results = {}
    for person in prefs:
        for item in prefs[person]:
            results.setdefault(item,{})

            # flipping item and person

            results[item][person] = prefs[person][item]
            #print(results)
    return results

#calling transforPrefs(prefs)

movies = transformPrefs(critics)
print(movies)

import Ranking_Critics
#Ranking_Critics.topmatches()

matches = Ranking_Critics.topmatches(movies,'Just My Luck',n=5)
print(matches)
