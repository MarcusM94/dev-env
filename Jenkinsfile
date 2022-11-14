#!/usr/bin/env groovy

        pipeline {
                agent any
        stages {
            stage('Build') {
                steps {
                    echo 'Fetching repos...'
                    git branch: 'main', credentialsId: '7acbb2e7-15ff-4412-ba2d-5911f34c887a', url: 'https://github.com/enxhiferko/TraceAnalyser'
                    git branch: 'main', credentialsId: '7acbb2e7-15ff-4412-ba2d-5911f34c887a', url: 'https://github.com/MarcusM94/CI-CD_Pipeline'    
                    bat 'dir'
                }
            }
        }
    }
