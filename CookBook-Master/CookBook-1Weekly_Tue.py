# # CHAPTER 1. 자료구조와 알고리즘
# #  ● 유용한 자료구조 파악
# #  ● collections 모듈에 제공되는 다양한 자료 사용법 파악
#
# # 1.1 시퀀스를 개별 변수로 나누기
# #   문제. N개의 요소를 가진 튜플이나 시퀀스가 있다. 이를 변수 N개로 나누어보자
# #   주의할점! 변수의 개수는 시퀀스에 일치해야 한다.
# #   해결
# p = (4,5)
# x,y = p
# print(x) # 4 출력
# print(y) # 5 출력
#
# data = ['ACME',50,91.1,(2012,12,21)]
# name,su,su2,date = data
# print(date) # (2012,12,21) 출력
# y,m,d = date
# print(y,m,d) # 2012 12 21 출력
#
# #   에러날 경우
# ## p = (4,5) # p 변수의 값은 2개
# ## x,y,z = p # 3개로 시퀀스했기 때문에 에러!
# #                            ┌─ 에 러 메 세 지 ─┐
# # Traceback (most recent call last):
# #   File "D:/python/source/CookBook-1Weekly_Tue.py", line 22, in <module>
# #     x,y,z = p
# # ValueError: not enough values to unpack (expected 3, got 2)
#
# # 놀라운 것은 순환 가능한 모든 객체에 적용할 수 있다.(ex.문자열, 파일, iterator, generator)
# A = '000400'
# a,b,c,d,e,f=A
# print(a,b,c,d,e,f)
#
# # 지극히 개인적인 예제
# dic={'A':'000000'}
# print(dic['A'][0]) # 0 출력
#
# # 특정 값을 무시하고 싶을 경우
# data1 = ['ACME',50,91.1,(2012,12,21)]
# _,su1,_,date=data1
# print(su1) # 50 출력
# # 1.2 임의 순환체의 요소 나누기
# # 문제. 순환체를 언패킹하려는데 요소가 N개 이상 포함되어 "값이 너무 많습니다"라는 예외가 발생할 때
# # 해결. * 을 쓴다.
# #예제1)
# import numpy as np
# def drop_first_last(grades):
#     first, *middle, last = grades
#     return sum(middle)
# #예제2)
# record = ('Dave','dave@example.com','773-555-1212','847-555-1212')
# name,email,*phone_number = record
# print(name) # Dave 출력
# print(phone_number) # 773~ 과 847~ 출력
# #이러한 별표가 붙은 변수는 리스트의 맨 앞에서도 사용할 수 있다
# #예제1)
# sales_record = [10,8,7,1,9,5,10,3]
# *trailing_qtrs, current_qtr = sales_record
# trailing_avg = sum(trailing_qtrs) / len(trailing_qtrs)
# print(sum(trailing_qtrs)) # 3을 제외한 합 = 50
# print(trailing_avg) # 7.1428 (50 / 7)
# # 즉 길이를 알수없는 순환체에 안성맞춤!!!!
# # 결국 길이가 일정하지 않은 튜플에 사용하면 상당히 편리하다는 점!!!
# #예제1)
# records = [('foo',1,2),('bar','hello'),('foo',3,4),]
# # 결국 foo뒤의 1,2나 hello나 3,4가 *args 이고
# # foo 와 bar 는 tage가 되는 것이다.
# def do_foo(x,y):
#     print('foo',x,y)
# def do_bar(s):
#     print('bar',s)
# for tag,*args in records:
#     if tag == 'foo':
#         do_foo(*args)
#     elif tag == 'bar':
#         do_bar(*args)
# # 언패킹 이후 특정 값을 버리고 싶다면 이렇게 해보자!!
# # 예제1)
# record = ('ACME',50,123.45,(12,18,2012))
# name,*_,(*_,year) = record
# print(name) # ACME 출력
# print(year) # 2012 출력
# # 재귀 알고리즘에서도 사용할 수 있다
# def sum(items):
#     head,*tail = items
#     return head + sum(tail) if tail else head
# items=[1,10,7,4,5,9]
# print(sum(items))
# # 1.3 마지막 N개 아이템 유지
# # 문제
# # 순환이나 프로세싱 중 마지막으로 발견한 N개의 아이템을 유지하고 싶다.
# # 해결
# # 이와 같은 용도로 collections.deque가 가장 알맞다.
# # 예를 들어, 다음에 나오는 코드는 여러줄에 대해서 간단한 텍스트 매칭을 수행하고 처음으로 발견한 N라인을 찾는다.
# from collections import deque
# def search(lines, pattern, history=5):
#     pre_lines = deque(maxlen=history)
#     for line in lines:
#         if pattern in line:
#             yield line, pre_lines
#             pre_lines.append(line)
# # 파일 사용 예
# if __name__ == '__main__':
#     with open(r"C:\Users\Won Tae CHO\Desktop\somefile.txt") as f:
#         for line,prevlines in search(f,'python',5):
#             for pline in prevlines:
#                 print(pline,end='')
#             print(line,end='')
#             print('-'*20)
# # 토론
# # 아이템을 찾는 코드를 작성할 때, 주로 yield를 포함한 제너레이터 함수를 만들곤 한다.
# # 이렇게 하면 검색 과정과 결과를 사용하는 코드를 분리할 수 있다.
# # deque(maxlen=N)으로 고정 크기 큐를 생성한다.
# # 큐가 꽉찬 상태에서 새로운 아이템을 넣으면 가장 마지막 아이템이 자동 삭제된다.
# # 예제1)
# q = deque(maxlen = 3)
# q.append(1)
# q.append(2)
# q.append(3)
# print(q) # 1, 2, 3 input됨
# q.append(4)
# print(q) # 가장 마지막인 1을 output 하고 4를 새로 input함
# q.appendleft(5) # 맨 왼쪽에서 append를 한다
# print(q)  # 5, 2, 3이 출력됨

# # 1.4 N 아이템의 최대 혹은 최소값 찾기
# # 문제
# # 컬렉션 내부에서 가장 크거나 작은 N개의 아이템을 찾아야 한다.
# # 해결
# # heapq 모듈에는 이용도에 적합한 nlargest() 와 nsmallest() 두 함수가 있다
# import heapq
# nums = [1,8,2,23,7,-4,18,23,42,37,2]
# print(heapq.nlargest(3, nums)) # 제일 큰수 3개 뽑기 (42,37,23)
# print(heapq.nsmallest(3,nums)) # 제일 작은수 3개 뽑기 (-4,1,2)
# # 복잡한 방법으로 사용하기
# portfolio = [{'name':'IBM','shares':100,'price':91.1},
#              {'name':'AAA','shares':200,'price':234}]
# cheap = heapq.nsmallest(1,portfolio,key=lambda s:s['price'])
# expensive = heapq.nlargest(1,portfolio,key=lambda s:s['price'])
# print(cheap) # [{'name': 'IBM', 'shares': 100, 'price': 91.1}] 출력
# print(expensive) # [{'name': 'AAA', 'shares': 200, 'price': 234}] 출력
#
# # 1.5 우선 순위 큐 구현
# # 문제
# # 주어진 우선 순위에 따라 아이템을 정렬하는 큐를 구현하고 항상 우선 순위가 가장 높은 아이템을 먼저 팝하도록 만들어야 한다.
# # 해결
# # heapq 모듈을 사용해 간단한 우선 순위 큐를 구현한다.
# class PriorQueue:
#     def __init__(self):
#         self._queue = []
#         self._idx = 0
#     def push(self,item,prior):
#         heapq.heappush(self._queue,(-prior,self._idx,item))
#         self._idx += 1
#     def pop(self):
#         return heapq.heappop(self._queue)[-1]
# class Item:
#     def __init__(self,name):
#         self.name = name
#     def __repr__(self):
#         return 'Item({!r})'.format(self.name)
# q = PriorQueue()
# q.push(Item('foo'),1)
# q.push(Item('bar'),5)
# q.push(Item('kkk'),3)
# print(q.pop()) # 1순위는 bar(5번)이다.
# print(q.pop()) #  bar가 삭제된 후 1순위는 kkk(3)가 된다
# print(q.pop()) #  kkk가 삭제된 후 1순위는 foo(1)가 된다
# # 1.6 딕셔너리의 키를 여러 값에 매핑하기
# # 문제
# # 딕셔너리의 키를 하나 이상의 값에 매핑하고 싶다
# # 해결
# # 하나의 키에 하나의 값이 매핑되어 있는 것을 딕셔너리라 부른다.
# # 키에 여러 값을 매핑하려면, 그 여러 값을 리스트나 세트와 같은 컨테이너에 따로 저장해 두어야 한다
# d = { 'a' : [1,2,3,],'b':[4,5]}
# e = {'a':{1,2,3},'b':{4,5}}
# # 아이템의 삽입 순서를 지켜야 한다면 리스트를 사용하는 것이 좋다.
# # 순서가 상관 없고 중복을 없애려면 세트를 사용해야 한다.
# # 이러한 딕셔너리를 쉽게 만들기 위해서 collections 모듈의 defaultdict를 사용한다.
# # defaultdict 의 기능 중에는 첫번째 값을 자동으로 초기화하는 것이 있어서 사용자는 추가에만 집중할 수 있다
# from collections import defaultdict
# d = defaultdict(list)
# d['a'].append(1)
# d['a'].append(2)
# d['b'].append(3)
# d = defaultdict(set)
# d['a'].add(1)
# d['a'].add(2)
# d['a'].add(4)
# # 토론
# # 이론적으로 여러 값을 가지는 딕셔너리를 만드는 것이 복잡하지는 않다.
# # 하지만 첫 번째 값에 대한 초기화를 스스로 하려면 꽤나 복잡한 과정을 거쳐야 한다.
# d = {}
# for key,value in pairs:
#     if key not in d:
#         d[key] = []
#         d[key].append(value)
# # defaultdict을 사용하면 좀 더 깔끔한 코드가 된다.
# d = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)

# # 1.7 딕셔너리 순서 유지
# # 문제
# # 딕셔너리를 만들고, 순환이나 직렬화할 때 순서를 조절하고 싶다
# # 해결
# # 딕셔너리 내부 아이템의 순서를 조절할려면 collections 모듈의 OrderedDijct을 사용한다.
# # 이 모듈을 사용하면 삽입 초기의 순서를 그대로 기억한다
# from collections import OrderedDict
# d = OrderedDict()
# d['foo']=1
# d['bar']=2
# d['spam']=3
# d['grok']=4
# for key in d:
#     print(key,d[key]) #  foo 1 / bar 2 / spam 3 / grok 4
#
# # 1.8 딕셔너리 계산
# # 문제
# # 딕셔너리 데이터에 여러 계산을 수행하고 싶다면??(최소값,최대값,정렬 등)
# # 해결
# # 딕셔너리에 주식 이름과 가격이 들어 있다고 가정해보자
# prices = {'ACME':45,'AAPL':612,'IBM':205,'HPQ':37,'FB':10}
# min_price = min(zip(prices.values(),prices.keys())) # zip 을 안 쓰면 에러가 난다
# print(min_price) # (10,'FB')
# max_price = max(zip(prices.values(),prices.keys())) # zip 을 안 쓰면 에러가 난다
# print(max_price) # (612,'AAPL')
# prices_and_names = zip(prices.values(),prices.keys())
# print(min(prices_and_names)) # (10,'FB')
# print(max(prices_and_names)) # zip()은 한번만 소비 가능한 이터레이터기 때문에 max()는 인자가 비어있다.
# # 만약 여러 엔트리가 동일한 값을 가지고 있을 때 비교 결과를 결정하기 위해서 키를 사용한다
# # 예제1)
# prices = {'AAA':45,'ZZZ':45}
# a = min(zip(prices.values(),prices.keys()))
# print(a) # values() 값이 동일하므로 key이 더 작은 AAA를 출력
# b = max(zip(prices.values(),prices.keys()))
# print(b) # values() 값이 동일하므로 key이 더 큰 ZZZ를 출력
#
# # 1.9 두 딕셔너리의 유사점 찾기
# # 문제
# # 두 딕셔너리가 있고 여기서 유사점을 찾고 싶다(동일한 키,동일한 값 등)
# # 해결
# a = { 'x':1,'y':2,'z':3}
# b = { 'x':10,'w':11,'z':3}
# # 두 딕셔너리의 유사점을 찾으려면 keys()와 item() 메소드에 집합 연산을 수행한다
# # 동일한 키 찾기
# print(a.keys() & b.keys()) # z x 출력
# # a에 있고 b에 없는 키 찾기
# print(a.keys() - b.keys()) # y 출력
# # (키, 값)이 동일한 것 찾기
# print(a.items() & b.items()) # (z,3) 출력
# # 특정 키를 제거한 새로운 딕셔너리 만들기
# c = {key:a[key] for key in a.keys() - {'z','w'}}
#     # 제너레이터 발생 후 a.keys()에서 z와 w를 제외한 a.keys를 for 문으로 돌린다.
# print(c) # {'x':1,'y':2} 출력

# # 1.10 순서를 깨지 않고 시퀀스의 중복 없애기
# # 문제
# # 시퀀스에서 중복된 값을 없애고 싶지만, 아이템의 순서는 유지하고 싶다
# # 해결
# # 시퀀스의 값이 해시가 가능하다면 이 문제는 세트와 제너레이터를 사용해서 쉽게 해결할 수 있다
# def dupe(items):
#     seen = set()
#     for item in items:
#         if item not in seen:
#             yield item
#             seen.add(item)
# a=[1,5,2,1,9,1,5,10]
# print(list(dupe(a))) # [1, 5, 2, 9, 10] 출력 //즉, 중복제거해도 시퀀스의 순서는 그대로
# # 하지만 해시 불가능한 dict와 같은 타입의 중복을 없애려면 수정이 필요하다
# def dupe(items,key=None):
#     seen = set()
#     for item in items:
#         val = item if key is None else key(item)
#         if val not in seen:
#             yield item
#             seen.add(val)
# a = [ {'x':1,'y':2},{'x':1,'y':3},{'x':1,'y':2},{'x':2,'y':4}]
# print(list(dupe(a,key=lambda x:(x['x'],x['y'])))) # x값 그리고 y값 동시에 중복값 제거
#                                                     # [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 2, 'y': 4}]
# print(list(dupe(a,key=lambda x:x['x']))) # x값에 대한 중복값 제거
#                                           # [{'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
# # 토론
# # 종복을 없애려면 대개 세트를 만드는 것이 가장 쉽지만 기존의 데이터 순서가 훼손되므로 앞의 방식을 사용하는게 좋다
# a = [1,5,2,1,9,1,5,10]
# print(set(a)) # {1, 2, 5, 9, 10} 출력

# 1.11 슬라이스 이름 붙이기
# 문제
# 프로그램 코드에 슬라이스를 지시하는 하드코딩이 너무 많아 이해하기 어려운 상황을 정리하고 싶을때???
# 해결
items = [0,1,2,3,4,5,6]
a = slice(2,4)
print(items[2:4]) # [2,3] 출력
print(items[a]) # [2,3] 출력
items[a] = [10,11] #items[2:4] 자리에 10,11을 넣는다
print(items) # [0, 1, 10, 11, 4, 5, 6] 출력
del items[a] # items[2:4] 자리를 삭제한다
print(items) # [0, 1, 4, 5, 6] 출력
# slice 인스턴스 s가 있다면 s.start와 s.stop, s.step 속성을 통해 좀더 많은 정보를 얻을 수 있다
a = slice(10,25,3)
print(a.start) # 10 출력
print(a.stop) # 25 출력
print(a.step) # 3 출력

