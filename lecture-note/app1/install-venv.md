# virtualenv 설치하기

프로젝트마다 다른  파이썬 환경을 사용할 수 있게 해 주는 툴입니다.

어려우신 분들은 건너뛰셔도 됩니다.

(주의!) 강의에서는 powershell을 사용하는데 cmd창을 사용하는 게 더 좋습니다. 

## 설치
```
pip install --upgrade pip
pip install virtualenv
```

## 새로운 환경 만들기 및 활성화
```
virtualenv myenv
myenv\Scripts\activate.bat
```

## myenv에서 패키지 설치  
```
pip install 패키지이름
pip freeze > requirement.txt
``` 

## myenv 비활성화
```
myenv/Scripts/deactivate.bat
```