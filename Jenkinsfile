pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps { checkout scm }
        }
        stage('Build') {
            steps { sh 'docker build -t devops-lab-app:${BUILD_NUMBER} -t devops-lab-app:latest .' }
        }
    }
}