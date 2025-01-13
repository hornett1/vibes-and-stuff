<script>
    import axios from 'axios';
    import { onMount } from 'svelte'; 
    import LcdMonitor from './LcdMonitor.svelte'; 

    let cassettes = [];
    let currentSong = null; // Текущее состояние для песни

    let intervalId;

    const fetchCassettes = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/api/cassettes/');
            cassettes = response.data; 
        } catch (error) {
            console.error("Error fetching cassettes:", error);
        }
    };

    const handlePlaySong = (song) => {
        currentSong = song; 
    };

    onMount(() => {
        fetchCassettes();
        intervalId = window.setInterval(fetchCassettes, 5000);

        if (typeof window !== 'undefined') {
            console.log('Adding TornPaper script to DOM');
            const script = document.createElement('script');
            script.src = 'https://cdn.jsdelivr.net/gh/happy358/TornPaper@v0.0.3/tornpaper.min.js';
            script.onload = () => {
                console.log('TornPaper script loaded');
                new Tornpaper({
                    filterName: "filter_tornpaper",
                    seed: 9,
                    tornFrequency: 0.05,
                    tornScale: 10,
                    grungeFrequency: 0.03,
                    grungeScale: 3
                });
            };
            document.body.appendChild(script);
        }


        return () => {
            clearInterval(intervalId);
        };
    });
</script>

<main class="size-full h-screen text-center">
    <!-- LCD монитор, показывающий информацию о текущей песне -->
    {#if currentSong}
        <LcdMonitor song={currentSong} />
    {/if}

    <span class="flex flex-row items-center justify-center">
        <h1 class="text-yellow-100">Cassettes List</h1>
        <a class="align-middle ml-1 text-blue-500 hover:underline" href="/audio/create_cassette">Create Cassette</a>
    </span>

    <ul class="mx-2 text-amber-700 flex flex-col justify-center">
        {#each cassettes as cassette}
        <li class="w-full rounded py-1 flex flex-row justify-between items-center my-1 h-24"
        style="background: url('/green-dust-and-scratches.png');
        background-color: {cassette.color1};
        background-blend-mode: overlay;">
                <a type="button" href="/audio/create_song/{cassette.id}">Create</a>
                <div class="relative flex-1 mx-4 text-center max-w-2xl h-full flex items-center justify-center">
                    <div class="relative w-full">
                        <h2 class="text-7xl text-black/70 reenie-beanie-regular" style="
                        background: url(/groovepaper.png); 
                        background-color: whitesmoke; 
                        filter: url(#filter_tornpaper);
                        white-space: nowrap;
                        overflow: hidden;
                        text-overflow: ellipsis;">{cassette.title}</h2>
                        <div class="absolute left-1/2 bottom-2 transform -translate-x-1/2 h-[2px] bg-gray-400 w-[98%]" style='background-image: url(/groovepaper.png)'></div>
                    </div>
                </div>
                <a type="button" class="text-red-600" href="/audio/delete_cassette/{cassette.id}">Delete</a>
            </li>  
        {/each}
    </ul>
</main>