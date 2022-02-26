with open('inner.py', encoding='utf-8') as f:
    exec(f.read())
#调试运行部分
from os import system
from pynput import keyboard
CVB = ('nwrbsl', 'NWRBSL')   

def responsekey(k):
    global stt
    try:
        if not stt:
            det(k.char)
            stt=1
    except AttributeError:
        if not stt:
            if k==keyboard.Key.enter or k==keyboard.Key.space:
                stt=1
                det('\n')

def drawski(i):
    t='%.1fs CD, %d times '%(sk[i].cd, sk[i].lf)
    if sk[i].ty==0 and skispeed:#疾速
        t+=', left:%.1fs'%ctnspeed
    elif sk[i].ty==5 and ctnlock>=0:#锁定
        t+=', left:%.1fs'%ctnlock
    return t

def drawB():
    print('TIME:%.1f/%d'%(max(stlf,0.0),TIMELIM))
    print('POWER_WASTED:%d/%d'%(dhp, MAXHP))
    if len(sk)>=1:
        print('SKILL E:%s'%drawski(0))
    if len(sk)>=2:
        print('SKILL R:%s'%drawski(1))
    for i in range(LAYER-1,-1,-1):
        t=''
        for j in range(WIDTH):
            t+=CVB[inblock(j,i)][bulbs[i][j]]
        print(t)

def loopB():
    global stlf,stt,cd,ctnspeed,ctnlock
    while ctnC():
        system("cls")
        loopC()
        drawB()
        sleep(FRAMEV*0.8)
    if stt!=3:
        print('YOU WIN!!')
    else:
        print('YOU LOSE!!')
        
def startB(level='0',skii=[]):
    initstt(level,ski=skii)
    loopB()

def keythr():
    with keyboard.Listener(on_press = responsekey) as lis:
        lis.join()
Thread(target=keythr).start()
input('测试平台；输入start开始游戏。输入quit退出程序。')
while True:
    cmd = input('Command:')
    if cmd == 'start':
        startB('02',[2, 3])
    elif cmd=='quit':
        break
