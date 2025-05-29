# Otitis Media Detection Using Transfer Learning

Otitis Media Detection using Transfer Learning is a deep learning technique that uses pre-trained models to quickly and accurately diagnose middle ear infections. The method involves fine-tuning pre-trained models on images of the middle ear to detect signs of Otitis Media. This approach can significantly reduce the time and error associated with manual inspections and improve the accuracy of diagnosis, making it a valuable tool for medical professionals.

ResearchGate Technical Report: https://www.researchgate.net/publication/375893659_Otitis_Media_Detection_Using_Deep_Learning

## 🚀 Quick Start Guide (Windows)

### Prerequisites
- Python 3.10+
- Node.js 18+
- Docker and Docker Compose
- Git

### Method 1: Manual Setup (Recommended)

#### Backend Setup

1. **Navigate to Backend Directory**
```cmd
cd backend
```

2. **Create and Activate Virtual Environment**
```cmd
python -m venv venv
venv\Scripts\activate
```

3. **Install Dependencies**
```cmd
pip install -r requirements.txt
```

4. **Create Environment File**
```cmd
copy .env.example .env
```

5. **Configure Environment Variables**
Edit `backend\.env` file with your settings:
```env
PROJECT_NAME=voyage_imaging
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_secure_password_here
POSTGRES_DB=voyage_imaging
DATABASE_URL=postgresql+asyncpg://postgres:your_secure_password_here@localhost:5432/voyage_imaging
```

6. **Start Database with Docker**
```cmd
docker-compose up -d
```

7. **Run Database Migrations**
```cmd
docker exec -it voyage_api alembic upgrade head
```

8. **Start Backend Server**
```cmd
python manage.py serve
```

**Backend will be running at: http://localhost:8000**

#### Frontend Setup

1. **Navigate to Frontend Directory (Open new terminal)**
```cmd
cd frontend
```

2. **Install Dependencies**
```cmd
npm install
```

3. **Create Environment File**
```cmd
copy .env.example .env.local
```

4. **Configure Frontend Environment**
Edit `frontend\.env.local`:
```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

5. **Start Frontend Server**
```cmd
npm run dev
```

**Frontend will be running at: http://localhost:3000**

### Method 2: Docker Compose Setup

#### Complete Containerized Setup

1. **Backend with Docker**
```cmd
cd backend
copy .env.example .env
REM Edit .env with your database credentials
docker-compose up -d
```

2. **Frontend with Docker**
```cmd
cd frontend
copy .env.example .env
REM Edit .env if needed
docker-compose up -d
```

### 🔗 Access URLs

- **Frontend Application**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **pgAdmin Database Management**: http://localhost:5050
  - Email: admin@admin.com
  - Password: admin

### 🗄️ Database Connection Details

- **Host**: localhost
- **Port**: 5432
- **Database**: voyage_imaging
- **Username**: postgres
- **Password**: your_secure_password_here

### 🛠️ Troubleshooting

1. **Port Conflicts**: Modify port mappings in `docker-compose.yml` files if needed
2. **Database Issues**: Check container status:
   ```cmd
   docker ps
   ```
3. **Migration Issues**: Ensure database is running before migrations:
   ```cmd
   docker-compose up -d db
   alembic upgrade head
   ```

### ✅ Verification Steps

1. Visit http://localhost:3000 - Frontend should load
2. Visit http://localhost:8000/docs - API documentation should be accessible
3. Check logs: `docker logs voyage_api`
4. Test image upload and prediction functionality



#### Preview

![image](https://user-images.githubusercontent.com/46085301/218257473-9f37c7ed-6b37-4a5a-9f53-9ce41173941d.png)

#### System Architecture

![image](https://user-images.githubusercontent.com/46085301/218257587-82b1a5e6-d750-4c83-bfc8-7cc667c465b3.png)

#### Some Examples
![examples_images](image.png)

## Tech Stack

**Client:** NextJs, TailwindCSS

**Server:** Python, FastAPI, PyTorch, ONNX

## Authors

- [Mada Nithish Reddy](https://www.github.com/nithish6606)
