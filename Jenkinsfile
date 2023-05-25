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
                echo 'Building Flask application...'
                rm -fr *.zip
                zip -r college-$BUILD_NUMBER.zip *
                aws s3 cp college-$BUILD_NUMBER.zip s3://flask-package-bucket/
                scp dependencies.sh root@10.1.3.53:/root/
                rm -fr *
                echo 'Flask application built successfully!'
                ssh root@10.1.3.53 'sh dependencies.sh'

                echo 'Deploying Flask application...'
                ssh root@10.1.3.53 "rm -rf *"
                aws s3 cp s3://flask-package-bucket/college-$BUILD_NUMBER.zip .
                scp college-$BUILD_NUMBER.zip root@10.1.3.53:/root/
                ssh root@10.1.3.53 "unzip college-$BUILD_NUMBER.zip"
                ssh root@10.1.3.53 "rm -rf *.zip"
                rm -fr *.zip
                echo 'Flask application deployed successfully!
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
