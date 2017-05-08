#예제1
# def greet(name):
#     def greet_message():
#         return 'Hello'
#     return "{} {}".format(greet_message(),name)
#
# print(greet("scott"))

#예제2
# def greet(name):
#     return "Hello {}".format(name)
#
# def uppercase(func):
#     def wrapper(name):
#         result = func(name)
#         return result.upper()
#
#     return wrapper
#
# new_greet = uppercase(greet)
# print(new_greet("scott"))

#문제167
# def find_job(name):
#     import csv
#     for emp_list in csv.reader(open(r"C:\Users\stu\Desktop\Python_data\emp1.csv",'r')):
#         if emp_list[2]==name:
#             return emp_list[3]
#
# def lower_case(func):
#     def swap(name):
#         result=func(name)
#         return result.lower()
#     return  swap
#
# new_find_job=lower_case(find_job)
# print(new_find_job('SCOTT'))

# 문제169
# def r_u_king(name):
#     if name != 'KING':
#         raise Exception("KING만 볼수 있지롱~")
#
# class Find_sal(object):
#     insert_name=None
#     def set_name(self,name):
#         r_u_king(name)
#         self.insert_name = name
#
#     def get_sal(self,name):
#         import csv
#         for emp_list in csv.reader(open(r"C:\Users\stu\Desktop\Python_data\emp1.csv", 'r')):
#             if emp_list[2] == name:
#                 return emp_list[6]
# find_sal = Find_sal()
# find_sal.set_name('KING')
# print(find_sal.get_sal('SCOTT'))

# 데코레이터 예제
# def is_admin(func):
#     def wrapper(*args, **kwargs):  # *arg =  리스트의 가변 매개변수
#         # **arg = 딕셔너리 가변 매개변수
#         if kwargs.get('name') != 'admin':
#             raise Exception("권한이 없다니까요")
#         return func(*args, **kwargs)
#     return wrapper
#
# class Greet(object):
#     current_user = None
#
#     @is_admin
#     def set_name(self, name):
#         self.current_user = name
#
#     def get_greeting(self, name):
#         return "Hello {}".format(name)
#
# greet = Greet()
# greet.set_name(name='admin')
# print(greet.get_greeting('WT'))

# 문제171
# def r_u_king(name):
#     def swap(*args,**swargs):
#         if swargs.get('name') != 'KING':
#             raise Exception("KING만 볼수 있지롱~")
#         return name(*args,**swargs)
#     return swap
#
# class Find_sal(object):
#     insert_name=None
#
#     @r_u_king
#     def set_name(self,name):
#         self.insert_name = name
#
#
#     def get_sal(self,name):
#         import csv
#         for emp_list in csv.reader(open(r"C:\Users\stu\Desktop\Python_data\emp1.csv", 'r')):
#             if emp_list[2] == name:
#                 return "{} 사원의 월급은 {}입니다".format(emp_list[2],emp_list[6])
# find_sal = Find_sal()
# find_sal.set_name(name='KING')
# print(find_sal.get_sal('SCOTT'))

# 문제172
# class Gun():
#     bullet = 0
#
#     @staticmethod
#     def charge(num):
#         Gun.bullet = num
#         print("총알이 {}발 장전되었다".format(num))
#
#     @staticmethod
#     def shoot(num):
#         for i in range(num):
#             print("탕!")
#             Gun.bullet-=1
#         Gun.print(Gun.bullet)
#
#     @staticmethod
#     def print(num):
#         if num == 10:
#             print("총알이 만땅입니다")
#         else:
#             print("총알이 {}발 남았습니다".format(Gun.bullet))
#
# gun_1=Gun()
# gun_1.charge(9)
# gun_1.shoot(2)
#
# gun_2=Gun()
# # gun_2.charge(8)
# gun_2.shoot(2)





# --딕셔너리를 사용할경우
# student = { 'name' : '김인호' , 'year' : 2, 'class' : 3, 'student_id' : 35 }
# print( '{}, {}학년 {}반 {}번'.format(student['name'],student['year'],student['class'],student['student_id']))

#--클래스로 사용할경우
# class student(object):
#     def __init__(self, name, year, class_num, student_id):
#         self.name = name
#         self.year = year
#         self.class_num = class_num
#         self.student_id = student_id
#         student.intro_myself(self)
#
#     def intro_myself(self):
#         return '{}, {}학년 {}반 {}번'.format\
#             (self.name, self.year, self.class_num ,self.student_id)
#
# stu = student('조원태',2,5,24)

# 클래스 데코레이터 예제
# from  functools import wraps
# class OnlyAdmin(object):
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         name = kwargs.get('name').upper()
#         self.func(name)
#
# @OnlyAdmin
# def greet(name):
#     print("Hello {}".format(name))
#
# greet(name='scott')

#문제176
# from functools import wraps
# class OnlyAdmin(object):
#     def __init__(self,func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         name = kwargs.get('name').upper()
#         return self.func(name)
#
# @OnlyAdmin
# def find_job(name):
#     import csv
#     for emp_list in csv.reader(open(r"C:\Users\stu\Desktop\Python_data\emp1.csv", 'r')):
#         if emp_list[2] == name:
#             return "당신의 직업은 {}입니다".format(emp_list[3])
#
# print(find_job(name='scott'))


# 추상메소드 예제
# from abc import ABCMeta, abstractmethod  # 파이썬은 추상 클래스를 제공 x
# class Animal(object):
#     __metaclass__ = ABCMeta  # 추상클래스로 선언
#
#     @abstractmethod  # 추상 메소드 선언
#     def bark(self):
#         pass # 비어있는 메소드
#
# class Cat(Animal):
#     def __init__(self):
#         self.sound= '야옹'
#     def bark(self):
#         return self.sound
#
# class Dog(Animal):
#     def __init__(self):
#         self.sound = '멍멍'
#     def bark(self):
#         return self.sound
# cat=Cat()
# dog=Dog()
# print(cat.bark())
# print(dog.bark())

# 문제177
# from abc import ABCMeta, abstractmethod
# class Beverage(object):
#     __metaclass__ = ABCMeta
#
#     @abstractmethod
#     def price(self):
#         pass
#
# class Americano(Beverage):
#     def __init__(self):
#         self.w_price = 4100
#     def price(self):
#         self.dollar = '%.2f' %(self.w_price / 1137)
#         return self.dollar
#
# class Caffelatte(Beverage):
#     def __init__(self):
#         self.w_pirce = 4700
#     def price(self):
#         self.dollar = '%.2f' %(self.w_pirce / 1137)
#         return self.dollar
# a = Americano()
# c = Caffelatte()
# print(c.price())
# print(a.price())

#문제179
# def my_power():
#     try:
#         x = input('분자 숫자를 입력 : ')
#         y = input('분모 숫자를 입력 : ')
#         return '%.2f' %(int(x) /  int(y))
#     except:
#         print('0으로는 나눌 수 없습니다')
# my_power()

#문제180
# import csv
# def find_sal():
#     name = input('이름을 입력 : ').upper()
#     for emp_list in csv.reader(open(r"C:\Users\stu\Desktop\Python_data\emp1.csv", 'r')):
#         if emp_list[2] == name:
#             return emp_list[6]
# print(find_sal())

#문제181
# def find_sal_pandas():
#     import pandas as pd
#     name = input('이름을 입력 : ')
#     emp = pd.DataFrame.from_csv(r"C:\Users\stu\Desktop\Python_data\emp.csv")
#     emp_sal = emp['sal'][emp['ename'] == name ].values[0]
#     return emp_sal
# print(find_sal_pandas())

#문제182
# import pandas as pd
# def find_sal_pandas():
#     try:
#         job = ''
#         while job == '':
#          job = input('직업을 입력 : ').upper()
#         emp = pd.DataFrame.from_csv(r"C:\Users\stu\Desktop\Python_data\emp.csv")
#         sal = emp[['sal','job']][emp['job']==job]
#         result = sal.groupby('job')['sal'].sum()
#         return result
#     except:
#         print('해당 직원은 없습니다')
# print(find_sal_pandas())

#문제183
# import csv
# def find_sal():
#     try:
#         name = ''
#         while name == '':
#             name = input('이름을 입력 : ').upper()
#         for emp_list in csv.reader(open(r"C:\Users\stu\Desktop\Python_data\emp1.csv", 'r')):
#             if emp_list[2] == name:
#                 print(emp_list[6])
#     except:
#         print('해당사원은 없습니다')
#     else:
#         print('월급 추출에 성공했습니다')
# find_sal()

#문제184
# def my_power():
#     try:
#         x = input('분자 숫자를 입력 : ')
#         y = input('분모 숫자를 입력 : ')
#         print('나눈 값은 ─>','%.1f' %(int(x) /  int(y)))
#     except:
#         print('E R R O R!!! 분모가 0 입니다')
#     else:
#         print('나눈 값 추출 성공!')
# my_power()

#exception 클래스 예제
# def my_power():
# 	try:
# 		x = input('분자 숫자를 입력 : ')
# 		y = input('분모 숫자를 입력 : ')
# 		return int(x) / int(y)
# 	except Exception as err: # 증조 할아버지 격
# 		print("예외가 발생했다")
# 	except ZeroDivisionError as err: # 증손자 격
# 		print("0으로 나눌 수 없다")
# my_power()

#NotImplementedError 예제 (오버라이딩 해야 정답임)
# class bird:
# 	def fly(self):
# 		pass
# class eagle(bird):
#     def fly(self):
#         print("베리 패.스.트")
# eagle = eagle()
# eagle.fly()

#문제186
# import pandas as pd
# def find_sal():
#     name = input('이름을 입력 : ').upper()
#     emp = pd.DataFrame.from_csv(r"C:\Users\stu\Desktop\Python_data\emp.csv")
#     sal = emp['sal'][emp['ename']==name].values[0]
#     if sal >= 3000:
#         raise Exception('해당 사원을 접근금지')
#     else:
#         print(sal)
# find_sal()

# def p187():
#     number = 0
#
#     while number not in range(1,10):
#         number = int(input('숫자를 입력하세요'))
#     else:
#         return number
#
#
# print(p187())

# def get_number():
#     num = ''
#     while num not in range(1,10):
#         try:
#             num = int(input('숫자를 입력하세요 '))
#         except ValueError:
#             continue
#     return num
# print(get_number())

# def action():
#     #printboard(state)
#     action = None
#     while action not in range(1, 10):
#          try:
#             action = int(input('Your move? '))
#          except ValueError:
#             continue
#     switch_map = {
#         1: (0, 0),
#         2: (0, 1),
#         3: (0, 2),
#         4: (1, 0),
#         5: (1, 1),
#         6: (1, 2),
#         7: (2, 0),
#         8: (2, 1),
#         9: (2, 2) }
#     return switch_map[action]
# print(action())

# DRAW=3
# def episode_over(winner):
#     if winner == DRAW:
#         print('Game over! It was a draw.')
#     else:
#         print('Game over! Winner: Player {0}'.format(winner))
# episode_over(1)

def play(agent1, agent2):
    state = emptystate()
    for i in range(9):
        if i % 2 == 0:
            move = agent1.action(state)
        else:
            move = agent2.action(state)
        state[move[0]][move[1]] = (i % 2) + 1
        winner = gameover(state)
        if winner != EMPTY:
            return winner
    return winner