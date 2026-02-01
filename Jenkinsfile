pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub'
                checkout scm
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                  echo "Stopping old Flask app (if running)..."
                  pkill -f app.py || true

                  echo "Starting new Flask app..."
                  nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful. Website updated.'
        }
        failure {
            echo '❌ Deployment failed. Check logs.'
        }
    }
}
