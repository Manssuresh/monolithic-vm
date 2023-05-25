 pipeline{
    agent any
    parameters{
        string(name: 'flaskbucketname', defaultValue: 'flaskbucketname', description: 'bucket name')
        string(name: 'backendhost', defaultValue: 'backendhost', description: 'host name')
    }
    stages{
        stage('Build') {
            steps {
                script{
                sh '''
                cd backend
                echo 'Building Flask application...'
                rm -fr *.zip
                zip -r flask-$BUILD_NUMBER.zip *
                aws s3 cp flask-$BUILD_NUMBER.zip s3://${flaskbucketname}/
                scp dependencies.sh root@${backendhost}:/root/
                rm -fr *
                echo 'Flask application built successfully!'
                '''
                }
            }
        }
        stage('Deploy') {
            steps {
                script{
                sh '''
                echo 'Deploying Flask application...'
                ssh root@${backendhost} "rm -rf *"
                aws s3 cp s3://${flaskbucketname}/flask-$BUILD_NUMBER.zip .
                scp flask-$BUILD_NUMBER.zip root@${backendhost}:/root/
                ssh root@${backendhost} "unzip flask-$BUILD_NUMBER.zip"
                ssh root@${backendhost} "sudo rm -rf *.zip"
                rm -fr *.zip
                echo 'Flask application deployed successfully!'
                '''
                }
            }
        }
        stage('Installation'){
            steps{
                script{
                sh '''
                echo 'installing the dependencies...'
                ssh root@${backendhost} "sh dependencies.sh"
                echo 'installed successfully'
                '''
                }
            }
        }
        stage('Run'){
            steps{
                script{
                sh '''
                echo 'running the flask application'
                ssh root@${backendhost} "nohup python3 app.py &"
                echo 'completed successfully'
                '''
                }
            }
        }
        stage('confirmation'){
            steps{
                script{
                    sh '''
                    ssh root@${backendhost} "sudo netstat -anlp | grep '80'"
                    '''
                }
            }
        }
    }
}