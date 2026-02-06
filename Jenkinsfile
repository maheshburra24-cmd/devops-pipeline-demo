pipeline {
    agent any

    stages {

        stage('Deploy on EC2 Host') {
            steps {
                sh '''
                  echo "Deploying application on EC2 host..."

                  ssh -o StrictHostKeyChecking=no ubuntu@localhost << 'EOF'
                    cd /home/ubuntu/devops-pipeline-demo

                    echo "Pulling latest code..."
                    git pull origin main

                    echo "Stopping old Flask app..."
                    pkill -f app.py || true

                    echo "Starting Flask app..."
                    nohup python3 app.py > app.log 2>&1 &
                  EOF
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
