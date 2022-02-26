j=0
for i in range(120,-1,-3):
    spawn.append([i,1,-1,-1])
    if j%5==2 or j%5==4:
        spawn.append([i,2,-1,-1])
    elif j%5==3:
        spawn.append([i,3,-1,-1])
    j+=1
spawnlayer(spawn, 90)
spawncolumn(spawn, 3.5, ty=2)
spawncolumn(spawn, 45)
spawn.sort(key=lambda x:x[0],reverse=True)
