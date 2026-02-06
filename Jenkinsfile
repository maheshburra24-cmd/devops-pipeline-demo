pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                  set -e

                  echo "Using Python:"
                  python3 --version

                  echo "Removing old virtual environment (if any)..."
                  rm -rf venv

                  echo "Creating fresh virtual environment..."
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

                  echo "Stopping old Flask app (if running)..."
                  pkill -f app.py || true

                  echo "Starting Flask app..."
                  . ./venv/bin/activate
                  python app.py &
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
