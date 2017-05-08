#★ class member로 사용했을때
# class yourclass:
#     pass
#
# class myclass:
#     def __init__(self):
#         self.message = "Hello"
#
#     def some_method(self):
#         print(self.message)
#
#
# obj = myclass()
# obj.some_method()
# print(obj.message)

#★ private member로 사용했을 때
class yourclass:
    pass

class myclass:
    def __init__(self):
        self.message = "Hello"
        self.__private = "Private"


    def some_method(self):
        print(self.message)
        print(self.__private)


obj = myclass()
obj.some_method() #메소드를 불러올 경우에는 private 도 출력이 됨
print(obj.message)
print(obj.__private) # 이렇게 따로 private 변수를 불러오면 에러가 난다