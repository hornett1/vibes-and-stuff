<script>
    import { onMount } from 'svelte';
    import axios from 'axios';

    let cassette = {
        id: 1,
        title: '',
        author: '',
        description: '',
        color1: '',
        color2: '',
        color3: '',
        accent_color: '',
        songs: [] 
    };

    let success = false;
    let errorMessage = null;

    async function addCassette(event) {
        event.preventDefault();

        try {
            const response = await axios.post('http://127.0.0.1:8000/api/cassettes/', cassette);
            console.log('Cassette added successfully:', response.data);
            success = true;
            errorMessage = null;
        } catch (error) {
            console.error('Error adding cassette:', error);
            errorMessage = 'Error adding cassette. Please try again.';
            success = false;
        }
    }
</script>

<main class="max-w-md mx-auto p-6 bg-yellow-100 text-white rounded-lg shadow-lg mt-36 overflow-hidden">
    <span class='flex flex-row'>
        <a href='/audio' class="text-2xl mb-4 text-amber-700">&#8678</a>
        <h1 class="text-2xl mb-4 text-amber-700">Add a New Cassette</h1>
    </span>
    <form on:submit={addCassette} class="space-y-4">
      <div>
        <label for="name" class="block text-sm font-medium text-amber-700">Title</label>
        <input id="name" bind:value={cassette.title} type="text" required class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100" />
      </div>
      <div>
        <label for="name" class="block text-sm font-medium text-amber-700">Author</label>
        <input id="name" bind:value={cassette.author} type="text" required class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100" />
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-amber-700">Description</label>
        <textarea id="description" bind:value={cassette.description} class="w-full p-2 bg-amber-700 rounded border border-gray-600 focus:outline-none focus:ring focus:ring-yellow-500 text-yellow-100"></textarea>
      </div>
      <div>
        <label for="description" class="block text-sm font-medium text-amber-700">Colors</label>
        <p class='text-amber-700'>Body Color</p>
        <input class='w-full p-2' type='color' bind:value={cassette.color1} style='background-color: {cassette.color1}'>
        <input class='w-full p-2' type='color' bind:value={cassette.color2} style='background-color: {cassette.color2}'>
        <input class='w-full p-2' type='color' bind:value={cassette.color3} style='background-color: {cassette.color3}'>
        <input class='w-full p-2' type='color' bind:value={cassette.accent_color} style='background-color: {cassette.accent_color}'>
      </div>
      <button type="submit" class="w-full bg-yellow-500 hover:bg-yellow-600 text-yellow-100 py-2 px-4 rounded">Add Cassette</button>
      {#if success}
      <p class="w-full py-2 px-4 text-wrap text-amber-700">Cassette added successfully</p>
      {:else if errorMessage}
      <p class="w-full py-2 px-4 text-wrap text-red-600">{errorMessage}</p>
      {/if}
    </form>
</main>

<style>
</style>
