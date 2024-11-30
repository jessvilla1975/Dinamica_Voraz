#!/bin/bash

# Salir si ocurre algún error
set -e

# Directorio base del proyecto
BASE_DIR=$(dirname "$0")

# Agregar el directorio raíz del proyecto al PYTHONPATH
export PYTHONPATH=$BASE_DIR

# Verificar si se proporcionó un test específico
if [ -n "$1" ]; then
    TEST_NAME=$1
    TEST_FILE="test/${TEST_NAME}.py"
    if [ -f "$TEST_FILE" ]; then
        echo "Ejecutando test: $TEST_FILE"
        python -m unittest test.${TEST_NAME}
    else
        echo "Error: El archivo $TEST_FILE no existe."
        exit 1
    fi
else
    echo "Ejecutando todos los tests..."
    python -m unittest discover -s test -p "*.py"
fi

echo "Ejecución de tests finalizada."

