pipeline {
  agent any
  
  stages {
    stage('Build Docker Image') {
      steps {
	git branch: 'main', url: 'https://github.com/hdubouillon/Resful-ML-endpoint'
        script {
		docker.build("hdubouillon/restful-ml-endpoint")
                }
      }
    }
    stage('Run Tests') {
      steps {
        sh 'docker run resful-ml-endpoint unittest app/test_main.py'
      }
    }
  }
  
  post {
    always {
      sh 'docker login -u $DOCKER_USERNAME -p $DOCKER_PASSWORD'
      sh 'docker push resful-ml-endpoint'
    }
  }
}