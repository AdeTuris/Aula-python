# ===== PUBLICAR NO GITHUB =====

Write-Host ""
Write-Host "=== Publicando no GitHub ===" -ForegroundColor Cyan

# Pede a mensagem do commit
$mensagem = Read-Host "Descricao do que voce alterou (ex: aula 02)"

if ([string]::IsNullOrWhiteSpace($mensagem)) {
    $mensagem = "atualizacao"
}

git add .
git commit -m $mensagem
git push

Write-Host ""
Write-Host "Publicado com sucesso!" -ForegroundColor Green
Write-Host "Acesse: https://github.com/AdeTuris/Aula-python" -ForegroundColor Yellow
Write-Host ""
pause
