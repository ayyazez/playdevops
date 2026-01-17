pipeline {
    agent any

    environment {
        // Application Configuration
        APP_NAME = 'product-management-app'
        DEPLOY_SERVER = '18.218.197.108'
        DEPLOY_USER = 'root'
        DEPLOY_PATH = '/root/project/playdevops'
        SSH_CREDENTIALS_ID = 'aws-server-ssh-key'

        // Backend Configuration
        PYTHON_VERSION = 'python3'
        BACKEND_PORT = '5000'

        // Frontend Configuration
        NODE_VERSION = '20.19.2'
        FRONTEND_PORT = '3000'
    }

    stages {

        stage('Checkout') {
            steps {
                echo '📥 Checking out code from repository...'
                checkout scm
                sh 'ls -la'
            }
        }

        stage('Setup Backend Environment') {
            steps {
                echo '🔧 Setting up Python virtual environment...'
                dir('backend') {
                   sh '''
                set -e

                echo "Checking Python version..."
                python3 --version

                echo "Creating virtual environment..."
                python3 -m venv venv

                echo "Upgrading pip..."
                venv/bin/pip install --upgrade pip

                echo "Installing dependencies..."
                venv/bin/pip install -r requirements.txt

                echo "Backend environment setup complete!"
            '''
                }
            }
        }

        stage('Setup Frontend Environment') {
            steps {
                echo '🔧 Installing Node.js dependencies...'
                dir('frontend') {
                    sh '''
                    set -e
    
                    echo "Checking Node and NPM versions..."
                    node --version
                    npm --version
    
                    echo "Cleaning old files..."
                    rm -rf node_modules build package-lock.json
    
                    echo "Configuring npm for CI..."
                    npm config set fetch-retries 5
                    npm config set fetch-retry-mintimeout 20000
                    npm config set fetch-retry-maxtimeout 120000
    
                    echo "Installing dependencies..."
                    npm install --no-audit --no-fund
    
                    echo "Frontend environment setup complete!"
                '''
                }
            }
        }
        

        stage('Build Backend') {
            steps {
                echo '🧪 Building Backend...'
                dir('backend') {
                    sh '''
                        set -e
                                 
                        echo "Starting backend server..."
                        venv/bin/python3 app.py &
                        BACKEND_PID=$!

                        echo "Waiting for backend to start..."
                        sleep 60

                        echo "Testing API endpoints..."
                        curl -f http://18.218.197.108:5000/api/health
                        curl -f http://18.218.197.108:5000/api/products

                        echo "Build Successfully!"

                    '''
                }
            }
        }

        stage('Build Frontend') {
            steps {
                echo '🔨 Building Frontend for production...'
                dir('frontend') {
                    sh '''
                        set -e
                        echo "Building React application..."
                        export REACT_APP_API_URL=http://${DEPLOY_SERVER}:5000/api
                        npm run build

                        echo "Build complete!"
                        ls -la build
                    '''
                }
            }
        }

        stage('Package Application') {
            steps {
                echo '📦 Packaging application for deployment...'
                sh '''
                    set -e
                    rm -rf deployment
                    mkdir -p deployment/backend deployment/frontend

                    echo "Copying backend files..."
                    cp backend/*.py deployment/backend/
                    cp backend/requirements.txt deployment/backend/
                    if [ -d backend/instance ]; then
                        cp -r backend/instance deployment/backend/
                    fi

                    echo "Copying frontend build..."
                    cp -r frontend/build deployment/frontend/

                    echo "Package created successfully!"
                    ls -R deployment
                '''
            }
        }

        /* stage('Deploy to Server') {
            steps {
                echo '🚀 Deploying to Production Server...'
                withCredentials([
                    sshUserPrivateKey(
                        credentialsId: "${SSH_CREDENTIALS_ID}",
                        keyFileVariable: 'SSH_KEY'
                    )
                ]) {
                    sh '''
                        set -e
                        chmod 600 $SSH_KEY

                        echo "Copying files to server..."
                        scp -i $SSH_KEY -r deployment/backend/* \
                            ${DEPLOY_USER}@${DEPLOY_SERVER}:${DEPLOY_PATH}/backend/

                        scp -i $SSH_KEY -r deployment/frontend/build \
                            ${DEPLOY_USER}@${DEPLOY_SERVER}:${DEPLOY_PATH}/frontend/

                        echo "Running deployment script on server..."
                        ssh -i $SSH_KEY ${DEPLOY_USER}@${DEPLOY_SERVER} "
                            cd ${DEPLOY_PATH} &&
                            chmod +x deploy.sh &&
                            ./deploy.sh
                        "

                        echo "Deployment complete!"
                    '''
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                echo '✅ Verifying Deployment...'
                sh '''
                    set -e
                    echo "Testing backend..."
                    curl -f http://${DEPLOY_SERVER}:5000/api/health

                    echo "Testing products endpoint..."
                    curl -f http://${DEPLOY_SERVER}:5000/api/products

                    echo "Testing frontend..."
                    curl -f http://${DEPLOY_SERVER}/

                    echo "All tests passed! Deployment successful!"
                '''
            }
        }
        */
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
            sh 'echo "Build Number: $BUILD_NUMBER"'
            sh 'date'
        }

        failure {
            echo '❌ Pipeline failed! Check logs for details.'
        }

        always {
            echo '🧹 Cleaning up...'
            sh '''
                //pkill -f "python app.py" || true
                //rm -rf deployment
                echo "Cleanup complete!"
            '''
            cleanWs()
        }
    }
}
