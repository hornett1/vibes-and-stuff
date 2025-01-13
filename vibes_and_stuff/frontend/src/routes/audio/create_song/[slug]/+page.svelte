<script>
    import { onMount } from 'svelte';
    import axios from 'axios';
    import { page } from '$app/stores';

    let slug= parseInt($page.params.slug);

    let song = {
        id: 1,
        title: '',
        author: '',
        uploader: 1,
        cassette_id: slug,
        cassette: '',
        uploader_name: '',
        source: ''
    };

    let file = null; 
    let responseData = null;
    let success = false;
    let errorMessage = null; 

    async function addSong(event) {
        event.preventDefault();


        const formData = new FormData();
        formData.append('title', song.title);
        formData.append('author', song.author);
        formData.append('uploader', song.uploader.toString());
        formData.append('uploader_name', song.uploader_name);
        formData.append('cassette_id', song.cassette_id.toString());
        formData.append('cassette', song.cassette);

        if (file) {
            formData.append('source', file);
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/songs/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            responseData = response.data;
            console.log('Song added successfully:', responseData);
            console.log('Cassette ID:', song.cassette_id);
            success = true;
            errorMessage = null;
        } catch (error) {
            console.error('Error adding song:', error);
            errorMessage = 'Error adding song. Please try again.';
            success = false;
        }
    }
</script>

<main class="max-w-md mx-auto p-6 bg-yellow-100 text-white rounded-lg shadow-lg mt-36 overflow-hidden">
    <span class='flex flex-row'>
        <a href='/audio' class="text-2xl mb-4 text-amber-700">&#8678</a>
        <h1 class="text-2xl mb-4 text-amber-700">Add a New Song</h1>
    </span>
    <form on:submit={addSong} class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-amber-700">Title</label>
        <input id="title" bind:value={song.title} type="text" required class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100" />
      </div>
      <div>
        <label for="artist" class="block text-sm font-medium text-amber-700">Author</label>
        <input id="artist" bind:value={song.author} type="text" required class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100" />
      </div>
      <div>
        <label for="source" class="block text-sm font-medium text-amber-700">File</label>
        <input id="source" type="file" class='text-amber-700' required on:change={(e) => file = (e.target).files?.[0] || null} />
      </div>
      <button type="submit" class="w-full bg-yellow-500 hover:bg-yellow-600 text-yellow-100 py-2 px-4 rounded">Add Song</button>
      {#if success && responseData }
      <p class="w-full py-2 px-4 text-wrap text-amber-700">Song added successfully</p>
      {:else if errorMessage}
      <p class="w-full py-2 px-4 text-wrap text-red-600">{errorMessage}</p>
      {/if}
    </form>
</main>

<style>
</style>
