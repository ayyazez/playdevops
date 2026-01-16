pipeline {
    agent any
    
    environment {
        // Application Configuration
        APP_NAME = 'product-management-app'
        DEPLOY_SERVER = '3.145.72.236'
        DEPLOY_USER = 'root'
        DEPLOY_PATH = '/root/project/playdevops'
        SSH_CREDENTIALS_ID = 'aws-server-ssh-key'
        
        // Backend Configuration
        PYTHON_VERSION = 'python'
        BACKEND_PORT = '5000'
        
        // Frontend Configuration
        NODE_VERSION = 'node'
        FRONTEND_PORT = '3000'
    }
    
    stages {
        stage('Checkout') {
            steps {
                echo '📥 Checking out code from repository...'
                checkout scm
                bat 'dir'
            }
        }
        
        stage('Setup Backend Environment') {
            steps {
                echo '🔧 Setting up Python virtual environment...'
                dir('backend') {
                    bat '''
                        @echo off
                        echo Checking Python version...
                        python --version
                        
                        echo Creating virtual environment...
                        if exist venv rmdir /s /q venv
                        python -m venv venv
                        
                        echo Activating virtual environment...
                        call venv\\Scripts\\activate.bat
                        
                        echo Upgrading pip...
                        python -m pip install --upgrade pip
                        
                        echo Installing dependencies...
                        pip install -r requirements.txt
                        
                        echo Backend environment setup complete!
                    '''
                }
            }
        }
        
        stage('Setup Frontend Environment') {
            steps {
                echo '🔧 Installing Node.js dependencies...'
                dir('frontend') {
                    bat '''
                        @echo off
                        echo Checking Node version...
                        node --version
                        npm --version
                        
                        echo Cleaning old node_modules...
                        if exist node_modules rmdir /s /q node_modules
                        if exist build rmdir /s /q build
                        
                        echo Installing dependencies...
                        npm install
                        
                        echo Frontend environment setup complete!
                    '''
                }
            }
        }
        
        stage('Test Backend') {
            steps {
                echo '🧪 Testing Backend...'
                dir('backend') {
                    bat '''
                        @echo off
                        echo Starting backend server for testing...
                        call venv\\Scripts\\activate.bat
                        
                        echo Running backend in background...
                        start /B python app.py
                        
                        echo Waiting for server to start...
                        timeout /t 15 /nobreak
                        
                        echo Testing API endpoints...
                        curl -f http://localhost:5000/api/health || exit /b 1
                        curl -f http://localhost:5000/api/products || exit /b 1
                        
                        echo Tests passed!
                        
                        echo Stopping backend server...
                        taskkill /F /IM python.exe /T || exit /b 0
                    '''
                }
            }
        }
        
        stage('Build Frontend') {
            steps {
                echo '🔨 Building Frontend for production...'
                dir('frontend') {
                    bat '''
                        @echo off
                        echo Building React application...
                        set REACT_APP_API_URL=http://%DEPLOY_SERVER%:5000/api
                        npm run build
                        
                        echo Build complete!
                        dir build
                    '''
                }
            }
        }
        
    
        
     
        
        
    }
    
    post {
        success {
            echo '✅ Pipeline completed successfully!'
            bat 'echo Build Number: %BUILD_NUMBER%'
            bat 'echo Deployment Time: %DATE% %TIME%'
        }
        
        failure {
            echo '❌ Pipeline failed!'
            bat 'echo Check logs for details'
        }
        
        always {
            echo '🧹 Cleaning up...'
            bat '''
                @echo off
                REM Kill any remaining Python processes from testing
                taskkill /F /IM python.exe /T 2>nul || exit /b 0
                
                REM Clean deployment directory
                if exist deployment rmdir /s /q deployment
                
                echo Cleanup complete!
            '''
            cleanWs()
        }
    }
}
