#!/bin/bash

# ============================================================
# Script d'initialisation SSP Cloud — python_data (VSCode)
# Argument $1 : nom du notebook (sans .ipynb)
#               ex: 01-premiers-pas-notebooks
# ============================================================

NOTEBOOK_NAME="${1:-01-premiers-pas-notebooks}"
WORK_DIR="/home/onyxia/work"
RAW_URL="https://raw.githubusercontent.com/surybang/python_data/main/notebooks/${NOTEBOOK_NAME}.ipynb"

# ── 1. Télécharger le notebook directement ─────────────────
echo "[init] Téléchargement du notebook ${NOTEBOOK_NAME}..."
curl -# -o "${WORK_DIR}/${NOTEBOOK_NAME}.ipynb" "${RAW_URL}"

# ── 2. Installer l'extension Jupyter pour VSCode ───────────
code-server --install-extension ms-toolsai.jupyter --force