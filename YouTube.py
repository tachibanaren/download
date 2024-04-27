import tkinter as tk
from tkinter import messagebox
from pytube import YouTube

def download_video():
    # ユーザーが入力したYouTubeのURLを取得
    url = url_entry.get()

    try:
        # YouTubeオブジェクトを作成
        video = YouTube(url)

        # 最高品質のmp4形式を選択してダウンロード
        stream = video.streams.get_highest_resolution()
        if stream:
            # ダウンロード実行
            stream.download()
            messagebox.showinfo("成功", "動画のダウンロードが完了しました。")
        else:
            messagebox.showerror("エラー", "適切な動画ストリームが見つかりませんでした。")
    except Exception as e:
        messagebox.showerror("エラー", f"ダウンロード中にエラーが発生しました:\n{e}")

# tkinterウィンドウの作成
root = tk.Tk()
root.title("YouTubeダウンローダー")

# URL入力欄
url_label = tk.Label(root, text="YouTubeのURL:")
url_label.pack()
url_entry = tk.Entry(root, width=50)
url_entry.pack()

# ダウンロードボタン
download_button = tk.Button(root, text="ダウンロード", command=download_video)
download_button.pack()

# ウィンドウを表示
root.mainloop()
