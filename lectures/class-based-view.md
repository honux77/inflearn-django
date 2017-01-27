# Class-based View

## function based view 와의 차이점
- GET, POST 와 같은 HTTP 메소드를 별도의 파이썬 메소드로 처리 
- 객체 지향의 장점을 적용 가능 -재사용성, Mixin 등
- 복잡한 구현을 가능하게 해줌

---
# Generic views

- 웹 개발시 자주 사용하는 기능을 장고에서 미리 제공해 줌
- 코드의 단순화, 빠른 개발을 가능하게 함
- 투표 앱의 index(), results(), detail() 모두 유사한 기능 수행