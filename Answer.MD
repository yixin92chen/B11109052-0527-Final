# 台科大資管 Python 考試作答區

---

## 基本資料

**學號：** B11109052  
**系級：** 資管系大四  
**姓名：** 陳以芯  

---

## 一、 原始碼分析報告 (Static Analysis) (共8小題，每小題3分，總共24分)

### 1.1 變數與邏輯對照表

| 原始變數名稱 | 代表意義 (Business Logic) | 建議修正名稱 |
|---|---|---|
| Q1 l1 (in load_proc) |資料檔案的每一行內容 |file_lines |
| Q2 d2 (in main) |圖書資料的記憶體儲存結構 |books_data |
| Q3 c_res (in check) |檢查 ISBN 是否存在的函式 |is_isbn_exist |

### 1.2 壞味道 (Code Smells) 診斷

請列出原程式碼中至少 5 個嚴重的設計問題，並說明為什麼不好：

- **Q1：**缺乏模組化，當全域變數 `d2` 被多個函式直接操作時，導致函式之間高度耦合，難以追蹤資料變化，且不利於單元測試。
- **Q2：**缺乏彈性，當檔案名稱 `F_NAME` 需要更改時，必須修改程式碼，違反開放封閉原則，降低了程式的可維護性。
- **Q3：**缺乏錯誤處理，當檔案不存在或讀取失敗時，程式會直接崩潰，無法應對意外情況。
- **Q4：**缺乏抽象，當檔案操作邏輯（如讀取和寫入）重複出現在多個函式中，增加了維護成本，且容易出現不一致的邏輯。
- **Q5：**缺乏語意化命名，當函式名稱如 `c_res` 和變數名稱如 `l1`、`d2` 不直觀時，降低了程式的可讀性，增加了理解和協作的難度。

---

## 二、 Vibe-Coding 協作紀錄 (共6小題，每小題3分，總共18分)

請記錄你如何引導 GitHub Copilot 進行重構。
重構的要求，請根據題目卷以及你發現的 Code Smells 來進行。

### 2.1 關鍵 Prompt 紀錄

請貼出你對 AI 下達過最有效的 3 個 Prompt：

```log
Prompt A：請將這份 legacy Python 程式重構為符合 Clean Code 原則的版本，使用 class 封裝圖書館功能，並將功能拆分成小型函式。 

Prompt B：請將檔案操作邏輯（如讀取和寫入檔案）抽象為通用函式，並加入錯誤處理機制，確保當檔案不存在或讀取失敗時，程式不會崩潰。 

Prompt C：請將變數和函式名稱語意化，例如將 `d2` 改為 `books_data`，`c_res` 改為 `is_isbn_exist`，並確保所有命名清晰且符合其功能。
```

### 2.2 AI 錯誤處理

1. AI 在撰寫過程中是否有出錯？（例如：漏寫了某個功能、語法錯誤）你是如何發現並請它修正的？
在 exit 指令執行時，未加入額外的操作（如顯示分類統計或其他結束時的資訊）。

2. 發現的問題： (範例：AI 漏掉了 exit 時要印出分類統計的功能)
問題 1：exit 指令執行時，僅儲存圖書資料並關閉系統，未執行額外的功能（如顯示分類統計）。

問題 2：在 borrow 指令中，未處理當圖書已被借出的情況，可能導致狀態重複更新。

問題 3：未處理空輸入的情況，可能導致程式崩潰。

3. 修正的對話： (範例：我告訴它「請在結束前迴圈遍歷 JSON 資料並計算分類總額」)
問題 1 修正對話：
我告訴 AI：「請在 exit 指令執行前，迴圈遍歷 books_data，統計每種狀態（如 available 和 borrowed）的數量，並印出統計結果。」

問題 2 修正對話：
我告訴 AI：「請在 borrow 指令中，檢查圖書的狀態是否為 available，若不是，則提示該書已被借出。」

問題 3 修正對話：
我告訴 AI：「請在每次輸入指令時，檢查是否為空輸入，若是，則提示用戶重新輸入。」
---

## 三、 成果驗證與測試  (共2小題，每小題10分，總共20分)

確保你的 `modern_library.py` 功能正確。

### 3.1 測試結果驗證 (Terminal)

請貼上執行程式並輸入 show 後，顯示資料清單。(請從呼叫執行程式到結束程式完整的把操作對話複製到下框)

```log
PS C:\Users\pclab\Desktop\題目_AI協作\NTUST-0527-Final-master> python legacy_lib.py
=== 圖書管理系統 v0.1 (Legacy) ===
> add 深入淺出Python/978001/available
Success
> add 資料結構理論/978002/available
Success
> add 演算法實作/978003/available
Success
> add 重複測試書/978001/available
ISBN Exist
> borrow 978002
Updated
> show
書名: 深入淺出Python, ISBN: 978001, 狀態: available
書名: 資料結構理論, ISBN: 978002, 狀態: borrowed
書名: 演算法實作, ISBN: 978003, 狀態: available
> exit
系統關閉
PS C:\Users\pclab\Desktop\題目_AI協作\NTUST-0527-Final-master> python modern_library.py
檔案 books.json 不存在，將建立新檔案。
=== 圖書管理系統 v0.3 (JSON Refactored) ===
> add 深入淺出Python/978001/available
Success
> add 資料結構理論/978002/available
Success
> add 演算法實作/978003/available
Success
> add 重複測試書/978001/available
ISBN Exist
> borrow 978002
Updated
> show
書名: 深入淺出Python, ISBN: 978001, 狀態: available
書名: 資料結構理論, ISBN: 978002, 狀態: borrowed
書名: 演算法實作, ISBN: 978003, 狀態: available
> exit
```

### 3.2 產出的資料檔案格式

請貼上重構後生成的 `books.json` 前幾行內容：

```json
[
    {
        "title": "深入淺出Python",
        "isbn": "978001",
        "status": "available"
    },
    {
        "title": "資料結構理論",
        "isbn": "978002",
        "status": "borrowed"
    },
    {
        "title": "演算法實作",
        "isbn": "978003",
        "status": "available"
    }
]
```

---

## 四、 Git 提交紀錄 (Commit History)  (共2小題，總共13分)

### 4.1. 請執行 `git log --oneline` 並將 Commit 紀錄貼在此處，以證明你的開發流程(此小題6分)


```log
# 請在此處貼上 git log 內容
06c7a96 (HEAD -> master) B11109052
```

### 4.2. GitHub Repository 連結(此小題7分)

將專案推送到 GitHub (Public) 若提交到 Private 連結不給分。 請設定 Repository 名稱為 `學號-0527-Final` Ex: B11526748-0527-Final **請用 - 不是 _**

```log
# 請貼上你的 Repo 網址
```

希望這兩份 Markdown 格式能幫你省下不少排版時間！祝你的考試順利舉行！

最後請保留整份專案資料夾歐！
