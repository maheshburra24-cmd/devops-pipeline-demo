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
                    # Capture metadata
                    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                    COMMIT_HASH=$(git rev-parse --short HEAD)
                    COMMIT_MSG=$(git log -1 --pretty=%B | tr -d '"' | tr -d "'")
                    NEW_PRICE=$(cat data/price.txt)
                    
                    # Try to get old price from previous commit, default to N/A if first commit
                    OLD_PRICE=$(git show HEAD~1:data/price.txt 2>/dev/null || echo "N/A")
                    
                    # Update deploy_info.txt (timestamp, hash, status, trigger)
                    echo "$TIMESTAMP" > data/deploy_info.txt
                    echo "$COMMIT_HASH" >> data/deploy_info.txt
                    echo "Success" >> data/deploy_info.txt
                    echo "GitHub Push" >> data/deploy_info.txt
                    
                    # Update change_log.txt (old_price, new_price, msg)
                    echo "$OLD_PRICE" > data/change_log.txt
                    echo "$NEW_PRICE" >> data/change_log.txt
                    echo "$COMMIT_MSG" >> data/change_log.txt
                '''
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
