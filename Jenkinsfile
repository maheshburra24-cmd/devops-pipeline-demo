pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                  set -e

                  echo "Using Python:"
                  python3 --version

                  echo "Cleaning old virtual environment..."
                  rm -rf venv

                  echo "Creating virtual environment..."
                  python3 -m venv venv

                  echo "Activating virtual environment..."
                  . ./venv/bin/activate

                  echo "Installing dependencies..."
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  set -e

                  echo "Stopping any existing Flask app..."
                  pkill -f app.py || true

                  echo "Starting Flask app detached from Jenkins..."
                  . ./venv/bin/activate

                  setsid python app.py > app.log 2>&1 < /dev/null &
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
