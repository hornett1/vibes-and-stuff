let lcd_monitor = document.getElementById('lcd-monitor');
let controls = document.querySelector('.radio-input');
let expand = document.getElementById('expand');
let cassette_player = document.getElementById('cassette-player');

let inactivityTimer;
let isCursorOnPlayer = false;

function resetTimer() {
    clearTimeout(inactivityTimer);
    controls.style.display = 'flex';
    lcd_monitor.style.display = 'block';
    expand.style.display = 'none';

    if (!isCursorOnPlayer) {
        inactivityTimer = setTimeout(hideControls, 2500);
    }
}

function hideControls() {
    if (!isCursorOnPlayer) { 
        controls.style.display = 'none';
        lcd_monitor.style.display = 'none';
        expand.style.display = 'block';
    }
}

cassette_player.addEventListener('mouseenter', function () {
    isCursorOnPlayer = true;
    resetTimer(); 
});

cassette_player.addEventListener('mouseleave', function () {
    isCursorOnPlayer = false;
    resetTimer(); 
});

expand.addEventListener('click', function () {
    controls.style.display = 'block';
    lcd_monitor.style.display = 'block';
    expand.style.display = 'none';
    resetTimer();
});

cassette_player.addEventListener('mousemove', resetTimer);
cassette_player.addEventListener('keypress', resetTimer);

resetTimer();
