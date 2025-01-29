document.addEventListener("DOMContentLoaded", () => {
  const cards = document.querySelectorAll('.card');

  cards.forEach(card => {
    card.addEventListener('click', () => {
      card.classList.toggle('is-flipped');
    });
  });
});

  function postImage(event) {
    event.preventDefault(); 
  
    const fileInput = document.getElementById('image');
    const titleInput = document.getElementById('title');
    const cardContainer = document.getElementById('list');
  
    const file = fileInput.files[0];
    const title = titleInput.value.trim();
  
    if (!file || !title) {
      alert('no info');
      return;
    }
  
    const formData = new FormData();
    formData.append('image', file);
    formData.append('title', title);
    
    console.log(csrftoken)
  
    fetch('/gallery/add/image/', {
      method: 'POST',
      body: formData,
      headers:{
        "X-CSRFToken": csrftoken,
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then(response => {
        if (!response.ok) {
          throw new Error(`error ${response.status}`);
        }

        const contentType = response.headers.get('Content-Type');
        // if (contentType && contentType.includes('application/json')) {
          return response.json();
        // } else {
          throw new Error('not app/json');
        // }

      })
      .then(data => {
        console.log('GREAT SUCCESS', data);
  
        cardContainer.innerHTML += data;
  
        fileInput.value = '';
        titleInput.value = '';
      })
      .catch(error => {
        console.error('Error', error);
      });
  }
  
  