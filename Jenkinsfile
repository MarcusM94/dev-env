        pipeline {
                agent { docker { image 'mcr.microsoft.com/windows-cssc/python3.7windows:ltsc2019' } }
        stages {
            stage('Build') {
                steps {
                    echo 'Fetching repos...'
                    git branch: 'main', credentialsId: '7acbb2e7-15ff-4412-ba2d-5911f34c887a', url: 'https://github.com/enxhiferko/TraceAnalyser'
                    bat 'dir'
                }
            }
        }
    }
