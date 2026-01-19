pipeline {
    agent any

    stages {
        stage('CampusFrance Tests') {
            steps {
                bat '''
                    echo === PYTHON ===
                    C:\\Python\\Python39\\python.exe --version

                    echo === VENV ===
                    C:\\Python\\Python39\\python.exe -m venv venv --clear
                    call venv\\Scripts\\activate.bat

                    echo === INSTALL ===
                    python -m pip install --upgrade pip
                    python -m pip install behave selenium webdriver-manager

                    echo === TESTS ===
                    python -m behave features -f pretty --no-capture --no-capture-stderr
                '''
            }
        }
    }
}
