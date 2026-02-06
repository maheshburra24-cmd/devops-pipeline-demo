pipeline {
    agent any

    stages {

        stage('Setup Virtual Environment') {
            steps {
                sh '''
                  python3 --version

                  # Create virtual environment if not exists
                  if [ ! -d "venv" ]; then
                    python3 -m venv venv
                  fi

                  . venv/bin/activate
                  pip install --upgrade pip
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                  echo "Restarting Flask app..."

                  pkill -f app.py || true

                  . venv/bin/activate
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
