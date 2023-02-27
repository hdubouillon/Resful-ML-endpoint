pipeline {
    agent any

    triggers {
        githubPush("https://github.com/hdubouillon/Resful-ML-endpoint")
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    def dockerImage = docker.build("hdubouillon/restful-ml-endpoint")
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    def testCommand = "python app/test_main.py"
                    def testExitCode = dockerImage.inside("-p 5000:5000") {
                        sh testCommand
                    }
                    if (testExitCode != 0) {
                        error "Tests failed!"
                    }
                }
            }
        }
        stage('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub') {
                        def customImage = dockerImage.push()
                    }
                }
            }
        }
    }
}