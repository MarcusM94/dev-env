        pipeline {
                agent { docker { image 'mcr.microsoft.com/windows-cssc/python3.7windows:ltsc2019' } }
        stages {
            stage('Build') {
                steps {
                    echo 'Fetching repos...'
                    git branch: 'main', credentialsId: '7acbb2e7-15ff-4412-ba2d-5911f34c887a', url: 'https://github.com/enxhiferko/TraceAnalyser'
                    git branch: 'main', credentialsId: '7acbb2e7-15ff-4412-ba2d-5911f34c887a', url: 'https://github.com/MarcusM94/CI-CD_Pipeline'
                    bat 'git'
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
