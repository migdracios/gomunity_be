# 📌초보 개발자들의 커뮤니티, 거뮤니티

---

## 프로젝트 소개

![gomunity_og](https://user-images.githubusercontent.com/97969957/185279549-76daa3f9-50dc-4eb7-b412-2f9faec1c2b3.png)

- 거뮤니티는 초보 개발자들이 모여 거리낌없이 질문하고 답변하면서 어려운 점을 해소하기 위한 웹 프로젝트입니다.
- 개발자는 구글링을 통해 자신이 가지고 있는 이슈와 비슷한 케이스를 찾고 트러블 슈팅하게 되지만 초보 개발자는 익숙하지 않아 쉽지 않습니다. 스택오버플로우 또한 마찬가지입니다.
- 따라서 더 나은 개발자가 되기 위한 초석과 같은 커뮤니티가 있어서 성장을 할 수 있는 사이트가 필요할 것 같다는 저희 팀의 경험으로 구상하게 되었습니다.
- 사용자가 될 초보 개발자가 거뮤니티를 통해서 어떤 질문이라도 편하게 질문하고, 답변을 받아 해결하면서 그것을 스스로가 정리해 다음 스텝으로 나아갈 수 있도록 희망합니다.
- 개발 공부를 하면서 알게된 꼭 나와 같은 초보들에게 공유하고 싶은 팁을 게시하는 자료게시판또한 있어 누구나 초보였던 시절에 불편했던 일들을 해결했던 자료를 공유하여 쉽게 찾을 수 있는 레퍼런스가 되기를 희망합니다.

# 📌기술 스택

---

## 서버

<div style="display:flex">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<div>

## 데이터베이스

<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white">

## 프론트엔드

<div style="display:flex">
    <img src="https://img.shields.io/badge/HTML5-e34f26?style=for-the-badge&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
    <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">    
<div>

## 프로젝트관리, 배포

<div style="display:flex">
    <img src="https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=Git&logoColor=white">
    <img src="https://img.shields.io/badge/Sourcetree-0052CC?style=for-the-badge&logo=Sourcetree&logoColor=white">
    <img src="https://img.shields.io/badge/Github-181717?style=for-the-badge&logo=Github&logoColor=white">
    <img src="https://img.shields.io/badge/Visual Studio Code-007ACC?style=for-the-badge&logo=Visual Studio Code&logoColor=white">    
<div>
<div style="display:flex">
    <img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=Docker&logoColor=white">
    <img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white">
    <img src="https://img.shields.io/badge/Amazon S3-569A31?style=for-the-badge&logo=Amazon S3&logoColor=white">
    <img src="https://img.shields.io/badge/Gunicorn-499848?style=for-the-badge&logo=Gunicorn&logoColor=white">
    <img src="https://img.shields.io/badge/NGINX-009639?style=for-the-badge&logo=NGINX&logoColor=white">
<div>

# 📌프로젝트 구조

---

## 프로젝트 아키텍쳐

![image](https://user-images.githubusercontent.com/97969957/185283041-45f4504d-e797-4714-9d7e-058568c20f8d.png)

### 서버

- 서버는 EC2 안에서 nginx,gunicorn/django,postgreSQL이 도커를 통해 이미지로 빌드되어 구축되어 있습니다.
- Lets Encrypt를 사용하여 443포트로 열린 HTTPS 도메인으로 배포되어 있습니다.
- 도메인은 Route 53을 사용하였습니다.

### 프론트엔드

- 프론트엔드는 S3를 통해 정적배포 되었습니다.
- AWS CloudFront으로 AWS SSL 인증서가 적용된 HTTPS 도메인으로 배포되어 있습니다.
- 도메인은 Gabia를 사용하였습니다.

# 버전 별 SA

---

## [ver.1.0]()

## [ver.1.1]()

## [ver.1.2]()

## [ver.1.2.1]()

## [ver.1.3]()

## [ver.1.4]()

# 이슈리포트

# 🐢 거뮤니티

초보 개발자들의 질의응답 커뮤니티 웹

[거뮤니티 링크](https://gomunity.shop)

## 1. 제작 기간 & 참여 인원

제작기간 : 2022년 0708 ~ 0812

참여인원

1. 황영상 : [✍블로그링크](https://velog.io/@migdracios)
2. 김태인 : [✍블로그링크](https://velog.io/@migdracios)
3. 김희정 : [✍블로그링크](https://velog.io/@migdracios)
4. 한건희 : [✍블로그링크](https://velog.io/@migdracios)

## 2. 사용 기술

### Backend

아이콘

### Frontend

아이콘

## 3. ERD

![Gomunity](https://user-images.githubusercontent.com/97969957/185282933-80713a8e-cdf6-47c4-ba20-ef985fddf0d0.png)

## 4. 핵심 기능

- 거뮤니티는 DRF의 CBV를 활용한 게시판 CRUD 구현이 핵심인 프로젝트입니다.
- 거뮤니티는 마크다운 에디터를 적용하여 질의응답하고, 자료를 공유하며 조회하는 것을 핵심으로 동작하고 있는 웹 서비스입니다. 또한 해시태그를 사용한 유사도 시스템이 적용되어 있어 유사한 질문글을 사용자에게 추천합니다.

<details>
<summary>질의응답 게시판</summary>
<div markdown="1">

1. 질문글 조회
        
    사용자는 로그인 없이 질문글을 조회할 수 있습니다.

    1. 질문글 목록 조회 [📜코드링크]()
        - 사용자는 질문글의 목록 조회할 수 있습니다.
        - 작성된 게시글의 제목, 작성자, 좋아요수, 댓글수 데이터를 시리얼라이저를 통해 클라이언트에 전달합니다.
    2. 질문글 상세 조회 [📜코드링크]()
        - 사용자는 질문글과 관련된 상세 내용을 조회할 수 있습니다.
        - 작성된 게시글의 제목, 작성자, 작성일, 좋아요수, 댓글 목록, 내용 등을 시리얼라이저를 통해 클라이언트에 전달합니다.
2. 질문글 작성 [📜코드링크]()
    - 사용자는 질문글 작성페이지에서 입력한 데이터를 데이터베이스 레코드로 저장할 수 있습니다.
    - 게시글 작성에 성공하면 성공 메시지를 클라이언트에 전달합니다.
    - 게시글 작성에 실패하면 오류 내용을 메시지로 클라이언트에 전달합니다.
3. 질문글 수정 [📜코드링크]()
    - 사용자는 작성된 질문글을 작성한 사용자로 제한하여 수정할 수 있습니다.
    - 사용자는 작성페이지를 통해서 기존 작성된 내용을 바탕으로 데이터를 수정하여 데이터베이스 레코드를 저장합니다.
4. 질문글 삭제 [📜코드링크]()
    - 사용자는 작성된 질문글을 작성한 사용자로 제한하여 삭제할 수 있습니다.
    - 사용자는 질문글 상세 페이지에서 삭제버튼을 통하여 데이터베이스의 작성글 레코드를 삭제합니다.
5. 질문글 검색 [📜코드링크]()
    - 사용자는 내용을 검색하여 일치하는 데이터 만을 조회할 수 있습니다.
    - DRF 제네릭뷰 서치필터를 사용하여 제목, 작성자, 내용 데이터와 일치하는 레코드를 클라이언트에 전달합니다.

</div>
</details>

<details>
<summary>자료 게시판</summary>
<div markdown="1">

1. 자료 조회 
    1. 자료 목록 조회 [📜코드링크]()
        - 사용자는 자료글의 목록을 조회할 수 있습니다.
        - 작성된 게시글의 제목, 작성자, 좋아요수 데이터를 시리얼라이저를 통해 클라이언트에 전달합니다.
    2. 자료 상세 조회 [📜코드링크]()
        - 사용자는 자료글의 상세 내용을 조회할 수 있습니다.
        - 작성된 게시글의 제목, 작성자, 좋아요수, 댓글, 내용 데이터를 시리얼라이저를 통해 클라이언트에 전달합니다.
2. 자료 작성 [📜코드링크]()
    - 사용자는 자료 작성페이지에서 입력한 데이터를 데이터베이스 레코드로 저장할 수 있습니다.
    - 게시글 작성에 성공하면 성공 메시지를 클라이언트에 전달합니다.
    - 게시글 작성에 실패하면 오류 내용을 메시지로 클라이언트에 전달합니다.
3. 자료 수정 [📜코드링크]()
    - 사용자는 작성된 자료글을 작성한 사용자로 제한하여 수정할 수 있습니다.
    - 사용자는 작성페이지를 통해서 기존 작성된 내용을 바탕으로 데이터를 수정하여 데이터베이스 레코드를 저장합니다.
4. 자료 삭제 [📜코드링크]()
    - 사용자는 작성된 자료글을 작성한 사용자로 제한하여 삭제할 수 있습니다.
    - 사용자는 자료글 상세 페이지에서 삭제버튼을 통하여 데이터베이스의 작성글 레코드를 삭제합니다.
    
</div>
</details>

<details>
<summary>유사 게시글 추천 시스템</summary>
<div markdown="1">



</div>
</details>
    
    

## 5. 핵심 트러블 슈팅

1. 핵심 트러블 슈팅 제목 [이슈 링크]()
    - 내용
    - 접근법
    - 해결
