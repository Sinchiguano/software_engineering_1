players=[1,2,3,5,4,3,2,1]


print(players[0])
players.append([7,8,9])
print("##############")
print(players)
print(players[:3])


players[:2]=[0,3]
print(players)

players[:]=[]
print(players)