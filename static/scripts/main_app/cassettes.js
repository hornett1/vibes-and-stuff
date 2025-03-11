function enableEdit() {
    const paragraphs = document.getElementsByClassName('editable');

    Array.from(paragraphs).forEach(p => {
        if (p.dataset.listenerAttached) return;
        p.dataset.listenerAttached = "true";  

        const cassetteId = p.dataset.id;
        p.dataset.originalText = p.innerText.trim();

        p.addEventListener("keydown", function (event) {
            if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                p.blur();
            }
        });

        p.addEventListener("blur", function () {
            const updatedText = p.innerText.trim();
            if (updatedText !== p.dataset.originalText) {
                const field = p.classList.contains('title') ? 'title' : 'author';
                fetch(`/cassettes/${cassetteId}/update/`, {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                        "X-CSRFToken": csrf_token 
                    },
                    body: JSON.stringify({ [field]: updatedText })
                })
                .then(response => response.json())
                .then(data => console.log("Успешно сохранено:", data))
                .catch(error => console.error("Ошибка:", error));

                p.dataset.originalText = updatedText;
            }
        });
    });
}

function enableCreate() {
    const title = document.getElementById('title');
    const author = document.getElementById('author');
    const color1 = document.getElementById('color1');
    const color2 = document.getElementById('color2');
    const color3 = document.getElementById('color3');
    const accent_color = document.getElementById('accent_color');

    fetch('/cassettes/create/', {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrf_token 
        },
        body: JSON.stringify({
            title: title.value.trim(),
            author: author.value.trim(),
            color1: color1.value.trim(),
            color2: color2.value.trim(),
            color3: color3.value.trim(),
            accent_color: accent_color.value.trim()
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("Создано:", data);
        location.reload();
    })
    .catch(err => console.log(err));

    location.reload()
}
