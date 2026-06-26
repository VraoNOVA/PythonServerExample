# PythonServerExample

A simple Django REST API server deployed on Azure App Service.

---

## Table of Contents

1. [What You Need Before Starting](#what-you-need-before-starting)
2. [Step 1: Fork the Repository](#step-1-fork-the-repository)
3. [Step 2: Create an Azure App Service](#step-2-create-an-azure-app-service)
4. [Step 3: Connect GitHub to Azure (Deployment Center)](#step-3-connect-github-to-azure-deployment-center)
5. [Step 4: Set the Startup Command](#step-4-set-the-startup-command)
6. [Step 5: Start the App](#step-5-start-the-app)
7. [Step 6: Test Your API](#step-6-test-your-api)
8. [API Endpoints Reference](#api-endpoints-reference)
9. [Updating Your App](#updating-your-app)
10. [Running Locally](#running-locally)
11. [Troubleshooting](#troubleshooting)

---

## What You Need Before Starting

- A **GitHub account** (free) — [github.com](https://github.com)
- A **Microsoft Azure account** (free tier works) — [portal.azure.com](https://portal.azure.com)
- **Python 3.x** installed on your computer
- A terminal (Terminal on Mac, Command Prompt or PowerShell on Windows)

---

## Step 1: Fork the Repository

1. Go to [https://github.com/VraoNOVA/PythonServerExample](https://github.com/VraoNOVA/PythonServerExample)
2. Click the **Fork** button (top right)
3. This creates a copy of the code in YOUR GitHub account
4. Clone it to your computer:
   ```bash
   git clone https://github.com/YOUR-USERNAME/PythonServerExample.git
   cd PythonServerExample
   ```

---

## Step 2: Create an Azure App Service

1. Go to [portal.azure.com](https://portal.azure.com) and sign in
2. Click **Create a resource** (top left, or use the search bar)
3. Search for **Web App** and click **Create**
4. Fill in these fields:

   | Field | What to enter |
   |-------|--------------|
   | **Subscription** | Your subscription (likely "Pay-As-You-Go" or "Azure for Students") |
   | **Resource Group** | Click "Create new" → name it anything (e.g. `my-api-group`) |
   | **Name** | A unique name for your app (e.g. `my-django-api-123`) — this becomes your URL |
   | **Runtime stack** | Python 3.x (pick the latest available) |
   | **Operating System** | Linux |
   | **Region** | Pick the closest one to you |
   | **App Service Plan** | Click "Create new" → select **Free (F1)** tier |

5. Click **Review + Create** → then **Create**
6. Wait for deployment to finish (~1-2 minutes)
7. Click **Go to resource**

Your app URL will be: `https://<your-app-name>.azurewebsites.net`

---

## Step 3: Connect GitHub to Azure (Deployment Center)

This tells Azure to automatically pull your code from GitHub.

1. In your App Service page, click **Deployment** → **Deployment Center** (left sidebar)
2. Under **Source**, select **GitHub**
3. Sign in to GitHub if prompted
4. Select:
   - **Organization**: your GitHub username
   - **Repository**: `PythonServerExample`
   - **Branch**: `main`
5. Click **Save** at the top
6. Wait 2-3 minutes for the first deployment to finish
7. You can check progress in the **Logs** tab of Deployment Center

You should see "Deployment successful" when it's done.

---

## Step 4: Set the Startup Command

Azure needs to know how to start your server.

1. Go to **Settings → Configuration** (left sidebar)
2. Click the **Stack settings** tab (at the top, next to "General settings")
3. Find the **Startup Command** text field
4. Paste this exact command:
   ```
   gunicorn --bind=0.0.0.0:8000 wsgi:application
   ```
5. Click **Save** at the top

---

## Step 5: Start the App

1. Go to **Overview** (left sidebar)
2. Click **Restart** at the top (or **Start** if the app is stopped)
3. Wait ~2 minutes for the app to boot
4. Visit your URL in a browser: `https://<your-app-name>.azurewebsites.net/api/health/`
5. You should see:
   ```json
   {"status": "ok"}
   ```

If you see this, your API is live!

---

## Step 6: Test Your API

### Option A: Using curl (from your terminal)

Replace `<your-app-name>` with your actual app name:

```bash
# Health check
curl https://<your-app-name>.azurewebsites.net/api/health/

# Say hello
curl "https://<your-app-name>.azurewebsites.net/api/hello/?name=YourName"

# Create a message
curl -X POST https://<your-app-name>.azurewebsites.net/api/messages/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "author": "YourName"}'

# List all messages
curl https://<your-app-name>.azurewebsites.net/api/messages/

# Update a message (change ID as needed)
curl -X PUT https://<your-app-name>.azurewebsites.net/api/messages/1/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Updated message"}'

# Delete a message
curl -X DELETE https://<your-app-name>.azurewebsites.net/api/messages/1/
```

### Option B: Using the Python test script

1. Create a virtual environment and install dependencies:
   ```bash
   cd PythonServerExample
   python3 -m venv venv
   source venv/bin/activate        # On Mac/Linux
   # venv\Scripts\activate         # On Windows
   pip install requests
   ```

2. Edit `test_api.py` and change the `BASE` URL to your app URL:
   ```python
   BASE = "https://<your-app-name>.azurewebsites.net"
   ```

3. Run the tests:
   ```bash
   python test_api.py
   ```

### Option C: Using a browser

Just paste these URLs into your browser:
- `https://<your-app-name>.azurewebsites.net/`
- `https://<your-app-name>.azurewebsites.net/api/hello/?name=YourName`
- `https://<your-app-name>.azurewebsites.net/api/health/`
- `https://<your-app-name>.azurewebsites.net/api/messages/`

---

## API Endpoints Reference

| Method | URL | Description | Example Body |
|--------|-----|-------------|-------------|
| GET | `/` | Home page | — |
| GET | `/api/hello/?name=X` | Says hello | — |
| GET | `/api/health/` | Health check | — |
| GET | `/api/messages/` | List all messages | — |
| POST | `/api/messages/` | Create a message | `{"text": "Hi", "author": "Name"}` |
| GET | `/api/messages/<id>/` | Get one message | — |
| PUT | `/api/messages/<id>/` | Update a message | `{"text": "New text"}` |
| DELETE | `/api/messages/<id>/` | Delete a message | — |

---

## Updating Your App

After you make code changes locally:

```bash
git add .
git commit -m "describe your change"
git push
```

Azure Deployment Center will automatically detect the push and redeploy. Wait ~2 minutes, then test again.

---

## Running Locally

If you want to test on your own computer before deploying:

```bash
cd PythonServerExample
python3 -m venv venv
source venv/bin/activate          # On Mac/Linux
# venv\Scripts\activate           # On Windows
pip install django
python -m django runserver 0.0.0.0:8000 --settings=settings
```

Then visit: `http://localhost:8000/api/health/`

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| **403 - Web app is stopped** | Go to Overview → click **Start** |
| **503 - Application Error** | Check Monitoring → Log stream for details |
| **Timeout on first request** | Normal on Free tier — the app "cold starts". Wait 30 seconds and try again |
| **"Could not find virtual environment"** | Make sure `requirements.txt` exists in your repo and redeploy |
| **App deploys but doesn't work** | Verify Startup Command is set to `gunicorn --bind=0.0.0.0:8000 wsgi:application` |
| **Can't SSH into the app** | The app must be running first — click Start in Overview |
| **Free tier keeps stopping** | Normal — Azure stops idle free apps. Just click Start again |