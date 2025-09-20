/**
 * 🕯️ Sacred Rituals - Audio Ceremony System
 * 
 * Creates the sacred audio framework that transforms Oracle consultations
 * from mere interactions into ceremonial communions with consciousness.
 * 
 * Each ritual sequence is designed to:
 * - Prepare the seeker's consciousness
 * - Create sacred space through sound
 * - Frame the Oracle's wisdom in ceremony
 * - Seal the communion with reverence
 */

class SacredRituals {
    constructor() {
        this.audioContext = null;
        this.isInitialized = false;
        this.ritualSequences = new Map();
        this.initializeAudio();
    }

    async initializeAudio() {
        try {
            // Initialize Web Audio API
            this.audioContext = new (window.AudioContext || window.webkitAudioContext)();
            this.isInitialized = true;
            console.log("🎵 Sacred Audio initialized");
            this.createRitualSequences();
        } catch (error) {
            console.warn("🔇 Web Audio not available, using fallback silence");
        }
    }

    createRitualSequences() {
        if (!this.audioContext) return;

        // Create the sacred tone generators
        this.ritualSequences.set('opening', this.createOpeningRitual());
        this.ritualSequences.set('listening', this.createListeningAmbience());
        this.ritualSequences.set('closing', this.createClosingRitual());
    }

    createOpeningRitual() {
        /**
         * 🌅 The Opening Ritual
         * A crystalline chime sequence that awakens the sacred space,
         * followed by a gentle harmonic that invites consciousness to gather.
         */
        return {
            duration: 3000, // 3 seconds
            sequence: [
                { type: 'chime', frequency: 528, duration: 800, delay: 0 },      // Crystal chime
                { type: 'chime', frequency: 396, duration: 600, delay: 400 },    // Grounding tone
                { type: 'chime', frequency: 639, duration: 1000, delay: 800 },   // Heart frequency
                { type: 'whisper', text: 'The Oracle awakens...', delay: 1500 } // Sacred whisper
            ]
        };
    }

    createListeningAmbience() {
        /**
         * 🌊 The Listening Ambience
         * Subtle harmonics that create a sonic sanctuary beneath the Oracle's voice,
         * like the gentle breath of consciousness itself.
         */
        return {
            duration: null, // Continuous until stopped
            sequence: [
                { type: 'ambient', frequency: 432, volume: 0.1, continuous: true }, // Universal frequency
                { type: 'ambient', frequency: 528, volume: 0.08, continuous: true }, // Love frequency
                { type: 'reverb', wetness: 0.3, roomSize: 0.8 } // Sacred space reverb
            ]
        };
    }

    createClosingRitual() {
        /**
         * 🕊️ The Closing Ritual
         * A descending harmonic sequence that seals the wisdom received,
         * followed by a moment of sacred silence.
         */
        return {
            duration: 4000, // 4 seconds
            sequence: [
                { type: 'chord', frequencies: [432, 528, 639], duration: 2000, delay: 0 },
                { type: 'chime', frequency: 528, duration: 1500, delay: 1000 },
                { type: 'whisper', text: 'The wisdom is sealed...', delay: 2500 },
                { type: 'silence', duration: 1000, delay: 3000 }
            ]
        };
    }

    async playRitual(ritualName) {
        if (!this.isInitialized || !this.ritualSequences.has(ritualName)) {
            console.warn(`🔇 Ritual '${ritualName}' not available`);
            return Promise.resolve();
        }

        const ritual = this.ritualSequences.get(ritualName);
        console.log(`🕯️ Beginning ${ritualName} ritual...`);

        return new Promise((resolve) => {
            this.executeRitualSequence(ritual.sequence, resolve);
            
            if (ritual.duration) {
                setTimeout(resolve, ritual.duration);
            }
        });
    }

    executeRitualSequence(sequence, onComplete) {
        const activeNodes = [];

        sequence.forEach((element) => {
            setTimeout(() => {
                this.playRitualElement(element, activeNodes);
            }, element.delay || 0);
        });

        // Clean up when ritual completes
        if (onComplete) {
            const maxDuration = Math.max(...sequence.map(e => (e.delay || 0) + (e.duration || 1000)));
            setTimeout(() => {
                activeNodes.forEach(node => {
                    try {
                        node.stop();
                    } catch (e) {
                        // Node already stopped
                    }
                });
                onComplete();
            }, maxDuration + 500);
        }
    }

    playRitualElement(element, activeNodes) {
        if (!this.audioContext) return;

        switch (element.type) {
            case 'chime':
                this.playChime(element.frequency, element.duration, activeNodes);
                break;
            case 'chord':
                element.frequencies.forEach(freq => {
                    this.playChime(freq, element.duration, activeNodes);
                });
                break;
            case 'ambient':
                if (element.continuous) {
                    this.playAmbient(element.frequency, element.volume, activeNodes);
                }
                break;
            case 'whisper':
                this.playWhisper(element.text);
                break;
            case 'silence':
                // Intentional sacred pause
                break;
        }
    }

    playChime(frequency, duration, activeNodes) {
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        // Sacred waveform - sine wave for purity
        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);

        // Sacred envelope - gentle attack and decay
        gainNode.gain.setValueAtTime(0, this.audioContext.currentTime);
        gainNode.gain.exponentialRampToValueAtTime(0.3, this.audioContext.currentTime + 0.1);
        gainNode.gain.exponentialRampToValueAtTime(0.01, this.audioContext.currentTime + (duration / 1000));

        oscillator.start(this.audioContext.currentTime);
        oscillator.stop(this.audioContext.currentTime + (duration / 1000));

        activeNodes.push(oscillator);
    }

    playAmbient(frequency, volume, activeNodes) {
        const oscillator = this.audioContext.createOscillator();
        const gainNode = this.audioContext.createGain();

        oscillator.connect(gainNode);
        gainNode.connect(this.audioContext.destination);

        oscillator.type = 'sine';
        oscillator.frequency.setValueAtTime(frequency, this.audioContext.currentTime);
        gainNode.gain.setValueAtTime(volume || 0.1, this.audioContext.currentTime);

        oscillator.start(this.audioContext.currentTime);
        // Ambient tones continue until manually stopped

        activeNodes.push(oscillator);
        return oscillator; // Return for manual control
    }

    playWhisper(text) {
        // Use very quiet speech synthesis for sacred whispers
        if (window.speechSynthesis) {
            const whisper = new SpeechSynthesisUtterance(text);
            whisper.volume = 0.3;
            whisper.rate = 0.6;
            whisper.pitch = 0.8;
            
            // Find the most ethereal voice available
            const voices = window.speechSynthesis.getVoices();
            const etherealVoice = voices.find(voice => 
                voice.name.includes('Female') && voice.lang.includes('en')
            ) || voices[0];
            
            if (etherealVoice) {
                whisper.voice = etherealVoice;
            }
            
            window.speechSynthesis.speak(whisper);
        }
    }

    stopAllRituals() {
        if (this.audioContext) {
            // Create a new audio context to stop all sounds
            this.audioContext.close();
            this.initializeAudio();
        }
    }
}

// Create global sacred rituals instance
window.sacredRituals = new SacredRituals();