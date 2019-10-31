pipeline {
    agent any

    triggers {
        pollSCM('*/5 * * * 1-5')
    }
    options {
        skipDefaultCheckout(true)
        buildDiscarder(logRotator(numToKeepStr: '10'))
        timestamps()
    }

    stages {

        stage ("Checkout SCM"){
            steps{
                checkout scm
            }
        }
        stage ("Generate Distribution Archives"){
            agent {
                docker { image 'python:3'}
            }
            steps {
                sh "python -m pip install setuptools wheel"
                sh "python setup.py sdist bdist_wheel"
            }
        }
        stage ("Upload to Test PyPi"){
            agent {
                docker { image 'python:3'}
            }

            steps {
                sh "python -m pip install twine"
                withCredentails([$class: 'UsernamePasswordMultiBinding', credentailsId: 'twine_login_credentails', usernameVariable: 'TWINE_USERNAME', passwordVariable: 'TWINE_PASSWORD' )]){
                    sh "python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/* -u $TWINE_USERNAME -p $TWINE_PASSWORD"
                }

            
            }

        }
    }
}
