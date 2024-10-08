import sys
input = sys.stdin.readline

N, M = map(int, input().split()) #O(1)

pokemon_list = []
for i in range(N):
    pokemon_list.append(input().rstrip())

pokemon = {pokemon: index+1 for index, pokemon in enumerate(pokemon_list)} #O(N)
pokemon_num = {v:k for k,v in pokemon.items()}


for _ in range(M):
    i = input().rstrip()
    if i.isnumeric(): #true
        i = int(i)
        print(pokemon_num[i]) #O(1)
    else:
        print(pokemon[i]) #O(1)