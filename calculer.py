from math import log
def caller(x):
    if x==0:
        return interest()
    elif x==1:
        return simple()
    elif x==2:
        return compound()
        

def question(list, y):
    if y not in list:
        return ('No')
    for i in range(len(list)):
        if list[i] == x :
            return i

def interest():
    list = [0,'월',2,'분기',4,5,'6개월',7,8,9,10,11,'연']
    con1 = question(list,input("Q : 6개월 or 분기 or 월 or 연 중 주어진 이율 분류는 무엇입니까?\nA : "))
    con2 = question(list,input("Q : 이율은 몇 %입니까?\nA : "))
    niz = question(list,input("Q : 6개월 or 분기 or 월 or 연 중 필요한 이율 분류는 무엇입니까?\nA : "))
    print('%s %d%입니다.' %(list[con1],(con2/con1)*niz))
    
    
        
    
def simple():
    #A = list[0], r = list[1], n = list[2], S= list[3]
    list = '원금, 이율, 기간, 원리합계'.split(', ')
    while True :
        niz = question(list,input("Q :원금, 이율, 기간, 원리합계 중 구하려는 것은 무엇입니까?\nA : "))
        if niz != 'No' :
            break
    list2 = [0,0,0,0]
    for i in range(len(list)) :
        if i != niz :
            list2[i] = int(input("Q. %s를 알려주세요.\nA. " % list[i]))
    if niz == 0:
        list2[0] = list2[3]/(1 + list2[2]*list2[1])
    elif niz == 1:
        list2[1] = (list2[3]-list2[0])/(list2[0]*list2[2])
    elif niz == 2:
        list2[2] = (list2[3]-list2[0])/(list2[0]*list2[1])
    elif niz == 3:
        list2[3] = list2[0]*(1+(list2[1]*list2[2]))
    print("%s는 %d입니다." % (list[niz],list2[2]))


def compound():
    #A = list[0], r = list[1], n = list[2], S= list[3]원
    list = '원금, 이율, 기간, 원리합계'.split(', ') 
    niz = question(list,input("Q :원금, 이율, 기간, 원리합계 중 구하려는 것은 무엇입니까?\nA : "))
    list2 = [0,0,0,0]
    for i in range(len(list)) :
        if i != niz :
            list2[i] = int(input("Q. %s를 알려주세요.\nA. " & list[i]))
    if niz == 0:
        list2[0] = list2[3]/((1 + list2[1])**list2[2])
    elif niz == 1:
        list2[1] = ((list2[3]/list2[0])**list2[2])-1
    elif niz == 2:
        list2[2] = log((list2[3]/list2[0]),1+list2[1])
    elif niz == 3:
        list2[3] = list2[0]*((1+list[1])**list[2])
    print("%s는 %d입니다." % (list[niz],list2[niz]))
    return 0
    







while True :
    x = input("Q : 이율 계산기, 단리이자 계산기, 복리 이자 계산기 중 필요하신 계산기는 무엇입니까?\nA : ")

    list = "이율 계산기, 단리이자 계산기, 복리 이자 계산기".split(', ')

    caller(question(list,x))
            
