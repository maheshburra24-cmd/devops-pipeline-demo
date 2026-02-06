pipeline {
    agent any

    stages {

        stage('Setup Python') {
            steps {
                sh '''
                  sudo apt-get update
                  sudo apt-get install -y python3 python3-pip
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                  python3 --version
                  pip3 install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  echo "Stopping old Flask app if running..."
                  pkill -f app.py || true

                  echo "Starting Flask app from Jenkins workspace..."
                  nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}
