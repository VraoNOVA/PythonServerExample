# PythonServerExample

A simple Django REST API server with CRUD endpoints.

## API Endpoints

| Method | URL | Description |
|--------|-----|-------------|
| GET | `/` | Home – welcome message |
| GET | `/api/hello/?name=Vivek` | Hello with optional name param |
| GET | `/api/health/` | Health check |
| GET | `/api/messages/` | List all messages |
| POST | `/api/messages/` | Create a message |
| GET | `/api/messages/<id>/` | Get a message by ID |
| PUT | `/api/messages/<id>/` | Update a message |
| DELETE | `/api/messages/<id>/` | Delete a message |

### Example POST request

```bash
curl -X POST https://<your-app>.azurewebsites.net/api/messages/ \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello world", "author": "Vivek"}'
```

---

## Deploy on Azure App Service

### Prerequisites

- An Azure account
- An App Service (Linux, Python 3.x runtime)

### Step 1: Create the App Service

1. Go to the [Azure Portal](https://portal.azure.com)
2. Click **Create a resource** → **Web App**
3. Fill in:
   - **Name**: your app name (e.g. `my-django-app`)
   - **Runtime stack**: Python 3.x
   - **Operating System**: Linux
   - **Region**: choose your preferred region
   - **App Service Plan**: Free (F1) or higher
4. Click **Review + Create** → **Create**

### Step 2: Clone the repo on the App Service

1. In the Azure Portal, go to your App Service
2. Enable **SSH** under **Settings → Configuration → General settings**
3. Go to **Development Tools → SSH** and open a terminal
4. Run:
   ```bash
   cd /home/site/wwwroot
   git clone https://github.com/VraoNOVA/PythonServerExample.git
   ```

### Step 3: Set the Startup Command

1. Go to **Settings → Configuration → Stack settings**
2. In the **Startup Command** field, enter:
   ```
   bash /home/site/wwwroot/PythonServerExample/startup.sh
   ```
3. Click **Save**

### Step 4: Restart and verify

1. Go to **Overview** → click **Restart**
2. Wait ~30 seconds, then visit:
   ```
   https://<your-app-name>.azurewebsites.net/
   ```
3. You should see:
   ```json
   {"message": "Welcome to the Django Server!", "status": "running"}
   ```

---

## Updating the App

Push changes to GitHub and restart the App Service. The startup script (`startup.sh`) automatically clones the latest code on every restart.

```bash
git add . && git commit -m "my changes" && git push
```

Then restart the App Service from Azure Portal: **Overview → Restart**

---

## Running Locally

```bash
pip install django
python -m django runserver 0.0.0.0:8000 --settings=settings
```