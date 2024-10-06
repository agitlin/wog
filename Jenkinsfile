pipeline {
    agent any

    stages {
        stage('Hello') {
            steps {
                git branch: 'main', url: 'https://github.com/agitlin/wog.git'
                sh 'python stam.py'
            }
        }
    }
}
