def fibd(maxGenerations, maxLives):

    youngBunnies = 1
    matureBunnies = 0
    listOfYoungBunnies = []
    howManyBunnies = []

    for gen in range(1, maxGenerations + 1):

        listOfYoungBunnies.append(youngBunnies)
        howManyBunnies.append(matureBunnies + youngBunnies)

        matureBunnies += youngBunnies
        youngBunnies = (matureBunnies - youngBunnies)

        if  (gen - maxLives) >= 0:
            matureBunnies -= listOfYoungBunnies[gen - maxLives]

    return(howManyBunnies[-1])

maxGenerations = 86
maxLives = 17

print(fibd(maxGenerations, maxLives))