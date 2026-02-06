pipeline {
    agent any

    stages {

        stage('Pull Latest Code') {
            steps {
                sh '''
                  cd /home/ubuntu/devops-pipeline-demo
                  git pull origin main
                '''
            }
        }

        stage('Record Deployment Metadata') {
            steps {
                sh '''
                  cd /home/ubuntu/devops-pipeline-demo

                  TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                  COMMIT_HASH=$(git rev-parse --short HEAD)
                  COMMIT_MSG=$(git log -1 --pretty=%B | tr -d '"' | tr -d "'")

                  NEW_PRICE=$(cat data/price.txt)

                  echo "$TIMESTAMP" > data/deploy_info.txt
                  echo "$COMMIT_HASH" >> data/deploy_info.txt
                  echo "Success" >> data/deploy_info.txt
                  echo "Jenkins Manual" >> data/deploy_info.txt

                  echo "$NEW_PRICE" > data/change_log.txt
                  echo "$COMMIT_MSG" >> data/change_log.txt
                '''
            }
        }

        stage('Restart Application') {
            steps {
                sh '''
                  sudo pkill -f app.py || true
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
