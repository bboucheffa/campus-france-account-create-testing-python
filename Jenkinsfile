pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup') {
            steps {
                bat '''
                    echo === TEST PYTHON ===
                    py --version

                    echo === CRÉATION VENV ===
                    py -m venv venv --clear

                    echo === ACTIVATION ===
                    call venv\\Scripts\\activate.bat

                    echo === PIP UPGRADE ===
                    python -m pip install --upgrade pip

                    echo === INSTALL PAQUETS ===
                    pip install behave selenium webdriver-manager

                    echo === TEST BEHAVE ===
                    behave --version
                '''
            }
        }

        stage('Tests') {
            steps {
                bat '''
                    call venv\\Scripts\\activate.bat
                    cd features
                    behave -f pretty --no-capture --no-capture-stderr
                '''
            }
        }
    }
}
