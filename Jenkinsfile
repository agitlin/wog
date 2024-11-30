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
                    docker.build("${DOCKER_IMAGE}")
                }
            }
        }

        stage('Run') {
            steps {
                script {
                    docker.image("${DOCKER_IMAGE}:latest").run('-p 8777:8777 --name wog')
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