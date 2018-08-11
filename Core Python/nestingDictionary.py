
d ={'k1': [{'nest' : ['this is deep',['hello']]}]}

for i in d:
    for j in d['k1'][0]:
        for k in d['k1'][0]['nest'][1]:
            print(k)






d = {'k1':[1,2,{'k2':['this is tricky',{'toughie':[1,2,['hello hard1']]}]}]}
#print(d['k1'][2]['k2'][1]['toughie'][2])

for x in d:
    for i in d['k1'][2]:
        for h in d['k1'][2]['k2']:
            for j in d['k1'][2]['k2'][1]:
                for k in d['k1'][2]['k2'][1]['toughie'][2]:
                    print (k)