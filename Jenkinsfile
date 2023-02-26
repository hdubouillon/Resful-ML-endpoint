pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                // Checkout code from Github repository
                git branch: 'main', url: 'https://github.com/hdubouillon/Resful-ML-endpoint'

                // Build Docker image
                script {
                    docker.build('Resful-ML-endpoint')
                }
            }
        }

        stage('Test') {
            steps {
                // Run unit tests
                sh 'pytest test_main.py'
            }
        }

        stage('Deploy') {
            steps {
                // Start a Docker container from the image
                script {
                    docker.withRegistry('https://registry.hub.docker.com', 'docker-hub-credentials-id') {
                        def customImage = docker.image('your-image-name').push('latest')
                        customImage.run('-p 5000:5000')
                    }
                }
            }
        }
    }

    // Trigger the pipeline whenever there is a new commit to the Github repository
    triggers {
        githubPush()
    }
}
