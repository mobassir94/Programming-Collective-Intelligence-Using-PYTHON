Books = {
    'Mobassir' : {'b :':"The Alchemist",'c :':"Quite - (the power of Introvert... by susan cain)",'a :':"Teach Yourself c"},
    'Shabab' : {'c :':"Core Python",'a :':"the silent intelligent",'b :':"programming collective intelligence"}
}


for bestbook in Books:
    print('\n',bestbook,' : ','\n')
    for topbooks in sorted(Books[bestbook],reverse = True)[:1]:
        print(topbooks,Books[bestbook][topbooks])