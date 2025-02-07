document.querySelector('.gallery').addEventListener('scroll', function(e) {
    let scrollLeft = e.target.scrollLeft;
    let scrollWidth = e.target.scrollWidth;
    let clientWidth = e.target.clientWidth;

    // Проверяем, если мы достигли конца галереи
    if (scrollLeft + clientWidth >= scrollWidth) {
        loadNextItems.call(this);  // Функция для загрузки следующих элементов
    }

    // Проверяем, если мы достигли начала галереи
    if (scrollLeft === 0) {
        loadPreviousItems.call(this);  // Функция для загрузки предыдущих элементов
    }
});

// Функция для загрузки следующих элементов
function loadNextItems() {
    let nextElement = this.querySelector('.gallery-item:first-child');
    if (nextElement) {
        this.appendChild(nextElement);  // Перемещаем элемент в конец
    }

    // После перемещения элемента сбрасываем scrollLeft в ноль
    this.scrollLeft -= nextElement.offsetWidth;  // Сдвигаем прокрутку назад, чтобы не было разрывов
}

// Функция для загрузки предыдущих элементов
function loadPreviousItems() {
    let prevElement = this.querySelector('.gallery-item:last-child');
    if (prevElement) {
        this.insertBefore(prevElement, this.firstChild);  // Перемещаем элемент в начало
    }

    // После перемещения элемента сбрасываем прокрутку в нужное место
    this.scrollLeft += prevElement.offsetWidth;  // Сдвигаем прокрутку вперед, чтобы не было разрывов
}
