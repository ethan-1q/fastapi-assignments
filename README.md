# fastapi-assignments
## 온보딩 실습 과제 2번
https://docs.google.com/document/d/1kWs3wPZjWy9h53Pnnb26254_fKzLMRtCG6P6xBxLNSE/edit

## 세팅
### Python 3.8.6
```
pip install -r requirements.txt
```
### MySQL 8.0
```
$ mysql -u root -p < ./init/init.sql

$ mysql -u root -p
> create user 'fastapi'@'%' identified by 'Fastapi1@';
> grant all privileges on *.* to 'fastapi'@'%';
> flush privileges;
```
### 환경변수
.env에 DB 접속 정보 설정
```
cp .env-template .env
```

## 실행
### 로컬 (Mac)
```
uvicorn app.main:app --reload
```
### Krane (CentOS 7)
venv 세팅 후 sudo
```
sudo uvicorn app.main:app --host 0.0.0.0 --port 80
```

## Docker
### 빌드
```
docker build -t idock.daumkakao.io/ethan.1q/fastapi-assignments-app:latest .
```
### 이미지 확인 및 d2hub 푸시
```
docker images
docker push idock.daumkakao.io/ethan.1q/fastapi-assignments-app:latest
```
### docker-compose
```
docker-compose up -d --build --remove-orphans
docker-compose ps
```

## 애조로
Krane IP 혹은 DKOSv3 ingress IP 도메인 등록
```
ethan-fastapi-assignments.devel.kakao.com
```

## DKOSv3
### Deploy
```
kubectl create secret generic fastapi-assignments-secrets \
    --from-literal=MYSQL_PASSWORD='패스워드' \
    --from-literal=MYSQL2_PASSWORD='패스워드'
kubectl create secret tls fastapi-assignments-ssl --key '인증서키파일' --cert '인증서파일'

source dkosv3.sh

kubectl get deploy,pod,svc,ingress
```

## 테스트
### 로컬 테스트
```
pytest
```

### 2-1. 테스트 URL
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/members?name=테스트  
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/members?name=한  

### 2-2. 테스트 URL
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/members?nick=t  
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/members?nick=tt  
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/members?nick=abcd  

### 2-3. 테스트 URL
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/krew?name=ethan.1q&dbonly=true  
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/krew?name=ethan.1q&dbonly=false  
https://ethan-fastapi-assignments.devel.kakao.com/api/v1/krew?name=ethan.1q&dbonly=true  

## 에러
세팅 도중 connection 관련 에러가 뜨면 프록시 설정을 참고한다.  
https://proxy-guide.dev.daumkakao.io/howto.html
