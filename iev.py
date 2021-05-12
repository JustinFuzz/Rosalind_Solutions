def iev(AA_AA, AA_Aa, AA_aa, Aa_Aa, Aa_aa, aa_aa):
    total = 0 
    total += AA_AA + AA_Aa + AA_aa + (Aa_Aa * 0.75) + (Aa_aa * 0.5) + (aa_aa * 0)
    return(total * 2)

num1 = 17884
num2 = 16767
num3 = 19440
num4 = 18297
num5 = 19765
num6 = 18662

print(iev(num1, num2, num3, num4, num5, num6))