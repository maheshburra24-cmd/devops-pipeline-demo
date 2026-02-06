pipeline {
    agent any

    options {
        disableConcurrentBuilds()
        buildDiscarder(logRotator(numToKeepStr: '10'))
    }

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Record Change Info') {
            steps {
                sh '''
                TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
                COMMIT=$(git rev-parse --short HEAD)
                PRICE=$(cat data/price.txt)

                echo "$TIMESTAMP" > data/deploy_info.txt
                echo "$COMMIT" >> data/deploy_info.txt
                echo "SUCCESS" >> data/deploy_info.txt
                echo "GitHub Push" >> data/deploy_info.txt

                echo "Updated price: $PRICE"
                '''
            }
        }
    }

    post {
        success {
            echo "CI pipeline finished successfully"
        }
        failure {
            echo "CI pipeline failed"
        }
    }
}
