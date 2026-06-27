"""
台灣鄉鎮市區人口密度查詢系統

使用 pandas 處理資料，並以 tkinter 建立 GUI 介面，
讓使用者可以根據區域名稱關鍵字查詢各鄉鎮市區的人口密度資訊。
"""

import pandas as pd
import tkinter as tk
from tkinter import ttk


def load_and_process_data(file_path):
    """
    讀取 CSV 檔案並進行資料整理

    步驟：
    1. 將第一列作為欄位名稱，並移除該列
    2. 移除最後 5 筆非資料內容（尾部說明資訊）
    3. 僅保留區域別、人口數、土地面積三個欄位
    4. 轉換數值型態並移除空值
    5. 新增人口密度欄位
    """
    # 讀取 CSV（UTF-8 with BOM 編碼），第一列作為欄位名稱
    df = pd.read_csv(file_path, header=1, encoding='utf-8-sig')

    # 移除最後 5 筆非資料內容（尾部說明資訊）
    df = df.iloc[:-5]

    # 僅保留所需欄位並重新命名
    df = df[['區域別', '年底人口數', '土地面積']].rename(
        columns={'年底人口數': '人口數'}
    )

    # 將人口數與土地面積轉換為數值型態
    df['人口數'] = pd.to_numeric(df['人口數'], errors='coerce')
    df['土地面積'] = pd.to_numeric(df['土地面積'], errors='coerce')

    # 移除含有空值的列
    df = df.dropna()

    # 新增人口密度欄位（人口數 / 土地面積）
    df['人口密度'] = df['人口數'] / df['土地面積']

    return df


def populate_treeview(tree, data_frame):
    """
    將 DataFrame 資料填入 Treeview 表格中

    人口密度四捨五入至小數點後兩位，人口數顯示為整數
    """
    # 清除現有資料
    for row in tree.get_children():
        tree.delete(row)

    # 逐筆插入資料
    for _, row in data_frame.iterrows():
        tree.insert('', 'end', values=(
            row['區域別'],
            int(row['人口數']),
            round(row['土地面積'], 2),
            round(row['人口密度'], 2),
        ))


def on_search(event=None):
    """
    查詢按鈕的點擊事件處理函式

    根據輸入框的關鍵字篩選區域別，若輸入為空則顯示全部資料
    """
    keyword = entry.get().strip()
    if keyword:
        filtered_df = df[df['區域別'].str.contains(keyword, na=False)]
    else:
        filtered_df = df
    populate_treeview(tree, filtered_df)


def main():
    global df, entry, tree

    # 建立主視窗
    root = tk.Tk()
    root.title('台灣鄉鎮市區人口密度查詢系統')
    root.geometry('900x600')

    # ---------- 上方控制區 ----------
    control_frame = ttk.Frame(root, padding=10)
    control_frame.pack(fill=tk.X)

    label = ttk.Label(control_frame, text='輸入區域名稱：')
    label.pack(side=tk.LEFT, padx=(0, 5))

    entry = ttk.Entry(control_frame, width=30)
    entry.pack(side=tk.LEFT, padx=(0, 5))
    entry.bind('<Return>', on_search)  # 按 Enter 也可觸發查詢

    search_btn = ttk.Button(control_frame, text='查詢', command=on_search)
    search_btn.pack(side=tk.LEFT)

    # ---------- 下方表格區 ----------
    table_frame = ttk.Frame(root, padding=(10, 0, 10, 10))
    table_frame.pack(fill=tk.BOTH, expand=True)

    # 定義欄位
    columns = ('區域別', '人口數', '土地面積', '人口密度')
    tree = ttk.Treeview(table_frame, columns=columns, show='headings')

    # 設定各欄位標題、寬度與置中對齊
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=180, anchor='center')

    # 加入垂直卷軸
    scrollbar = ttk.Scrollbar(table_frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)

    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    # ---------- 載入資料並顯示 ----------
    df = load_and_process_data('各鄉鎮市區人口密度.csv')
    populate_treeview(tree, df)

    root.mainloop()


if __name__ == '__main__':
    main()
