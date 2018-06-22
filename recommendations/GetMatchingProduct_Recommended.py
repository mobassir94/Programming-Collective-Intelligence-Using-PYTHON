from recommendationDataset import critics
from RecommendMovie import getRecommendation
import Ranking_Critics
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


#Ranking_Critics.topmatches()

matches = Ranking_Critics.topmatches(movies,'Just My Luck',n=5)
print(matches)

recommendation = getRecommendation(movies,'Just My Luck')

print('recommended : ')
for match in recommendation:
    print(match)