import turtle as t
import time
text="""
有一个人前来买瓜
哥们儿
这瓜多少钱一斤啊
两块钱一斤
㦱撡
这瓜皮子是金子做的
还是瓜粒子是金子做的
你瞧瞧现在哪有瓜呀
这都是大棚的瓜
你嫌贵我还嫌贵呢
给我挑一个
行
这个怎么样
这个保熟吗
我开水果摊的
能卖你生瓜蛋子
我问你这瓜保熟吗
你故意找茬是不是
你要不要吧
你这瓜要是熟我肯定要啊
哪它要是不熟怎么办呀
哎 要是不熟我自己吃了它
满意了吧
十五斤 三十块
你这哪够十五斤
你这称有问题呀
你故意找茬是不是 你要不要吧
吸铁石
另外，你说的
这瓜要是生的 你自己吞进去 啊
你褟蟆劈我瓜是不是
杀人啦




"""

t.bgpic("00.png")
t.update()
t.goto(-210,170)
t.penup()
t.hideturtle()
for i in range(len(text)):
    print(text[i],end="",flush=True)
    #print(i)
    t.write(text[i],move=True,font=("宋体",18,"normal"))
    if text[i]=="\n":
        
        t.clear()
        t.goto(-210,170)

    if i==6:
        t.bgpic("01.png")
    if i==86:
        t.bgpic("02.png")
    if i==180:
        t.bgpic("03.png")
    if i==210:
        t.bgpic("04.png")        
    if i==220:
        t.bgpic("05.png")         
    if i==250:
        t.bgpic("06.png")      
    time.sleep(0.1)








