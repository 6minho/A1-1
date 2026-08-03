# 프롬프트 모음

## 이미지 생성

### Project A 홈 화면 UI 생성

Create a high-fidelity mobile app UI screen design for the home screen of a running crew matching app called 'Project A'. Make it a vertical smartphone screen, full-screen mobile interface filling the entire frame edge-to-edge, like a real screenshot. Style: clean minimal, modern, soft rounded cards, flat UI design, mint green accent color (#2EC4B6). Include a search bar, app header title, a recommended crew card with photo/title/avatars/tag chips/status text/CTA button, and a bottom navigation bar with 4 icons.

## 영상 생성

### VOLT 광고 씬2 냉각 팬 영상 프롬프트

Low angle dramatic reveal, VOLT cooling fan descending into frame, fan blades spinning at high speed, powerful airflow pushing dust away, visible air currents, blue glow expanding outward, red light smoothly fading into cool blue, heat haze disappearing, smoke quickly dispersing, fast rotation, dynamic motion, powerful cooling effect, cinematic, photorealistic

## 자동화

### 날씨 기반 Discord 코멘트 생성 (n8n)

다음 날씨 정보를 받아서 1개 버전의 날씨 코멘트를 한국어로 작성해줘. 답변할 때 날씨 코멘트에 대해서만 답해.

날씨: {{ $json.list[0].weather[0].main }}
강수확률: {{ Math.round($('HTTP Request').item.json.list[0].pop *100)}}%
기온: {{ Math.round($('HTTP Request').item.json.list[0].main.temp )}}°C

