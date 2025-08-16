---

````markdown
# 🧹 File Cleaner Tool

A simple **GUI-based File Cleaner Tool** to quickly remove unwanted files (like `.jpg`, `.mp4`, `.pdf` etc.) from any folder.  
Supports both **Windows (EXE)** and **Linux/Ubuntu/Debian (Python)** environments.

---

## 📥 Installation & Usage

### 🔹 Windows (EXE file ব্যবহার)
1. Download **`file_cleaner.exe`** from [Releases](https://github.com/itshahin111/file-cleaner/tree/master/dist).
2. Double-click to open the tool.
3. Select the **folder** you want to clean.
4. Choose the **file formats** you want to delete (e.g., `.jpg`, `.mp4`, `.pdf`).
5. Click **Delete** → All selected files will be removed ✅

> 💡 Note: Windows-এ Python ইনস্টল না থাকলেও `.exe` ফাইল কাজ করবে।

---

### 🔹 Linux / Ubuntu / Debian (Python File ব্যবহার)

#### 1️⃣ Install Python (if not installed):
```bash
sudo apt update
sudo apt install python3 python3-pip -y
````

#### 2️⃣ Clone the project:

```bash
git clone https://github.com/itshahin111/file-cleaner.git
cd file-cleaner
```

#### 3️⃣ Install dependencies:

```bash
pip3 install -r requirements.txt
```

#### 4️⃣ Run the tool:

```bash
python3 src/file_cleaner.py
```

👉 GUI will open → **Select folder** → **Choose file formats** → **Click Delete ✅**

---

### 🔹 (Optional) Run with Virtual Environment (venv)

#### 1️⃣ Create venv:

```bash
python3 -m venv venv
```

#### 2️⃣ Activate venv:

Linux / Ubuntu / Debian:

```bash
source venv/bin/activate
```

Windows (PowerShell):

```powershell
.\venv\Scripts\Activate
```

#### 3️⃣ Install dependencies:

```bash
pip install -r requirements.txt
```

#### 4️⃣ Run inside venv:

```bash
python src/file_cleaner.py
```

👉 To deactivate venv:

```bash
deactivate
```

---

## ⚠️ Important Notes

* 🗑 **Backup your data** – Once deleted, files **cannot be restored**.
* 🔑 May require **Admin Permission** if cleaning **system folders**.
* 🖥 On Linux, you can create a **`.desktop` shortcut** for easy access.
* 🪟 On Windows, you can pin the `.exe` file to **Start Menu / Taskbar**.

---

## 📸 Screenshots

*(Screenshot from 2025-08-16 11-30-56.png)*

---

## 📜 License

This project is licensed under the **MIT License** – free to use and modify.

---


