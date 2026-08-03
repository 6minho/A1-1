# main.py
# 나만의 프롬프트 관리 프로그램

# 기본 프롬프트 데이터 (이전 미션에서 작성한 프롬프트 3개)

import json

prompts = [
    {
        "title": "Project A 홈 화면 UI 생성",
        "content": "Create a high-fidelity mobile app UI screen design for the home screen of a running crew matching app called 'Project A'. Make it a vertical smartphone screen, full-screen mobile interface filling the entire frame edge-to-edge, like a real screenshot. Style: clean minimal, modern, soft rounded cards, flat UI design, mint green accent color (#2EC4B6). Include a search bar, app header title, a recommended crew card with photo/title/avatars/tag chips/status text/CTA button, and a bottom navigation bar with 4 icons.",
        "category": "이미지 생성",
        "favorite": False,
        "views" : 0
    },
    {
        "title": "날씨 기반 Discord 코멘트 생성 (n8n)",
        "content": "다음 날씨 정보를 받아서 1개 버전의 날씨 코멘트를 한국어로 작성해줘. 답변할 때 날씨 코멘트에 대해서만 답해.\n\n날씨: {{ $json.list[0].weather[0].main }}\n강수확률: {{ Math.round($('HTTP Request').item.json.list[0].pop *100)}}%\n기온: {{ Math.round($('HTTP Request').item.json.list[0].main.temp )}}°C",
        "category": "자동화",
        "favorite": False,
        "views" : 0
    },
    {
        "title": "VOLT 광고 씬2 냉각 팬 영상 프롬프트",
        "content": "Low angle dramatic reveal, VOLT cooling fan descending into frame, fan blades spinning at high speed, powerful airflow pushing dust away, visible air currents, blue glow expanding outward, red light smoothly fading into cool blue, heat haze disappearing, smoke quickly dispersing, fast rotation, dynamic motion, powerful cooling effect, cinematic, photorealistic",
        "category": "영상 생성",
        "favorite": False,
        "views" : 0
    }
]

CATEGORIES = ["텍스트 생성", "이미지 생성", "영상 생성", "페르소나", "자동화", "기타"]


def input_non_empty(prompt_text):
    while True:
        value = input(prompt_text).strip()
        if value:
            return value
        print("입력값이 비어있습니다. 다시 입력해주세요.")


def choose_category():
    print("\n카테고리 선택:")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")
    print("7) 직접 입력")

    choice = input("선택: ").strip()

    if choice.isdigit() and 1 <= int(choice) <= len(CATEGORIES):
        return CATEGORIES[int(choice) - 1]
    elif choice == "7" or choice == str(len(CATEGORIES) + 1):
        return input_non_empty("카테고리 직접 입력: ")
    else:
        print("잘못된 입력입니다. '기타'로 등록됩니다.")
        return "기타"


def add_prompt():
    print("\n=== 프롬프트 추가 ===")
    title = input_non_empty("제목: ")
    content = input_non_empty("내용: ")
    category = choose_category()

    prompts.append({
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    })

    print(f"\n'{title}' 프롬프트가 추가되었습니다!")

def show_list():
    print("\n=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for i, p in enumerate(prompts, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")

    print(f"\n총 {len(prompts)}개의 프롬프트")


def show_by_category():
    print("\n=== 카테고리별 조회 ===")
    for i, cat in enumerate(CATEGORIES, 1):
        print(f"{i}) {cat}")

    choice = input("선택: ").strip()

    if not choice.isdigit() or not (1 <= int(choice) <= len(CATEGORIES)):
        print("잘못된 입력입니다.")
        return

    selected = CATEGORIES[int(choice) - 1]
    filtered = [p for p in prompts if p["category"] == selected]

    print(f"\n[{selected}] 카테고리 프롬프트:")

    if not filtered:
        print("해당 카테고리에 프롬프트가 없습니다.")
        return

    for i, p in enumerate(filtered, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. {p['title']}{star}")

    print(f"\n총 {len(filtered)}개의 프롬프트") 

def search_prompt():
    print("\n=== 프롬프트 검색 ===")
    keyword = input_non_empty("검색어: ")

    results = [p for p in prompts if keyword in p["title"] or keyword in p["content"]]

    print("\n검색 결과:")

    if not results:
        print("검색 결과가 없습니다.")
        return

    for i, p in enumerate(results, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star}")

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

def show_detail():
    print("\n=== 프롬프트 상세 보기 ===")
    show_list()

    num = input("\n번호 입력: ").strip()

    if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    p["views"] += 1
    star = " ⭐" if p["favorite"] else ""

    print("\n" + "─" * 30)
    print(f"제목: {p['title']}")
    print(f"카테고리: {p['category']}")
    print(f"즐겨찾기: {star if star else '없음'}")
    print(f"조회수: {p['views']}")
    print("─" * 30)
    print("내용:")
    print(p["content"])
    print("─" * 30)

def toggle_favorite():
    print("\n=== 즐겨찾기 관리 ===")
    show_list()

    num = input("\n프롬프트 번호 입력: ").strip()

    if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    p["favorite"] = not p["favorite"]

    if p["favorite"]:
        print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에 추가했습니다!")
    else:
        print(f"\n'{p['title']}' 프롬프트를 즐겨찾기에서 해제했습니다.")

def save_to_json():
    filename = "prompts.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(prompts, f, ensure_ascii=False, indent=2)
    print(f"\n{filename} 파일로 저장되었습니다!")

def load_from_json():
    global prompts
    filename = "prompts.json"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            prompts = json.load(f)
        print(f"\n{filename} 파일을 불러왔습니다! (총 {len(prompts)}개)")
    except FileNotFoundError:
        print(f"\n{filename} 파일을 찾을 수 없습니다.")    

def export_to_markdown():
    filename = "prompts_export.md"

    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 프롬프트 모음\n\n")

        for cat in CATEGORIES:
            cat_prompts = [p for p in prompts if p["category"] == cat]
            if not cat_prompts:
                continue

            f.write(f"## {cat}\n\n")

            for p in cat_prompts:
                star = " ⭐" if p["favorite"] else ""
                f.write(f"### {p['title']}{star}\n\n")
                f.write(f"{p['content']}\n\n")

    print(f"\n{filename} 파일로 내보냈습니다!")

def show_favorites():
    print("\n=== 즐겨찾기 목록 ===")
    favorites = [p for p in prompts if p["favorite"]]

    if not favorites:
        print("즐겨찾기한 프롬프트가 없습니다.")
        return

    for i, p in enumerate(favorites, 1):
        print(f"{i}. [{p['category']}] {p['title']} ⭐")

    print(f"\n총 {len(favorites)}개의 즐겨찾기")

def edit_prompt():
    print("\n=== 프롬프트 수정 ===")
    show_list()

    num = input("\n수정할 프롬프트 번호 입력: ").strip()

    if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]

    print(f"\n현재 제목: {p['title']}")
    new_title = input("새 제목 (변경 없으면 Enter): ").strip()
    if new_title:
        p["title"] = new_title

    print(f"\n현재 내용: {p['content']}")
    new_content = input("새 내용 (변경 없으면 Enter): ").strip()
    if new_content:
        p["content"] = new_content

    print(f"\n현재 카테고리: {p['category']}")
    change_cat = input("카테고리를 변경하시겠습니까? (y/n): ").strip().lower()
    if change_cat == "y":
        p["category"] = choose_category()

    print(f"\n'{p['title']}' 프롬프트가 수정되었습니다!")

def delete_prompt():
    print("\n=== 프롬프트 삭제 ===")
    show_list()

    num = input("\n삭제할 프롬프트 번호 입력: ").strip()

    if not num.isdigit() or not (1 <= int(num) <= len(prompts)):
        print("잘못된 번호입니다.")
        return

    p = prompts[int(num) - 1]
    confirm = input(f"'{p['title']}' 프롬프트를 삭제하시겠습니까? (y/n): ").strip().lower()

    if confirm == "y":
        prompts.pop(int(num) - 1)
        print(f"\n'{p['title']}' 프롬프트가 삭제되었습니다.")
    else:
        print("\n삭제가 취소되었습니다.")

def show_top_viewed():
    print("\n=== 조회수 Top 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    sorted_prompts = sorted(prompts, key=lambda p: p["views"], reverse=True)

    for i, p in enumerate(sorted_prompts, 1):
        star = " ⭐" if p["favorite"] else ""
        print(f"{i}. [{p['category']}] {p['title']}{star} (조회수: {p['views']})")

def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 추가/제거")
    print("7. 즐겨찾기 목록")
    print("8. 데이터 JSON으로 저장")
    print("9. JSON 데이터 불러오기")
    print("10. 카테고리별 Markdown 내보내기")
    print("11. 프롬프트 수정")
    print("12. 프롬프트 삭제")
    print("13. 조회수 Top 목록")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            add_prompt()
        elif choice == "2":
            show_list()
        elif choice == "3":
            show_by_category()
        elif choice == "4":
            search_prompt()
        elif choice == "5":
            show_detail()
        elif choice == "6":
            toggle_favorite()
        elif choice == "7":
            show_favorites()
        elif choice == "8":
            save_to_json()
        elif choice == "9":
            load_from_json()
        elif choice == "10":
            export_to_markdown()
        elif choice == "11":
            edit_prompt()
        elif choice == "12":
            delete_prompt()
        elif choice == "13":
            show_top_viewed()
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()