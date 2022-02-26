j, cdf = 0, 118
rlay = randint(0,LAYER-1)
for k in range(3):
    spawn.append([cdf+k, 2, -1, rlay])
while cdf>1:
    if j%4==0 or j%4==1:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,1,-1,-1])
    elif j%4==3:
        spawn.append([cdf,2,-1,-1])
    if randint(0,4)==0:
        spawn.append([cdf,2,-1,-1])
    cdf-=4.1
    j+=1
spawncolumn(spawn, 100, 0)
spawnlayer(spawn, 50, 0)
spawnlayer(spawn, 50, 3)
spawnlayer(spawn, 6, ty=2)
spawn.sort(key=lambda x:x[0],reverse=True)
