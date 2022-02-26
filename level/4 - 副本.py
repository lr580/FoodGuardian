j, cdf = 0, 120
while cdf>1:
    if j%4==0 or j%4==1:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,1,-1,-1])
    elif j%4==3:
        spawn.append([cdf,2,-1,-1])
    if randint(0,7)==0:
        spawn.append([cdf,2,-1,-1])
    cdf-=4
    j+=1
spawncolumn(spawn, 100, 0)
spawncolumn(spawn, 40, ty=2)
spawncolumn(spawn, 70, 0)
spawnrange(spawn, 110)
spawnrange(spawn, 25)
spawn.sort(key=lambda x:x[0],reverse=True)
