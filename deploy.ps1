# Deploy Script for AI Research Agent

$project = Read-Host "Enter your Google Cloud Project ID"
if (-not $project) {
    Write-Host "Project ID is required." -ForegroundColor Red
    exit 1
}

Write-Host "Setting project to $project..." -ForegroundColor Cyan
gcloud config set project $project

Write-Host "Enabling necessary services..." -ForegroundColor Cyan
gcloud services enable cloudbuild.googleapis.com run.googleapis.com

Write-Host "Deploying to Cloud Run..." -ForegroundColor Cyan
# Initial deployment
gcloud run deploy research-agent `
    --source . `
    --region us-central1 `
    --allow-unauthenticated `
    --set-env-vars "GEMINI_API_KEY=placeholder,SERPAPI_API_KEY=placeholder"

Write-Host "Deployment initiated!" -ForegroundColor Green
Write-Host "IMPORTANT: Please go to the Google Cloud Console URL provided in the output above." -ForegroundColor Yellow
Write-Host "Navigate to 'Edit & Deploy New Revision' -> 'Variables & Secrets' to update your real API Keys." -ForegroundColor Yellow
