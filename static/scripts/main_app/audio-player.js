const audioPlayer = document.getElementById('song-player');
const songTitle = document.getElementById('song-title');
const songAuthor = document.getElementById('song-author');

const playBtn = document.getElementById('value-1');
const pauseBtn = document.getElementById('value-2');
const repeatBtn = document.getElementById('value-3');
const shuffleBtn = document.getElementById('value-4');
const prevBtn = document.getElementById('value-5');
const nextBtn = document.getElementById('value-6');

let currentPlaylist = [];
let currentSongIndex = 0;
let isRepeat = false;
let isShuffle = false;

function savePlayerState() {
    localStorage.setItem('playerState', JSON.stringify({
        source: audioPlayer.src.replace(window.location.origin, ''),
        title: songTitle?.textContent || '',
        author: songAuthor?.textContent || '',
        time: audioPlayer.currentTime,
        isPlaying: !audioPlayer.paused,
        isRepeat,
        isShuffle,
}));
}

function loadPlayerState() {
    const savedState = JSON.parse(localStorage.getItem('playerState'));
    if (savedState?.source) {
        audioPlayer.src = savedState.source;
        if (songTitle) songTitle.textContent = savedState.title;
        if (songAuthor) songAuthor.textContent = savedState.author;
        audioPlayer.currentTime = savedState.time || 0;
        isRepeat = savedState.isRepeat;
        isShuffle = savedState.isShuffle;
        repeatBtn.checked = isRepeat;
        shuffleBtn.checked = isShuffle;

        audioPlayer.play()
    }
}

function playSong(source, title, author) {
    if (!audioPlayer) return;
    
    audioPlayer.src = '/media/' + source;
    if (songTitle) songTitle.textContent = title;
    if (songAuthor) songAuthor.textContent = author;

    audioPlayer.play()

    savePlayerState();
}

function handlePlay() {
    if (audioPlayer.paused) {
        audioPlayer.play()
    }
    savePlayerState();
}

function handlePause() {
    if (!audioPlayer.paused) {
        audioPlayer.pause();
    }
    savePlayerState();
}

function playNext() {
    if (currentPlaylist.length === 0) return;

    currentSongIndex = isShuffle
        ? Math.floor(Math.random() * currentPlaylist.length)
        : (currentSongIndex + 1) % currentPlaylist.length;

    const nextSong = currentPlaylist[currentSongIndex];
    playSong(nextSong.source, nextSong.title, nextSong.author);
}

function playPrev() {

    currentSongIndex = isShuffle
        ? Math.floor(Math.random() * currentPlaylist.length)
        : (currentSongIndex - 1 + currentPlaylist.length) % currentPlaylist.length;

    const prevSong = currentPlaylist[currentSongIndex];
    playSong(prevSong.source, prevSong.title, prevSong.author);
}

function toggleRepeat() {
    isRepeat = !isRepeat;
    audioPlayer.loop = isRepeat;
    savePlayerState();
}

function toggleShuffle() {
    isShuffle = !isShuffle;
    savePlayerState();
}

function updatePlayPauseButtons() {
    if (audioPlayer.paused) {
        playBtn.classList.add('active');
        pauseBtn.classList.remove('active');
    } else {
        playBtn.classList.remove('active');
        pauseBtn.classList.add('active');
    }
}

function initializeEventListeners() {
    if (playBtn) playBtn.addEventListener('click', handlePlay);
    if (pauseBtn) pauseBtn.addEventListener('click', handlePause);

    if (repeatBtn) repeatBtn.addEventListener('change', toggleRepeat);
    if (shuffleBtn) shuffleBtn.addEventListener('change', toggleShuffle);
    if (prevBtn) prevBtn.addEventListener('click', playPrev);
    if (nextBtn) nextBtn.addEventListener('click', playNext);

    if (audioPlayer) {
        audioPlayer.addEventListener('timeupdate', savePlayerState);
        audioPlayer.addEventListener('ended', () => {
            if (!isRepeat) playNext();
        });
        audioPlayer.addEventListener('play', () => {
            savePlayerState();
            updatePlayPauseButtons();
        });
        audioPlayer.addEventListener('pause', () => {
            savePlayerState();
            updatePlayPauseButtons();
        });
    }
}

function initPlayer() {
    if (!audioPlayer) return;

    audioPlayer.volume = 0.5;
    initializeEventListeners();
    loadPlayerState();

    audioPlayer.play().then(() => {
        updatePlayPauseButtons();
    }).catch(error => {
        console.log('Autoplay was prevented:', error);
    });

    updatePlayPauseButtons();
}

document.addEventListener('DOMContentLoaded', initPlayer);
