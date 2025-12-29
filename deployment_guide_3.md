# Deployment Guide 3: The Final Fix

This guide will help you **push the stability fixes** (error handling + model switch) to your deployed app.

---

## 🛑 Step 1: Ensure Your Terminal is Clean

1.  Click inside your VS Code terminal.
2.  Try pressing **`Esc`** a few times to make sure you aren't in any weird mode.
3.  If you see lines starting with `>`, type `q` to quit.

---

## 🚀 Step 2: Push the Fixes

Run these 3 commands exactly, one by one:

### 1. Stage the changes
```powershell
git add .
```

### 2. Commit (Save) the changes
```powershell
git commit -m "Switch to stable Gemini Flash model and fix hangs"
```
*(If it says "nothing to commit", that's fine, just move to the next step)*

### 3. Push to Cloud
```powershell
git push
```

---

## ✅ Step 3: Verify on Streamlit Cloud

1.  Go to your app URL.
2.  Bottom right corner should show **"Updating..."** or **"Baking..."**. Wait for it to finish.
3.  **Refresh the page** (`Ctrl + R`).
4.  Run a query (e.g., "AI in Healthcare").
5.  **Watch:** It should now be faster and if it hits a snag, it will retry instead of freezing.

---

## ❓ Common Issues

### "Updates were rejected" (The Merge Error)
If `git push` fails with "Updates were rejected":
1.  Run: `git pull`
2.  If a weird screen opens (Vim):
    *   Press `Esc`
    *   Type `:wq`
    *   Press `Enter`
3.  Run: `git push` again.
