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
        // One or more steps need to be included within the steps block.
        }
    }

    }
