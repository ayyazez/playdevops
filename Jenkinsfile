pipeline {
    agent any
    
    environment {
        // Docker Configuration
        DOCKER_REGISTRY = 'https://docker.io/'
        DOCKER_CREDENTIALS_ID = 'dockerhub-creds'
        DOCKER_IMAGE_BACKEND = 'akhan101/product-backend'
        DOCKER_IMAGE_FRONTEND = 'akhan101/product-frontend'
        DOCKER_IMAGE_Nginx = 'akhan101/product-nginx'
        DOCKER_IMAGE_DATABASE = 'postgres'
        
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
                        docker.build("${DOCKER_IMAGE_BACKEND}:new")
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
                        docker.build("${DOCKER_IMAGE_FRONTEND}:new")
                    }
                }
            }
        }
          stage('Build Nginx') {
            steps {
                echo '🔨 Building Nginx Docker Image...'
                dir('nginx') {
                    script {
                        sh 'ls -la'
                        dockerImageNginx = docker.build("${DOCKER_IMAGE_Nginx}:${IMAGE_TAG}")
                        docker.build("${DOCKER_IMAGE_Nginx }:new")
                    }
                }
            }
        }

         stage('Test Frontend') {
            steps {
                echo '🧪 Testing Frontend...'
                dir('frontend') {
                    sh '''
                        # Create a Docker network for front-end
                        docker network create app-network
                        # Run front-end container for testing
                        docker run -d  -p 3001:3000 --name frontend  --network app-network  ${DOCKER_IMAGE_FRONTEND}:${IMAGE_TAG}
                        
                        # Wait for container to be ready
                        sleep 10
                        
                        # Test health endpoint
                       # curl -f http://18.220.180.174:3001 || exit 1
                        
                        # Cleanup
                        # docker stop test-backend
                        # docker rm test-backend
                    '''
                }
            }
        }
        stage('Test Nginx') {
            steps {
                echo '🧪 Testing Nginx...'
                dir('nginx') {
                    sh '''
                        
                        # Run nginx containers for testing
                        docker run -d -p 80:80 --name nginx --network app-network ${DOCKER_IMAGE_Nginx}:${IMAGE_TAG}
                        
                    '''
                }
            }
        }
/*        stage('Test Backend') {
            steps {
                echo '🧪 Testing Backend...'
                dir('backend') {
                    sh '''
                        # Run backend container for testing
                        docker run -d --name backend -p 5001:5000 ${DOCKER_IMAGE_BACKEND}:${IMAGE_TAG}
                        
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
        */
/*          stage('Test Database old ') {
        // ─────────────────────────────────────────
            steps {
                echo '🧪 Testing Database Container...'
                sh '''
                    echo Starting test database container...
                docker run -d \
                --name test-database \
                -e POSTGRES_DB=$DB_NAME \
                -e POSTGRES_USER=$DB_USER \
                -e POSTGRES_PASSWORD=$DB_PASSWORD \
                -p 5433:5432 \
                $IMG_DATABASE:$IMAGE_TAG

            echo "Waiting for database to initialize..."
            sleep 20

            echo "Testing database connection..."
            docker exec test-database pg_isready -U $DB_USER -d $DB_NAME || exit 1

            echo "Checking products table exists and has data..."
            docker exec test-database psql -U $DB_USER -d $DB_NAME -c "SELECT COUNT(*) FROM products;" || exit 1

            echo "Database tests passed!"
                '''
            }
        }
   */
    stage('Test Database Connection') {
            steps {
                echo '🧪 Testing Database...'
                sh '''
                    # Start database container
                    docker run -d --name test-database \
                        -e POSTGRES_DB=productdb \
                        -e POSTGRES_USER=productuser \
                        -e POSTGRES_PASSWORD=productpass \
                        -p 5433:5432 \
                        ${DOCKER_IMAGE_DATABASE}:15-alpine
                    
                    # Wait for database to be ready
                    sleep 15
                    
                    # Test database connection
                    docker exec test-database pg_isready -U productuser -d productdb || exit 1
                    
                    # Check if table exists and has data
                    # docker exec test-database psql -U productuser -d productdb -c "SELECT COUNT(*) FROM products;" 
                    
                    # Cleanup
                     docker stop test-database
                     docker rm test-database
                '''
            }
        }
        stage('Test Backend with Database') {
            steps {
                echo '🧪 Testing Backend with Database...'
                sh '''
                    # Create network for testing
                    # docker network create test-network || true
                    
                    # Start database
                    docker run -d --name test-db \
                        --network app-network \
                        -e POSTGRES_DB=productdb \
                        -e POSTGRES_USER=productuser \
                        -e POSTGRES_PASSWORD=productpass \
                        ${DOCKER_IMAGE_DATABASE}:15-alpine
                    
                    # Wait for database
                    sleep 15
                    
                    # Start backend
                    docker run -d --name test-backend \
                        --network test-network \
                        -p 5001:5000 \
                        -e DB_TYPE=postgresql \
                        -e DB_USER=productuser \
                        -e DB_PASSWORD=productpass \
                        -e DB_HOST=test-db \
                        -e DB_PORT=5432 \
                        -e DB_NAME=productdb \
                        ${DOCKER_IMAGE_BACKEND}:${IMAGE_TAG}
                    
                    # Wait for backend to connect to database
                    sleep 20
                    
                    # Test health endpoint
                   # curl -f http://localhost:5001/api/health || exit 1
                    
                    # Test products endpoint
                    # curl -f http://localhost:5001/api/products || exit 1
                    
                    # Cleanup
                   # docker stop test-backend test-db
                   # docker rm test-backend test-db
                   # docker network rm test-network
                '''
            }
        }
       /*  // ─────────────────────────────────────────
        stage('Test Backend + Database old') {
        // ─────────────────────────────────────────
            steps {
                echo '🧪 Testing Backend connected to Database...'
                sh '''
                    echo Creating test network...
                    echo Starting test database on network...
                    docker run -d \
                        --name test-db \
                        --network test-network \
                        -e POSTGRES_DB=%DB_NAME% \
                        -e POSTGRES_USER=%DB_USER% \
                        -e POSTGRES_PASSWORD=%DB_PASSWORD% \
                        %IMG_DATABASE%:%IMAGE_TAG%
                    echo Waiting for database to be ready...
                    sleep 20
                    echo Starting test backend on network...
                    docker run -d \
                        --name test-backend \
                        --network test-network \
                        -p 5001:5000 \
                        -e DB_TYPE=postgresql \
                        -e DB_HOST=test-db \
                        -e DB_PORT=%DB_PORT% \
                        -e DB_USER=%DB_USER% \
                        -e DB_PASSWORD=%DB_PASSWORD% \
                        -e DB_NAME=%DB_NAME% \
                        %IMG_BACKEND%:%IMAGE_TAG%
                    echo Waiting for backend to connect to database...
                    sleep 25 
                    echo Testing health endpoint...
                     curl -f http://localhost:5001/api/health || exit /b 1 
                    echo Testing products endpoint...
                     curl -f http://localhost:5001/api/products || exit /b 1 
                    echo All backend + database tests passed!
                '''
            }
        }        */
        stage('Push to Registry') {
            steps {
                echo '📤 Pushing Docker Images to Registry...'
                script {
                    docker.withRegistry("",
                    "${DOCKER_CREDENTIALS_ID}") {
                        
                        // Push nginx images
                        dockerImageNginx.push("${IMAGE_TAG}")
                        dockerImageNginx.push("new")
                        
                        // Push backend images
                        dockerImageBackend.push("${IMAGE_TAG}")
                        dockerImageBackend.push("new")
                        
                        // Push frontend images
                        dockerImageFrontend.push("${IMAGE_TAG}")
                        dockerImageFrontend.push("new")

                        
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
               cd /root/project/playdevops
            '''
            // Clean workspace
            cleanWs()
        }
    }
}
