pipeline {
    agent any

    stages {

        stage('Update Code') {
            steps {
                sh '''
                  cd /home/ubuntu/devops-pipeline-demo
                  git pull origin main
                '''
            }
        }

        stage('Restart Application') {
            steps {
                sh '''
                  pkill -f app.py || true
                  cd /home/ubuntu/devops-pipeline-demo
                  nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Website updated successfully'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}
