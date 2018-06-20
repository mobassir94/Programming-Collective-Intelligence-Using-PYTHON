"""
The code for the pearson Correlation Score first finds the item rated by both critics.It then calculates the sums and
the sum of the squares of the ratings for the two critics, and calculates the sum of the products of their ratings,finally it uses
these results to calculate the sum of the pearson correlation coefficient (r)--> (shown in the commented section called
"calculating pearson correlation coefficient r"
...........................................................

Details on [earson correlation coefficient here : https://study.com/academy/lesson/pearson-correlation-coefficient-formula-example-significance.html

Pearson's r calculating formula here : https://study.com/cimages/multimages/16/begning.jpg

"""

# Method Below Returns the pearson Correlation Coefficient r for person1/p1 and person2/p2
from math import sqrt
from recommendationDataset import critics
def pearsons_r(prefs,p1,p2):
    similar = {}
    for items in prefs[p1]:
        if items in prefs[p2]:
            similar[items] = 1
            #print(similar[items])
    n=len(similar)
    #print(n)
    if n==0: return 0  #if they have no or 0 preferences

    #adding person1's preferences in sum1 and person2's preferences in sum2

    sum1 = sum(prefs[p1][iter] for iter in similar)
    sum2 = sum(prefs[p2][iter] for iter in similar)

    #summing up the squares

    sum1sqr = sum(pow(prefs[p1][iter],2) for iter in similar)

    sum2sqr = sum(pow(prefs[p2][iter], 2) for iter in similar)

    #summing the products

    productSum = sum(prefs[p1][iter] * prefs[p2][iter] for iter in similar)

  # calculating pearson correlation coefficient r

    numerator = productSum - ((sum1 * sum2 )/n)
    denominator = sqrt((sum1sqr-pow(sum1,2)/n) * (sum2sqr-pow(sum2,2)/n))
    if denominator == 0: return 0

    r = numerator/denominator
    print(r)


# calling pearsons_r method

pearsons_r(critics, 'Michael Phillips','Toby')