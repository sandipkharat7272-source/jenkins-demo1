pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        stage('Extract Data') {
            steps {
                bat: 'https://github.com/sandipkharat7272-source/jenkins-demo1.git'

            }
        }

    }
}
