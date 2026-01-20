pipeline {
    agent any
    
    environment {
        // Docker Configuration
        DOCKER_REGISTRY = 'https://index.docker.io/v1'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
        DOCKER_IMAGE_BACKEND = 'akhan101/product-backend'
        DOCKER_IMAGE_FRONTEND = 'akhan101/product-frontend'
        IMAGE_TAG = "${BUILD_NUMBER}"
        
        // Application Configuration
        APP_NAME = 'product-management-app'
        DEPLOY_SERVER = '192.168.10.172'
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

         stage('Test Frontend') {
            steps {
                echo '🧪 Testing Frontend...'
                dir('frontend') {
                    sh '''
                        # Run front-end container for testing
                        docker run -d --name test-frontend -p 80:80 ${DOCKER_IMAGE_FRONTEND}:${IMAGE_TAG}
                        
                        # Wait for container to be ready
                        sleep 10
                        
                        # Test health endpoint
                       # curl -f http://18.220.180.174:3000 || exit 1
                        
                        # Cleanup
                        # docker stop test-backend
                        # docker rm test-backend
                    '''
                }
            }
        }
        
        stage('Test Backend') {
            steps {
                echo '🧪 Testing Backend...'
                dir('backend') {
                    sh '''
                        # Run backend container for testing
                        docker run -d --name test-backend -p 5001:5000 ${DOCKER_IMAGE_BACKEND}:${IMAGE_TAG}
                        
                        # Wait for container to be ready
                        sleep 10
                        
                        # Test health endpoint
                        # curl -f http://18.220.180.174:5001/api/health || exit 1
                        
                        # Test products endpoint
                      #  curl -f http://18.220.180.174:5001/api/products || exit 1
                        
                        # Cleanup
                        # docker stop test-backend
                        # docker rm test-backend
                    '''
                }
            }
        }
        
        stage('Push to Registry') {
            steps {
                echo '📤 Pushing Docker Images to Registry...'
                script {
                    docker.withRegistry( "${DOCKER_REGISTRY}",
                    "${DOCKER_CREDENTIALS_ID}") {
                        // Push backend images
                        dockerImageBackend.push("${IMAGE_TAG}")
                        dockerImageBackend.push("latest")
                        
                        // Push frontend images
                        dockerImageFrontend.push("${IMAGE_TAG}")
                        dockerImageFrontend.push("latest")
                    }
                }
            }
        }
        
     /*   stage('Deploy to Server') {
            steps {
                echo '🚀 Deploying to Production Server...'
                sshagent(credentials: ["${SSH_CREDENTIALS_ID}"]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no ${DEPLOY_USER}@${DEPLOY_SERVER} '
                            # Navigate to application directory
                            cd /root/project/playdevops
                            
                            # Pull latest images
                            docker compose pull
                            
                            # Stop and remove old containers
                            docker compose down
                            
                            # Start new containers
                            docker compose up -d
                            
                            # Wait for health checks
                            sleep 20
                            
                            # Verify deployment
                            docker compose ps
                        '
                    """
                }
            }
        } */
        
        stage('Verify Deployment') {
            steps {
                echo '✅ Verifying Deployment...'
                script {
                    sh """
                        # Test backend
                      #  curl -f http://${DEPLOY_SERVER}:5000/api/health || exit 1
                        
                        # Test frontend
                        # curl -f http://${DEPLOY_SERVER}/ || exit 1
                    """
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
               # docker ps -a | grep test-backend | awk '{print $1}' | xargs -r docker rm -f || true
            '''
            // Clean workspace
            cleanWs()
        }
    }
}
