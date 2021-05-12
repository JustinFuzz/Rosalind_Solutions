def fib(maxGenerations, numChildren):
    youngBunnies = 1
    matureBunnies = 0
    for gen in range(maxGenerations):
        matureBunnies += youngBunnies
        youngBunnies = (matureBunnies - youngBunnies) * numChildren

    return(matureBunnies)

#Change these values.
numGenerations = 5
numChildren = 3

print(fib(numGenerations, numChildren))