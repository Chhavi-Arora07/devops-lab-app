pipeline {
    agent any
    triggers { pollSCM('H/2 * * * *') }
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'docker build -t devops-lab-app:${BUILD_NUMBER} -t devops-lab-app:latest .' }
        }
        stage('Test') {
            steps { sh 'docker run --rm devops-lab-app:latest python -m pytest -q' }
        }
        stage('Deploy') {
            steps {
                sh 'docker rm -f devops-lab-app || true'
                sh 'docker run -d --name devops-lab-app -p 5000:5000 devops-lab-app:latest'
            }
        }
    }
    post {
        success { echo 'Pipeline succeeded, app deployed on port 5000' }
        failure { echo 'Pipeline failed, check the console output' }
        always  { sh 'docker image prune -f' }
    }
}