j, cdf = 0, 116
rlay = randint(0,LAYER-1)
for i in range(5):
    spawn.append([cdf+i, 2, -1, rlay])
spawncolumn(spawn, 100, 1, 2)
while cdf>90:
    spawn.append([cdf,1,-1,-1])
    spawn.append([cdf,2,-1,-1])
    cdf-=4.6  
while cdf>2:
    if j%4==0:
        spawn.append([cdf,3,-1,-1])
    elif j%4==1 or j%4==3:
        spawn.append([cdf,1,-1,-1])
    elif j%4==2:
        spawn.append([cdf,2,-1,-1])
    if randint(0,7)==0:
        spawn.append([cdf,3,-1,-1])
    j+=1
    cdf-=4.1
spawnlayer(spawn, 45, ty=3)
spawnrange(spawn, 15)
spawn.sort(key=lambda x:x[0],reverse=True)
