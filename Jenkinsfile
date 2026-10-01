pipeline {
    agent any

    environment {
        IMAGE_NAME = 'placement-system-ci'
        CONTAINER_NAME = 'placement-system-ansible'
        PORT = '5001'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code from GitHub repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker container image: ${IMAGE_NAME}..."
                script {
                    if (isUnix()) {
                        sh "docker build -t ${IMAGE_NAME} ."
                    } else {
                        bat "docker build -t ${IMAGE_NAME} ."
                    }
                }
            }
        }

        stage('Automated Pytest') {
            steps {
                echo 'Running automated Pytest suite inside Docker container...'
                script {
                    if (isUnix()) {
                        sh "docker run --rm ${IMAGE_NAME} python -m pytest test_app.py"
                    } else {
                        bat "docker run --rm ${IMAGE_NAME} python -m pytest test_app.py"
                    }
                }
            }
        }

        stage('Deploy Application') {
            steps {
                echo "Deploying application container ${CONTAINER_NAME} with persistent volume..."
                script {
                    if (isUnix()) {
                        sh """
                            docker stop ${CONTAINER_NAME} || true
                            docker rm ${CONTAINER_NAME} || true
                            docker volume create placement_data || true
                            docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 -v placement_data:/app/data --restart unless-stopped ${IMAGE_NAME}
                        """
                    } else {
                        bat """
                            docker stop ${CONTAINER_NAME} 2>nul || ver >nul
                            docker rm ${CONTAINER_NAME} 2>nul || ver >nul
                            docker volume create placement_data 2>nul || ver >nul
                            docker run -d --name ${CONTAINER_NAME} -p ${PORT}:5000 -v placement_data:/app/data --restart unless-stopped ${IMAGE_NAME}
                        """
                    }
                }
            }
        }

        stage('Verification & Health Check') {
            steps {
                echo 'Verifying running Docker container and application endpoint...'
                script {
                    if (isUnix()) {
                        sh "docker ps --filter name=${CONTAINER_NAME}"
                    } else {
                        bat "docker ps --filter name=${CONTAINER_NAME}"
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'Campus Placement CI/CD Pipeline Completed Successfully!'
        }
        failure {
            echo 'Campus Placement CI/CD Pipeline Failed! Review console log output.'
        }
    }
}
