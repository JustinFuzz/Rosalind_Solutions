def iprb(k, m, n):
    
    total = k + m + n

    k_k = (k / total) * ((k - 1) / (total - 1)) #100
    k_m = (k / total) * (m / (total - 1))     #100
    k_n = (k / total) * (n / (total - 1))     #100

    m_m = (m / total) * ((m - 1) / (total - 1)) #75
    m_k = (m / total) * (k / (total - 1))     #100
    m_n = (m / total) * (n / (total - 1))     #50

    n_n = (n / total) * ((n - 1) / (total -1))  #0
    n_k = (n / total) * (k / (total - 1))     #100
    n_m = (n / total) * (m / (total - 1))     #50

    result =  k_k + k_m + k_n + m_k + n_k  + (m_m * 0.75)  + (m_n * 0.5) + (n_m * 0.5) + (n_n * 0)

    return result

homo_dom = 24
hetero = 21
homo_rec = 18

print(iprb(homo_dom, hetero, homo_rec))