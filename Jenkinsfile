pipeline {
  agent any
  options {
    buildDiscarder(logRotator(numToKeepStr: '5'))
  }
  environment {
    DOCKERHUB_CREDENTIALS = credentials('riotwwks-dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t riotwwks/test-cicd:latest .'
      }
    }
    stage('Login') {
      steps {
        script {
          withCredentials([usernamePassword(credentialsId: 'riotwwks-dockerhub', usernameVariable: 'DOCKERHUB_USERNAME', passwordVariable: 'DOCKERHUB_PASSWORD')]) {
          sh 'echo $DOCKERHUB_PASSWORD | docker login -u $DOCKERHUB_USERNAME --password-stdin'
          }
        }
      }
    }
    stage('Push') {
      steps {
        sh 'docker push riotwwks/test-cicd:latest'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
