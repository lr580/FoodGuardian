j, cdf = 0, 120
while cdf>90:
    spawn.append([cdf,1,-1,-1])
    if j%2:
        cdf-=4
    else:
        spawn.append([cdf,1,-1,-1])
        cdf-=5
    j+=1
spawncolumn(spawn, 70)
spawncolumn(spawn, 12, 2)
while cdf>3:
    if j%4==1 or j%4==0:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,1,-1,-1])
        spawn.append([cdf,1,-1,-1])
    elif j%4==3:
        spawn.append([cdf,2,-1,-1])
    if randint(0,4)==0:
        spawn.append([cdf,2,-1,-1])
    cdf-=4.5
    j+=1
spawn.sort(key=lambda x:x[0],reverse=True)
