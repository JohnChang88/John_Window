# python用物件導向程式與grid寫個bmi程式，有視窗window
# 使用 Python 的內建模組 `tkinter` 來建立簡單的視窗應用程式。使用 `tkinter` 創建一個 BMI 計算器的視窗介面：

import tkinter as tk

def calculate_bmi():
    try:
        height_cm = float(height_entry.get())
        weight_kg = float(weight_entry.get())
        bmi = weight_kg / ((height_cm / 100) ** 2)
        result_label.config(text=f"你的 BMI 數值為：{bmi:.2f}")
    except ValueError:
        result_label.config(text="請輸入有效的數字。")

# 建立主視窗
root = tk.Tk()
root.title("BMI 計算器")

# 身高輸入框
height_label = tk.Label(root, text="身高（公分）：")
height_label.pack()
height_entry = tk.Entry(root)
height_entry.pack()

# 體重輸入框
weight_label = tk.Label(root, text="體重（公斤）：")
weight_label.pack()
weight_entry = tk.Entry(root)
weight_entry.pack()

# 計算按鈕
calculate_button = tk.Button(root, text="計算 BMI", command=calculate_bmi)
calculate_button.pack()

# 顯示結果的標籤
result_label = tk.Label(root, text="")
result_label.pack()

# 啟動視窗主迴圈
root.mainloop()


# 這個視窗應用程式會要求使用者輸入身高和體重，並顯示計算出的 BMI 數值。
