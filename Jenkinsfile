pipeline {
    agent any

    environment {
        // Configuration Python/Venv
        PYTHON = '/usr/bin/python3'
        VENV_PATH = "${WORKSPACE}/venv"
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
                    echo 'Installation des dépendances Python...'

                    // Créer le venv si pas existant
                    sh '''
                        ${PYTHON} -m venv ${VENV_PATH} || true
                        . ${VENV_PATH}/bin/activate
                        pip install --upgrade pip
                        pip install -r requirements.txt
                    '''
                }
            }
        }

        stage('Tests Behave') {
            steps {
                script {
                    echo 'Lancement des tests Behave...'

                    sh '''
                        . ${VENV_PATH}/bin/activate
                        cd features
                        behave -f pretty --no-capture --no-capture-stderr
                    '''
                }
            }
        }
    }
}