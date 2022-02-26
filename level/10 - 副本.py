j, ct= 0, 112
spawnrange(spawn, 120, 4, 1, 3)
spawncolumn(spawn, 90, 2, 3)
spawnlayer(spawn, 50, 2)
while ct>15:
    if j%5 == 2 or j%5 == 4:
        spawn.append([ct, 2, -1, -1])
    elif j%5 == 3:
        spawn.append([ct, 3, -1, -1])
    else:
        spawn.append([ct, 1, -1, -1])
    ct -= 2.2
    j += 1
spawnrquick(spawn, 12, 12)
spawn.sort(key=lambda x:x[0],reverse=True)
