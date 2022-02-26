j=0
for i in range(120,-1,-3):
    spawn.append([i,1,-1,-1])
    if(j%2):
        spawn.append([i,1,-1,-1])
    j+=1
spawnlayer(spawn, 100)
spawncolumn(spawn, 75)
spawnlayer(spawn, 50)
spawnall(spawn, 3)
spawn.sort(key=lambda x:x[0],reverse=True)
