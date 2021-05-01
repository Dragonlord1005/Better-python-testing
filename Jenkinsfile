pipeline {
    agent any
    stages {
    stage('Poetry Setup') {
        steps {
            bat 'poetry shell'
            bat 'poetry lock'
            bat 'poetry install'
        }
    }

    stage('Test') {
        steps {
            bat 'poetry run pytest'
        }
    }

    stage('Build') {
        steps {
            bat 'poetry run pyinstaller gametest.py'
        }
    }

    }
