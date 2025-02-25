def can_arrange(boys, girls):
    boys.sort()
    girls.sort()
    n = len(boys)
    def check_pattern(first):
        
        seq = []
        if first == 'b':
            for i in range(n):
                seq.append(boys[i])
                seq.append(girls[i])
        else:
            for i in range(n):
                seq.append(girls[i])
                seq.append(boys[i])
        return all(seq[i] <= seq[i+1] for i in range(2 * n - 1))
    return check_pattern('b') or check_pattern('g')

t = int(input())
for _ in range(t):
    n = int(input())
    boys = list(map(int, input().split()))
    girls = list(map(int, input().split()))
    print("YES" if can_arrange(boys, girls) else "NO")
    
