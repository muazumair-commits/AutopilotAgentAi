# How to Rotate Your API Key

If you hit a rate limit (`429 RESOURCE_EXHAUSTED`), follow these steps to switch to a new API key.

## 1. Update Local Environment
(This fixes the app when you run `streamlit run app.py` on your own computer)

1.  Open the file named `.env` in your project folder.
2.  Find the line starting with `GEMINI_API_KEY=`.
3.  Replace the text inside the quotes with your **new* key.
    ```env
    GEMINI_API_KEY="AIzaSyNewKey..."
    ```
4.  Save the file.

## 2. Update Streamlit Cloud
(This fixes the live website)

**You do NOT need to use Git for this.**

1.  Go to your deployed app URL.
2.  Click **"Manage app"** in the bottom right corner (or go to share.streamlit.io).
3.  Click the **three dots (⋮)** next to your app → **Settings**.
4.  Click on the **Secrets** tab.
5.  You will see your secrets in TOML format. Update the key there:
    ```toml
    GEMINI_API_KEY = "Your_New_Double_Quoted_Key_Here"
    ```
6.  Click **Save**.

The app will automatically restart with the fresh quota.
