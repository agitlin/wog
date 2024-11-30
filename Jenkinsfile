pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'agitlin/wog:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                url: 'https://github.com/agitlin/wog.git'
            }
                
        }

        stage('Build') {
            steps {
                script {
                    writeFile file: 'scores.txt', text: '69'
                    sh 'docker-compose build'
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    sh 'docker-compose start app'
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    try {
                        sh 'python3 test_scores_service.py'
                    } catch (Exception e) {
                        error "Tests failed"
                    }
                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker stop wog'
                    sh 'docker rm wog'
g                }
            }
        }
    }
}