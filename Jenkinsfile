pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Fetching latest code from GitHub'
                checkout scm
            }
        }

        stage('Record Change Metadata') {
            steps {
                sh '''
                    TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                    COMMIT_HASH=$(git rev-parse --short HEAD)
                    NEW_PRICE=$(cat data/price.txt)

                    echo "$TIMESTAMP" > data/deploy_info.txt
                    echo "$COMMIT_HASH" >> data/deploy_info.txt
                    echo "SUCCESS" >> data/deploy_info.txt
                    echo "GitHub Push" >> data/deploy_info.txt

                    echo "Updated price: $NEW_PRICE"
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    echo "Stopping existing Flask app if running..."
                    pkill -f app.py || true

                    echo "Starting Flask app from Jenkins workspace..."
                    nohup ./venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully. Website updated.'
        }
        failure {
            echo 'Pipeline failed. Check console logs.'
        }
    }
}
