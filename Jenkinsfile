pipeline {
    agent any

    options {
      ansiColor('xterm')
      disableConcurrentBuilds()
    }

    stages {
        stage ("Generate Distribution Archives"){
            when { branch 'master' }
            agent {
                docker { image 'python:3'}
            }
            steps {
                sh "python -m pip install setuptools wheel setupext-janitor"
                sh "python setup.py clean --all"
                sh "python setup.py sdist bdist_wheel"
            }
        }
        stage ("Upload to Test PyPi"){
            when { branch 'master' }
            agent {
                docker { image 'python:3'}
            }
            steps {
                sh "python -m pip install twine"
                withCredentials([usernamePassword(credentialsId: 'twine_login_credentials', usernameVariable: 'TWINE_USERNAME', passwordVariable: 'TWINE_PASSWORD')]) {
                    sh 'python -m twine upload dist/* -u $TWINE_USERNAME -p $TWINE_PASSWORD'
                }
            }

        }
    }
}
