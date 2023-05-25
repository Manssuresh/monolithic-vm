pipeline {
    agent any

    environment {
        FRONTEND_INSTANCE = '10.1.3.5'
        BACKEND_INSTANCE = '10.1.3.53'
        FRONTEND_DEPLOY_PATH = '/root/'
        BACKEND_DEPLOY_PATH = '/root/'
        DB_HOST = 'python.cwvcthgt8zhp.ap-south-1.rds.amazonaws.com'
        DB_USER = 'thanshi'
        DB_PASSWORD = 'thanshi123'
        DB_NAME = 'pythonf'
        TABLE_NAME = 'studentlist'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature', url: 'https://github.com/kalpanaIronbanda/monolithic-vm.git'
            }
        }

        stage('Build and Deploy Backend') {
            steps {
                dir('backend') {
                    // Update backend configuration file with RDS credentials and table name
                    sh "sed -i 's|DB_HOST = .*|DB_HOST = \"${env.DB_HOST}\"|' app.py"
                    sh "sed -i 's|DB_USER = .*|DB_USER = \"${env.DB_USER}\"|' app.py"
                    sh "sed -i 's|DB_PASSWORD = .*|DB_PASSWORD = \"${env.DB_PASSWORD}\"|' app.py"
                    sh "sed -i 's|DB_NAME = .*|DB_NAME = \"${env.DB_NAME}\"|' app.py"
                    sh "sed -i 's|<tablename>|${env.TABLE_NAME}|' app.py"

                    // Deploy backend files to the backend EC2 instance
                    sh "scp -r * root@${env.BACKEND_INSTANCE}:${env.BACKEND_DEPLOY_PATH}"
                    sh "ssh root@${env.BACKEND_INSTANCE} \"cd ${env.BACKEND_DEPLOY_PATH} && sh dependencies.sh && nohup python3 app.py &\""
                    sh "ssh root@${env.BACKEND_INSTANCE} 'netstat -anlp | grep "80"'"
                    echo "successfully running the flask"

                    // Get the backend URL
                    script {
                        def backendUrl = sh (
                            script: "curl http://${env.BACKEND_INSTANCE}/",
                            returnStdout: true
                        ).trim()
                        env.BACKEND_URL = backendUrl
                    }
                }
            }
        }

        stage('Build and Deploy Frontend') {
            steps {
                dir('frontend') {
                    // Update frontend environment variables with backend URL
                    sh "sed -i 's|{{BACKEND_URL}}|${env.BACKEND_URL}|' src/app.js"
                    echo "updated successfully"

                    // Deploy frontend build to the frontend EC2 instance
                    sh "scp -r * root@${env.FRONTEND_INSTANCE}:${env.FRONTEND_DEPLOY_PATH}"
                    sh "ssh root@${env.FRONTEND_INSTANCE} 'yum install nodejs -y && cd ${env.FRONTEND_DEPLOY_PATH} && npm install && nohup npm start &'"
                }
            }
        }
    }
}
