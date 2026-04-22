import os
import shutil

# 기본 경로 및 이동할 목적지 경로 설정
base_dir = "./_posts"
target_parent_dir = os.path.join(base_dir, "AI")

def reorganize_folders():
    # 1. _posts 폴더 존재 여부 확인
    if not os.path.exists(base_dir):
        print(f"❌ '{base_dir}' 폴더를 찾을 수 없습니다. 블로그 최상위 경로에서 실행해주세요.")
        return

    # 2. _posts/AI 폴더 생성 (이미 존재하면 건너뜀)
    if not os.path.exists(target_parent_dir):
        os.makedirs(target_parent_dir)
        print(f"📁 '{target_parent_dir}' 폴더를 생성했습니다.")

    # 3. _posts 안의 항목들을 순회하며 폴더 이동 처리
    for item_name in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item_name)

        # 조건: 대상이 '폴더'이고, 새로 만든 'AI' 폴더가 아닌 경우
        if os.path.isdir(item_path) and item_name != "AI":
            target_path = os.path.join(target_parent_dir, item_name)
            
            try:
                # 해당 폴더를 AI 폴더 내부로 이동
                shutil.move(item_path, target_path)
                print(f"✅ 이동 완료: {item_name} -> AI/{item_name}")
            except Exception as e:
                print(f"❌ 이동 실패 ({item_name}): {e}")

if __name__ == "__main__":
    print("🚀 폴더 구조 재배치 자동화를 시작합니다...")
    reorganize_folders()
    print("🎉 모든 폴더 이동 작업이 완료되었습니다!")
