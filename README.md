# 나만의 프롬프트 관리 프로그램

Python 콘솔 기반 프롬프트 저장·검색 프로그램입니다.
GenAI 미션들에서 작성했던 프롬프트를 카테고리별로 관리하고, 검색·즐겨찾기·조회수 기록까지 지원합니다.

## 저장소

https://github.com/6minho/A1-1

---

## 실행 방법

```bash
python main.py
```

Python 3.10 이상이 필요합니다. (개발 환경: Python 3.14.6)

---

## 기능 목록

### 필수 기능
- 프롬프트 추가
- 프롬프트 목록 보기
- 카테고리별 조회
- 프롬프트 검색 (제목/내용)
- 프롬프트 상세 보기
- 즐겨찾기 추가/제거
- 즐겨찾기 목록 보기

### 보너스 1 — 영속화 및 내보내기
- 프롬프트 데이터를 JSON 파일로 저장 (`prompts.json`)
- JSON 파일 불러오기
- 카테고리별 Markdown 파일 내보내기 (`prompts_export.md`)

### 보너스 2 — CRUD 및 사용 기록
- 프롬프트 수정
- 프롬프트 삭제
- 상세 보기 시 조회수 자동 기록
- 조회수 기준 Top 목록 정렬

---

## 등록된 프롬프트 카테고리

텍스트 생성, 이미지 생성, 영상 생성, 페르소나, 자동화, 기타

기본 데이터로 등록된 3개 프롬프트는 이전 미션에서 실제로 작성했던 프롬프트입니다.

| 제목 | 카테고리 | 출처 |
|---|---|---|
| Project A 홈 화면 UI 생성 | 이미지 생성 | 캡스톤 디자인 프로젝트 (GPT Image 2) |
| 날씨 기반 Discord 코멘트 생성 (n8n) | 자동화 | n8n 자동화 워크플로우 과제 |
| VOLT 광고 씬2 냉각 팬 영상 프롬프트 | 영상 생성 | AI 광고 영상 제작 프로젝트 |

---

## 코드 구조

모든 기능은 함수 단위로 분리되어 있습니다.

```
main.py
├── input_non_empty()      # 빈 값 검증 공통 함수
├── choose_category()      # 카테고리 선택
├── add_prompt()           # 프롬프트 추가
├── show_list()            # 목록 조회
├── show_by_category()     # 카테고리별 조회
├── search_prompt()        # 검색
├── show_detail()          # 상세 보기 (조회수 기록 포함)
├── toggle_favorite()      # 즐겨찾기 추가/제거
├── show_favorites()       # 즐겨찾기 목록
├── save_to_json()         # JSON 저장 (보너스1)
├── load_from_json()       # JSON 불러오기 (보너스1)
├── export_to_markdown()   # Markdown 내보내기 (보너스1)
├── edit_prompt()          # 프롬프트 수정 (보너스2)
├── delete_prompt()        # 프롬프트 삭제 (보너스2)
├── show_top_viewed()      # 조회수 Top 정렬 (보너스2)
├── show_menu()            # 메뉴 출력
└── main()                 # 메인 루프
```

### 자료구조 선택 이유

프롬프트 데이터는 `list[dict]` 구조로 저장합니다.

- **list**: 프롬프트는 등록 순서를 유지하며 번호로 접근해야 하므로(메뉴에서 "번호 입력" 방식 사용), 순서가 보장되고 인덱스 접근이 O(1)인 리스트가 적합합니다.
- **dict**: 각 프롬프트는 제목·내용·카테고리·즐겨찾기·조회수처럼 이름이 있는 여러 속성을 가지므로, 키-값 구조인 딕셔너리가 필드 접근(`p["title"]`)을 명확하게 해줍니다.
- 대안으로 클래스(`class Prompt`) 사용도 고려했으나, 이 프로젝트 규모에서는 `json.dump`로 바로 직렬화 가능한 dict가 JSON 저장/불러오기 기능(보너스1)과 궁합이 더 좋아 dict를 선택했습니다.

---

## 정책 및 예외 처리

- **동명 프롬프트 처리**: 제목 중복 검사를 별도로 하지 않습니다. 같은 제목의 프롬프트가 여러 개 등록되어도 각 항목은 리스트 내 위치(번호)로 구분되므로 동작에는 문제가 없습니다. 다만 사용자가 제목만으로 구분하기 어려울 수 있어, 상세 보기(5번)에서 번호와 카테고리를 함께 표시해 구분을 돕습니다.
- **카테고리 직접 입력**: 카테고리 선택 시 7번(직접 입력)을 고르면 자유 텍스트로 새 카테고리를 만들 수 있습니다. 기존 6개 카테고리와 다른 이름을 입력해도 별도 경고 없이 등록되며, 이렇게 생성된 카테고리는 "카테고리별 조회" 메뉴의 고정 목록(1~6번)에는 나타나지 않고 "프롬프트 목록"에서만 확인 가능합니다. 잘못된 번호를 입력하면 자동으로 "기타" 카테고리로 등록됩니다.
- **삭제 시 확인 절차**: 삭제는 되돌릴 수 없는 작업이므로 `y/n` 확인 절차를 거친 뒤에만 실제로 삭제합니다.

---

## 개발 환경

| 항목 | 버전 |
|---|---|
| Python | 3.14.6 |
| Git | 2.55.0 |
| 에디터 | VSCode + Python Extension |

![VSCode Python 확장 설치](screenshots/01_env_vscode_python.png)

Git 설정은 공용 PC 사용을 고려해 `--local` 스코프로 지정했습니다. `--global`이 아닌 프로젝트 폴더 안(`.git/config`)에만 사용자 정보가 저장되어, 다른 사용자에게 영향을 주지 않습니다.

```
PS C:\Users\DiCiA\Desktop\prompt-manager> python --version
Python 3.14.6
PS C:\Users\DiCiA\Desktop\prompt-manager> git --version
git version 2.55.0.windows.3
PS C:\Users\DiCiA\Desktop\prompt-manager> git config --local --list --show-origin
file:.git/config    core.repositoryformatversion=0
file:.git/config    core.filemode=false
file:.git/config    core.bare=false
file:.git/config    core.logallrefupdates=true
file:.git/config    core.symlinks=false
file:.git/config    core.ignorecase=true
file:.git/config    user.name=육민호
file:.git/config    user.email=alsgh3920@gmail.com
```

![Python/Git 버전 및 Git 설정](screenshots/02_env_version_gitconfig.png)

---

## 실행 화면

### 메뉴
![메뉴](screenshots/03_menu.png)

### 프롬프트 추가
![프롬프트 추가](screenshots/04_add_prompt.png)

### 프롬프트 목록
![프롬프트 목록](screenshots/05_list.png)

### 카테고리별 조회
![카테고리별 조회](screenshots/06_category.png)

### 프롬프트 검색
![프롬프트 검색](screenshots/07_search.png)

### 프롬프트 상세 보기 (조회수 기록)
![프롬프트 상세 보기](screenshots/08_detail.png)

### 즐겨찾기 추가
![즐겨찾기 추가](screenshots/09_favorite_add.png)

### 즐겨찾기 해제
![즐겨찾기 해제](screenshots/10_favorite_delete.png)

### 즐겨찾기 목록
![즐겨찾기 목록](screenshots/11_favorite_list.png)

### JSON 저장 (보너스1)
![JSON 저장](screenshots/12_json_save.png)

### 저장된 JSON 파일 내용
![JSON 파일 내용](screenshots/13_json_file.png)

### Markdown 내보내기 실행 결과 (보너스1)
![Markdown 내보내기 실행](screenshots/14_markdown_export_output.png)

### 내보내진 Markdown 파일 내용
![Markdown 파일 내용](screenshots/15_markdown_export_file.png)

---

## Git 명령어 사용 기록

필수로 요구된 8개 명령어(`init, add, commit, push, pull, checkout, clone, merge`)를 모두 사용했습니다.

### git clone 실행 로그

> `octocat/Hello-World` 공개 저장소를 별도 폴더에 클론하여 구조와 로그를 확인한 뒤 삭제했습니다.

```
C:\Users\DiCiA\Desktop>cd C:\Users\DiCiA\Desktop\prompt-manager

C:\Users\DiCiA\Desktop\prompt-manager>git clone https://github.com/octocat/Hello-World.git
Cloning into 'Hello-World'...
remote: Enumerating objects: 13, done.
remote: Total 13 (delta 0), reused 0 (delta 0), pack-reused 13 (from 1)
Receiving objects: 100% (13/13), done.

C:\Users\DiCiA\Desktop\prompt-manager>
```

> 클론 후 구조와 로그를 확인한 뒤 `Hello-World` 폴더는 삭제했습니다.

### git log --oneline --graph

`feature/list` 브랜치를 생성해 프롬프트 목록 조회 기능을 작업한 뒤 `main`에 병합했고(`checkout`, `merge`), 기능 단위로 커밋을 분리했습니다.

```
*   69395f1 (HEAD -> main, origin/main, origin/HEAD) Fix formatting in registered prompt categories
*   01b7f9c feat: 조회수 기준 Top 목록 정렬 기능 구현
*   d468bc0 feat: 프롬프트 조회수 기록 기능 구현
*   9383f0e docs: 즐겨찾기 메뉴 문구 수정
*   0bc5a6d feat: 프롬프트 삭제 기능 구현
*   07664d4 feat: 프롬프트 수정 기능 구현
*   542c23e feat: 카테고리별 Markdown 내보내기 기능 구현
*   f07615a feat: 프롬프트 JSON 불러오기 기능 구현
*   e99a434 feat: 프롬프트 JSON 저장 기능 구현
*   0f7fd30 docs: README 작성
*   1933061 feat: 즐겨찾기 목록 조회 기능 구현
*   f478c76 feat: 즐겨찾기 관리 기능 구현
*   f2949ec feat: 프롬프트 상세 보기 기능 구현
*   ba48811 feat: 프롬프트 검색 기능 구현
*   45cbf15 feat: 카테고리별 조회 기능 구현
*   5fe32ed feat: 프롬프트 목록 조회 기능 구현
*   ace42fc feat: 프롬프트 추가 기능 구현
* eb4c9fd (feature/list) feat: 프롬프트 목록 조회 기능 구현
|/
*   b734891 feat: 기본 프롬프트 데이터 및 메뉴 뼈대 구현
*   44c8d76 chore: 프로젝트 초기 설정 및 .gitignore 추가
```

![git log graph](screenshots/16_git_log.png)

---

## 개발 과정 메모

- `add_prompt()`와 `show_list()`를 커밋 하나에 같이 넣는 실수가 있었고, `git rebase -i`로 커밋을 두 개로 분리해 기능 단위 커밋 원칙을 지켰습니다.
- Git 사용자 정보는 공용 PC 환경을 고려해 `--global` 대신 `--local`로 설정해, 다른 사용자의 Git 환경에 영향을 주지 않도록 했습니다.
- `clone`은 별도 폴더에서 공개 저장소(`octocat/Hello-World`)를 내려받아 확인 후 삭제하는 방식으로 사용 기록을 남겼습니다.
- `pull`은 GitHub 웹에서 README를 직접 수정한 뒤 로컬에서 받아오는 방식으로 사용 기록을 남겼습니다.
