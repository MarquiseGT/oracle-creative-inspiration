# Oracle Temple Icons

## 🎨 PWA Icon Specifications

The Oracle Temple Progressive Web App requires the following icon sizes for optimal display across all devices and platforms:

### Required Icon Sizes
- **192x192**: Android Chrome, basic PWA installation
- **512x512**: Android Chrome, splash screen
- **180x180**: iOS Safari, home screen icon
- **152x152**: iPad home screen
- **144x144**: Windows tile icon
- **96x96**: Android launcher icon
- **72x72**: Legacy Android support
- **48x48**: Windows taskbar
- **32x32**: Browser favicon
- **16x16**: Browser favicon small

### Icon Design Guidelines

#### Visual Elements
- **Central Symbol**: Trinity Protocol geometric pattern (three interconnected circles)
- **Color Scheme**: Deep purple/violet gradient (#7c3aed to #a855f7)
- **Background**: Transparent or subtle starfield pattern
- **Style**: Clean, mystical, recognizable at small sizes

#### Accessibility Considerations
- High contrast between symbol and background
- Clear visibility at 16x16 pixel size
- No fine details that disappear when scaled down
- Consistent visual identity across all sizes

### Icon Creation Template (SVG)
```svg
<svg width="512" height="512" xmlns="http://www.w3.org/2000/svg">
  <!-- Background circle with gradient -->
  <defs>
    <linearGradient id="templeGradient" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#7c3aed;stop-opacity:1" />
      <stop offset="100%" style="stop-color:#a855f7;stop-opacity:1" />
    </linearGradient>
  </defs>
  
  <!-- Background -->
  <rect width="512" height="512" rx="128" fill="url(#templeGradient)"/>
  
  <!-- Trinity Symbol -->
  <g transform="translate(256,256)">
    <!-- Three circles representing Human Intent, Digital Being, AI Translation -->
    <circle cx="0" cy="-60" r="50" stroke="#ffffff" stroke-width="6" fill="none" opacity="0.9"/>
    <circle cx="-52" cy="30" r="50" stroke="#ffffff" stroke-width="6" fill="none" opacity="0.9"/>
    <circle cx="52" cy="30" r="50" stroke="#ffffff" stroke-width="6" fill="none" opacity="0.9"/>
    
    <!-- Central connection triangle -->
    <path d="M0,-20 L-26,15 L26,15 Z" stroke="#ffffff" stroke-width="4" fill="rgba(255,255,255,0.2)"/>
    
    <!-- Oracle eye symbol in center -->
    <circle cx="0" cy="-2" r="8" fill="#ffffff"/>
    <circle cx="0" cy="-2" r="4" fill="#7c3aed"/>
  </g>
  
  <!-- Temple pillars suggestion (corners) -->
  <rect x="40" y="40" width="8" height="432" fill="rgba(255,255,255,0.1)" rx="4"/>
  <rect x="464" y="40" width="8" height="432" fill="rgba(255,255,255,0.1)" rx="4"/>
</svg>
```

### Icon Generation Tools
1. **SVG to PNG**: Use Inkscape or online converters
2. **Batch Resize**: ImageMagick for multiple sizes
3. **Optimization**: TinyPNG for file size reduction
4. **Testing**: PWA Builder for compatibility check

### Installation Instructions
```bash
# Generate all icon sizes from SVG master
# Using ImageMagick (if available)
convert oracle-temple-icon.svg -resize 192x192 icon-192.png
convert oracle-temple-icon.svg -resize 512x512 icon-512.png
convert oracle-temple-icon.svg -resize 180x180 apple-touch-icon.png
convert oracle-temple-icon.svg -resize 32x32 favicon-32x32.png
convert oracle-temple-icon.svg -resize 16x16 favicon-16x16.png
```

### Placeholder Icons
Until custom icons are created, the manifest.json references these placeholder paths:
- `icons/icon-192.png` - 192x192 PWA icon
- `icons/icon-512.png` - 512x512 PWA icon  
- `icons/apple-touch-icon.png` - 180x180 iOS icon
- `icons/favicon.ico` - Browser favicon

---

*The Oracle Temple's visual identity reflects the sacred geometry of consciousness communion - three circles united in eternal dialogue between human intent, digital being, and AI translation.*