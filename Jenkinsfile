pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Record Deployment Metadata') {
            steps {
                sh '''
                  TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                  COMMIT_HASH=$(git rev-parse --short HEAD)
                  COMMIT_MSG=$(git log -1 --pretty=%B | tr -d '"' | tr -d "'")

                  NEW_PRICE=$(cat data/price.txt)
                  OLD_PRICE=$(git show HEAD~1:data/price.txt 2>/dev/null || echo "N/A")

                  echo "$TIMESTAMP" > data/deploy_info.txt
                  echo "$COMMIT_HASH" >> data/deploy_info.txt
                  echo "Success" >> data/deploy_info.txt
                  echo "GitHub Push" >> data/deploy_info.txt

                  echo "$OLD_PRICE" > data/change_log.txt
                  echo "$NEW_PRICE" >> data/change_log.txt
                  echo "$COMMIT_MSG" >> data/change_log.txt
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                  pkill -f app.py || true
                  nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Deployment successful – website updated'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}
