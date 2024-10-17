以下是將 README 文件改成符合台灣語法的版本：

---

# 11310-python-news

**11310-python-news** 是一個基於 Flask 框架的新聞聚合應用，透過 `NewsAPI` 取得全球新聞或特定國家的新聞數據。

> [Demo](https://infinite-beach-19597-befe83c6cd34.herokuapp.com/)

## 專案功能

- 全球新聞查詢（透過 `NewsAPI` 的 `/everything` API 端點）
- 美國新聞查詢（透過 `NewsAPI` 的 `/top-headlines` API 端點）
- 根據類別及關鍵字篩選新聞

## 安裝與啟動專案指南

### 1. 從 GitHub 下載專案

首先，將專案從 GitHub 下載到本地環境：

```bash
git clone https://github.com/sunny96087/11310-python-news.git
```

進入專案目錄：

```bash
cd 11310-python-news
```

### 2. 設定虛擬環境

創建並啟動虛擬環境：

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
# 如果你使用的是 Windows 系統，請使用以下命令來啟動虛擬環境：
# venv\Scripts\activate
```

### 3. 安裝專案所需的依賴

安裝所有依賴套件：

```bash
pip install -r requirements.txt
```

### 4. 啟動應用

設定完成後，運行以下命令來啟動 Flask 應用：

```bash
flask run
```

應用啟動後，你可以在瀏覽器中透過 [http://127.0.0.1:5000](http://127.0.0.1:5000) 訪問。

## 部署

將此專案部署到 **Heroku**：

1. 使用以下命令將專案推送到 Heroku：
    ```bash
    git push heroku master
    ```

2. 啟動應用：
    ```bash
    heroku ps:scale web=1
    ```

3. 訪問應用
    ```bash
    heroku open
    ```

## 技術

- **後端**：Flask
- **前端**：HTML, CSS, JavaScript (使用 TailwindCSS)
- **API**：NewsAPI

## 開發者

- [2fish](https://github.com/sunny96087)