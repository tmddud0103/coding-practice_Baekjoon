import sys
sys.stdin = open('input.txt')

prime_ox = [True for _ in range(4000001)]
for i in range(2, int(4000001 ** 0.5)):
    if prime_ox[i]:
        for j in range(i+i, 4000001, i):
            prime_ox[j] = False
prime_list = [i for i, j in enumerate(prime_ox) if j == True and i >=2 ]
sum_prime = [0] * (len(prime_list) + 1)
for i in range(len(prime_list)):
    sum_prime[i+1] = sum_prime[i] + prime_list[i]

N = int(sys.stdin.readline().lstrip())

answer = 0
start = 0
end = 1

while start < len(sum_prime) and prime_list[end-1] <= N:
    if sum_prime[end] - sum_prime[start] == N:
        answer += 1
        start += 1
    elif sum_prime[end] - sum_prime[start] > N:
        start += 1
    else:
        if end < len(sum_prime) - 1:
            end += 1
        else:
            start += 1

print(answer)