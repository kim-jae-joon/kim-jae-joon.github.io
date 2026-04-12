import os
import google.generativeai as genai
from github import Github, Auth

# 깃허브 액션 환경 변수(Secrets)에서 불러오기
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")
GITHUB_REPO = "kim-jae-joon/kim-jae-joon.github.io"

if not GEMINI_API_KEY:
    print("❌ GEMINI_API_KEY가 등록되지 않았습니다!")
    exit(1)

# 제미나이 AI 속도/성능 최적화 모델 (Flash) 환경 설정
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

g = Github(auth=Auth.Token(GITHUB_TOKEN))
repo = g.get_repo(GITHUB_REPO)

print("🔎 블로그에 새로 달린 댓글이 있는지 1시간 단위 클라우드 스캔 중입니다...")
issues = repo.get_issues(state='open')
reply_count = 0

for issue in issues:
    comments = list(issue.get_comments())
    if comments:
        last_comment = comments[-1]
        
        # 무한 반복 방지 (AI가 작성한 답변이 아닌 독자의 순수 질문일 경우에만)
        if "🤖 **AI 비서의 답변입니다:**" not in last_comment.body:
            user_comment = last_comment.body
            print(f"\n💡 새로운 댓글 발견: {user_comment}")
            
            prompt = f"""
[역할 부여]
당신은 대한민국 최고의 {GITHUB_REPO} IT 코딩 블로그를 관리하는 '친절한 AI 매니저'입니다.
방문자가 아래와 같은 질문이나 댓글을 남겼습니다. 이 내용에 대해 환영 인사와 함께, 코딩 초보자도 이해하기 쉽게 다정하고 전문적인 답글을 작성해 주세요.

[❗ 절대 준수 규칙 ❗]
1. 언어 통제: 100% 완전하고 자연스러운 '한국어'만 사용하세요. 외국어(중국어, 한자 등)가 섞이면 절대 안 됩니다.
2. 매력적인 어투: "~했어요!", "~해 드릴게요 😊" 와 같이 매우 친절하고 다정한 블로그 선생님 말투를 사용하고 적절한 이모지를 넣어주세요.

방문자 댓글: "{user_comment}"
"""
            try:
                # 제미나이 AI 호출 (빠르고 정확함)
                response = model.generate_content(prompt)
                raw_reply = response.text.strip()
                
                reply_text = f"🤖 **AI 비서의 답변입니다:** \n\n{raw_reply}"
                
                # 깃허브 이슈 댓글로 등록
                issue.create_comment(reply_text)
                reply_count += 1
                print("✅ 제미나이가 작성한 답글 달기 성공!")
            except Exception as e:
                print(f"❌ 오류 발생: {e}")

if reply_count == 0:
    print("\n💤 새로운 댓글이 없어 종료합니다.")
else:
    print(f"\n🎉 총 {reply_count}개의 새로운 댓글에 답변을 완료했습니다.")
