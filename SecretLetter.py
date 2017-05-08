#ord() -> 문자를 숫자로 바꿔주는 아스키 코드 함수
#chr() -> 숫자를 문자로 바꿔주는 아스키 코드 함수
# list = []
# su = input('문자의 개수 입력 : ')
# su6 = input('시크릿 숫자를 입력 : ')
# for i in su6:
#     list.append(i)
# for i in list:
#     cnt=0
#     i[cnt:]
#     cnt+=6

dic = {}
dic[65]=[0,0,0,0,0,0]
dic[66]=[0,0,1,1,1,1]
dic[67]=[0,1,0,0,1,1]
dic[68]=[0,1,1,1,0,0]
dic[69]=[1,0,0,1,1,0]
dic[70]=[1,0,1,0,0,1]
dic[71]=[1,1,0,1,0,1]
dic[72]=[1,1,1,0,1,0]

list1=[]
for i in range(18):
    list1.append(i)
print(list1)
