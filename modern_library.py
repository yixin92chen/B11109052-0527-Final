import os
import json

books_data = []  # 原本的 d2
FILE_NAME = "books.json"  # 改為 JSON 檔案

def load_books():
    """從 JSON 檔案載入圖書資料"""
    global books_data
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r", encoding="utf-8") as file:
                books_data = json.load(file)
        except json.JSONDecodeError:
            print(f"檔案 {FILE_NAME} 格式錯誤，無法解析。")
        except Exception as e:
            print(f"載入圖書資料時發生錯誤: {e}")
    else:
        print(f"檔案 {FILE_NAME} 不存在，將建立新檔案。")
        save_books()  # 如果檔案不存在，立即生成空的 JSON 檔案

def save_books():
    """將圖書資料儲存到 JSON 檔案"""
    try:
        with open(FILE_NAME, "w", encoding="utf-8") as file:
            json.dump(books_data, file, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"儲存圖書資料時發生錯誤: {e}")

def is_isbn_exist(isbn):
    """檢查 ISBN 是否存在"""
    return any(book['isbn'] == isbn for book in books_data)

def main():
    load_books()
    print("=== 圖書管理系統 v0.3 (JSON Refactored) ===")
    
    while True:
        command = input("> ").strip()
        
        if command == "exit":
            save_books()
            print("系統關閉")
            break
            
        elif command.startswith("add "):
            raw_data = command[4:].split("/")
            if len(raw_data) == 3:
                if not is_isbn_exist(raw_data[1]):
                    books_data.append({"title": raw_data[0], "isbn": raw_data[1], "status": raw_data[2]})
                    print("Success")
                else:
                    print("ISBN Exist")
            else:
                print("Format Error")
                
        elif command == "show":
            for book in books_data:
                print(f"書名: {book['title']}, ISBN: {book['isbn']}, 狀態: {book['status']}")
                
        elif command.startswith("borrow "):
            target_isbn = command[7:]
            for book in books_data:
                if book['isbn'] == target_isbn:
                    if book['status'] == "available":
                        book['status'] = "borrowed"
                        print("Updated")
                    else:
                        print("This book is already borrowed")
                    break
            else:
                print("Book not found")
        else:
            print("Unknown Command")

if __name__ == "__main__":
    main()