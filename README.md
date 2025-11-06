# Tasks

A simple Task Manager API built with FastAPI, SQLAlchemy, and Gunicorn.

---

## Installation & Execution

### Clone the repo:

```bash
git clone https://github.com/reyhanebnyd/Tasks.git
cd Tasks
```
### Create virtual environment and install dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
### run locally
```bash
uvicorn app.main:app --reload
```
## API endpoints
| Method | Path          | Description         |
| ------ | ------------- | ------------------- |
| POST   | /tasks/     | Create a new task   |
| GET    | /tasks/     | List all tasks      |
| GET    | /tasks/{id} | Get a task by ID    |
| PUT    | /tasks/{id} | Update a task by ID |
| DELETE | /tasks/{id} | Delete a task by ID |

## request example (create task)
```bash
{
  "title": "Write file",
  "description": "Create a new Python file"
}
```
## response example
```bash
 {
    "title": "code",
    "description": "write new file",
    "is_completed": false,
    "id": 1,
    "created_at": "2025-11-06T17:39:05.560143"
  }
```
### Deployment on VPS (Ubuntu)

SSH into VPS
```bash
ssh ubuntu@188.121.121.107
```
update and upgrade
```bash
sudo apt update
sudo apt upgrade -y
```
install postgresql and python
```bash
sudo apt install postgresql postgresql-contrib -y
sudo apt install python3-pip python3-venv -y
sudo systemctl start postgresql
sudo systemctl enable postgresql
```
set up username and password
```bash
sudo -u postgres psql
CREATE DATABASE tasks_db;
CREATE USER youruser WITH PASSWORD 'yourpassword';
GRANT ALL PRIVILEGES ON DATABASE tasks_db TO youruser;
GRANT ALL ON SCHEMA public TO youruser;
ALTER ROLE youruser SET search_path TO public;
ALTER SCHEMA public OWNER TO youruser;
\q
```
create .env
```bash
nano .env
```
then add this:
```bash
DATABASE_URL=postgresql://youruser:yourpassword@localhost/tasks_db
```
## clone the repo and steup venv
```bash
git clone https://github.com/reyhanebnyd/Tasks.git
cd Tasks
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```
## create systemd service
```bash
sudo nano /etc/systemd/system/tasks.service
```
paste:
```bash
[Unit]
Description=FastAPI Task Manager
After=network.target

[Service]
User=ubuntu
Group=www-data
WorkingDirectory=/home/ubuntu/Tasks
Environment="PATH=/home/ubuntu/Tasks/venv/bin"
ExecStart=/home/ubuntu/Tasks/venv/bin/gunicorn -w 4 -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000 app.main:app
Restart=always
RestartSec=3
TimeoutStopSec=20
KillMode=mixed

[Install]
WantedBy=multi-user.target
```

## start the service
```bash
sudo systemctl daemon-reload
sudo systemctl start tasks.service
sudo systemctl enable tasks.service
sudo systemctl status tasks.service
```
## access API
http://188.121.121.107:8000/docs
