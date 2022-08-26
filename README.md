# 🐢 거뮤니티
![gomunity_og](https://user-images.githubusercontent.com/97969957/185279549-76daa3f9-50dc-4eb7-b412-2f9faec1c2b3.png)  
- 초보 개발자들의 질의응답 커뮤니티 웹  
- 질의응답 및 자료 공유 게시판 사용을 주 목적으로 함  
  
### [☝거뮤니티 배포 링크](https://gomunity.shop)

## 1. 제작 기간 & 참여 인원

제작기간 : 2022년 0708 ~ 0818, 5주
참여인원 : 4명

## 2. 사용 기술

### Backend

<div style="display:flex">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<div>

### Database

<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white">

### Frontend

<div style="display:flex">
    <img src="https://img.shields.io/badge/HTML5-e34f26?style=for-the-badge&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
    <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">    
<div>

### Deploy

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

## 3. ERD

![Gomunity](https://user-images.githubusercontent.com/97969957/185282933-80713a8e-cdf6-47c4-ba20-ef985fddf0d0.png)
    
## 4. AWS 아키텍쳐

![image](https://user-images.githubusercontent.com/97969957/185283041-45f4504d-e797-4714-9d7e-058568c20f8d.png)

## 5. API 개발 명세
### [🚩 POSTMAN API 명세 Documnetation](https://documenter.getpostman.com/view/19965228/UzQpwndu)

## 6. 핵심 기능

- 거뮤니티는 DRF Serializer를 활용한 게시판 CRUD 구현 및 배포를 핵심 목표로 삼고 개발한 프로젝트입니다.
- DRF Simple JWT를 활용하여 로그인 기능이 구현되어 있습니다.
- 거뮤니티는 마크다운 에디터를 적용하여 질의응답하고, 자료를 공유하며 조회하는 것을 핵심으로 동작하고 있는 웹 서비스입니다. 
- 해시태그를 사용한 유사도 시스템이 적용되어 있어 유사한 질문글을 사용자에게 추천합니다.

<details>
<summary>질의응답 게시판</summary>
<div markdown="1">

### 1. 질문글 조회
        
사용자가 로그인 없이도 게시글을 조회할 수 있도록 Access Token 없이 GET 요청함
  
  **질문글 목록 조회** [🔥code](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/qna/views.py#L134-L138)
  
      - 질문글 Serializer를 사용하여, 작성된 게시글의 제목, 작성자, 좋아요수, 댓글수 데이터를 Return

  **질문글 상세 조회** [🔥code](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/qna/views.py#L38-L41)  
  
      - 질문글 Serializer를 사용하여, 작성된 게시글의 제목, 작성자, 작성일, 좋아요수, 댓글 목록, 내용 데이터를 Return
        
### 2. 질문글 작성 

**질문글 작성** [🔥code](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/qna/views.py#L43-L57)

    - 작성자, 제목, 해시태그, 내용, 썸네일 이미지를 Request
    - Serializer is_valid() 통과 후 save()메서드로 레코드 저장
    - 섬네일 이미지의 이름을 변경 후, boto3의 s3.upload_file() 메서드를 통하여 username/imagename 형태로 S3 저장
    - 200,400 status_code 및 메시지 리턴
  
### 3. 질문글 수정 

**질문글 수정** [🔥code](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/qna/views.py#L59-L74)

    - URL로 게시글 PK 요구
    - 작성자, 제목, 해시태그, 내용, 썸네일 이미지 중 일부를 Request
    - Serializer is_valid() 및 Partial 메서드를 사용하여 데이터 검증 이후 save()메서드로 업데이트
    - 섬네일 이미지의 이름을 변경 후, boto3의 s3.upload_file() 메서드를 통하여 username/imagename 형태로 S3 저장
    - 200,400 status_code 및 메시지 리턴
    
### 4. 질문글 삭제 

**질문글 삭제** [🔥code](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/qna/views.py#L76-L80)

    - URL로 게시글 PK 요구
    - 작성자 Request
    - 게시글의 레코드를 삭제, 200,400 status_code 및 메시지 리턴
    
### 5. 질문글 검색 

**질문글 검색** [🔥code](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/qna/views.py#L141-L145)

    - 사용자는 내용을 검색하여 일치하는 데이터 만을 조회할 수 있습니다.
    - DRF 제네릭뷰 서치필터를 사용하여 제목, 작성자, 내용 데이터와 일치하는 레코드를 클라이언트에 전달합니다.

</div>
</details>

<details>
<summary>자료 게시판</summary>
<div markdown="1">

1. 자료 조회 
    1. 자료 목록 조회 [📜코드링크](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/archive/views.py#L108-L111)
        - 사용자는 자료글의 목록을 조회할 수 있습니다.
        - 작성된 게시글의 제목, 작성자, 좋아요수 데이터를 시리얼라이저를 통해 클라이언트에 전달합니다.
    2. 자료 상세 조회 [📜코드링크](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/archive/views.py#L20-L23)
        - 사용자는 자료글의 상세 내용을 조회할 수 있습니다.
        - 작성된 게시글의 제목, 작성자, 좋아요수, 댓글, 내용 데이터를 시리얼라이저를 통해 클라이언트에 전달합니다.
2. 자료 작성 [📜코드링크](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/archive/views.py#L25-L32)
    - 사용자는 자료 작성페이지에서 입력한 데이터를 데이터베이스 레코드로 저장할 수 있습니다.
    - 게시글 작성에 성공하면 성공 메시지를 클라이언트에 전달합니다.
    - 게시글 작성에 실패하면 오류 내용을 메시지로 클라이언트에 전달합니다.
3. 자료 수정 [📜코드링크](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/archive/views.py#L34-L42)
    - 사용자는 작성된 자료글을 작성한 사용자로 제한하여 수정할 수 있습니다.
    - 사용자는 작성페이지를 통해서 기존 작성된 내용을 바탕으로 데이터를 수정하여 데이터베이스 레코드를 저장합니다.
4. 자료 삭제 [📜코드링크](https://github.com/migdracios/gomunity_be/blob/cdd28297e5ca5c2b9d1293067ae67069c192678c/archive/views.py#L44-L48)
    - 사용자는 작성된 자료글을 작성한 사용자로 제한하여 삭제할 수 있습니다.
    - 사용자는 자료글 상세 페이지에서 삭제버튼을 통하여 데이터베이스의 작성글 레코드를 삭제합니다.
    
</div>
</details>

<details>
<summary>유사 게시글 추천 시스템</summary>
<div markdown="1">



</div>
</details>
    
    

## 7. 핵심 트러블 슈팅

1. 핵심 트러블 슈팅 제목 [이슈 링크]()
    - 내용
    - 접근법
    - 해결
