# Deployment Guide 2: From Scratch to Streamlit Cloud

**The Issue**: The error `git : The term 'git' is not recognized` means **Git is not installed** on your computer. You cannot upload to GitHub without it.

Follow these exact steps to fix it and deploy.

---

## Step 1: Install Git (CRITICAL)

1.  **Download**: Go to [git-scm.com/download/win](https://git-scm.com/download/win) and download the "64-bit Git for Windows Setup".
2.  **Install**: Run the installer. **Just keep clicking "Next"** through all the options (the defaults are fine).
3.  **Restart Terminal**:
    *   **Close** your current VS Code/Terminal window completely.
    *   **Re-open** it.
    *   Type `git --version` in the terminal. If it prints a version number (e.g., `git version 2.x.x`), you are ready.

---

## Step 2: Configure Git (One-time setup)

Before you can commit code, Git needs to know who you are. Run these two commands in your terminal (replace with your info):

```powershell
git config --global user.name "Your Name"
git config --global user.email "your_email@example.com"
```

---

## Step 3: upload to GitHub

Now that Git is working, run the commands you tried earlier.

**Make sure you are in your project folder:** `c:\AI_Work\AI-Research-Portfolio`

```powershell
# 1. Initialize the repository
git init

# 2. Add all files (the .gitignore I made will automatically block secrets)
git add .

# 3. Save the changes
git commit -m "Initial commit for Streamlit Cloud"

# 4. Rename branch to main
git branch -M main

# 5. Connect to your GitHub Repo
# (Make sure you have created an empty repo on GitHub.com first!)
git remote add origin https://github.com/muazumair-commits/AutopilotAgentAi.git

# 6. Upload
git push -u origin main
```
*Note: A window might pop up asking you to sign in to GitHub. Go ahead and sign in.*

---

## Step 4: Deploy on Streamlit Cloud

1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click **"New app"**.
3.  Choose your repository: `muazumair-commits/AutopilotAgentAi`.
4.  Main file path: `app.py`.
5.  Click **"Deploy!"**.

### 🛑 CRITICAL FINAL STEP: Secrets
The app will **crash** immediately looking for your API keys. You must add them manually.

1.  On your deployed app's screen, click **"Manage app"** (bottom right) -> the **three dots** (settings) -> **Settings** -> **Secrets**.

2.  Paste your keys exactly like this (Toml format). **IMPORTANT: Make sure to wrap your actual keys in double quotes `""` and do NOT copy the triple backticks**:

    ```toml
    GEMINI_API_KEY = "Your_actual_Gemini_key_starts_with_AIza..."
    SERPAPI_API_KEY = "Your_actual_SerpAPI_key_here"
    ```

    *Example of what it should look like inside the box:*
    `GEMINI_API_KEY = "AIzaSyD..."`

3.  Click **Save**. The app will restart and work perfectly!
