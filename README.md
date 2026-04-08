app/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 앱의 루트  
├── core/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 설정 파일 같은 것들 모아놓은 곳  
│&emsp;&emsp;&emsp;└── config.py&emsp;&emsp;&emsp;&emsp;&emsp;# 기본 설정 파일  
├── data/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 앱에서 사용할 데이터 클래스들  
│&emsp;&emsp;&emsp;└── user.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 유저 클래스  
├── router/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 라우터들 모아놓은 곳  
│&emsp;&emsp;&emsp;└── user_router.py&emsp;&emsp;&emsp;# 유저 관련된 라우터  
├── schema/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# DTO라고 보면 됨  
│&emsp;&emsp;&emsp;└── user_schema.py&emsp;&emsp;# User관련된 DTO들  
├── static/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 정적 파일들 모아놓은 곳  
│&emsp;&emsp;&emsp;└── css/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# css 파일들 모아놓은 곳  
│&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;└── style.css&emsp;&emsp;# 공통 스타일 시트  
├── template/&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 템플릿 파일들 모아 놓은 곳  
│&emsp;&emsp;&emsp;├── base.html&emsp;&emsp;&emsp;&emsp;# 공통 템플릿 파일  
│&emsp;&emsp;&emsp;├── index.html&emsp;&emsp;&emsp;&emsp;# 앱 초기 화면  
│&emsp;&emsp;&emsp;└── users.html&emsp;&emsp;&emsp;&emsp;# user목록 화면  
├── main.py&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 앱을 실행하는 파일  
├── .gitignore&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 버전관리를 하지 않을 파일들을 명시해 두는 곳  
└── pyproject.toml&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;# 패키지 관리하는 파일  


```bash
$env:PYTHONPATH = "app"
```

```bash
uvicorn app.main:app --reload
```
