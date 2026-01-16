pipeline {
    agent any

    environment {
        // Docker Configuration
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_CREDENTIALS_ID = 'docker-hub-credentials'
        DOCKER_IMAGE_BACKEND = 'your-dockerhub-username/product-backend'
        DOCKER_IMAGE_FRONTEND = 'your-dockerhub-username/product-frontend'
        IMAGE_TAG = "${BUILD_NUMBER}"

        // Application Configuration
        APP_NAME = 'product-management-app'
        DEPLOY_SERVER = '3.145.72.236'
        DEPLOY_USER = 'root'
        SSH_CREDENTIALS_ID = 'aws-server-ssh-key'
    }

    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code from repository...'
                checkout scm
                bat 'dir'
            }
        }

        stage('Build Backend') {
            steps {
                echo '🔨 Building Backend Docker Image...'
                dir('backend') {
                    script {
                        bat 'dir'
                        def dockerImageBackend = docker.build("${DOCKER_IMAGE_BACKEND}:${IMAGE_TAG}")
                        dockerImageBackend.push()
                        dockerImageBackend.push('latest')
                    }
                }
            }
        }

        stage('Build Frontend') {
            steps {
                echo '🔨 Building Frontend Docker Image...'
                dir('frontend') {
                    script {
                        bat 'dir'
                        def dockerImageFrontend = docker.build("${DOCKER_IMAGE_FRONTEND}:${IMAGE_TAG}")
                        dockerImageFrontend.push()
                        dockerImageFrontend.push('latest')
                    }
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }

        failure {
            echo '❌ Pipeline failed!'
        }

        always {
            echo '🧹 Cleaning up...'
            bat """
                for /F "tokens=1" %%i in ('docker ps -a ^| findstr test-backend') do docker rm -f %%i
            """
            cleanWs()
        }
    }
}
