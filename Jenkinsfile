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
                    
                    def status= sh( returnStatus: true, script: 'python3 test_scores_service.py' )
                    if (status!=0) {
                        echo "Test failed"
                        failed
                    } else {
                        echo "Test suceeded"
                    }
                    

                }
            }
        }

        stage('Finalize') {
            steps {
                script {
                    sh 'docker-compose start app'
g                }
            }
        }
    }
}