pipeline {
    agent any 
    stages {
        stage('checkout code'){
            steps {
                checkout scm

            }
        }
        stages('extract data') {
           steps {
                bat "python extract.py"
                 
           } 
        }  
    
    }
}