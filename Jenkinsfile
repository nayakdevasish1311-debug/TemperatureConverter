pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Run Tests') {
            steps {
                // If on Windows, Jenkins uses 'bat'. If on Linux/Mac, keep it as 'sh'
                bat 'python -m unittest test_app.py' 
            }
        }
    }
}
