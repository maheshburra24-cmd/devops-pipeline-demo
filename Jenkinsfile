pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                  set -e

                  echo "Using Python:"
                  python3 --version

                  if [ ! -d "venv" ]; then
                    echo "Creating virtual environment..."
                    python3 -m venv venv
                  fi

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

                  echo "Restarting Flask app..."

                  pkill -f app.py || true

                  . ./venv/bin/activate
                  nohup python app.py > app.log 2>&1 &
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
