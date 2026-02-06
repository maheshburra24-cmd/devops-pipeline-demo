pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Deploy Application') {
            steps {
                sh '''
                    if ! command -v python3 >/dev/null 2>&1; then
                      apt update
                      apt install -y python3 python3-venv python3-pip
                    fi

                    if [ ! -d "venv" ]; then
                      python3 -m venv venv
                      . venv/bin/activate
                      pip install -r requirements.txt
                    fi

                    pkill -9 -f app.py || true
                    nohup ./venv/bin/python app.py > app.log 2>&1 &
                '''
            }
        }
    }

    post {
        success {
            echo 'Website updated successfully'
        }
    }
}
