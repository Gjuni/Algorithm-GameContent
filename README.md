# Algorithm-GameContent
Algorithm & Game Content python Project

## Tools
* VS Code - python3 (Flask), Html, CSS(bootstrap), JS
* git - code upload
* AWS - Release

## Git Rules
1. git issue 템플릿은 "SK 이슈 템플릿"을 사용할 것
2. issue 제목은 [feat], [refac], [document], [fix] + 제목으로 할 것
3. issue 내용은 작업 내용을 적을 것
4. issue 를 파고 branch 생성 이후 본인 작업 진행
5. branch 작업이 끝난 이후 PR 올리기
6. PR에 reviewer는 gjuni와 friedpenguin80 를 반드시 참조 후 comment 이후 Merge 할 것

## Code Convention
1. 함수와 변수명은 반드시 Carmel Case를 사용할 것

## Commit Message Convention
| Tag Name       | Description                                    |
|----------------|------------------------------------------------|
| :sparkles: Feature    | 새로운 기능을 추가                              |
| :bug: Fix          | 버그 수정                                      |
| :hammer:  Refactoring | 프로덕션 코드 리팩토링                         |
| :memo: Docs        | 문서 수정 및 기타 코드 수정 (CICD)                                      |

## File 구조
DDD : Domain Driven Design
: 각 기능 별로 파일을 나눔.

<pre>
<code>
  SK-python-project/
├── README.md
├── requirements.txt
├── .gitignore
├── app.py                   
├── 
├── templates/                # HTML 템플릿 파일들
│   ├── index.html           # 메인 페이지 
│   ├── thread_all.html      # 스레드 목록 페이지 
│   └── user.html            # 사용자 페이지 
├── 
├── static/                   # 정적 파일들
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── script.js
│   └── images/
├── 
├── config/                  
│   ├── __init__.py
│   └── mongodb.py
│   
├── 
├── user/                   
│   ├── __init__.py
│   ├── userController.py
│   ├── userService.py
│   └── userModel.py
</code>  
</pre>

## Server Architecture
<img width="1141" height="571" alt="프로젝트 AWS 아키텍처" src="https://github.com/user-attachments/assets/d541410d-8e22-48c5-a617-b2ef501742b6" />

## API
<pre>
  <code>
API 구현

/user
	/code : 인증 코드 요청 및 메일 전송
	/login : 로그인 로직

/thread
    /<thread_id> : 게시글 상세 조회
	/write : 글 작성 페이지로 라우팅
	/upload : 글 작성
	/all : 글 전체 조회
	/dailySecure : 데일리시큐 RSS
	/secureNews : 보안 뉴스 RSS
	/downloadDaily : 데일리시큐 RSS 엑셀 파일 다운로드
	/downloadSecure : 보안 뉴스 RSS 엑셀 파일 다운로드

  </code>
</pre>

## Cloud URL
[cloudURL](http://43.201.21.61/)


