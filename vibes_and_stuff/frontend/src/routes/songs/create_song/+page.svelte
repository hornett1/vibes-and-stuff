<script lang="ts">
    import { onMount } from 'svelte';
    import axios from 'axios';
    import type { Song } from '../../../lib/types'; 

    let song: Song = {
        id: 1,
        title: '',
        author: '',
        uploader: 1,
        uploader_name: '',
        source: ''
    };

    let file: File | null = null; 
    
    async function addSong(event: Event) {
        event.preventDefault();

        const formData = new FormData();
        formData.append('title', song.title);
        formData.append('author', song.author);
        formData.append('uploader', song.uploader.toString());
        formData.append('uploader_name', song.uploader_name);

        if (file) {
            formData.append('source', file);
        }

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/songs/', formData, {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            });
            console.log('Song added successfully:', response.data);
        } catch (error) {
            console.error('Error adding song:', error);
        }
    }
</script>

<main class="max-w-md mx-auto p-6 bg-yellow-100 text-white rounded-lg shadow-lg mt-36 overflow-hidden">
    <h1 class="text-2xl mb-4 text-amber-700">Add a New Song</h1>
    <form on:submit={addSong} class="space-y-4">
      <div>
        <label for="title" class="block text-sm font-medium text-amber-700">Title</label>
        <input id="title" bind:value={song.title} type="text" required class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100" />
      </div>
      <div>
        <label for="artist" class="block text-sm font-medium text-amber-700">Artist</label>
        <input id="artist" bind:value={song.author} type="text" required class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100" />
      </div>
      <div>
        <label for="source" class="block text-sm font-medium text-amber-700">File</label>
        <input id="source" type="file" on:change={(e) => file = (e.target as HTMLInputElement).files?.[0] || null} />
      </div>
      <button type="submit" class="w-full bg-yellow-500 hover:bg-yellow-600 text-white py-2 px-4 rounded">Add Song</button>
    </form>
</main>
