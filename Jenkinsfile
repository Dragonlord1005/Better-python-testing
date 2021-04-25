// Jenkinsfile (Declarative Pipeline)
pipeline {
    agent any 
    stages {
        stage('Build') { 
            steps {
                bat 'poetry shell'
                bat 'poetry install'
            }
        }
        stage('Test') { 
            steps {
                bat 'pytest'
            }
        }
        stage('Deploy') { 
            steps {
                bat 'pyinstaller test.py -y'
            }
        }
    }
}