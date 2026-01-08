if (-not (Test-Path venv)) {
    python -m venv venv
}

$python = "venv\Scripts\python.exe"

if (-not (Test-Path markitdown)) {
    git clone https://github.com/microsoft/markitdown.git
}

& $python -m pip install -e "markitdown/packages/markitdown[all]"

if (-not (Get-Command gemini -ErrorAction SilentlyContinue)) {
    if (Get-Command winget -ErrorAction SilentlyContinue) {
        winget install Google.Gemini
    } else {
        Write-Error "winget not found. Install Gemini manually."
    }
}