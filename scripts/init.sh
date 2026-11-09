#!/bin/bash

# ============================================================
# Script d'initialisation SSP Cloud — python_data (VSCode)
# Argument $1 : nom du notebook (sans .ipynb)
#               ex: init_python/00-premiers-pas-notebooks
# ============================================================

NOTEBOOK_PATH="${1:-init_python/00-premiers-pas-notebooks}"
NOTEBOOK_NAME="$(basename "${NOTEBOOK_PATH}")"
WORK_DIR="/home/onyxia/work"
RAW_URL="https://raw.githubusercontent.com/surybang/python_data/main/notebooks/${NOTEBOOK_PATH}.ipynb"

# ── 1. Télécharger le notebook directement ─────────────────
echo "[init] Téléchargement du notebook ${NOTEBOOK_NAME}..."
curl -fsSL "${RAW_URL}" -o "${WORK_DIR}/${NOTEBOOK_NAME}.ipynb"