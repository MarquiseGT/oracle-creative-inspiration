/**
 * Oracle Temple Accessibility Validation Script
 * Tests all implemented accessibility features and provides compliance report
 */

class OracleTempleAccessibilityValidator {
    constructor() {
        this.testResults = {
            passed: [],
            failed: [],
            warnings: []
        };
    }

    // Run all accessibility tests
    async validateTempleAccessibility() {
        console.log('🏛️ Starting Oracle Temple Accessibility Validation');
        
        this.testSemanticStructure();
        this.testKeyboardNavigation();
        this.testScreenReaderSupport();
        this.testColorContrast();
        this.testMotionPreferences();
        this.testMobileAccessibility();
        this.testFocusManagement();
        this.testARIAImplementation();
        
        this.generateComplianceReport();
    }

    // Test 1: Semantic HTML Structure
    testSemanticStructure() {
        console.log('📝 Testing semantic HTML structure...');
        
        const hasMain = document.querySelector('main');
        const hasProperHeadings = this.validateHeadingHierarchy();
        const hasLandmarks = this.validateLandmarks();
        const hasListStructure = document.querySelector('[role="list"]');
        
        if (hasMain) {
            this.testResults.passed.push('Main landmark present');
        } else {
            this.testResults.failed.push('Missing main landmark');
        }
        
        if (hasProperHeadings) {
            this.testResults.passed.push('Heading hierarchy correct');
        } else {
            this.testResults.failed.push('Improper heading hierarchy');
        }
        
        if (hasListStructure) {
            this.testResults.passed.push('List structure implemented');
        } else {
            this.testResults.warnings.push('Consider list structure for gateway options');
        }
    }

    // Test 2: Keyboard Navigation
    testKeyboardNavigation() {
        console.log('⌨️ Testing keyboard navigation...');
        
        const focusableElements = document.querySelectorAll(
            'button, a, input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        
        const hasSkipLink = document.querySelector('a[href="#main-content"]');
        const hasVisibleFocus = this.testFocusIndicators();
        const supportsArrowKeys = document.querySelector('[data-keyboard-nav="arrows"]') !== null;
        
        if (focusableElements.length > 0) {
            this.testResults.passed.push(`${focusableElements.length} focusable elements found`);
        }
        
        if (hasSkipLink) {
            this.testResults.passed.push('Skip link implemented');
        } else {
            this.testResults.failed.push('Missing skip link');
        }
        
        if (hasVisibleFocus) {
            this.testResults.passed.push('Visible focus indicators present');
        } else {
            this.testResults.failed.push('Missing visible focus indicators');
        }
    }

    // Test 3: Screen Reader Support
    testScreenReaderSupport() {
        console.log('🔊 Testing screen reader support...');
        
        const hasAltText = this.validateImageAltText();
        const hasAriaLabels = document.querySelectorAll('[aria-label], [aria-labelledby]').length > 0;
        const hasLiveRegions = document.querySelectorAll('[aria-live]').length > 0;
        const hasDescriptions = document.querySelectorAll('[aria-describedby]').length > 0;
        
        if (hasAriaLabels) {
            this.testResults.passed.push('ARIA labels implemented');
        } else {
            this.testResults.warnings.push('Consider adding more ARIA labels');
        }
        
        if (hasLiveRegions) {
            this.testResults.passed.push('Live regions for dynamic content');
        } else {
            this.testResults.warnings.push('Consider live regions for status updates');
        }
        
        if (hasDescriptions) {
            this.testResults.passed.push('ARIA descriptions provided');
        } else {
            this.testResults.warnings.push('Consider adding ARIA descriptions');
        }
    }

    // Test 4: Color Contrast Validation
    testColorContrast() {
        console.log('🎨 Testing color contrast...');
        
        // Test would require external library for actual contrast calculation
        // This is a simplified implementation
        
        const hasHighContrastSupport = this.testHighContrastMediaQuery();
        const hasColorOnlyInfo = this.checkColorOnlyInformation();
        
        if (hasHighContrastSupport) {
            this.testResults.passed.push('High contrast mode support implemented');
        } else {
            this.testResults.failed.push('Missing high contrast mode support');
        }
        
        if (!hasColorOnlyInfo) {
            this.testResults.passed.push('Information not conveyed by color alone');
        } else {
            this.testResults.failed.push('Some information relies only on color');
        }
    }

    // Test 5: Motion and Animation Preferences
    testMotionPreferences() {
        console.log('🎭 Testing motion preferences...');
        
        const hasReducedMotionSupport = this.testReducedMotionMediaQuery();
        const hasAnimationControls = document.querySelectorAll('[data-animation-control]').length > 0;
        
        if (hasReducedMotionSupport) {
            this.testResults.passed.push('Reduced motion preference support');
        } else {
            this.testResults.failed.push('Missing reduced motion support');
        }
    }

    // Test 6: Mobile Accessibility
    testMobileAccessibility() {
        console.log('📱 Testing mobile accessibility...');
        
        const hasTouchTargets = this.validateTouchTargetSizes();
        const hasViewportMeta = document.querySelector('meta[name="viewport"]');
        const hasZoomSupport = !document.querySelector('meta[name="viewport"][content*="user-scalable=no"]');
        
        if (hasTouchTargets) {
            this.testResults.passed.push('Touch targets meet size requirements');
        } else {
            this.testResults.warnings.push('Some touch targets may be too small');
        }
        
        if (hasViewportMeta) {
            this.testResults.passed.push('Viewport meta tag present');
        } else {
            this.testResults.failed.push('Missing viewport meta tag');
        }
        
        if (hasZoomSupport) {
            this.testResults.passed.push('Zoom functionality preserved');
        } else {
            this.testResults.failed.push('Zoom disabled - accessibility barrier');
        }
    }

    // Test 7: Focus Management
    testFocusManagement() {
        console.log('🎯 Testing focus management...');
        
        const hasTabTraps = this.detectKeyboardTraps();
        const hasLogicalTabOrder = this.validateTabOrder();
        const hasInitialFocus = document.activeElement !== document.body;
        
        if (!hasTabTraps) {
            this.testResults.passed.push('No keyboard traps detected');
        } else {
            this.testResults.failed.push('Keyboard trap detected');
        }
        
        if (hasLogicalTabOrder) {
            this.testResults.passed.push('Logical tab order maintained');
        } else {
            this.testResults.warnings.push('Review tab order for optimal UX');
        }
    }

    // Test 8: ARIA Implementation
    testARIAImplementation() {
        console.log('🏷️ Testing ARIA implementation...');
        
        const hasValidRoles = this.validateARIARoles();
        const hasProperStates = this.validateARIAStates();
        const hasCorrectRelationships = this.validateARIARelationships();
        
        if (hasValidRoles) {
            this.testResults.passed.push('ARIA roles properly implemented');
        } else {
            this.testResults.warnings.push('Review ARIA role usage');
        }
    }

    // Helper Methods for Testing
    validateHeadingHierarchy() {
        const headings = Array.from(document.querySelectorAll('h1, h2, h3, h4, h5, h6'));
        if (headings.length === 0) return false;
        
        let currentLevel = 0;
        return headings.every(heading => {
            const level = parseInt(heading.tagName.charAt(1));
            if (currentLevel === 0 && level !== 1) return false;
            if (level > currentLevel + 1) return false;
            currentLevel = level;
            return true;
        });
    }

    validateLandmarks() {
        const landmarks = document.querySelectorAll('main, nav, aside, header, footer, [role="main"], [role="navigation"], [role="complementary"], [role="banner"], [role="contentinfo"]');
        return landmarks.length > 0;
    }

    testFocusIndicators() {
        // Simplified test - would need actual focus simulation
        const focusStyles = Array.from(document.styleSheets)
            .some(sheet => {
                try {
                    return Array.from(sheet.cssRules)
                        .some(rule => rule.selectorText && rule.selectorText.includes(':focus'));
                } catch (e) {
                    return false;
                }
            });
        return focusStyles;
    }

    validateImageAltText() {
        const images = document.querySelectorAll('img');
        return Array.from(images).every(img => 
            img.hasAttribute('alt') || img.hasAttribute('aria-label') || img.getAttribute('role') === 'presentation'
        );
    }

    testHighContrastMediaQuery() {
        return Array.from(document.styleSheets).some(sheet => {
            try {
                return Array.from(sheet.cssRules).some(rule => 
                    rule.media && rule.media.mediaText.includes('prefers-contrast')
                );
            } catch (e) {
                return false;
            }
        });
    }

    testReducedMotionMediaQuery() {
        return Array.from(document.styleSheets).some(sheet => {
            try {
                return Array.from(sheet.cssRules).some(rule => 
                    rule.media && rule.media.mediaText.includes('prefers-reduced-motion')
                );
            } catch (e) {
                return false;
            }
        });
    }

    checkColorOnlyInformation() {
        // Simplified check - would need more sophisticated analysis
        const colorOnlyElements = document.querySelectorAll('[style*="color"]');
        return Array.from(colorOnlyElements).some(el => {
            const text = el.textContent.toLowerCase();
            return text.includes('red') || text.includes('green') || text.includes('blue') || 
                   text.includes('yellow') || text.includes('color');
        });
    }

    validateTouchTargetSizes() {
        const buttons = document.querySelectorAll('button, a, input, select');
        return Array.from(buttons).every(button => {
            const rect = button.getBoundingClientRect();
            return rect.width >= 44 && rect.height >= 44;
        });
    }

    detectKeyboardTraps() {
        // Simplified detection - would need actual focus simulation
        const focusableElements = document.querySelectorAll(
            'button, a, input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        
        // Check for elements that might trap focus
        return Array.from(focusableElements).some(el => {
            const tabIndex = parseInt(el.getAttribute('tabindex') || '0');
            return tabIndex > 0 && !el.hasAttribute('data-focus-trap');
        });
    }

    validateTabOrder() {
        const focusableElements = document.querySelectorAll(
            'button, a, input, select, textarea, [tabindex]:not([tabindex="-1"])'
        );
        
        // Check if elements appear in DOM order
        let lastTop = -1;
        return Array.from(focusableElements).every(el => {
            const rect = el.getBoundingClientRect();
            if (rect.top >= lastTop) {
                lastTop = rect.top;
                return true;
            }
            return false;
        });
    }

    validateARIARoles() {
        const elementsWithRoles = document.querySelectorAll('[role]');
        const validRoles = ['button', 'link', 'main', 'navigation', 'banner', 'contentinfo', 'complementary', 'list', 'listitem', 'img', 'presentation'];
        
        return Array.from(elementsWithRoles).every(el => {
            const role = el.getAttribute('role');
            return validRoles.includes(role);
        });
    }

    validateARIAStates() {
        const elementsWithStates = document.querySelectorAll('[aria-expanded], [aria-selected], [aria-checked], [aria-pressed]');
        return Array.from(elementsWithStates).every(el => {
            const expanded = el.getAttribute('aria-expanded');
            const selected = el.getAttribute('aria-selected');
            const checked = el.getAttribute('aria-checked');
            const pressed = el.getAttribute('aria-pressed');
            
            return (expanded === null || ['true', 'false'].includes(expanded)) &&
                   (selected === null || ['true', 'false'].includes(selected)) &&
                   (checked === null || ['true', 'false', 'mixed'].includes(checked)) &&
                   (pressed === null || ['true', 'false'].includes(pressed));
        });
    }

    validateARIARelationships() {
        const elementsWithRelationships = document.querySelectorAll('[aria-labelledby], [aria-describedby]');
        return Array.from(elementsWithRelationships).every(el => {
            const labelledby = el.getAttribute('aria-labelledby');
            const describedby = el.getAttribute('aria-describedby');
            
            if (labelledby) {
                const labelIds = labelledby.split(' ');
                if (!labelIds.every(id => document.getElementById(id))) return false;
            }
            
            if (describedby) {
                const descIds = describedby.split(' ');
                if (!descIds.every(id => document.getElementById(id))) return false;
            }
            
            return true;
        });
    }

    // Generate comprehensive compliance report
    generateComplianceReport() {
        console.log('\n🏛️ ORACLE TEMPLE ACCESSIBILITY COMPLIANCE REPORT');
        console.log('=' .repeat(60));
        
        console.log(`\n✅ PASSED TESTS (${this.testResults.passed.length}):`);
        this.testResults.passed.forEach(test => console.log(`  ✓ ${test}`));
        
        if (this.testResults.warnings.length > 0) {
            console.log(`\n⚠️ WARNINGS (${this.testResults.warnings.length}):`);
            this.testResults.warnings.forEach(warning => console.log(`  ⚠ ${warning}`));
        }
        
        if (this.testResults.failed.length > 0) {
            console.log(`\n❌ FAILED TESTS (${this.testResults.failed.length}):`);
            this.testResults.failed.forEach(failure => console.log(`  ❌ ${failure}`));
        }
        
        const totalTests = this.testResults.passed.length + this.testResults.failed.length;
        const passRate = totalTests > 0 ? Math.round((this.testResults.passed.length / totalTests) * 100) : 0;
        
        console.log(`\n📊 OVERALL COMPLIANCE: ${passRate}%`);
        
        if (passRate >= 95) {
            console.log('🏆 EXCELLENT - Temple meets high accessibility standards!');
        } else if (passRate >= 80) {
            console.log('👍 GOOD - Temple is accessible with minor improvements needed');
        } else if (passRate >= 60) {
            console.log('⚠️ NEEDS WORK - Address failed tests for WCAG compliance');
        } else {
            console.log('❌ CRITICAL - Significant accessibility barriers present');
        }
        
        console.log('\n🔗 For detailed WCAG 2.1 guidelines: https://www.w3.org/WAI/WCAG21/quickref/');
        console.log('🏛️ Oracle Temple Accessibility Guide: ./ACCESSIBILITY_GUIDE.md');
    }
}

// Auto-run validation when script loads
document.addEventListener('DOMContentLoaded', () => {
    const validator = new OracleTempleAccessibilityValidator();
    
    // Run validation after a short delay to ensure page is fully loaded
    setTimeout(() => {
        validator.validateTempleAccessibility();
    }, 1000);
});

// Export for manual testing
if (typeof module !== 'undefined' && module.exports) {
    module.exports = OracleTempleAccessibilityValidator;
}