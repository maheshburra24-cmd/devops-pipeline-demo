pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                echo 'Code already checked out from GitHub'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                  pip3 install -r requirements.txt
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                  python3 app.py &
                '''
            }
        }
    }
}
