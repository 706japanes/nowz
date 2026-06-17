import os
import sys
from pathlib import Path

def create_project(title: str):
    """
    입력받은 제목을 기반으로 표준화된 영상 제작 폴더 구조를 생성합니다.
    """
    # 1. 기본 구조 정의 (상대 경로 리스트)
    structure = [
        "CAM/VIDEO",
        "CAM/POP",
        "대본",
        "AUDIO/BGM",
        "AUDIO/FX",
        "AUDIO/VOICE"
    ]

    # 2. 루트 경로 설정 (현재 작업 디렉토리 기준)
    base_path = Path(os.getcwd())
    root_path = base_path / title

    # 중복 확인
    if root_path.exists():
        print(f"❌ 오류: '{title}' 폴더가 이미 존재합니다. 이름을 변경하거나 기존 폴더를 확인해주세요.")
        return

    print(f"🚀 프로젝트 생성 시작: {title}")
    
    try:
        # 루트 폴더 생성
        root_path.mkdir(parents=True, exist_ok=True)
        print(f"✅ 메인 폴더 생성 완료: {root_path}")

        # 하위 폴더들 생성
        for path_str in structure:
            target_path = root_path / path_str
            target_path.mkdir(parents=True, exist_ok=True)
            print(f"  - 생성 완료: {path_str}")

        print(f"\n✅ 모든 구조가 성공적으로 생성되었습니다.")
        print(f"📂 경로: {root_path}")

    except Exception as e:
        print(f"❌ 오류 발생: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("⚠️ 사용법: python create_project_structure.py [프로젝트명]")
        print("예시: python create_project_structure.py 260609_월급_관리의_첫걸음")
    else:
        # 공백이 포함된 제목을 처리하기 위해 인자들을 합침 (예: "260609 월급 관리" -> "260609_월급_관리")
        raw_title = " ".join(sys.argv[1:])
        # 파일 시스템에서 안전하게 사용하기 위해 공백을 언더바(_)로 치환할지 선택 가능하나, 
        # 일단 입력한 그대로를 폴더명으로 생성합니다.
        create_project(raw_title)