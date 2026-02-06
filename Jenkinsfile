pipeline {
    agent any

    stages {

        stage('Clone Latest Code') {
            steps {
                sh '''
                  rm -rf /tmp/devops-pipeline-demo
                  git clone https://github.com/maheshburra24-cmd/devops-pipeline-demo.git /tmp/devops-pipeline-demo
                '''
            }
        }

        stage('Sync Code to EC2 App Folder') {
            steps {
                sh '''
                  sudo mkdir -p /home/ubuntu/devops-pipeline-demo
                  sudo rsync -av --delete \
                    /tmp/devops-pipeline-demo/ \
                    /home/ubuntu/devops-pipeline-demo/
                '''
            }
        }

        stage('Record Deployment Metadata') {
            steps {
                sh '''
                  cd /home/ubuntu/devops-pipeline-demo

                  TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                  COMMIT_HASH=$(git -C /tmp/devops-pipeline-demo rev-parse --short HEAD)
                  COMMIT_MSG=$(git -C /tmp/devops-pipeline-demo log -1 --pretty=%B | tr -d '"' | tr -d "'")

                  NEW_PRICE=$(cat data/price.txt)
                  OLD_PRICE=$(cat data/change_log.txt 2>/dev/null | head -n 1 || echo "N/A")

                  echo "$TIMESTAMP" > data/deploy_info.txt
                  echo "$COMMIT_HASH" >> data/deploy_info.txt
                  echo "Success" >> data/deploy_info.txt
                  echo "Manual Trigger" >> data/deploy_info.txt

                  echo "$OLD_PRICE" > data/change_log.txt
                  echo "$NEW_PRICE" >> data/change_log.txt
                  echo "$COMMIT_MSG" >> data/change_log.txt
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
            echo '✅ Deployment successful – website updated'
        }
        failure {
            echo '❌ Deployment failed'
        }
    }
}
