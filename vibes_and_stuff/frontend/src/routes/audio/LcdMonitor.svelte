<script>
    export let song; // Получаем песню как пропс
</script>

{#if song}
    <div class='lcd-monitor'>
        <h2 class='text-xl font-bold'>{song.title}</h2>
        <p class='text-lg'>{song.author}</p>
        <audio controls src="{song.source}"></audio>
        <p class='text-center text-sm'>{song.uploader_name}</p>
    </div>
{/if}

<style>
    .lcd-monitor {
        font-family: 'LCD Dot';
        background-color: #3b4d3b; 
        color: #1c1c1c;
        text-shadow: 0 0 2px #2e2e2e;
        text-rendering: geometricPrecision;
        border: 1px solid #000000;
        box-shadow: inset 0 0 10px #000000, 3px 3px 3px rgba(0,0,0,0.3);
        padding: 10px;
        margin: 20px 0;
    }

    .lcd-monitor::selection {
        color: #3b4d3b;
        background-color: #1c1c1c;
        text-shadow: 0 0 2px #3b4d3b;
    }
</style>
