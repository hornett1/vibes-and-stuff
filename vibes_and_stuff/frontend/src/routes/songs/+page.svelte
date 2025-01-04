<script lang="ts">
    import { onMount } from 'svelte';
    import axios from 'axios';
    import type { Song } from '../../lib/types'; 
    

    let songs:Song[] = [];
    let intervalId: NodeJS.Timeout;

    const fetchSongs = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/songs/');
            songs = response.data; 
        } catch (error) {
            console.error("Error fetching songs:", error);
        }
    };

    onMount(() => {
        fetchSongs();
        intervalId = setInterval(fetchSongs, 5000);

        return () => {
            clearInterval(intervalId);
        };
    });
</script>

<main class='size-full h-screen text-center'>
    <span class="flex flex-row items-center justify-center">
        <h1 class="text-yellow-100">Songs List</h1>
        <a class="align-middle ml-1 text-blue-500 hover:underline" href="/songs/create_song">Create</a>
      </span>
      
    <ul class='ml-1 text-amber-700 flex flex-col justify-center'>
        {#each songs as song}
            <li class='bg-yellow-100 rounded-md w-fit m-1 p-1'>{song.title} - {song.author}
                <audio controls src="{song.source}"></audio>
                <p class='text-black text-center'>Uploaded by {song.uploader_name}</p>
                <a href='songs/delete_song/{song.id}' class='text-red-600'>Delete</a>
            </li>
        {/each}
    </ul>
</main>

<style>
    h1 {
        font-size: 1.4rem;
        font-weight: bold;
    }
</style>