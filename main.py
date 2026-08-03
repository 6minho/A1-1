# main.py
# 나만의 프롬프트 관리 프로그램

# 기본 프롬프트 데이터 (이전 미션에서 작성한 프롬프트 3개)
prompts = [
    {
        "title": "Project A 홈 화면 UI 생성",
        "content": "Create a high-fidelity mobile app UI screen design for the home screen of a running crew matching app called 'Project A'. Make it a vertical smartphone screen, full-screen mobile interface filling the entire frame edge-to-edge, like a real screenshot. Style: clean minimal, modern, soft rounded cards, flat UI design, mint green accent color (#2EC4B6). Include a search bar, app header title, a recommended crew card with photo/title/avatars/tag chips/status text/CTA button, and a bottom navigation bar with 4 icons.",
        "category": "이미지 생성",
        "favorite": False
    },
    {
        "title": "날씨 기반 Discord 코멘트 생성 (n8n)",
        "content": "다음 날씨 정보를 받아서 1개 버전의 날씨 코멘트를 한국어로 작성해줘. 답변할 때 날씨 코멘트에 대해서만 답해.\n\n날씨: {{ $json.list[0].weather[0].main }}\n강수확률: {{ Math.round($('HTTP Request').item.json.list[0].pop *100)}}%\n기온: {{ Math.round($('HTTP Request').item.json.list[0].main.temp )}}°C",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "VOLT 광고 씬2 냉각 팬 영상 프롬프트",
        "content": "Low angle dramatic reveal, VOLT cooling fan descending into frame, fan blades spinning at high speed, powerful airflow pushing dust away, visible air currents, blue glow expanding outward, red light smoothly fading into cool blue, heat haze disappearing, smoke quickly dispersing, fast rotation, dynamic motion, powerful cooling effect, cinematic, photorealistic",
        "category": "영상 생성",
        "favorite": False
    }
]


def show_menu():
    print("\n=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


def main():
    while True:
        show_menu()
        choice = input("선택: ").strip()

        if choice == "1":
            print("(다음 단계에서 구현 예정)")
        elif choice == "2":
            print("(다음 단계에서 구현 예정)")
        elif choice == "3":
            print("(다음 단계에서 구현 예정)")
        elif choice == "4":
            print("(다음 단계에서 구현 예정)")
        elif choice == "5":
            print("(다음 단계에서 구현 예정)")
        elif choice == "6":
            print("(다음 단계에서 구현 예정)")
        elif choice == "7":
            print("(다음 단계에서 구현 예정)")
        elif choice == "0":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 입력입니다. 다시 선택해주세요.")


if __name__ == "__main__":
    main()