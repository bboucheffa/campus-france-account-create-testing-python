pipeline {
    agent any
    stages {
        stage('CampusFrance Tests') {
            steps {
                bat '''
                    echo "=== PYTHON OK ==="
                    python --version

                    echo "=== VENV ==="
                    python -m venv venv --clear
                    call venv\\Scripts\\activate.bat

                    echo "=== INSTALL ==="
                    pip install --upgrade pip
                    pip install behave selenium webdriver-manager

                    echo "=== TESTS ==="
                    cd features
                    behave -f pretty --no-capture --no-capture-stderr
                '''
            }
        }
    }

}
