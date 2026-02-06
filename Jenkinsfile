pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub'
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
                cd /var/jenkins_home/workspace/devops-price-pipeline

                # Ensure virtual environment exists
                if [ ! -d "venv" ]; then
                  apt update
                  apt install -y python3 python3-venv python3-pip
                  python3 -m venv venv
                  ./venv/bin/pip install -r requirements.txt
                fi

                # Start app only if not already running
                if pgrep -f app.py > /dev/null; then
                  echo "Flask app already running"
                else
                  echo "Starting Flask app"
                  nohup ./venv/bin/python app.py > app.log 2>&1 </dev/null &
                fi
                '''
            }
        }
    }

    post {
        success {
            echo 'Deployment successful. Website updated.'
        }
        failure {
            echo 'Deployment failed. Check logs.'
        }
    }
}
