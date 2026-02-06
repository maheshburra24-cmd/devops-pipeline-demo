pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                sh '''
                  rm -rf devops-pipeline-demo
                  git clone https://github.com/maheshburra24-cmd/devops-pipeline-demo.git
                '''
            }
        }

        stage('Record Deployment Info') {
            steps {
                sh '''
                  cd devops-pipeline-demo

                  TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                  COMMIT_HASH=$(git rev-parse --short HEAD)
                  COMMIT_MSG=$(git log -1 --pretty=%B | tr -d '"' | tr -d "'")
                  NEW_PRICE=$(cat data/price.txt)

                  OLD_PRICE=$(git show HEAD~1:data/price.txt 2>/dev/null || echo "N/A")

                  echo "$TIMESTAMP" > data/deploy_info.txt
                  echo "$COMMIT_HASH" >> data/deploy_info.txt
                  echo "Success" >> data/deploy_info.txt
                  echo "GitHub Push / Manual Build" >> data/deploy_info.txt

                  echo "$OLD_PRICE" > data/change_log.txt
                  echo "$NEW_PRICE" >> data/change_log.txt
                  echo "$COMMIT_MSG" >> data/change_log.txt
                '''
            }
        }

        stage('Build Website Image') {
            steps {
                sh '''
                  cd devops-pipeline-demo
                  docker build -t price-web .
                '''
            }
        }

        stage('Deploy Website Container') {
            steps {
                sh '''
                  docker stop price-web || true
                  docker rm price-web || true
                  docker run -d --name price-web -p 5000:5000 price-web
                '''
            }
        }
    }

    post {
        success {
            echo "✅ Deployment successful – price & metadata updated"
        }
        failure {
            echo "❌ Deployment failed"
        }
    }
}
