        pipeline {
        agent any
        stages {
            stage('Build') {
                steps {
                    echo 'Fetching repos...'
                    bat 'java --version'    
                    bat 'git --version'
                }
            }
             stage('Run Parallel Tests'){
                     parallel{
                             stage('Trace Analysis'){
                                     steps{
                                           echo 'Starting Trace Testing...'
                                     }
                             }
                             stage('Timing Requirment Testing'){
                                     steps{
                                           echo 'Starting Timing Requirment Testing...'
                                     }
                             }                                 
                     }
             }
                
        }
    }
