**Explore the Readme Folder for an in-depth overview.**

**End-to-End MLOps Project with ETL Pipelines - Building a Network Security System**

**Technology Stack Utilized for the MLOps Network Security System Project**

**Development Environment:**
- IDE: Visual Studio Code
- Version Control: GitHub
- Packaging: Python setup.py

**Backend Technologies:**
- Programming Language: Python
- Database: MongoDB Atlas
- Cloud Platform: AWS (EC2, S3, ECR)

**MLOps and Machine Learning Stack:**
- ML Framework: TensorFlow or PyTorch (used for model training)
- Experiment Tracking: MLflow
- Remote Experiment Repository: DagsHub
- Hyperparameter Tuning: Scikit-learn or Optuna

**Data Engineering:**
- ETL Pipeline: Python-based data processing
- Data Validation: Custom validation components
- Data Transformation: Pandas and NumPy

**DevOps and Deployment:**
- Containerization: Docker
- CI/CD: GitHub Actions
- Deployment: AWS EC2 instance
- Container Registry: AWS ECR

**Monitoring and Logging:**
- Logging: Custom logging implementation
- Exception Handling: Custom error management

**Key Project Components:**
- Network security system
- Machine learning model training
- Batch prediction pipeline
- Model artifact management


3.Reference : Krish Naik https://www.udemy.com/course/complete-mlops-bootcamp-with-10-end-to-end-ml-projects/



















### Network Security Projects For Phising Data

Setup github secrets:
AWS_ACCESS_KEY_ID=<your key>

AWS_SECRET_ACCESS_KEY=< your key>

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = 788614365622.dkr.ecr.us-east-1.amazonaws.com/networkssecurity
ECR_REPOSITORY_NAME = networkssecurity


Docker Setup In EC2 commands to be Executed
#optinal

sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker
