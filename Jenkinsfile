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
                sh 'ls -la'
            }
        }
        
        stage('Build Backend') {
            steps {
                echo '🔨 Building Backend Docker Image...'
                dir('backend') {
                    script {
                        sh 'ls -la'
                        dockerImageBackend = docker.build("${DOCKER_IMAGE_BACKEND}:${IMAGE_TAG}")
                        docker.build("${DOCKER_IMAGE_BACKEND}:latest")
                    }
                }
            }
        }
        
        stage('Build Frontend') {
            steps {
                echo '🔨 Building Frontend Docker Image...'
                dir('frontend') {
                    script {
                        sh 'ls -la'
                        dockerImageFrontend = docker.build("${DOCKER_IMAGE_FRONTEND}:${IMAGE_TAG}")
                        docker.build("${DOCKER_IMAGE_FRONTEND}:latest")
                    }
                }
            }
        }
        
    
    post {
        success {
            echo '✅ Pipeline completed successfully!'
            // Send success notification (optional)
        }
        
        failure {
            echo '❌ Pipeline failed!'
            // Send failure notification (optional)
        }
        
        always {
            echo '🧹 Cleaning up...'
            // Clean up test containers
            sh '''
                docker ps -a | grep test-backend | awk '{print $1}' | xargs -r docker rm -f || true
            '''
            // Clean workspace
            cleanWs()
        }
    }
}
