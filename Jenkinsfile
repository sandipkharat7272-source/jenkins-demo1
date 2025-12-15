pipeline {
    agent any 
    stages {
        stages ('checkout code'){
            steps {
                checkout scm

            }
        }
        stages('extract data') {
           stages {
            bat "python extract .py"

           } 
        }  
    
    }
}