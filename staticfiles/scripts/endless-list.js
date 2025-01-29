let block = Number(document.getElementById("block").value);
let blocks = Number(document.getElementById("blocks").value);
let curY = window.scrollY;

function onScroll() {
    let newY = window.scrollY;
    let dy = newY - curY;
    console.log(newY, dy, window.innerHeight);
    
    // Если прокрутка почти до конца страницы, загружаем новые блоки
    if (newY + window.innerHeight >= document.body.scrollHeight - 200 && block < blocks) {
        block++;

        fetch('?page=' + block, {
            headers: {
                'X-Requested-With': 'XMLHttpRequest'
            }
        })
        .then(response => {
            console.log(response);
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text();
        })
        .then(data => {
            document.getElementById("list").innerHTML += data;
            document.getElementById("block").value = block;

            if (block >= blocks) {
                console.log('end');
            }
        })
        .catch(error => console.log('Error:', error));
    }
}

// Добавляем обработчик события scroll
document.body.addEventListener("scroll", onScroll);

// Используем IntersectionObserver для скрытия/показа блоков
let observer = new IntersectionObserver((entries, observer) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.style.visibility = 'visible'; // Элемент стал видимым
        } else {
            entry.target.style.visibility = 'hidden'; // Элемент скрылся
        }
    });
}, {
    threshold: 0.1 // Блок будет считаться видимым, если хотя бы 10% его высоты видно в окне
});

// Наблюдаем за всеми блоками
document.querySelectorAll('.block').forEach(block => {
    observer.observe(block);
});
