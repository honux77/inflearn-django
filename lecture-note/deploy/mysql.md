# 데이터베이스를 mysql로 변경하기
먼저 mysql을 설치합니다. 윈도우, 리눅스, 맥 각자 버전에 맞는 mysql을 설치하면 됩니다.

참고로 실제 서비스에서는 웹 서버와 디비 서버는 반드시 별도의 물리서버로 분리 운영되어야 하고, 디비의 2중화와 백업도 거의 필수적입니다.

## mysql 참고 강좌

초보분들은 유튜브의 '이것이 MySQL이다' 를 보시는 것도 좋습니다.

[유튜브 영상 링크](https://youtu.be/_s7avLLmnUc?list=PLVsNizTWUw7HhYtI-4GGmlJ5yxNdwNI_X)

## mysql 설치 및 초기화

- 다운로드 및 설치
> mac의 경우 설치 중간에 root 패스워드를 알려주는데 잃어버릴 경우 리셋이 매우 어렵습니다. 반드시 저장을 해 놓는 게 좋습니다.
- 루트 사용자 로그인
```
$ mysql -u root -p
```
- 데이터베이스 생성
- 사용자 생성: 아이디 honux 이고 password가 cs1234인 사용자 생성
- 데이터베이스에 권한 부여

```
> create database djangodb character set utf8;
> create user 'honux'@'%' identified by 'cs1234';
> grant all on djangodb.* to 'honux'@'%';
> flush privileges;
```
## mysqlclient 설치
```
pip install mysqlclient
```
## settings.py 수정
```
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/Users/honux/my.cnf',
        },
    }
}
```
## my.cnf 생성 
```
# my.cnf
[client]
database = djangodb
user = honux
password = cs1234
default-character-set = utf8
```
## migration 수행
```
$ python manage.py makemigrations
$ python manage.py migrate
```

## db 확인
```
$ mysql -u honbux -p
> use djangodb
> show tables;
```
## 동작 확인
```
$ python manage.py createsuperuser
```
## 참고 링크
https://docs.djangoproject.com/en/1.10/ref/databases/#mysql-db-api-drivers
