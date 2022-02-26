spawnlayer(spawn, 90)
spawncolumn(spawn, 50)
spawnlayer(spawn, 10)
j, cdf = 0, 120
while cdf>3:
    spawn.append([cdf,1,-1,-1])
    if j%2:
        cdf-=4
    else:
        spawn.append([cdf,1,-1,-1])
        cdf-=5
    j+=1
spawn.sort(key=lambda x:x[0],reverse=True)
