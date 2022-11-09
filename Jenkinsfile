        pipeline {
                agent docker { image 'mcr.microsoft.com/windows-cssc/python3.7windows:ltsc2019' }
        stages {
            stage('Build') {
                steps {
                    echo 'Fetching repos...'
                    git clone https://github.com/enxhiferko/TraceAnalyser.git
                    git clone https://github.com/MarcusM94/CI-CD_Pipeline.git
                    bat 'dir'
                }
            }
        }
    }
