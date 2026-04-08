app                        // 앱의 루트
 |-- core                  // 설정 파일 같은 것들 모아놓은 곳
     |-- config.py         // 기본 설정 파일
 |-- data                  // 앱에서 사용할 데이터 클래스들
     |-- user.py           // 유저 클래스
 |-- router                // 라우터들 모아놓은 곳
     |-- user_router.py    // 유저 관련된 라우터
 |-- schema                // DTO라고 보면 됨
     |-- user_schema.py    // User관련된 DTO들
 |-- static                // 정적 파일들 모아놓은 곳
       |-- css             // css 파일들 모아놓은 곳
             |-- style.css // 공통 스타일 시트
 |-- template              // 템플릿 파일들 모아 놓은 곳
       |-- base.html       // 공통 템플릿 파일
       |-- index.html      // 앱 초기 화면
       |-- users.html      // user목록 화면
 |-- main.py               // 앱을 실행하는 파일
 |-- .gitignore            // 버전관리를 하지 않을 파일들을 명시해 두는 곳
 |-- pyproject.toml        // 패키지 관리하는 파일
