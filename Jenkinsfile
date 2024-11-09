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
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push riotwwks/test-cicd:latest'
      }
    }
    stage('Trigger CD Pipeline') {
      steps {
        script {
          echo 'Triggering CD pipeline...'
          build job: 'cd-pipeline-job', wait: false  // Триггер для CD pipeline
        }
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}