import os
import sys

arg = sys.argv
original = os.path.basename(arg[1])
filename, ext = os.path.splitext(original)

gomi_name = [
    "重要",
    "無題",
    "未完成",
    "作業中",
    "社外秘",
    "要確認",
    "優先度高",
    "削除厳禁",
    "絶対消すな",
    "変更禁止",
    "上書き保存禁止",
    "社外持ち出し厳禁",
    "YYYYMMDD",
    "問い合わせ中",
    "未記入アリ",
    "没",
    "仮",
    "確定",
    "最新版",
    "最終版",
    "最終確認版",
    "確認終了版",
    "最終確認終了版",
    "修正版",
    "修正版の修正版",
    "訂正版",
    "修正済",
    "訂正済",
    "調整済",
    "反映済",
    "完成",
    "最終ver",
    "原本",
    "コピー",
    "バックアップ",
    "A案",
    "Final",
    "Final-Final",
    "Fix",
    "Copy",
    "Backup",
    "ver1",
]

def yes_no_input():
    while True:
        choice = input("リネームしますか？ [y/N]: ").lower()
        if choice in ["y", "yes"]:
            return True
        elif choice in ["n", "no"]:
            return False

def checker():
    gomi_list = []
    for gomi in gomi_name:
        if gomi in filename:
            gomi_list.append(gomi)
        else:
            pass
    return gomi_list

def main():
    print("チェックしています...")
    gomi_list = checker()
    if len(gomi_list) == 0:
        print("ゴミファイル名ではありません。")
    else:
        print("ゴミファイル名です。")
        result = yes_no_input()
        if result == True:
            for gomi in gomi_list:
                filename = filename.replace(gomi, '')
            os.rename(original, filename)
            print("リネームしました。")
        elif result == False:
            print("キャンセルしました。")
    sys.exit()

if __name__ == "__main__":
    main()
