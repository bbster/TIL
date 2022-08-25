# 어트리뷰트란 클래스 내부에 포함되어 있는 변수나 메서드를 의미
class Drama:
    # 클래스 속성 메서드 단계와 동일한 위치
    def __init__(self, name, broadcaster, episode): # 초기화를 위한 메서드  / 인스턴스화 할때 반드시 처음에 실행되는 메서드
        self.name = name # 어트리뷰트
        self.broadcaster = broadcaster
        self.episode = episode

    def my_watching_broadcast(self): # 클래스의 메서드
            return self.name, self.broadcaster, self.episode

drama_instance = Drama("wooyoungwoo", "netflix", 1) # Drama라는 클래스의 인스턴스 생성
print(f"내가 현재 시청하는 드라마: {drama_instance.my_watching_broadcast()}")

# getattr(object, name, default)
# 해당 객체의 어트리뷰트를 돌려준다.
# drama_instance라는 객체의 속성값에 name이 있으면 그 name값 리턴
getattr_result = getattr(drama_instance, "name") # 공식 문서에 따르면 drama_instance.name과 동일하다
print(f"getattr : {getattr_result}")
# getattr_result = getattr(drama_instance, "name", "broadcaster") # 첫번째 name에 대한 값만 리턴
# print(f"getattr : {getattr_result}")
getattr_result = getattr(drama_instance, "broadcaster")
print(f"getattr : {getattr_result}")
getattr_result = getattr(drama_instance, "episode", "episode")
print(f"getattr : {getattr_result}")
print(f"getattr_ids : {id(getattr_result)}")

# setattr(object, name, value)
# 해당 객체의 어트리뷰트 중 새로운 값으로 수정할수 있다.
# drama_instance라는 객체의 episode라는 속성의 값을 2로 세팅한다.
setattr_result = setattr(drama_instance, "episode", 2)
getattr_result = getattr(drama_instance, "episode", "episode")
print(f"setattr후 결과값 : {getattr_result}")
print(f"getattr_ids : {id(getattr_result)}")

# hasattr(object, name)
print(f"hasattr : {hasattr(drama_instance, 'name')}")
print(f"hasattr : {hasattr(drama_instance, 'nothing')}")

def something(*args, **kwargs):
    print(args)
    print(kwargs)

