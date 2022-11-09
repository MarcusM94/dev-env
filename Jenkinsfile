        pipeline {
                agent { docker { image 'mcr.microsoft.com/windows-cssc/python3.7windows:ltsc2019' } }
        stages {
            stage('Build') {
                steps {
                    echo 'Fetching repos...'
                    git
                }
            }
        }
    }
