# =========================
# Variables
# =========================
$VENV = "venv"
$Python = "$VENV\Scripts\python.exe"
$Pip = "$VENV\Scripts\pip.exe"

# =========================
# venv
# =========================
if (-not (Test-Path $VENV)) {
    Write-Host "Creating virtual environment..."
    python3.13 -m venv $VENV
}

# =========================
# markitdown
# =========================
if (-not (Test-Path "markitdown")) {
    Write-Host "Cloning markitdown repository..."
    git clone https://github.com/microsoft/markitdown.git
}

Write-Host "Installing markitdown (editable, all extras)..."
& $Pip install -e "markitdown/packages/markitdown[all]"

# =========================
# gemini
# =========================
if (-not (Get-Command brew -ErrorAction SilentlyContinue)) {
    Write-Error "Homebrew not installed"
    exit 1
}

Write-Host "Installing gemini..."
brew install gemini

# =========================
# final
# =========================
Write-Host "Everything is ok"
