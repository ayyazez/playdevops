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
                        dockerImageBackend.push()          // push versioned image
                        dockerImageBackend.push('latest')  // push latest tag
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
                        dockerImageFrontend.push()          // push versioned image
                        dockerImageFrontend.push('latest')  // push latest tag
                    }
                }
            }
        }
    } // end stages

    post {
        success {
