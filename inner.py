#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from threading import Thread
from time import sleep
from random import randint
from os import getcwd, path
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from datetime import datetime
from math import log

#--非窗口部分--
#常量定义
TIMELIM = 120
MAXHP = 580
FRAMEV = 0.1
LRV = [0.2, 0.1]
UDV = [0.4, 0.1]
SHUTV = [0.2, 0.1]
SHUTQV = [1, 0.1]
LIGV = [TIMELIM, 0.5, 0.2, 0.5, TIMELIM]
LAYER = 4
WIDTH = 7
LVNUM = 10
PATH = getcwd()
PSW = 'lr581'

#全局变量定义
dhp = stlf = xptr = yptr = stt = cd = sttm = mlv = selelv = selesk = 0
bulbs, spawn, lig, sk, msk, record = [], [], [], [], [], [] #若连等号指针警告
skispeed = ctnspeed = ctnlock = au = infj = infp = motp = motcd = stlogin = 0
wavev = xbf = ybf = -1

#属性常量定义
MCTNSPEED = 25
MCTNLOCK = 20
CURE = 150
SATT = ((35,3),(5,16),(12,6),(40,3),(45,2),(30,3)) #0疾速 1传送 2意念 3广播 4保鲜 5宣传;0CD, 1次数
SKGET = (2,3,5,6,7,8)#通过第几关可以获得该技能

#加载AES加解密模板
def fillu16(tx):
    tx = tx.encode('utf-8')
    return tx + ('\0' * (16 - len(tx) % 16)).encode('utf-8')
def encrypt(text, key=''):
    return b2a_hex(AES.new(fillu16(key), AES.MODE_CBC, b'0000000000000000').encrypt(fillu16(text))).decode('utf-8') if key else text
def decrypt(text, key=''):
    return bytes.decode(AES.new(fillu16(key), AES.MODE_CBC, b'0000000000000000').decrypt(a2b_hex(text.encode('utf-8')))).rstrip('\0') if key else text

#读取加密存档并配置
with open(path.join(PATH, 'saves', 'saves.tx'), encoding='utf-8') as f:
    exec(decrypt(f.read(), PSW))
selelv = mlv+1
sk = msk[:]
if stt==99:#第一次进入游戏
    stt=10
    stlogin=1

#游戏逻辑实现函数定义
def hgci(lt, p):
    psum = [p[0] for i in range(len(p))]
    for i in range(1,len(p)):
        psum[i]=p[i]+psum[i-1]
    pci = randint(0, sum(p)-1)
    for i in range(0, len(psum)):
        if pci<psum[i]:
            return lt[i]

def spawnlayer(x, st, r=-1, ty=1):
    if r==-1:
        r=randint(0,LAYER-1)
    for i in range(WIDTH-1):
        x.append([st, ty, i, r])

def spawncolumn(x, st, c=-1, ty=1):
    if c==-1:
        c=randint(0, WIDTH-2)
    for i in range(LAYER):
        x.append([st, ty, c, i])

def spawnrange(x, st, xi=-1, y=-1, ty=1, r=1):
    if xi==-1:
        xi=randint(1, WIDTH-3)
    if y==-1:
        y=randint(1,LAYER-2)
    for i in range(max(0,y-r),min(LAYER,y+r+1)):
        for j in range(max(0,xi-r),min(WIDTH-1,xi+r+1)):
            x.append([st, ty, j, i])

def spawnall(x, st, ty=1):
    for i in range(LAYER):
        spawnlayer(x, st, i, ty)

def spawnquick(x, st, ctn=5, c=-1, r=-1, ty=1):
    for i in range(ctn):
        spawn.append([st-i, ty, c, r])

def spawnrquick(x, st, ctn=5, c=-1, r=-1, w=[5,2,3]):
    for i in range(ctn):
        spawn.append([st-i, hgci([1,2,3], w), c, r])

def infrate(t):
    return 5-log(t/125+1,2) if t<=1200 else 1.6

def infgen():
    global infj, infp
    spawn.append([stlf+infrate(stlf), hgci([1,2,3], [int(5+infrate(stlf)), 2, 3]), -1, -1])
    infj+=1
    if infj>=3 and randint(0,3)==1:
        infj = 0
        spawn.append([stlf+infrate(stlf), hgci([1,2,3], [5, 2, 3]), -1, -1])
    if 25+2*infrate(stlf)<=infp:
        infp = 0
        rp = hgci(list(range(5)), [5,6,3,6,4])
        if rp==0:
            spawnlayer(spawn, stlf, ty=hgci([1,2,3], [13, 2, 5]))
        elif rp==1:
            spawncolumn(spawn, stlf, ty=hgci([1,2,3], [13, 2, 5]))
        elif rp==2:
            spawnrange(spawn, stlf)
        elif rp==3:
            spawnquick(spawn, stlf)
        elif rp==4:
            spawnrquick(spawn, stlf)
    spawn.sort(key=lambda x:x[0])

def initstt(level='-1', ski=[]):
    global dhp, stlf, xptr, yptr, stt, bulbs, cdlr, cdud, spawn, lig, skispeed, ctnspeed, ctnlock, sk
    global sttm, infj, infp, motp, motcd, xbf, ybf
    dhp = 0
    if selelv<=10:
        stlf = TIMELIM
    else:
        stlf = 0.04
    xptr = WIDTH - 1 #自左边(0)向右边递增
    yptr = 0 #自底层(0)向顶层递增
    stt = 0 #0正常/游戏中 1 CD时间  2 输了 3 赢了, 其他非游戏状态stt见开发日志
    cd = 0 #冷却完毕
    bulbs = [[0 for i in range(WIDTH-1)]+[4] for j in range(LAYER)]#0无剩菜, 1普剩, 2大剩, 3顽剩, 4梯, 5宣传中
    spawn=[]
    with open(path.join(PATH, 'level' , '%s.py'%level)) as f:
        tx = decrypt(f.read(), PSW)
        exec(tx)
    lig = []
    skispeed = 0 #常规移动速度
    ctnspeed = 0 #疾速技能未在使用
    ctnlock = 0 #锁定技能未在使用
    sk = [] #技能栏清空f
    ski = list(map(lambda x:x.ty if isinstance(x, skill) else x, ski))
    for i in range(len(ski)): #初始化技能
        sk.append(skill(SATT[ski[i]][0], ski[i] ,SATT[ski[i]][1], i))
    sttm = 0 #是否是鼠标确认状态
    infj = 0 #无限模式周期变量
    infp = 20 #无尽模式周期变量2
    motp = 0 #动作变量，0正常，1朝左，2朝右，3朝上，5收拾
    motcd = 0 #动作执行变量
    xbf = 5 #坐标记忆变量
    ybf = 0 #坐标记忆变量

def inblock(x,y):
    return x==xptr and y==yptr

def updbfxy():
    global xbf, ybf
    xbf, ybf = xptr, yptr

def det(k):
    global xptr, yptr, cd, wavev, motp, motcd
    if k==97 or k==65 or k=='a' or k=='A':#为了兼容black版本和正式版
        if xptr>0 and cd<=0:
            updbfxy()
            xptr-=1
            cd = LRV[skispeed]
            motp = 1
            motcd = cd
    elif k==100 or k==68 or k=='d' or k=='D':
        if xptr<WIDTH-1 and cd<=0:
            updbfxy()
            xptr+=1
            cd = LRV[skispeed]
            motp = 2
            motcd = cd
    elif k==119 or k==87 or k=='w' or k=='W':
        if yptr<LAYER-1 and xptr == WIDTH - 1 and cd<=0:
            updbfxy()
            yptr+=1
            cd = UDV[skispeed]
            motp = 3
            motcd = cd
    elif k==115 or k==83 or k=='s' or k=='S':
        if yptr>0 and xptr == WIDTH - 1 and cd<=0:
            updbfxy()
            yptr-=1
            cd = UDV[skispeed]
            motp = 3
            motcd = cd
    elif k==101 or k==69 or k=='e' or k=='E':
        if len(sk)>=1:
            sk[0].use()
    elif k==114 or k==82 or k=='r' or k=='R':
        if len(sk)>=2:
            sk[1].use()
    elif k==32 or k==10 or k=='\n':#10是回车,32是空格,'\n'是black传入的
        if cd<=0 and bulbs[yptr][xptr] in (1,2,3):
            updbfxy()
            if bulbs[yptr][xptr] == 3:
                cd = SHUTQV[skispeed]
            else:
                cd = SHUTV[skispeed]
            bulbs[yptr][xptr] = 0
            ligi=xyti(xptr, yptr)
            lig.pop(ligi)
            if not au:
                wavev = 10
            motp = 5
            motcd = cd

class light(object):
    def __init__(self, cd, x, y, ty):
        self.CD = cd #频率
        self.cd = cd #还剩多久耗品质一次
        self.x = x
        self.y = y
        self.ty = ty
    def csm(self):
        global dhp
        self.cd-=FRAMEV
        if self.cd<=0:
            dhp+=1
            self.cd=self.CD
    def __repr__(self):
        return '<cd:%.1f,x:%d,y:%d,ty:%d>'%(self.cd, self.x, self.y, self.ty)

def csmall():
    [i.csm() for i in lig]

def exist(x,y):
    for i in lig:
        if x==i.x and y==i.y:
            return True
    return False

def full(x1=0,x2=WIDTH-2,y1=0,y2=LAYER-1):
    fill=0
    for i in lig:
        if i.x >= x1 and i.x <= x2 and i.y >= y1 and i.y <= y2:
            fill+=1
    return fill>=(x2-x1+1)*(y2-y1+1)

def xyti(x,y):
    for i in range(len(lig)):
        if lig[i].x==x and lig[i].y==y:
            return i
    return None

def ranpos(x=-1, y=-1):
    if x==-1 and y==-1:
        if full():
            return []
        x1,y1=randint(0, WIDTH-2),randint(0, LAYER-1)
        while exist(x1, y1):
            x1,y1=randint(0, WIDTH-2),randint(0, LAYER-1)
    elif y==-1:
        if full(x, x):
            return []
        x1,y1=x,randint(0, LAYER-1)
        while exist(x1,y1):
            y1=randint(0, LAYER-1)
    elif x==-1:
        if full(0, WIDTH-2, y, y):
            return []
        x1,y1=randint(0, WIDTH-2),y
        while exist(x1,y1):
            x1=randint(0, WIDTH-2)
    else:
        if exist(x,y):
            return []
        x1,y1=x,y
    return [x1,y1]

def summon():
    if selelv==11 and len(spawn)==0:#无尽模式
        infgen()
    i=0
    while i<len(spawn) and ((stlf<=spawn[i][0] and selelv<=10) or (selelv==11 and stlf>=spawn[i][0])):
        xy = ranpos(spawn[i][2],spawn[i][3])
        if xy: #可以生成
            lig.append(light(LIGV[spawn[i][1]], xy[0], xy[1], spawn[i][1]))
            bulbs[xy[1]][xy[0]] = spawn[i][1]
        i+=1
    for j in range(i):
        spawn.pop(0)
    
class skill(object):
    def __init__(self, cd, ty, lf, pos):
        self.CD = cd #频率
        self.cd = 0 #距离下次可用时间
        self.ty = ty #技能类别：0疾速 1传送 2意念 3广播 4保鲜 5宣传
        self.lf = lf #还能用多少次
        self.pos = pos #0是按E使用，1按R使用
    def use(self):
        global sttm
        if self.cd > 0:
            return False
        if self.lf <= 0:
            return False
        if self.ty == 4 and selelv == 11:
            return False
        if self.ty in (1,5):#需要鼠标确认位置的技能
            sttm = self.ty #进入鼠标确认环节
            #useskill(self.ty) #非窗口化调试阶段使用这个
        else:
            useskill(self.ty)
            self.csm()
        return True
    def csm(self):
        self.cd = self.CD
        if selelv<=10:#非无尽模式
            self.lf -= 1
    def loop(self):
        self.cd=max(0, self.cd-FRAMEV)
    def __repr__(self):
        return '<CD:%d, cd:%.1f, ty:%d, lf:%d, pos:%d>'%(self.CD, self.cd, self.ty, self.lf, self.pos)

def useskill(ty, ax=0, ay=0):
    global wavev, lig
    if ty==0:#疾速
        global skispeed, ctnspeed
        skispeed = 1
        ctnspeed = MCTNSPEED
    elif ty==1:#传送
        global xptr, yptr
        xptr, yptr = ax, ay
        updbfxy()
        for i in range(len(sk)): #消耗特判
            if sk[i].ty==1:
                sk[i].csm()
    elif ty==2:#意念
        for i in range(max(0,xptr-1),min(WIDTH-1,xptr+2)):
            for j in range(max(0,yptr-1), min(LAYER, yptr+2)):
                ligi = xyti(i,j)
                if ligi==None or ligi!=None and lig[ligi].ty!=5:
                    bulbs[j][i]=0
                if ligi!=None and lig[ligi].ty!=5:
                    lig.pop(ligi)
    elif ty==3:#广播
        lig = list(filter(lambda i:i.ty==5, lig))
        if len(lig)>0:
            lock = lig[0].y
        else:
            lock = -1
        for i in range(0, WIDTH-1):
            for j in range(0, LAYER):
                if lock>=0 and j==lock:
                    continue
                bulbs[j][i]=0
    elif ty==4:#保鲜
        global dhp
        dhp=max(dhp-CURE,0)
    elif ty==5:#宣传
        global ctnlock
        ctnlock = MCTNLOCK
        for i in range(0, WIDTH-1):
            ligi = xyti(i, ay)
            if ligi != None:
                lig.pop(ligi)
            lig.append(light(TIMELIM, i, ay, 5))
            bulbs[ay][i] = 5
        for i in range(len(sk)):#消耗特判
            if sk[i].ty==5:
                sk[i].csm()
    if not au:
        wavev = ty

def unspeed():
    global skispeed, ctnspeed
    skispeed = 0
    ctnspeed = 0

def unlock():
    dels, ay, rabs = [], -1, 0
    for i in range(len(lig)):
        if lig[i].ty == 5:
            dels.append(i)
            ay = lig[i].y
    for i in dels:
        lig.pop(i-rabs)
        rabs+=1
    for i in range(0, WIDTH-1):
        bulbs[ay][i] = 0

def pathpower(xp,yp,x,y,ty):#ty:1普2大3顽,AB间耗品质数
    p=0
    if y==yptr:
        p+=abs(xp-x)*LRV[0]
    else:
        p+=abs(WIDTH-1-xp)+abs(WIDTH-1-x)*LRV[0]+abs(y-yp)*UDV[0]
    p*=1/LIGV[ty]
    return p

def pathpow(xp,yp):#某点到所有灯的耗品质数
    return sum([pathpower(xp,yp,i.x,i.y,i.ty) for i in lig])

def minppow():#生成所有点的pathpow列表
    mz=[]
    for i in range(0,LAYER):
        mz.append([])
        for j in range(0,WIDTH-1):
            mz[-1].append(pathpow(j,i))
    return mz

def loopC():
    global stlf, stt, cd, ctnspeed, ctnlock, infp, dhp
    csmall()
    summon()
    stt=0
    if selelv<=10:
        stlf-=FRAMEV
    else:
        stlf+=FRAMEV
    cd=cd-FRAMEV if cd>=0 else 0
    if selelv==11:
        infp+=FRAMEV
        dhp = max(0, dhp-FRAMEV)
    if ctnspeed>0:
        ctnspeed=max(0,ctnspeed-FRAMEV)
        if ctnspeed<=0:
            unspeed()
    if ctnlock>0:
        ctnlock=max(0,ctnlock-FRAMEV)
        if ctnlock<=0:
            unlock()
    for i in sk:
        i.loop()

def ctnC():
    global stt
    if stt>=11:
        return False
    if stlf>=0:
        if dhp>MAXHP:
            stt=3
            return False
        return True
    else:
        stt = 2
        return False
    
def timeio(dn = datetime.now()):
    return [dn.year, dn.month, dn.day, dn.hour, dn.minute, dn.second]

def weight(bg, so, d, tot):
    return round(((tot-d)*bg+d*so)/max(1,tot))

def dbhg(pos, poso, d, tot):
    return [weight(pos[0], poso[0], d, tot), weight(pos[1], poso[1], d, tot)]

def initsaves():
    with open(path.join(PATH, 'saves', 'saves.tx'), 'w', encoding='utf-8') as f:
        f.write(encrypt('stt=99\nmlv=0\nmsk=[]\nrecord=[]', PSW))
