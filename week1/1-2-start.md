# 파이썬과 장고 설치하기 

## 적합한 버전 찾기 
먼저 장고 홈페이지를 방문해서 장고와 호환되는 파이썬 버전을 확인합니다.

https://docs.djangoproject.com/en/2.0/releases/2.0/ 

링크의 문서를 보면 python 3.6의 최신 버전을 추천하는 것을 확인할 수 있습니다.

### 공식 홈페이지 다운로드
파이썬 홈페이지에서 2018년 1월 현재 3.6의 최신인 3.6.4를 다운받아 설치합니다.

https://www.python.org/downloads/ 


## 장고 설치

장고는 장고 공식 홈페이지의 내용을 참고해서 2.0.1 버전을 설치하기로 합니다. 
명령창을 열고 pip를 이용해 장고를 설치할 수 있습니다.

```
$ pip install Django==2.0.1
```

## 설치 확인
명령창을 열고 python3를 실행합니다. 

```python
>> import django
>> print(django.get_version())
2.0.1
```

## (옵션) jupyter 설치 

조금 더 편리하게 사용할 수 있는 jupyter도 설치하면 좋습니다.
잘 설치가 안 될 경우 넘어가셔도 무방합니다.

```
$ pip install jupyter
```
## 참고 문서

https://docs.djangoproject.com/en/2.0/intro/install/