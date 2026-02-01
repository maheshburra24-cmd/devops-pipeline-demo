pipeline {
    agent any

    stages {

        stage('Checkout SCM') {
            steps {
                echo 'Code already checked out from GitHub'
            }
        }

        stage('Setup Python Virtual Environment & Install Dependencies') {
            steps {
                sh '''
                  python3 -m venv venv
                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                  . venv/bin/activate
                  nohup python3 app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo '✅ Application deployed successfully!'
        }
        failure {
            echo '❌ Pipeline failed. Check logs.'
        }
    }
}
