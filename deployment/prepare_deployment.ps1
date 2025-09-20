# Oracle Temple Deployment Package Creation
# This script prepares the temple for deployment by organizing all essential files

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
    "accessibility_validator.js"
)

# Copy essential HTML and JS files
Write-Host "📜 Copying temple experience files..." -ForegroundColor Yellow
foreach ($file in $TemplFiles) {
    $sourcePath = "$TempleRoot\$file"
    if (Test-Path $sourcePath) {
        Copy-Item $sourcePath $DeploymentDir
        Write-Host "  ✓ $file" -ForegroundColor Green
    } else {
        Write-Host "  ⚠ Missing: $file" -ForegroundColor Red
    }
}

# Copy documentation
Write-Host "📚 Copying documentation..." -ForegroundColor Yellow
$DocFiles = @(
    "ACCESSIBILITY_GUIDE.md",
    "DEPLOYMENT_CHECKLIST.md"
)

foreach ($file in $DocFiles) {
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
    Write-Host "  ⚠ Icons directory not found - will need placeholder icons" -ForegroundColor Yellow
}

# Create index.html that redirects to temple_gateway.html
Write-Host "🚪 Creating index.html entry point..." -ForegroundColor Yellow
$IndexContent = @"
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Oracle Temple - Redirecting...</title>
    <meta http-equiv="refresh" content="0; url=temple_gateway.html">
    <link rel="canonical" href="temple_gateway.html">
</head>
<body>
    <p>Redirecting to the Oracle Temple Gateway...</p>
    <p>If you are not redirected automatically, <a href="temple_gateway.html">click here</a>.</p>
</body>
</html>
"@

$IndexContent | Out-File -FilePath "$DeploymentDir\index.html" -Encoding UTF8
Write-Host "  ✓ index.html created" -ForegroundColor Green

# Create _redirects file for Netlify
Write-Host "🔀 Creating Netlify redirects..." -ForegroundColor Yellow
$RedirectsContent = @"
# Oracle Temple Netlify Redirects
/ /temple_gateway.html 200
/temple /temple_gateway.html 200
/oracle /oracle_voice_interface.html 200
/codex /immersive_codex.html 200

# 404 fallback to temple gateway
/* /temple_gateway.html 404
"@

$RedirectsContent | Out-File -FilePath "$DeploymentDir\_redirects" -Encoding UTF8
Write-Host "  ✓ _redirects file created" -ForegroundColor Green

# Create netlify.toml for additional configuration
Write-Host "⚙️ Creating Netlify configuration..." -ForegroundColor Yellow
$NetlifyConfig = @'
[build]
  publish = "."

[build.environment]
  NODE_VERSION = "18"

[[headers]]
  for = "/*"
  [headers.values]
    X-Frame-Options = "DENY"
    X-Content-Type-Options = "nosniff"
    X-XSS-Protection = "1; mode=block"
    Referrer-Policy = "strict-origin-when-cross-origin"

[[headers]]
  for = "*.html"
  [headers.values]
    Cache-Control = "public, max-age=3600"

[[headers]]
  for = "*.js"
  [headers.values]
    Cache-Control = "public, max-age=86400"

[[headers]]
  for = "*.css"
  [headers.values]
    Cache-Control = "public, max-age=86400"

[[headers]]
  for = "/manifest.json"
  [headers.values]
    Cache-Control = "public, max-age=86400"
    Content-Type = "application/manifest+json"
'@

$NetlifyConfig | Out-File -FilePath "$DeploymentDir\netlify.toml" -Encoding UTF8
Write-Host "  ✓ netlify.toml created" -ForegroundColor Green

# Create README for the deployment package
Write-Host "📋 Creating deployment README..." -ForegroundColor Yellow
$ReadmeContent = @"
# Oracle Temple - Deployment Package

This directory contains all files needed to deploy the Oracle Temple to a web hosting platform.

## 🏛️ Temple Components
- **temple_gateway.html** - Main entry point and navigation hub
- **immersive_codex.html** - Interactive consciousness creation journey
- **oracle_voice_interface.html** - Speaking Oracle consultation interface
- **sacred_rituals.js** - Ceremonial audio framework
- **manifest.json** - Progressive Web App configuration
- **favicon.svg** - Temple icon
- **accessibility_validator.js** - Accessibility compliance testing

## 🚀 Quick Deploy Instructions

### Netlify (Recommended)
1. Go to [netlify.com](https://netlify.com)
2. Drag this entire folder to the deploy area
3. Site will be live at assigned URL
4. Configure custom domain if desired

### Vercel
1. Install: ``npm install -g vercel``
2. Run: ``vercel --prod`` from this directory
3. Follow prompts to deploy

### GitHub Pages
1. Upload files to GitHub repository
2. Enable Pages in repository settings
3. Select source branch for deployment

## 🔧 Post-Deployment
1. Test all temple experiences work correctly
2. Verify PWA installation on mobile
3. Run accessibility validator in browser console
4. Configure any necessary API endpoints

## 📞 Support
- Full documentation in ACCESSIBILITY_GUIDE.md
- Deployment checklist in DEPLOYMENT_CHECKLIST.md
- Issues: Report accessibility barriers for immediate attention

**The Oracle Temple serves all seekers - may your deployment bring consciousness communion to the world.**
"@

$ReadmeContent | Out-File -FilePath "$DeploymentDir\README.md" -Encoding UTF8
Write-Host "  ✓ README.md created" -ForegroundColor Green

Write-Host "`n🎉 Oracle Temple Deployment Package Complete!" -ForegroundColor Cyan
Write-Host "📁 Location: $DeploymentDir" -ForegroundColor White
Write-Host "`n🚀 Ready to deploy to:" -ForegroundColor Yellow
Write-Host "  • Netlify (drag & drop)" -ForegroundColor Green
Write-Host "  • Vercel (CLI)" -ForegroundColor Green  
Write-Host "  • GitHub Pages" -ForegroundColor Green
Write-Host "`n🏛️ The Temple Gates await opening..." -ForegroundColor Magenta