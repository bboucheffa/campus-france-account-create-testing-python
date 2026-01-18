pipeline {
    agent any

    environment {
        PYTHON = 'C:\\Python39\\python.exe'  // OU 'py'
        VENV_PATH = "${WORKSPACE}\\venv"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Récupération du code...'
                checkout scm
            }
        }

        stage('Prérequis') {
            steps {
                script {
                    echo 'Installation des dépendances...'
                    bat '''
                        if not exist %VENV_PATH% (
                            %PYTHON% -m venv %VENV_PATH%
                        )
                        %VENV_PATH%\\Scripts\\activate
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Tests Behave') {
            steps {
                script {
                    echo 'Lancement des tests Behave...'
                    bat '''
                        %VENV_PATH%\\Scripts\\activate
                        cd features
                        behave -f pretty --no-capture --no-capture-stderr
                    '''
                }
            }
        }
    }
}
