from recommendationDataset import critics

def EuclideanDistance(prefs,person1,person2):
    si = {}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1


    if len(si)==0:
        return 0
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2)
                        for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)

#calling function

result=EuclideanDistance(critics,'Toby','Mick LaSalle')
print(result)
result=EuclideanDistance(critics,'Lisa Rose','Gene Seymour')
print(result)


