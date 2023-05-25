pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/your/repo.git'
            }
        }
        
        stage('Build and Deploy Frontend') {
            // agent {
            //     label 'frontend'
            // }
            steps {
                scripts{
                    sh """
                    cd frontend
                    npm install // Or any other build commands for your frontend
                    
                    // Deploy frontend to the frontend EC2 instance
                    scp  -r frontend/ ssh root@10.1.3.5:/root/
                    """
                }

            }
        }
        
        stage('Build and Deploy Backend') {
            // agent {
            //     label 'backend'
            // }
            steps {
                scripts{
                    sh """
                    cd backend  
                    // Deploy backend to the backend EC2 instance
                    scp -r backend/ root@10.1.3.53:/root/
                    """
                }

            }
        }
    }
}
