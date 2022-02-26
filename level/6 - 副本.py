j, cdf = 0, 120
while cdf>1.5:
    if j%4==0:
        spawn.append([cdf,3,-1,-1])
    elif j%4==1 or j%4==3:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,2,-1,-1])
    rd = randint(0,9)
    if rd==0:
        spawn.append([cdf,3,-1,-1])
    elif rd==1:
        spawn.append([cdf,2,-1,-1])
    elif rd==2 or rd==3:
        spawn.append([cdf,1,-1,-1])
    j+=1
    cdf-=4.1
spawnrange(spawn, 110, ty=3)
spawnrange(spawn, 85)
spawnrange(spawn, 50, ty=2)
spawnlayer(spawn, 30)
spawnrange(spawn, 10)
spawn.sort(key=lambda x:x[0],reverse=True)
