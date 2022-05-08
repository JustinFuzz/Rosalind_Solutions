def gc(f):
    actualArray = f.read().split(">")  
    #dictionary to track all codes and percent of CG
    dictGC = {}

    for i in range(1,len(actualArray)):
        wantedString = actualArray[i]
        #get id of strand
        wantedID = wantedString[:wantedString.index("\n")]
        
        #get strand
        wantedStrand = wantedString[wantedString.index("\n"):]
        wantedStrand = wantedStrand.replace("\n", "")
        
        numCG = 0
        for j in range(len(wantedStrand)):
            if wantedStrand[j] == 'C' or wantedStrand[j] == 'G':
                numCG += 1

        dictGC[wantedID] = numCG / len(wantedStrand)
    
    #get highest value
    all_keys = list(dictGC.keys())
    all_values = list(dictGC.values())
    highestGC = max(all_values)

    print(all_keys[all_values.index(highestGC)])
    print(highestGC * 100)
    return 

f = open("../rosalind_gc.TXT", "r")

gc(f)