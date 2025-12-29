# Deployment Guide: Autonomous Market Research Agent

This guide covers how to test your agent locally and deploy it to your Google Cloud Portfolio.

## 1. Local Verification (Check if it works)

Before deploying, ensure the application runs correctly on your machine.

### Option A: Run with Python (Fastest)

1.  **Install Dependencies**:
    ```powershell
    pip install -r requirements.txt
    ```
2.  **Set Environment Variables**:
    Make sure your `.env` file has your keys:
    ```
    GEMINI_API_KEY=your_key
    SERPAPI_API_KEY=your_key
    ```
3.  **Run the App**:
    ```powershell
    streamlit run app.py
    ```
4.  **Verify**: Open the URL shown (usually `http://localhost:8501`) and try generating a report.

### Option B: Run with Docker (Closer to Production)

1.  **Build the Image**:
    ```powershell
    docker build -t research-agent .
    ```
2.  **Run the Container**:
    ```powershell
    docker run -p 8501:8501 --env-file .env research-agent
    ```
3.  **Verify**: Open `http://localhost:8501`.

---

## 2. Deploy to Google Cloud Portfolio

We will use **Google Cloud Run** for a serverless, scalable deployment.

### Prerequisites
- [Google Cloud SDK (gcloud)](https://cloud.google.com/sdk/docs/install) installed and authenticated.
- A Google Cloud Project created.

### Step-by-Step Deployment

#### 1. Initialize Google Cloud
Run these commands in your terminal:
```powershell
# Login to Google Cloud
gcloud auth login

# Set your project ID (replace YOUR_PROJECT_ID)
gcloud config set project YOUR_PROJECT_ID
```

#### 2. Enable Required Services
```powershell
gcloud services enable cloudbuild.googleapis.com run.googleapis.com
```

#### 3. Deploy
You can use the automated script provided in this repo, or run the command manually.

**Using the Script (Recommended):**
Run the `deploy.ps1` script in PowerShell. It will ask for your Project ID and handle the rest.
```powershell
.\deploy.ps1
```

**Manual Command:**
```powershell
gcloud run deploy research-agent `
  --source . `
  --region us-central1 `
  --allow-unauthenticated
```
*Note: You will be prompted to enter environment variables (keys) during the first deployment or you can set them in the Google Cloud Console UI.*

### Post-Deployment
- Requires `GEMINI_API_KEY` and `SERPAPI_API_KEY`.
- Go to the **Cloud Run** section in Google Cloud Console.
- Click on your service (`research-agent`).
- Go to **Edit & Deploy New Revision** > **Variables & Secrets**.
- Add your API keys there and redeploy.

Your agent is now live on your Google Cloud Portfolio!

---

## 3. Deploy to Streamlit Community Cloud (Easier Alternative)

Streamlit Cloud pulls directly from GitHub.

### Step 1: Push to GitHub
1.  **Create a Repository** on GitHub (e.g., `ai-research-agent`).
2.  **Initialize & Push** (Run in your project folder):
    ```powershell
    git init
    # .gitignore is already created for you to exclude secrets
    git add .
    git commit -m "Initial commit"
    git branch -M main
    # Replace URL with your actual repo URL
    git remote add origin https://github.com/YOUR_USERNAME/ai-research-agent.git
    git push -u origin main
    ```

### Step 2: Deploy on Streamlit Cloud
1.  Go to [share.streamlit.io](https://share.streamlit.io/).
2.  Click **"New app"**.
3.  Select your repository (`ai-research-agent`), branch (`main`), and main file (`app.py`).
4.  Click **"Deploy!"**.

### Step 3: Add Secrets (Critical)
The app will error initially because it doesn't have your keys.
1.  On your app dashboard, clicking **"Manage app"** (bottom right) or the **Settings** menu.
2.  Go to **Secrets**.
3.  Paste your keys like this:
    ```toml
    GEMINI_API_KEY = "AIza..."
    SERPAPI_API_KEY = "ae0f..."
    ```
4.  Save. The app will reboot and start working!
