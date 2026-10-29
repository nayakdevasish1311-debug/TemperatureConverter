pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install --upgrade pip'
                sh 'if [ -f requirements.txt ]; then pip install -r requirements.txt; fi'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m unittest test_app.py'
            }
        }
    }
}
