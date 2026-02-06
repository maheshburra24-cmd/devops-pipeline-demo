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
                    COMMIT_MSG=$(git log -1 --pretty=%B | tr -d '"' | tr -d "'")
                    NEW_PRICE=$(cat data/price.txt)

                    echo "$TIMESTAMP" > data/deploy_info.txt
                    echo "$COMMIT_HASH" >> data/deploy_info.txt
                    echo "SUCCESS" >> data/deploy_info.txt
                    echo "GitHub Push" >> data/deploy_info.txt

                    echo "Updated price: $NEW_PRICE"
                '''
            }
        }

        stage('Sync Code to Production Directory') {
            steps {
                sh '''
                    echo "Syncing latest code to live application directory..."
                    cd /home/ubuntu/devops-pipeline-demo
                    git pull origin main
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
