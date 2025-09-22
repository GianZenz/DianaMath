// DianaMath - Interactive JavaScript

// Global variables
let currentUser = null;
let soundEnabled = true;

// Initialize the app when the page loads
document.addEventListener('DOMContentLoaded', function() {
    initializeApp();
    addGlobalEventListeners();
    startHeartbeatAnimation();
});

function initializeApp() {
    // Add loading animation
    document.body.style.opacity = '0';
    setTimeout(() => {
        document.body.style.transition = 'opacity 0.5s ease-in';
        document.body.style.opacity = '1';
    }, 100);
    
    // Initialize tooltips
    initializeTooltips();
    
    // Add keyboard navigation
    addKeyboardSupport();
    
    // Initialize progress animations
    animateProgressBars();
    
    console.log('🎉 DianaMath initialized successfully!');
}

function addGlobalEventListeners() {
    // Add click sound to buttons
    document.addEventListener('click', function(e) {
        if (e.target.matches('button, .topic-card, .nav-link, .option-button')) {
            playSound('click');
        }
    });
    
    // Add hover effects to interactive elements
    document.addEventListener('mouseover', function(e) {
        if (e.target.matches('.topic-card, .achievement-card, .progress-card')) {
            addSparkleEffect(e.target);
        }
    });
    
    // Remove sparkle effect when mouse leaves
    document.addEventListener('mouseout', function(e) {
        if (e.target.matches('.topic-card, .achievement-card, .progress-card')) {
            removeSparkleEffect(e.target);
        }
    });
}

function playSound(type) {
    if (!soundEnabled) return;
    
    // Create audio context for sound effects
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    
    let frequency;
    switch(type) {
        case 'correct':
            frequency = 523.25; // C5 note
            break;
        case 'incorrect':
            frequency = 293.66; // D4 note
            break;
        case 'click':
            frequency = 440; // A4 note
            break;
        case 'achievement':
            frequency = 659.25; // E5 note
            break;
        default:
            frequency = 440;
    }
    
    const oscillator = audioContext.createOscillator();
    const gainNode = audioContext.createGain();
    
    oscillator.connect(gainNode);
    gainNode.connect(audioContext.destination);
    
    oscillator.frequency.value = frequency;
    oscillator.type = 'sine';
    
    gainNode.gain.setValueAtTime(0.1, audioContext.currentTime);
    gainNode.gain.exponentialRampToValueAtTime(0.01, audioContext.currentTime + 0.3);
    
    oscillator.start(audioContext.currentTime);
    oscillator.stop(audioContext.currentTime + 0.3);
}

function addSparkleEffect(element) {
    // Create sparkle particles
    for (let i = 0; i < 5; i++) {
        setTimeout(() => {
            createSparkle(element);
        }, i * 100);
    }
}

function createSparkle(element) {
    const sparkle = document.createElement('div');
    sparkle.className = 'sparkle';
    sparkle.innerHTML = '✨';
    sparkle.style.position = 'absolute';
    sparkle.style.pointerEvents = 'none';
    sparkle.style.fontSize = '1rem';
    sparkle.style.zIndex = '1000';
    
    const rect = element.getBoundingClientRect();
    const x = rect.left + Math.random() * rect.width;
    const y = rect.top + Math.random() * rect.height;
    
    sparkle.style.left = x + 'px';
    sparkle.style.top = y + 'px';
    
    document.body.appendChild(sparkle);
    
    // Animate sparkle
    sparkle.animate([
        { 
            opacity: 0, 
            transform: 'translateY(0px) scale(0.5)' 
        },
        { 
            opacity: 1, 
            transform: 'translateY(-20px) scale(1)' 
        },
        { 
            opacity: 0, 
            transform: 'translateY(-40px) scale(0.5)' 
        }
    ], {
        duration: 1000,
        easing: 'ease-out'
    }).onfinish = () => {
        sparkle.remove();
    };
}

function removeSparkleEffect(element) {
    // Clean up any remaining sparkles
    document.querySelectorAll('.sparkle').forEach(sparkle => {
        sparkle.style.animation = 'fadeOut 0.3s ease-out forwards';
        setTimeout(() => sparkle.remove(), 300);
    });
}

function showCelebration(message) {
    // Create celebration overlay
    const celebration = document.createElement('div');
    celebration.className = 'celebration-overlay';
    celebration.innerHTML = `
        <div class="celebration-content">
            <div class="celebration-icon">🎉</div>
            <h2>${message}</h2>
            <div class="celebration-sparkles">
                ${'⭐'.repeat(5)}
            </div>
        </div>
    `;
    
    celebration.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        background: rgba(102, 126, 234, 0.9);
        display: flex;
        align-items: center;
        justify-content: center;
        z-index: 10000;
        animation: celebrationIn 0.5s ease-out;
    `;
    
    const style = document.createElement('style');
    style.textContent = `
        @keyframes celebrationIn {
            from { opacity: 0; transform: scale(0.5); }
            to { opacity: 1; transform: scale(1); }
        }
        .celebration-content {
            text-align: center;
            color: white;
            font-family: 'Comic Neue', cursive;
        }
        .celebration-icon {
            font-size: 5rem;
            margin-bottom: 1rem;
            animation: bounce 0.6s infinite alternate;
        }
        .celebration-sparkles {
            font-size: 2rem;
            margin-top: 1rem;
            animation: sparkleRotate 2s linear infinite;
        }
        @keyframes bounce {
            to { transform: translateY(-20px); }
        }
        @keyframes sparkleRotate {
            to { transform: rotate(360deg); }
        }
    `;
    
    document.head.appendChild(style);
    document.body.appendChild(celebration);
    
    // Play celebration sound
    playSound('achievement');
    
    // Remove after 3 seconds
    setTimeout(() => {
        celebration.style.animation = 'celebrationIn 0.5s ease-out reverse';
        setTimeout(() => {
            celebration.remove();
            style.remove();
        }, 500);
    }, 3000);
}

function initializeTooltips() {
    // Add tooltips to important elements
    const tooltipElements = document.querySelectorAll('[data-tooltip]');
    
    tooltipElements.forEach(element => {
        element.addEventListener('mouseenter', showTooltip);
        element.addEventListener('mouseleave', hideTooltip);
    });
}

function showTooltip(event) {
    const text = event.target.getAttribute('data-tooltip');
    const tooltip = document.createElement('div');
    tooltip.className = 'tooltip';
    tooltip.textContent = text;
    tooltip.style.cssText = `
        position: absolute;
        background: #333;
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 10px;
        font-size: 0.9rem;
        z-index: 1000;
        pointer-events: none;
        white-space: nowrap;
        opacity: 0;
        transition: opacity 0.3s ease;
    `;
    
    document.body.appendChild(tooltip);
    
    const rect = event.target.getBoundingClientRect();
    tooltip.style.left = (rect.left + rect.width / 2 - tooltip.offsetWidth / 2) + 'px';
    tooltip.style.top = (rect.top - tooltip.offsetHeight - 10) + 'px';
    
    setTimeout(() => tooltip.style.opacity = '1', 10);
}

function hideTooltip() {
    const tooltip = document.querySelector('.tooltip');
    if (tooltip) {
        tooltip.style.opacity = '0';
        setTimeout(() => tooltip.remove(), 300);
    }
}

function addKeyboardSupport() {
    document.addEventListener('keydown', function(e) {
        // Number keys for multiple choice answers
        if (e.key >= '1' && e.key <= '4') {
            const optionButtons = document.querySelectorAll('.option-button');
            const index = parseInt(e.key) - 1;
            if (optionButtons[index] && !optionButtons[index].disabled) {
                optionButtons[index].click();
            }
        }
        
        // Enter key for next question
        if (e.key === 'Enter') {
            const nextButton = document.querySelector('.next-button');
            if (nextButton) {
                nextButton.click();
            }
        }
        
        // Escape key to go back
        if (e.key === 'Escape') {
            const backButton = document.querySelector('.back-button');
            if (backButton) {
                backButton.click();
            }
        }
    });
}

function animateProgressBars() {
    const progressBars = document.querySelectorAll('.progress-fill');
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const progressBar = entry.target;
                const targetWidth = progressBar.style.width;
                progressBar.style.width = '0%';
                
                setTimeout(() => {
                    progressBar.style.transition = 'width 1.5s ease-out';
                    progressBar.style.width = targetWidth;
                }, 200);
            }
        });
    });
    
    progressBars.forEach(bar => observer.observe(bar));
}

function startHeartbeatAnimation() {
    // Add subtle heartbeat animation to the logo
    const logo = document.querySelector('.logo');
    if (logo) {
        setInterval(() => {
            logo.style.animation = 'pulse 0.6s ease-in-out';
            setTimeout(() => {
                logo.style.animation = '';
            }, 600);
        }, 5000);
    }
}

function showEncouragement(type = 'general') {
    const encouragements = {
        general: [
            "You're doing amazing! 🌟",
            "Keep up the great work! 💪",
            "You're getting stronger at math! 🚀",
            "Fantastic effort! 🎯",
            "You're a math superstar! ⭐"
        ],
        correct: [
            "Brilliant! That's exactly right! 🎉",
            "Perfect! You nailed it! 🎯",
            "Excellent work! You're on fire! 🔥",
            "Outstanding! Keep it up! 🌟",
            "Amazing! You're getting really good at this! 🚀"
        ],
        incorrect: [
            "Good try! Let's keep practicing! 💪",
            "Almost there! You're learning! 🌱",
            "Great effort! Every try makes you stronger! ⭐",
            "Don't worry, mistakes help us learn! 📚",
            "Keep going! You've got this! 🎯"
        ]
    };
    
    const messages = encouragements[type] || encouragements.general;
    const message = messages[Math.floor(Math.random() * messages.length)];
    
    // Create floating message
    const floatingMessage = document.createElement('div');
    floatingMessage.textContent = message;
    floatingMessage.style.cssText = `
        position: fixed;
        top: 20%;
        left: 50%;
        transform: translateX(-50%);
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: white;
        padding: 1rem 2rem;
        border-radius: 25px;
        font-family: 'Comic Neue', cursive;
        font-size: 1.2rem;
        font-weight: bold;
        z-index: 1000;
        box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        animation: encouragementFloat 3s ease-out forwards;
    `;
    
    // Add animation keyframes
    if (!document.querySelector('#encouragement-styles')) {
        const style = document.createElement('style');
        style.id = 'encouragement-styles';
        style.textContent = `
            @keyframes encouragementFloat {
                0% {
                    opacity: 0;
                    transform: translateX(-50%) translateY(20px) scale(0.8);
                }
                20% {
                    opacity: 1;
                    transform: translateX(-50%) translateY(0) scale(1);
                }
                80% {
                    opacity: 1;
                    transform: translateX(-50%) translateY(0) scale(1);
                }
                100% {
                    opacity: 0;
                    transform: translateX(-50%) translateY(-20px) scale(0.8);
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(floatingMessage);
    
    setTimeout(() => {
        floatingMessage.remove();
    }, 3000);
}

// Utility functions for the exercise page
function updateStreakIndicator(streak) {
    const indicator = document.querySelector('.streak-indicator');
    if (indicator) {
        indicator.innerHTML = '🔥'.repeat(Math.min(streak, 5));
        if (streak >= 5) {
            showCelebration("Amazing streak! You're on fire! 🔥");
        }
    }
}

function confettiEffect() {
    // Create confetti particles
    for (let i = 0; i < 50; i++) {
        setTimeout(() => {
            createConfetti();
        }, i * 50);
    }
}

function createConfetti() {
    const confetti = document.createElement('div');
    const colors = ['#ff6b6b', '#4ecdc4', '#ffd93d', '#ff8a65', '#9c27b0', '#00bcd4'];
    const shapes = ['🎉', '🌟', '⭐', '🎈', '🎊'];
    
    confetti.textContent = shapes[Math.floor(Math.random() * shapes.length)];
    confetti.style.cssText = `
        position: fixed;
        top: -10px;
        left: ${Math.random() * 100}%;
        font-size: ${Math.random() * 20 + 10}px;
        color: ${colors[Math.floor(Math.random() * colors.length)]};
        pointer-events: none;
        z-index: 1000;
        animation: confettiFall ${Math.random() * 3 + 2}s linear forwards;
    `;
    
    // Add confetti animation if not exists
    if (!document.querySelector('#confetti-styles')) {
        const style = document.createElement('style');
        style.id = 'confetti-styles';
        style.textContent = `
            @keyframes confettiFall {
                to {
                    transform: translateY(100vh) rotate(720deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(confetti);
    
    setTimeout(() => {
        confetti.remove();
    }, 5000);
}

// Export functions for use in other scripts
window.DianaMath = {
    playSound,
    showCelebration,
    showEncouragement,
    confettiEffect,
    updateStreakIndicator
};

console.log('🎮 DianaMath interactive features loaded!');