with open('inner.py', encoding='utf-8') as f:
    exec(f.read())
#--窗口部分--
import pygame
from pygame.locals import *
from os import system

pygame.init()
#窗口属性常量
SWID = 1400
SHEI = 800
PATHC = path.join(PATH,'pic')
BG = pygame.image.load(path.join(PATHC, 'bg.png'))
ICO = pygame.image.load(path.join(PATHC, 'icon.png')) #图标实际上无法透明图层渲染
BULP = [[pygame.image.load(path.join(PATHC, 'bulb%d%d.png'%(i,j))) for i in range(6)] for j in range(3)]
PTUF = pygame.image.load(path.join(PATHC, 'ptuf.png'))
PTDF = pygame.image.load(path.join(PATHC, 'ptdf.png'))
PTLF = pygame.image.load(path.join(PATHC, 'ptlf.png'))
PTRF = pygame.image.load(path.join(PATHC, 'ptrf.png'))
PTRO = pygame.image.load(path.join(PATHC, 'ptro.png'))
BGB = pygame.image.load(path.join(PATHC, 'bgb.png'))
LOGO = pygame.image.load(path.join(PATHC, 'logo.png'))
BGB.set_alpha(255) #0完全透明,255完全不透明
AU = [pygame.image.load(path.join(PATHC, 'auon.png')),pygame.image.load(path.join(PATHC, 'auoff.png'))]
MU = [pygame.image.load(path.join(PATHC, 'muon.png')),pygame.image.load(path.join(PATHC, 'muoff.png'))]
BUTBGX, BUTBGY, BUTCTX, BUTCTY, BUTJMX, BUTJMY = 50, 140, 300, 50, 300, 30
BUTT = [[BUTBGX, BUTBGY+i*(BUTCTY+BUTJMY),
         BUTBGX+BUTCTX, BUTBGY+BUTCTY+i*(BUTCTY+BUTJMY)] for i in range(8)]
HPX, HPY = 25, 30
STX, STY = 25, 90
SUX, SUY = 25, 150
IOSX, IOSY = 25, 200
WLX, WLY = 25, 550
SKIXY = [[425, 30], [425, 90]]
EWID, EHEI, BBLDX, BBLDY = 125, -125, 450, 715
BLD = [[[BBLDX+j*EWID, BBLDY+(i+1)*EHEI,
    BBLDX+(j+1)*EWID, BBLDY+i*EHEI] for j in range(WIDTH)] for i in range(LAYER)]
PTRX, PTRY, PRTW, PTRH = 515, 640, 50, 80
PTR = [[[PTRX+j*EWID, PTRY+i*EHEI,
    PTRX+(j+1)*EWID, PTRY+(i-1)*EHEI] for j in range(WIDTH)] for i in range(LAYER)]
BGMBX, BGMBY, BGMBW, BGMBD = 1320, 30, 1370, 80
SNDBX, SNDBY, SNDBW, SNDBD = 1320, 100, 1370, 150
LOGOX, LOGOY, LOGOW, LOGOD = 70, 170, 350, 350
CPS = {'dgold':[218,165,32], 'choco':[255,255,255], 'dred':[250,128,114], 'nred':[255,255,0],
       'board':[205,133,63]}
DFONT = 'SimHei' #win10/7均可用 微软雅黑
PATHB = path.join(PATH, 'sound')
BMENU = path.join(PATHB,'menu.ogg')
BPT = [path.join(PATHB,'easy.ogg'), path.join(PATHB,'hard.ogg'), path.join(PATHB,'infinity.ogg')]
BSK = [path.join(PATHB,'ski1.wav'), path.join(PATHB,'ski2.wav'), path.join(PATHB,'ski3.wav'),
       path.join(PATHB,'ski4.wav'), path.join(PATHB,'ski5.wav'), path.join(PATHB,'ski6.wav')]
BRO = [[path.join(PATHB, 'hit1.wav'), path.join(PATHB, 'hit2.wav'), path.join(PATHB, 'hit3.wav')],
       [path.join(PATHB, 'swf1.wav'), path.join(PATHB, 'swf2.wav'), path.join(PATHB, 'swf3.wav')]]
SKWAV = [BSK[0], BSK[1], BSK[2], BSK[3], BSK[4], BSK[5]] #声音对应表
pygame.mixer.music.set_volume(0.8)
pygame.mixer.music.load(BMENU)
pygame.mixer.music.play(-1)
FRN = 50 #帧率
FRM = 1/FRN
LR = 580

#文本常量
TITLE = '餐馆守卫者 Food Guardian'
CNNUM='零一二三四五六七八九十'
SKN = ['疾速', '传送', '意念', '广播', '保鲜', '宣传']
SKDSB = ['你可以爆发潜能，在一段时间内移动和收拾剩菜速度大幅增加。\n在接下来的20秒内，所有移动和收拾只需要0.1秒即可。',
         '你作为栋梁之材，习有混元形意太极，可以在楼内瞬间传送至某一位置。\n按下按键释放技能后，用鼠标点击要传送到的位置即可发动技能。',
         '你强烈的保卫粮食意愿通过量子波动，使得你所在格及其周围八格所有剩菜都被自动收拾。',
         '你播放餐馆广播，以非正式学时和评优为奖励，呼吁所有在场顾客参与志愿收拾，一瞬间将场上所有剩菜收拾干净。',
         '你对剩菜使用保鲜剂耗子尾汁，使得品质大幅增加。\n每次发动技能恢复150点被损耗的品质，恢复后的可损耗品质不大于580。\n该技能无尽模式无法使用！',
         '你在某一层楼拉起横幅，呼吁顾客珍惜粮食。在这期间该层的顾客不会留下剩菜，并且主动收拾已有剩菜。\n按下按键释放技能后，用鼠标点击要宣传的楼层即可发动技能。宣传瞬间会自动收拾该层已有剩菜，并且宣传的楼层在20秒内不会有新的剩菜。']
TXBG = '据联合国报道，全球超过8.2亿人仍在挨饿！有关专家估算，我国每年在餐桌上浪费的食物约合2000亿元，相当于2亿多人一年的口粮。这鲜明的对比着实触目惊心！\n对此，作为南海校区某餐馆打工人的你想要用自己的行动减少餐馆的剩饭浪费。已知一种新技术可以加工剩饭菜，而食物越新鲜，效果越好。因此你想要以最快速度收拾顾客的剩菜。\n(按下左下角文字按钮以继续)'
TXRUL = '每个房间的餐桌都可能产生剩菜，剩菜放得越久，新鲜度越低，从而影响加工品质。你的任务是让总品质损耗尽可能降低。\n如果是无尽模式，则你的任务是尽可能坚持足够久，尽量晚使损耗品质达到最大可损耗品质。'
TXRO = '使用WSAD进行移动。每次左右移动后你需要休息0.2秒，无法活动；每次上下移动需要0.5秒。只能在楼梯口上下移动。每次收拾普通餐或大餐需要0.2秒，收拾顽固餐需要1秒。\n通过第二关后，将解锁技能，使用按键E或R释放技能。最多可以选择两个技能。技能详情在技能选择处查看。'
EGG = ['彩蛋1:[成就]千钧一发:你的损耗品质值恰好为最大可损耗值！',
        '彩蛋2:[成就]粮食守卫:恭喜你在无尽模式坚持了580秒以上！算下来每秒只损耗1单位品质以下呢！你一定选了技能%s吧！'%SKN[4],
        '彩蛋3:58这个数字有什么特别的含义么=w=',
        '彩蛋4th哟，斯巴拉西斯巴拉西~ -lr580卿']
STFIN = ['恭喜过关，下一关会出现新的剩菜：大餐，其损耗品质功率为普通餐的2.5倍，请注意！',
         '恭喜过关，解锁技能：%s，可前往查看！'%SKN[0],
         '恭喜过关，解锁技能：%s，可前往查看！'%SKN[1],
         '恭喜过关，下一关会出现新的剩菜：顽固餐，这种剩菜很难处理，需要消耗1秒的时间，请注意！',
         '恭喜过关，解锁技能：%s，可前往查看！'%SKN[2],
         '恭喜过关，解锁技能：%s，可前往查看！'%SKN[3],
         '恭喜过关，解锁技能：%s，可前往查看！'%SKN[4],
         '恭喜过关，解锁技能：%s，可前往查看！'%SKN[5],
         '恭喜过关，下一关是最后一关常规关卡，加油！',
         '恭喜通关，已解锁无尽模式，可前往挑战！(该模式会自动恢复品质,技能无限使用,但%s不可用)'%SKN[4]]
STBUT = ['下一关','选择技能','选择技能','下一关','选择技能',
         '选择技能','选择技能','选择技能','下一关','前往挑战']
TIPS = ['操作技巧：在需要左右移动比较短距离的时候，连按按键比按住不放更容易控制距离，以防止走过头了。',
        '游戏技巧：没有剩菜时，站在二层或三层楼梯口能够以最快速度应变新产生的剩菜。',
        '游戏技巧：不要吝啬使用技能，正常情况下技能的次数都是足够使用的，尤其是传送技能。',
        '游戏技巧：如果某些关卡很难通过，尝试更换技能搭配，也许能轻而易举地过关。',
        '粮食知识：剩饭剩菜可以转化为肥料、饲料，使用一些生物学新技术可以让转化率高达80%！']

#窗口变量
mu = au = 0 #默认背景音乐和游戏音效打开
sttlv = 0 #关卡介绍显示变量
sttsk = -1 #技能介绍显示变量,由于有0号技能，初始化为-1
wind = 0 #为1时游戏胜利触发胜利处理函数
running = 1 #运行常量
motn = 0 #移动中第几帧
mott = 0 #移动中总帧
stnwsk = 0 #第一次获得技能
tino = -1 #TIPS下标变量
ptilvio = 0#正在展示关卡记录

#窗口辅助函数
def pt(tx, x, y, ft, color=(0,0,0)): #输出单行文字
    screen.blit(ft.render(tx, True, color), (x,y))
def truelen(tx, size): #返回真实长度(单位:像素)
    return sum(map(lambda x:size if ord(x)>128 else size/2, tx))
def cfbg(tx, sq, size): #返回字体在矩形里居中显示的开始坐标(左上角)
    return [(sq[0]+sq[2]-truelen(tx, size))/2, (sq[1]+sq[3]-size)/2]
def ptcf(tx, sq, ft, ftq, color=(0,0,0)): #在矩形中心输出文字
    pt(tx, *cfbg(tx, sq, ftq), ft, color)
def pts(tx, x, y, wid, size, ft, color=(0,0,0)): #输出多行文字
    dhei,lf=0,0
    for rf in range(len(tx)):
        if truelen(tx[lf:rf], size) >= wid or tx[rf]=='\n':
            pt(tx[lf:rf].strip('\n'), x, y+dhei, ft, color)
            dhei+=size
            lf=rf
    if lf<rf+1:
        pt(tx[lf:].strip('\n'), x, y+dhei, ft, color)
def inrec(x1, y1, x2, y2, m): #假设所有矩形x1,y1分别<=x2,y2
    return m[0]>=x1 and m[0]<=x2 and m[1]>=y1 and m[1]<=y2

#窗口函数
def playm(k):#备用动画函数判断模板
    global xptr, yptr, cd
    if k==97 or k==65 or k=='a' or k=='A':
        if xptr>0 and cd<=0:
            pass
    elif k==100 or k==68 or k=='d' or k=='D':
        if xptr<WIDTH-1 and cd<=0:
            pass
    elif k==119 or k==87 or k=='w' or k=='W':
        if yptr<LAYER-1 and xptr == WIDTH - 1 and cd<=0:
            pass
    elif k==115 or k==83 or k=='s' or k=='S':
        if yptr>0 and xptr == WIDTH - 1 and cd<=0:
            pass
    elif k==101 or k==69 or k=='e' or k=='E':
        if len(sk)>=1:
            pass
    elif k==114 or k==82 or k=='r' or k=='R':
        if len(sk)>=2:
            pass
    elif k==32 or k==10 or k=='\n':
        pass

def skiopt(i):
    if selelv==11 and sk[i].ty==4:
        t='%s,该技能无尽模式不可用。'%SKN[sk[i].ty]
    else:
        t='%s,冷却时间:%.1fs'%(SKN[sk[i].ty], sk[i].cd)
    if selelv!=11:
        t+='剩余次数:%d'%sk[i].lf
    
    if sk[i].ty==0 and skispeed:
        t+=',失效倒计时:%.1fs'%ctnspeed
    if sk[i].ty==5 and ctnlock:
        t+=',失效倒计时:%.1fs'%ctnlock
    return t

def golvnam():
    return '第%s关'%CNNUM[selelv] if selelv <= 10 else '无尽模式'

def gomlv():
    return '第%s关'%CNNUM[mlv+1] if mlv+1 <= 10 else '已通关'

def stdsc():
    return '剩余' if selelv<=10 else '已坚持'

def stfinio():
    global stnwsk
    pts(STFIN[mlv-1], WLX, WLY-300, 320, 40, FONT2, CPS['dred'])
    ptcf(STBUT[mlv-1], BUTT[6], FONT, 50, CPS['choco'])
    if mlv in SKGET:
        stnwsk = 1

def drawA():
    pt('所选关卡:%s'%golvnam(), SUX, SUY, FONT2, CPS['choco'])
    pt('已损耗品质:%d/%d'%(dhp, MAXHP), HPX, HPY, FONT2, CPS['choco'])
    if selelv<=10:
        pt('%s时间:%.1f/%d'%(stdsc(), max(0,stlf), TIMELIM), STX, STY, FONT2, CPS['choco'])
    else:
        pt('%s时间:%.1f'%(stdsc(), max(0,stlf)), STX, STY, FONT2, CPS['choco'])
    if len(sk)>=1:
        pt('技能[E]%s'%skiopt(0), SKIXY[0][0], SKIXY[0][1], FONT3, CPS['choco'])
    if len(sk)>=2:
        pt('技能[R]%s'%skiopt(1), SKIXY[1][0], SKIXY[1][1], FONT3, CPS['choco'])
    if stt==2:
        pt('你赢了！！', WLX, WLY, FONT, CPS['nred'])
        if dhp==LR:
            pts(EGG[0], WLX, WLY-300, 320, 40, FONT2, CPS['dred'])
        if mlv+1==selelv:#首次通关
            stfinio()
    elif stt==3:
        if selelv<=10:
            pt('你输了！！', WLX, WLY, FONT, CPS['nred'])
        else:
            if stlf>=LR:
                pts(EGG[1], WLX, WLY-300, 360, 40, FONT2, CPS['dred'])
            pt('游戏结束！', WLX, WLY, FONT, CPS['nred'])
    ptcf('返回菜单', BUTT[-1], FONT, 50, CPS['choco'])
    if sttm == 1:
        pt('请点击要传送到的区域。', IOSX, IOSY, FONT2, CPS['choco'])
    elif sttm == 5:
        pt('请点击要宣传的楼层。', IOSX, IOSY, FONT2, CPS['choco'])
    for i in range(LAYER):
        for j in range(WIDTH):
            screen.blit(BULP[j//2 if j<=5 else 0][bulbs[i][j]].convert(), (BLD[i][j][0],BLD[i][j][1]))

def nwzlvio(i):#i是按钮序号
    global ptilvio
    if i<5 and 1+i+(stt-30)*5==selelv:
        ptilvio=1
    else:
        ptilvio=0

def jselelv(t):#t是第t关；t为11选无限
    global selelv, ptilvio, sttlv
    ret = True
    if ptilvio == 1:
        if sttlv == selelv:
            ptilvio = 0
            sttlv = 0
            startA(str(selelv), sk)
            ret = False #防止再倒回去触发ptilvio
    if t<=mlv+1:
        selelv=t
    return ret

def showrsk(t):#这次t就是下标了
    if len(record[t][1])==0:
        return '无'
    elif len(record[t][1])==1:
        return SKN[record[t][1][0]]
    else:
        return '%s,%s'%(SKN[record[t][1][0]],SKN[record[t][1][1]])

def showlv(t):
    if t<mlv+1:#已通过
        if len(record)<t:#因为SK改了所以这里也有待修改，下标！
            pts(EGG[3], BLD[3][0][0],BLD[3][0][1], EWID*WIDTH-40, 40, FONT2, CPS['dred'])
            return
        pt('已通关，最佳纪录创造时间:%d/%d/%d %d:%d:%d'%(record[t-1][2][0],
            record[t-1][2][1],record[t-1][2][2],record[t-1][2][3],record[t-1][2][4],record[t-1][2][5])
           ,BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])
        pt('损耗品质:%d'%record[t-1][0],
           BLD[3][0][0],BLD[3][0][1]+40, FONT2, CPS['board'])
        pt('所用技能:%s'%showrsk(t-1),
           BLD[3][0][0],BLD[3][0][1]+80, FONT2, CPS['board'])
        if record[t-1][0]==LR:
            pts(EGG[0], BLD[3][0][0],BLD[3][0][1]+120, EWID*WIDTH-40, 40, FONT2, CPS['dred'])
        if record[t-1][-1][-2]==LR//10:
            pts(EGG[2], BLD[3][0][0],BLD[3][0][1]+240, EWID*WIDTH-40, 40, FONT2, CPS['dred'])
    elif t==mlv+1 and mlv!=10:
        pt('未通关', BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])
    elif t==11:#无尽模式
        if len(record)==11:#挑战过无限模式
            pt('最佳纪录创造时间:%d/%d/%d %d:%d:%d'%(record[t-1][2][0],
            record[t-1][2][1],record[t-1][2][2],record[t-1][2][3],record[t-1][2][4],record[t-1][2][5])
           ,BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])
            pt('坚持时长:%.1fs'%record[t-1][0],
           BLD[3][0][0],BLD[3][0][1]+40, FONT2, CPS['board'])
            pt('所用技能:%s'%showrsk(t-1),
           BLD[3][0][0],BLD[3][0][1]+80, FONT2, CPS['board'])
            if record[t-1][0]>=LR:
                pts(EGG[1], BLD[3][0][0],BLD[3][0][1]+120, EWID*WIDTH-40, 40, FONT2, CPS['dred'])
            if record[t-1][-1][-2]==LR//10:
                pts(EGG[2], BLD[3][0][0],BLD[3][0][1]+240, EWID*WIDTH-40, 40, FONT2, CPS['dred'])
        elif mlv!=10:#未解锁
            pt('通过第十关后解锁', BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])
        else:
            pt('未挑战', BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])
    else:
        pt('通过第%s关后解锁'%CNNUM[t-1], BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])

def jselesk(t):#t是技能序号
    global selesk
    if SKGET[t]<=mlv:
        selesk = t

def showskn(t):
    if SKGET[t]<=mlv:
        return SKN[t]
    else:
        return '第%s关解锁'%CNNUM[SKGET[t]+1]

def showsk(t):
    if SKGET[t]<=mlv:
        pt(SKN[t], BLD[3][0][0],BLD[3][0][1], FONT2, CPS['board'])
        pt('按下E或R选择技能按键(若选两个,必须先选E)', BLD[3][0][0],BLD[3][0][1]+40, FONT2, CPS['board'])
        if t==0:
            ndline = '冷却时间：%ds'%(SATT[t][0]-MCTNSPEED)
            ndline+=', 持续时间:%ds'%MCTNSPEED
        elif t==5:
            ndline = '冷却时间：%ds'%(SATT[t][0]-MCTNLOCK)
            ndline+=', 持续时间:%ds'%MCTNLOCK
        else:
            ndline = '冷却时间：%ds'%SATT[t][0]
        pt(ndline,BLD[3][0][0],BLD[3][0][1]+80, FONT2, CPS['board'])
        pt('可用次数：%d次'%SATT[t][1],BLD[3][0][0],BLD[3][0][1]+120, FONT2, CPS['board'])
        pts('描述:%s'%SKDSB[t], BLD[3][0][0],BLD[3][0][1]+160, EWID*WIDTH-40, 40, FONT2, CPS['board'])
    else:
        pt('第%s关解锁。'%CNNUM[SKGET[t]+1], BLD[3][0][0], BLD[3][0][1]+160, FONT2, CPS['board'])

def bindsk(k):
    if sttsk<0:#未选中技能
        return
    if SKGET[sttsk]>mlv:#无资格选择
        return
    if k==101:#按下按键e
        if not sk:#正常选择
            sk.append(sttsk)
        else:
            if len(sk)==2 and sk[1] == sttsk:#交换选择
                sk[1], sk[0] = sk[0], sk[1]
            elif len(sk)==1 and sk[0] == sttsk:#单技能时解除重复选择
                sk.pop(0)
            elif len(sk)==2 and sk[0] == sttsk:#双技能时解除重复选择
                sk[0] = sk[1]
                sk.pop(1)
            else:#正常选择
                sk[0] = sttsk
    elif k==114 and len(sk)>=1:#按下按键r
        if len(sk)==1:
            if sk[0]==sttsk:#重复选择
                return
            sk.append(sttsk)#正常选择
        else:
            if sk[1]==sttsk:#解除选择
                sk.pop(1)
            elif sk[0]==sttsk:#交换选择
                sk[1], sk[0] = sk[0], sk[1]
            else:#正常选择
                sk[1] = sttsk

def skpttn():
    global sk, sttsk
    if len(sk) and isinstance(sk[0], skill):
        sk = list(map(lambda x:x.ty, sk))#技能栏特判恢复
    sttsk = -1

def nwrec():
    msk = list(map(lambda x:x.ty if isinstance(x, skill) else x, sk))
    if selelv==11:#无尽模式
        return [round(stlf,1), msk, timeio()]
    else:
        return [dhp, msk, timeio()]

def nwzrec():
    if len(record)<selelv:#第一次通过
        record.append(nwrec())
    elif selelv==11 and stlf>record[-1][0] or selelv<=10 and dhp<record[selelv-1][0]:
        record[selelv-1] = nwrec()

def saveF():
    global msk
    msk = list(map(lambda x:x.ty if isinstance(x, skill) else x, sk))
    tx = 'stt=11\nmlv=%d\nmsk=%s\nrecord=%s'%(mlv,str(msk),str(record))
    with open(path.join(PATH, 'saves', 'saves.tx'), 'w', encoding='utf-8') as f:
        f.write(encrypt(tx,PSW))
        
def windeal():
    global wind, mlv, msk, selelv
    if stt<2 or stt>3 or wind==0:
        return
    if stt==2 or selelv==11:
        nwzrec()
    if selelv==mlv+1 and stt==2:
        selelv+=1
        mlv = min(10, mlv+1)
    saveF()
    wind=0#处理完毕

def drawP():
    global motcd, motp
    if mott==0:#未在移动
        screen.blit(PTUF ,PTR[yptr][xptr])
        motp = 0
    else:#正在移动
        ddy=0
        if motp==0:
            ptp = PTUF
        elif motp==1:
            ptp = PTLF
        elif motp==2:
            ptp = PTRF
        elif motp==3:
            ptp = PTDF
        elif motp==5:
            if (motn%(FRN//5))<5:
                ptp = PTUF
            else:
                ptp = PTRO
                ddy=10
        screen.blit(ptp, dbhg(PTR[ybf][xbf], (PTR[yptr][xptr][0],PTR[yptr][xptr][1]-ddy), motn, mott))

def loopA():
    while ctnC() and running:
        loopC()
        sleep(FRAMEV)

def redmotcd():
    global motcd, motn, mott, motp
    if stt>=10:
        return
    if motcd!=0:#初始化移动条件
        mott = motcd * FRN
        motn = 1
        motcd = 0
    elif motn!=mott:#移动一格
        motn+=1
    elif motn==mott: #移动完毕
        motn = 0
        mott = 0
        motp = 0

def loopmot():
    while running:
        redmotcd()
        sleep(FRM)

def startA(level='0',skii=[]):
    global wind, stnwsk
    initstt(level, ski=skii)
    Thread(target=loopA).start()
    pygame.mixer.music.load(BPT[(selelv-1)//5])
    if not mu:
        pygame.mixer.music.play(-1)
    wind = 1
    stnwsk = 0

def playwave():
    global wavev
    if wavev==10:
        pygame.mixer.Sound(BRO[skispeed][randint(0,2)]).play()
    elif wavev <= 5 and wavev >=0:
        pygame.mixer.Sound(SKWAV[wavev]).play()
    wavev = -1

def clickswitch(event):
    global stt, ax, ay, sttm, au, mu, sttlv, sttsk, stnwsk, tino, ptilvio
    mousecfm = 0 #已经找到区域，则停止继续检索
    for i in range(len(BUTT)):
        if inrec(*BUTT[i], event.pos):
            mousecfm = 1
            if stt==11:
                if i==7:
                    pygame.quit()
                elif i==3:#开始游戏
                    startA(str(selelv), skii=sk)
                elif i==4:#关卡设置
                    stt=13
                elif i==5:#游戏帮助
                    stt=14
                elif i==6:#游戏背景
                    stt=10
            elif stt<=3:
                if i==7:
                    stt=11
                    skpttn()
                    pygame.mixer.music.load(BMENU)
                    if not mu:
                        pygame.mixer.music.play(-1)
                if mlv+1==selelv and i==6:
                    skpttn()
                    if mlv in SKGET:
                        stt=40
                    else:
                        startA(str(mlv+1), skii=sk)
            elif stt==13:
                if i==3:#关卡选择
                    stt=30
                elif i==4:#技能选择
                    stt=40
                elif i==5:#返回
                    stt=11
            elif stt==30:#关卡选择第一页
                if i>=0 and i<=4:#一到五关
                    sttlv=i+1
                    if jselelv(i+1):
                        ptilvio = 1
                elif i==5:#下一页
                    stt=31
                    if sttlv!=11:#无尽选中时翻页不撤销显示
                        sttlv=0
                elif i==6:#无尽模式
                    sttlv=11
                    if jselelv(11):
                        ptilvio = 1
                elif i==7:#返回
                    ptilvio = 0
                    stt=13
                    sttlv=0
            elif stt==31:#关卡选择第二页
                if i>=0 and i<=4:#六到十关
                    sttlv=i+6
                    if jselelv(i+6):
                        ptilvio = 1
                elif i==5:#上一页
                    stt=30
                    if sttlv!=11:
                        sttlv=0
                elif i==6:#无尽模式
                    sttlv=11
                    if jselelv(11):
                        ptilvio = 1
                elif i==7:#返回
                    ptilvio = 0
                    stt=13
                    sttlv=-1
            elif stt==40:#技能选择
                if i>=0 and i<=5:#选择技能
                    sttsk=i
                elif i==6:#返回
                    stt=11
                    sttsk=-1
                if i==7:
                    startA(str(selelv), skii=sk)
            elif stt==14 or (stt>=21 and stt<=29):#游戏帮助，游戏规则，操作指南, TIPS
                if i==3:#游戏规则
                    stt=21
                elif i==4:#操作指南
                    stt=22
                elif i==5:#TIPS
                    stt=23
                    if tino+1==len(TIPS):
                        tino = 0
                    else:
                        tino += 1
                elif i==6:
                    if stlogin:
                        startA(str(selelv), skii=sk)
                    else:
                        stt=11
            elif stt==10:#游戏背景
                if i==7:
                    if stlogin:
                        stt=21
                    else:
                        stt=11
            elif stt==23:#TIPS
                if i==7:
                    stt==11
            break
    for i in range(LAYER):
        if mousecfm and not sttm: #or stt>=10:
            break
        for j in range(WIDTH):
            if inrec(*BLD[i][j], event.pos):
                ax, ay = j, i
                if sttm==0:
                    break
                useskill(sttm, j, i)
                sttm = 0
                mousecfm = 1
                break
    if inrec(BGMBX, BGMBY, BGMBW, BGMBD, event.pos):
        if mu:
            if pygame.mixer.music.get_busy():
                pygame.mixer.music.unpause()
            else:
                pygame.mixer.music.play(-1)
        else:
            pygame.mixer.music.pause()
        mu = not mu
        mousecfm = 1
    elif inrec(SNDBX, SNDBY, SNDBW, SNDBD, event.pos):
        au = not au
        mousecfm = 1
    return mousecfm

def sttdraw():
    if stt>=11:
        pt('所选关卡:%s'%golvnam(), STX, STY, FONT2, CPS['choco'])
        pt('最新关卡:%s'%gomlv(), HPX, HPY, FONT2, CPS['choco'])
        if len(sk)>=1:
            pt('技能[E]%s'%SKN[sk[0]], SKIXY[0][0], SKIXY[0][1], FONT2, CPS['choco'])
        if len(sk)>=2:
            pt('技能[R]%s'%SKN[sk[1]], SKIXY[1][0], SKIXY[1][1], FONT2, CPS['choco'])
    if stt==11: #常规进入界面
        for i, j in zip(range(3,8), ('开始游戏', '关卡设置',
                        '游戏帮助', '游戏背景', '退出')):
            ptcf(j, BUTT[i], FONT, 50, CPS['choco'])
        screen.blit(LOGO.convert_alpha(), (LOGOX, LOGOY))
    elif stt==13: #关卡设置
        screen.blit(LOGO.convert_alpha(), (LOGOX, LOGOY))
        for i,j in zip(range(3,6),('关卡选择', '技能选择', '返回')):
            ptcf(j, BUTT[i], FONT, 50, CPS['choco'])
    elif stt==30:#关卡选择第一页
        for i,j in zip(range(8), ('第一关', '第二关', '第三关', '第四关', '第五关',
                                  '下一页', '无尽模式', '返回')):
            if ptilvio == 1 and (i+1==sttlv or i==6 and sttlv==11):
                ptcf('开始游戏', BUTT[i], FONT, 50, CPS['choco'])
            else:
                ptcf(j, BUTT[i], FONT, 50, CPS['choco'])
            #print(ptilvio)
    elif stt==31:#关卡选择第二页
        for i,j in zip(range(8), ('第六关', '第七关', '第八关', '第九关', '第十关',
                                  '上一页', '无尽模式', '返回')):
            if ptilvio == 1 and ((i<5 and i+6==sttlv) or i==6 and sttlv==11):
                ptcf('开始游戏', BUTT[i], FONT, 50, CPS['choco'])
            else:
                ptcf(j, BUTT[i], FONT, 50, CPS['choco'])
    elif stt==40:#技能选择
        for i,j in zip(range(7), list(map(showskn, range(0,6)))+['返回']):
            ptcf(j, BUTT[i], FONT, 50, CPS['choco'])
        if stnwsk:
            ptcf('下一关', BUTT[7], FONT, 50, CPS['choco'])
        else:
            ptcf('开始游戏', BUTT[7], FONT, 50, CPS['choco'])
    elif stt==14 or stt>=21 and stt<=29:#游戏帮助
        screen.blit(LOGO.convert_alpha(), (LOGOX, LOGOY))
        bkb = '开始游戏' if stlogin else '返回'
        for i,j in zip(range(3,7), ('游戏规则', '操作指南', 'TIPS', bkb)):
            ptcf(j, BUTT[i], FONT, 50, CPS['choco'])
    elif stt==10:#游戏背景
        if stlogin:
            ptcf('游戏规则', BUTT[7], FONT, 50, CPS['choco'])
        else:
            ptcf('回到菜单', BUTT[7], FONT, 50, CPS['choco'])
        screen.blit(BGB.convert(), BLD[3][0])
        pts(TXBG, BLD[3][0][0], BLD[3][0][1], EWID*WIDTH-40, 40, FONT2, CPS['board'])
    if stt==21:
        screen.blit(BGB.convert(), BLD[3][0])
        pts(TXRUL, BLD[3][0][0], BLD[3][0][1], EWID*WIDTH-40, 40, FONT2, CPS['board'])
    elif stt==22:
        screen.blit(BGB.convert(), BLD[3][0])
        pts(TXRO, BLD[3][0][0], BLD[3][0][1], EWID*WIDTH-40, 40, FONT2, CPS['board'])
    elif stt==23:
        screen.blit(BGB.convert(), BLD[3][0])
        if tino+1==len(TIPS):
            pt('(再次点击TIPS以回到第一页)', BLD[3][0][0], BLD[3][0][1], FONT2, CPS['board'])
        else:
            pt('(再次点击TIPS以翻页)', BLD[3][0][0], BLD[3][0][1], FONT2, CPS['board'])
        if (tino==2 or tino==3) and mlv<tino+1:
            pts('第%s关解锁'%CNNUM[tino+2], BLD[3][0][0], BLD[3][0][1]+40, EWID*WIDTH-40, 40, FONT2, CPS['board'])
        else:
            pts(TIPS[tino], BLD[3][0][0], BLD[3][0][1]+40, EWID*WIDTH-40, 40, FONT2, CPS['board'])
    if sttlv>0:
        screen.blit(BGB.convert(), BLD[3][0])
        showlv(sttlv)
    elif sttsk>=0:
        screen.blit(BGB.convert(), BLD[3][0])
        showsk(sttsk)
    screen.blit(AU[au].convert_alpha(), (SNDBX, SNDBY))
    screen.blit(MU[mu].convert_alpha(), (BGMBX, BGMBY))

#窗口基本设置
system('cls')
pygame.key.set_repeat(99)
FONT = pygame.font.SysFont(DFONT, 50) #字号 大
FONT2 = pygame.font.SysFont(DFONT, 40) #中大
FONT3 = pygame.font.SysFont(DFONT, 30) #中
screen = pygame.display.set_mode((SWID, SHEI))
pygame.display.set_icon(ICO.convert_alpha())
pygame.display.set_caption(TITLE)
Thread(target=loopmot).start()

#窗口循环
while True:
    try:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = 0
                saveF()
                pygame.quit()
            elif event.type == KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = 0
                    saveF()
                    pygame.quit()
                elif event.key == pygame.K_w: #无论大小写全半角均有效
                    pass
                if stt==0:#游戏可操作状态
                    det(event.key)
                    playm(event.key)
                elif stt==40:#技能选择
                    bindsk(event.key)
            elif event.type == MOUSEBUTTONUP:
                clickswitch(event)   
        screen.blit(BG.convert(),(0,0))
        sttdraw()
        if stt<=9:
            drawA()
            drawP()
            windeal()
        if wavev>=0 and not au: #触发音效
            playwave()
        pygame.display.update()
    except Exception as e:
        if e.__str__() == 'display Surface quit' or e.__str__() == 'video system not initialized' or e.__str__() == 'mixer system not initialized' or e.__str__() == 'cannot convert without pygame.display initialized':
            break
        else:
            print('BUG:', e)
