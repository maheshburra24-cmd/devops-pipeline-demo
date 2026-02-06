pipeline {
    agent any

    stages {

        stage('Update Code') {
            steps {
                sh '''
                  git config --global --add safe.directory /home/ubuntu/devops-pipeline-demo
                  cd /home/ubuntu/devops-pipeline-demo
                  git fetch origin
                  git reset --hard origin/main
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
