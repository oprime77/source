# 부모에게 물려받은 메소드 실행 예제
# class father:
#     def base_method(self):
#         print("Father")
#
# class child(father):
#     pass
#
# father= father()
# father.base_method()
#
# child = child()
# child.base_method()

class father:
    def __init__(self):
        print("Hello")
        self.message="Good Morning"

class child(father):
    def __init__(self):
        #father.__init__(self)
        super().__init__()
        print("Hello~~ I am child")

father= father()
child = child()



#print(father.message)
#print(child.message)