
# 클래스 변수와 인스턴스 변수
- 클래스 변수: 모든 클래스의 인스턴스간에 값을 공유하는 변수
- 인스턴스 변수: 인스턴스마다 개별적으로 다른 값을 가지는 변수
```pthon
class User:
    num_users = 0 # class 변수
    def __init__(self, name):
        self.name = name # instance 변수
        User.num_users += 1
    # ...
```

