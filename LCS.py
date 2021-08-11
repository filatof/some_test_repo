def lcs(A, B):
    # Use a breakpoint in the code line below to debug your script.
    F = [[0] * (len(B) + 1) for _ in range(len(A) + 1)]
    P = [[None] * (len(B) + 1) for _ in range(len(A) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
            if A[i - 1] == B[j - 1]:
                F[i][j] = F[i - 1][j - 1] + 1
                P[i][j] = (i - 1, j - 1, A[i - 1])
            else:
                # F[i][j] = max(F[i-1][j], F[i][j-1])
                if F[i - 1][j] > F[i][j - 1]:
                    F[i][j] = F[i - 1][j]
                    P[i][j] = (i - 1, j , '')
                else:
                    F[i][j] = F[i][j - 1]
                    P[i][j] = (i, j -1 , '')

    ans = ''
    cur = P[-1][-1]
    for x in P:
        print(x)
    while cur is not None:
        ans += cur[2]
        cur = P[cur[0]][cur[1]]
        # print(P[cur[0]][cur[1]])

    print(ans[::-1])
    for x in F:
        print(x)
    return F[-1][-1]

A = "fish"
B = "fich"
print(lcs(A, B))
