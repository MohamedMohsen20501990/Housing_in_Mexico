🏠 Mexico Housing Price Prediction

An end-to-end Machine Learning project for predicting housing prices in Mexico using a Random Forest Regressor.

The project covers the complete workflow from data preparation and model training to automated testing, API development, containerization, and cloud deployment.

🚀 Project Workflow
Raw Data
   ↓
Data Wrangling
   ↓
Model Training
   ↓
Saved ML Model
   ↓
FastAPI
   ↓
Pytest
   ↓
Docker
   ↓
Docker Hub
   ↓
Azure Container Apps

🛠️ Technologies
Python
Pandas — Data processing
Scikit-learn — Machine learning
FastAPI — REST API
Pytest — Automated testing
Docker — Containerization
Docker Hub — Container image registry
Azure Container Apps — Cloud deployment
📁 Project Structure
housing_in_mexico/
│
├── data/
│   ├── raw/                  # Original datasets
│   └── processed/            # Processed datasets
│
├── models/
│   └── rf_model.pkl          # Trained Random Forest model
│
├── notebooks/                # Jupyter notebooks
│
├── src/
│   ├── data.py               # Data processing
│   ├── model.py              # Model loading & prediction
│   └── main.py               # FastAPI application
│
├── tests/
│   ├── test_data.py          # Data processing tests
│   ├── test_model.py         # Model tests
│   └── test_main.py          # API tests
│
├── Dockerfile                # Docker image configuration
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation

🔌 API

The trained model is exposed through a FastAPI REST endpoint:

POST /predict

Example Request
{
  "area": 60,
  "lat": 19.9,
  "lon": -99.8
}


The API returns the predicted housing price.

Interactive Swagger documentation is available at:

/docs

🧪 Testing

The project includes automated tests covering:

Data processing
Data saving
Model predictions
FastAPI endpoints

Run the tests with:

pytest -v

🐳 Docker
Build the image
docker build -t mexico_housing_api .

Run the container
docker run -p 8000:8000 mexico_housing_api


The API will then be available at:

http://localhost:8000


Swagger documentation:

http://localhost:8000/docs

☁️ Deployment

The application is containerized using Docker and the image is stored on Docker Hub.

The container is deployed to Azure Container Apps, allowing the FastAPI application and trained ML model to run in the cloud.

Deployment workflow
Docker Image
     ↓
Docker Hub
     ↓
Azure Container Apps
     ↓
FastAPI API
     ↓
ML Prediction

🔄 CI/CD — Planned

The next stage of the project is to implement GitHub Actions CI/CD to automate the deployment workflow:

Git Push
   ↓
Run Tests
   ↓
Build Docker Image
   ↓
Push Image to Docker Hub
   ↓
Deploy to Azure

📌 Project Repository

The complete source code is available on GitHub:

https://github.com/MohamedMohsen20501990/Housing_in_Mexico.git