let cassettes = document.querySelectorAll('.cassette');

let togglers = document.querySelectorAll('.toggler');

function scrollCassetteIntoView(cassette) {
    const rect = cassette.getBoundingClientRect();
    const viewportHeight = window.innerHeight;
    const scrollTop = window.scrollY;
    const documentHeight = document.documentElement.scrollHeight;
    const cassetteHeight = rect.height;
    const buffer = 50; // Добавляем буферную зону
    
    // Проверяем, находится ли кассета в начале документа
    if (rect.top + scrollTop < viewportHeight / 2) {
        window.scrollTo({
            top: Math.max(0, scrollTop + rect.top - buffer),
            behavior: 'smooth'
        });
    }
    // Проверяем, находится ли кассета в конце документа
    else if (rect.bottom + scrollTop > documentHeight - viewportHeight / 2) {
        window.scrollTo({
            top: Math.min(
                documentHeight - viewportHeight,
                scrollTop + rect.top - (viewportHeight - cassetteHeight) + buffer
            ),
            behavior: 'smooth'
        });
    }
    // Для кассет в середине
    else {
        window.scrollTo({
            top: scrollTop + rect.top - (viewportHeight - cassetteHeight) / 2,
            behavior: 'smooth'
        });
    }
}

togglers.forEach(toggler => {
    toggler.addEventListener('click', function() {
        let cassette = this.closest('.cassette');
        if (cassette) {
            // Закрываем все другие открытые кассеты
            cassettes.forEach(c => {
                if (c !== cassette && c.classList.contains('is-flipped')) {
                    c.classList.remove('is-flipped');
                    setTimeout(() => { c.style.zIndex = '1'; }, 500); // После анимации
                }
            });

            cassette.classList.toggle('is-flipped');
            cassette.style.zIndex = cassette.classList.contains('is-flipped') ? '1000' : '1';
        }
    });
});

document.querySelectorAll('.hider').forEach(hider => {
    hider.addEventListener('click', function() {
        let cassette = this.closest('.cassette');
        if (cassette) {
            cassette.classList.toggle('is-flipped');
            setTimeout(() => { 
                cassette.style.zIndex = '1';
            }, 500); // После анимации
        }
    });
});
