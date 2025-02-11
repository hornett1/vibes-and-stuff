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

function preloadAudio(source) {
    return new Promise((resolve, reject) => {
        const audio = new Audio('/media/' + source);
        audio.addEventListener('canplaythrough', () => {
            resolve(source);
        }, { once: true });
        audio.addEventListener('error', reject);
    });
}

function loadPlaylistFromCassette(cassetteElement) {
    const songButtons = cassetteElement.querySelectorAll('button[onclick^="playSong"]');
    currentPlaylist = Array.from(songButtons).map(button => {
        try {
            const onclickStr = button.getAttribute('onclick');
            const params = onclickStr.match(/playSong\('([^']*)',\s*'([^']*)',\s*'([^']*)'/);
            
            if (!params || params.length < 4) {
                console.log('Invalid onclick format:', onclickStr);
                return null;
            }

            return {
                source: params[1],
                title: params[2],
                author: params[3],
                element: button
            };
        } catch (error) {
            console.log('Error parsing button:', error);
            return null;
        }
    }).filter(song => song !== null);
    
    if (currentPlaylist.length > 0) {
        currentPlaylist.slice(0, 3).forEach(song => {
            preloadAudio(song.source)
                .catch(error => console.log('Preload failed:', error));
        });
    }
}

function playSong(source, title, author, buttonElement = null) {
    if (!audioPlayer) return;
    
    if (buttonElement) {
        const cassetteElement = buttonElement.closest('section.cassette');
        if (cassetteElement) {
            loadPlaylistFromCassette(cassetteElement);
            currentSongIndex = currentPlaylist.findIndex(song => 
                song && song.source === source
            );
        }
        
        if (currentPlaylist[currentSongIndex + 1]) {
            preloadAudio(currentPlaylist[currentSongIndex + 1].source)
                .catch(error => console.log('Preload failed:', error));
        }
    }
    
    audioPlayer.src = '/media/' + source;
    if (songTitle) songTitle.textContent = title;
    if (songAuthor) songAuthor.textContent = author;
    
    audioPlayer.play().catch(error => {
        console.log('Error playing song:', error);
        playBtn.checked = false;
        pauseBtn.checked = true;
    });
}

function handlePlay() {
    if (playBtn.checked && audioPlayer.paused) {
        audioPlayer.play().catch(error => {
            console.log('Error playing:', error);
            playBtn.checked = false;
            pauseBtn.checked = true;
        });
    }
}

function handlePause() {
    if (pauseBtn.checked && !audioPlayer.paused) {
        audioPlayer.pause();
    }
}

function playNext() {
    if (currentPlaylist.length === 0) return;

    if (isShuffle) {
        let newIndex;
        do {
            newIndex = Math.floor(Math.random() * currentPlaylist.length);
        } while (newIndex === currentSongIndex);
        currentSongIndex = newIndex;
    } else {
        currentSongIndex = (currentSongIndex + 1) % currentPlaylist.length;
    }

    const nextSong = currentPlaylist[currentSongIndex];
    playSong(nextSong.source, nextSong.title, nextSong.author, nextSong.element);
}

function playPrev() {
    if (currentPlaylist.length === 0) return;
    
    if (isShuffle) {
        currentSongIndex = Math.floor(Math.random() * currentPlaylist.length);
    } else {
        currentSongIndex = (currentSongIndex - 1 + currentPlaylist.length) % currentPlaylist.length;
    }
    
    const prevSong = currentPlaylist[currentSongIndex];
    playSong(prevSong.source, prevSong.title, prevSong.author, prevSong.element);
}

function toggleRepeat() {
    isRepeat = !isRepeat;
    audioPlayer.loop = isRepeat;
}

function toggleShuffle() {
    isShuffle = !isShuffle;
}

function initializeEventListeners() {
    if (playBtn) playBtn.addEventListener('change', handlePlay);
    if (pauseBtn) pauseBtn.addEventListener('change', handlePause);
    if (repeatBtn) repeatBtn.addEventListener('change', toggleRepeat);
    if (shuffleBtn) shuffleBtn.addEventListener('change', toggleShuffle);
    if (prevBtn) prevBtn.addEventListener('click', playPrev);
    if (nextBtn) nextBtn.addEventListener('click', playNext);
    
    if (audioPlayer) {
        audioPlayer.addEventListener('ended', () => {
            if (isRepeat) {
                audioPlayer.play().catch(error => console.log('Playback failed:', error));
            } else {
                playNext();
            }
        });

        audioPlayer.addEventListener('play', () => {
            playBtn.checked = true;
            pauseBtn.checked = false;
        });

        audioPlayer.addEventListener('pause', () => {
            playBtn.checked = false;
            pauseBtn.checked = true;
        });
    }
}

function initPlayer() {
    if (!audioPlayer) return;
    
    audioPlayer.volume = 0.5;
    if (audioPlayer.paused) {
        playBtn.checked = false;
        pauseBtn.checked = true;
    } else {
        playBtn.checked = true;
        pauseBtn.checked = false;
    }
    initializeEventListeners();
}

if (document.getElementById('song-player')) {
    document.addEventListener('DOMContentLoaded', initPlayer);
} 