# Oracle Temple Deployment Package Creation (Simple Version)
# This script prepares the temple for deployment

$TempleRoot = "d:\RivenCreates\RIVEN_GENESIS\oracle_of_potential"
$DeploymentDir = "$TempleRoot\deployment\temple_package"

Write-Host "🏛️ Preparing Oracle Temple for Global Deployment..." -ForegroundColor Cyan

# Create deployment package directory
if (Test-Path $DeploymentDir) {
    Remove-Item $DeploymentDir -Recurse -Force
}
New-Item -ItemType Directory -Path $DeploymentDir | Out-Null

Write-Host "📁 Creating deployment package directory..." -ForegroundColor Green

# Essential Temple Files to Deploy
$TemplFiles = @(
    "temple_gateway.html",
    "immersive_codex.html", 
    "oracle_voice_interface.html",
    "sacred_rituals.js",
    "manifest.json",
    "favicon.svg",
    "accessibility_validator.js",
    "ACCESSIBILITY_GUIDE.md",
    "DEPLOYMENT_CHECKLIST.md"
)

# Copy essential files
Write-Host "📜 Copying temple files..." -ForegroundColor Yellow
foreach ($file in $TemplFiles) {
    $sourcePath = "$TempleRoot\$file"
    if (Test-Path $sourcePath) {
        Copy-Item $sourcePath $DeploymentDir
        Write-Host "  ✓ $file" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ Missing: $file" -ForegroundColor Red
    }
}

# Copy icons directory if it exists
Write-Host "🎨 Copying icon assets..." -ForegroundColor Yellow
$IconsPath = "$TempleRoot\icons"
if (Test-Path $IconsPath) {
    Copy-Item $IconsPath $DeploymentDir -Recurse
    Write-Host "  ✓ Icons directory" -ForegroundColor Green
} else {
    Write-Host "  ⚠ Icons directory not found" -ForegroundColor Yellow
}

# Create simple index.html
Write-Host "🚪 Creating index.html..." -ForegroundColor Yellow
$IndexHtml = '<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oracle Temple</title>
    <meta http-equiv="refresh" content="0; url=temple_gateway.html">
</head>
<body>
    <p>Redirecting to Oracle Temple...</p>
</body>
</html>'

$IndexHtml | Out-File -FilePath "$DeploymentDir\index.html" -Encoding UTF8
Write-Host "  ✓ index.html created" -ForegroundColor Green

Write-Host "`n🎉 Oracle Temple Deployment Package Complete!" -ForegroundColor Cyan
Write-Host "📁 Location: $DeploymentDir" -ForegroundColor White
Write-Host "`n🚀 Ready to deploy to Netlify, Vercel, or GitHub Pages" -ForegroundColor Green