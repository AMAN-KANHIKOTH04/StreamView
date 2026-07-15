document.addEventListener('DOMContentLoaded', () => {
    const playerContainer = document.getElementById('player-container');
    const uiOverlay = document.getElementById('ui-overlay');
    
    if (playerContainer || uiOverlay) {
        let idleTimer;
        function resetIdleTimer() {
            if (playerContainer) playerContainer.classList.remove('idle');
            if (uiOverlay) uiOverlay.classList.remove('controls-hidden');
            clearTimeout(idleTimer);
            idleTimer = setTimeout(() => {
                if (playerContainer) playerContainer.classList.add('idle');
                if (uiOverlay) uiOverlay.classList.add('controls-hidden');
            }, 3000);
        }
        const target = playerContainer || document.body;
        target.addEventListener('mousemove', resetIdleTimer);
        target.addEventListener('touchstart', resetIdleTimer);
        target.addEventListener('click', resetIdleTimer);
        resetIdleTimer();
    }

    const progressSlider = document.getElementById('progress-slider');
    const progressFill = document.getElementById('progress-fill');
    if (progressSlider && progressFill) {
        progressSlider.addEventListener('input', (e) => {
            progressFill.style.width = e.target.value + '%';
        });
    }
});