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
Pandas — data processing
Scikit-learn — machine learning
FastAPI — REST API
Pytest — automated testing
Docker — containerization
Docker Hub — container image registry
Azure Container Apps — cloud deployment
📁 Project Structure
housing_in_mexico/
├── data/
│   ├── raw/
│   └── processed/
├── models/
│   └── rf_model.pkl
├── notebooks/
├── src/
│   ├── data.py
│   ├── model.py
│   └── main.py
├── tests/
│   ├── test_data.py
│   ├── test_model.py
│   └── test_main.py
├── Dockerfile
├── requirements.txt
└── README.md

🔌 API

The model is exposed through a FastAPI endpoint:

POST /predict


Example request:

{
  "area": 60,
  "lat": 19.9,
  "lon": -99.8
}


The API returns the predicted housing price.

Swagger documentation is available at:

/docs

🧪 Testing

The project includes automated tests for data processing, model predictions, and the FastAPI endpoint.

Run the tests with:

pytest -v

🐳 Docker

Build the image:

docker build -t mexico_housing_api .


Run the container:

docker run -p 8000:8000 mexico_housing_api


The API will then be available at:

http://localhost:8000

☁️ Deployment

The application is containerized with Docker and deployed to Azure Container Apps using an image stored in Docker Hub.

The next stage of the project is to implement GitHub Actions CI/CD to automatically:

Run tests
Build the Docker image
Push the image to Docker Hub
Deploy the new version to Azure
📌 Project

GitHub repository:

https://github.com/MohamedMohsen20501990/Housing_in_Mexico.git