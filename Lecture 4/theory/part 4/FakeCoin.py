import enum

Scale = enum.Enum(
    "Scale", ["LeftHeavy", "RightHeavy", "Balanced"]
)

coin_real = 2
coin_fake = 1

def compare(left, right):
    delta = sum(right) - sum(left)
    if delta < 0:
        return Scale.LeftHeavy
    elif delta > 0:
        return Scale.RightHeavy
    else:
        return Scale.Balanced


compare([coin_fake], [coin_real])

def find_fake(*, coins, compare):
    pile = list(coins)
    while len(pile) > 1:
        n = len(pile) // 2
        A = pile[:n]   # lấy phân nửa bên phải số coin (0,1,2,3,...,n-1)
        B = pile[n : 2 * n] # (n, n+1, n+2,..., 2*n-1)

        result = compare(A, B)
        if result == Scale.LeftHeavy:
            pile = B # coin ở nhóm B [n/3]
        elif result == Scale.RightHeavy:
            pile = A # coin ở nhóm A [n/3]
        elif result == Scale.Balanced:
            C = pile[2 * n :]
            pile = C # coin ở nhóm C n-2[n/3]

    print(pile[0])
    return pile[0]

test_pass = 0
test_fail = 0


coins = [2,1,2,2,2,2,2,2]
found = find_fake(coins=coins, compare=compare)
if found == coin_fake:
    test_pass = 1
else:
    test_fail = 1

print("Tests passed:", test_pass)
print("Tests failed:", test_fail)