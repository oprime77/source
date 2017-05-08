# class ClassVar:
#     text_list=[]   # 클래스의 정의 시점에서 바로 메모리에 할당됨
#     def add(self,text):
#         self.text_list.append(text)
#     def print_list(self):
#         print(self.text_list)
#
# if __name__ == '__main__':
#     a = ClassVar()
#     a.add('a')
#     a.print_list()
#
#     b = ClassVar()
#     a.add('b')
#     b.print_list()
#
# __init__() 을 안 쓴 잘못된 예

class ClassVar:
    def __init__(self):
        self.text_list = []
    def add(self, text):
        self.text_list.append(text)
    def print_list(self):
        print(self.text_list)

if __name__ == '__main__':
    a = ClassVar()
    a.add('a')
    a.print_list()

    b = ClassVar()
    b.add('b')
    b.print_list()