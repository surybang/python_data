#!/bin/bash

# ============================================================
# Script d'initialisation SSP Cloud — python_data
# Usage : appelé par SSP Cloud au démarrage du service
# Argument $1 : nom du notebook (sans .ipynb)
#               ex: 01-premiers-pas-notebooks
# ============================================================

REPO_URL="https://github.com/surybang/python_data.git"
WORK_DIR="/home/onyxia/work"
REPO_DIR="${WORK_DIR}/python_data"
NOTEBOOK_NAME="${1:-01-premiers-pas-notebooks}"

# ── 1. Cloner le repo ──────────────────────────────────────
echo "[init] Clonage du repo python_data..."
git clone --depth 1 "${REPO_URL}" "${REPO_DIR}"

# ── 2. Installer les dépendances si requirements.txt existe ─
if [ -f "${REPO_DIR}/requirements.txt" ]; then
    echo "[init] Installation des dépendances..."
    pip install -r "${REPO_DIR}/requirements.txt" --quiet
fi

# ── 3. Placer le notebook à la racine du workspace ─────────
NOTEBOOK_SRC="${REPO_DIR}/notebooks/${NOTEBOOK_NAME}.ipynb"

if [ -f "${NOTEBOOK_SRC}" ]; then
    cp "${NOTEBOOK_SRC}" "${WORK_DIR}/${NOTEBOOK_NAME}.ipynb"
    echo "[init] Notebook prêt : ${NOTEBOOK_NAME}.ipynb"
else
    echo "[init] AVERTISSEMENT : notebook introuvable → ${NOTEBOOK_SRC}"
fi

echo "[init] Initialisation terminée."