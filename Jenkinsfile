pipeline {
    agent any

    stages {

        stage('Checkout Code') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/sandipkharat7272-source/jenkins-demo1.git'
            }
        }

        stage('Extract Data') {
            steps {
                echo 'Extracting data'
            }
        }

    }
}
