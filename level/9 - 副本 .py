j, cdf = 0, 120
spawnrquick(spawn, 120, 7, r=1)
spawncolumn(spawn, 100, ty=2)
spawnrange(spawn, 80, ty=3)
spawnlayer(spawn, 60, randint(0,1))
spawnlayer(spawn, 60, randint(2,3))
spawncolumn(spawn, 40, ty=3)
spawnrquick(spawn, 20, 11, r=randint(0,LAYER-1))
while cdf>6:
    if j%4==0:
        spawn.append([cdf,3,-1,-1])
    elif j%4==1 or j%4==3:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,2,-1,-1])
    j+=1
    cdf-=3
spawn.sort(key=lambda x:x[0],reverse=True)
