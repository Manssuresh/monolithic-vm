pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                git branch: 'feature', url: 'https://github.com/kalpanaIronbanda/monolithic-vm.git'
            }
        }
        

        
        stage('Build and Deploy Backend') {
            steps {
                script{
                sh """
                cd backend
                #Or any other build commands for your backend
                
                #Deploy backend to the backend EC2 instance
                scp -r * root@10.1.3.53:/root/
                ssh root@10.1.3.53 'sh dependencies.sh'
                """
                }
            }
        }
        stage('Run the Backend app'){
            steps{
                script{
                    sh """
                    echo 'running the app....'
                    ssh root@10.1.3.53 'nohup python3 app.py &'
                    echo 'running succcessfully'
                    ssh root@10.1.3.53 'netstat -anlp | grep 80 -w'
                    """
                }
            }
        }
        // stage('Build and Deploy Frontend') {
        //     steps {
        //         script{
        //         sh """
        //         cd frontend // Or any other build commands for your frontend
                
        //         // Deploy frontend to the frontend EC2 instance
        //         scp -r frontend/ root@10.1.3.5:/root/
        //         """
        //         }
        //     }
        // }
    }
}
