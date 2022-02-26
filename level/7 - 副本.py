j, cdf = 0, 120
spawnlayer(spawn, 120)
spawnrange(spawn, 100)
spawncolumn(spawn, 80, ty=3)
spawncolumn(spawn, 60)
spawncolumn(spawn, 40, ty=2)
spawncolumn(spawn, 20, ty=3)
spawn.append([4, 2, -1, -1])
while cdf>6:
    if j%4==0:
        spawn.append([cdf,3,-1,-1])
    elif j%4==1 or j%4==3:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,2,-1,-1])
    if randint(0,10)==1:
        spawnquick(spawn, cdf)
    j+=1
    cdf-=4.1
spawn.sort(key=lambda x:x[0],reverse=True)
