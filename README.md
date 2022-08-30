# 🐢 거뮤니티
![gomunity_og](https://user-images.githubusercontent.com/97969957/185279549-76daa3f9-50dc-4eb7-b412-2f9faec1c2b3.png)  
- 초보 개발자들의 질의응답 커뮤니티 웹  
- 질의응답 및 자료 공유 게시판 사용을 주 목적으로 함  
  
### [☝거뮤니티 배포 링크☝](https://gomunity.shop)

<br>

## 1. 제작 기간 & 참여 인원

제작기간 : 2022년 0708 ~ 0818, 5주
참여인원 : 4명


## 2. 사용 기술

### Backend

<div style="display:flex">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white">
    <img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=Django&logoColor=white">
<div>

> Django는 팀원 전원의 주요 기술 스택입니다.  
> Django Rest Framework를 활용한 RESTful API 구현, Serializer, 커스텀 Validation 구현으로 활용되었습니다.

### Database

<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=PostgreSQL&logoColor=white">

> PostgreSQL은 Django 및 DRF 공식문서에서 사용을 권장하는 데이터베이스 종류입니다.  
> 학습지향인 프로젝트 거뮤니티 특성 및 방향성을 고려하여 공식문서를 참조하여 개발이 가능할 스택으로 선택하였습니다.  
> 또한 차후 거뮤니티에 추가될 기능을 공식문서를 통해 계획하기에 좋다고 판단하여 우선으로 고려되어 사용했습니다.

### Frontend

<div style="display:flex">
    <img src="https://img.shields.io/badge/HTML5-e34f26?style=for-the-badge&logo=HTML5&logoColor=white">
    <img src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=CSS3&logoColor=white">
    <img src="https://img.shields.io/badge/Javascript-F7DF1E?style=for-the-badge&logo=JavaScript&logoColor=white">    
<div>

### Deploy & Tools

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
![gomunity (1)](https://user-images.githubusercontent.com/97969957/187371617-783405eb-9ae5-4375-b042-f5de8c9c145c.png)


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

    - 검색 키워드 Request
    - 
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
  
  
<details>
<summary>ManyToManyField와 related_name</summary>
<div markdown="1">

---

### ✍상황

- 사용자가 질문글과 답글을 작성하면, 다른 사용자는 좋아요를 각각 질문글과 답글에 상호작용할 수 있음
- 그렇기 때문에 질문글과 답글에 각각 좋아요 필드가 필요함
- 사용자-질문글 테이블에 M:M으로 연결되는 `질문글 좋아요 테이블`과 사용자-답글 테이블에 M:M으로 연결되는 `답글 좋아요 테이블`을 각각 생성하고 싶음
- ERD 대로 코드를 작성하고, migrations을 하는 중 하기와 같은 오류코드를 뱉어냈다.

![Untitled](https://user-images.githubusercontent.com/97969957/186821329-a9a492ae-bac0-427b-b33c-39d6e0d5c066.png)

```python
class QnAQuestion(models.Model):
    user = models.ForeignKey(UserModel, verbose_name="질문작성자", on_delete=models.CASCADE)
    title = models.CharField("제목", max_length=100)
    content = models.TextField("질문글")
    like = models.ManyToManyField(UserModel, through="QuestionLike")
    created_at = models.DateTimeField("생성시간", auto_now_add=True)
    updated_at = models.DateTimeField("수정시간", auto_now=True)

    def __str__(self):
        return f"작성된 질문은 {self.title} 입니다"
```

- 작성된 ERD대로 ManyToMany 필드를 작성하려고 하자 오류가 발생하면서 마이그레이션이 실행되지 않았음

### ✍오류코드

![Untitle1d](https://user-images.githubusercontent.com/97969957/186821341-753f6c3c-f7f1-4c8a-aca2-2c48f802b402.png)

### ✍트러블슈팅

[점프 투 파이썬](https://wikidocs.net/71791)

- 구글링을 통해 문제의 내용을 찾아보니 QnAQuestion 모델에서 사용한 user와 like 필드가 모두 UserModel과 연결이 되어있어서 생긴 문제
- `UserModel.qnaquestions_set`처럼 User모델을 통해서 데이터에 접근하려 할때 user를 기준으로 할지, like를 기준으로 해야할지 명확하지 않다는 것이 이유였다

### ✍해결

하나의 모델에서 참조하고 있는 유저모델이 두 개나 있다!

- ERD의 설계 상으로는 문제가 없었으나 물리적으로 모델을 생성할 때 각 필드가 참조하고 있는 모델이 동일하기 때문에 발생한 문제
- 그러나 모델을 생성하는 과정에서 발생한 문제로, 이는 하나의 모델이 **`역참조할 때`** 바라봐야 할 필드가 무엇인지 확실하게 정의해줘야 한다

related_name 메서드로 충돌 피하기

- ManyToMany 필드에 **`related_name을 지정해주는 것`**으로 충돌을 피할 수 있다.(다른 필드에서도 가능하지만, 이름을 굳이 추가적으로 바꿔주지는 않았다)

```jsx
like = models.ManyToManyField(UserModel, related_name='question_like', through="QuestionLike")
```

</div>
</details>
  
  
