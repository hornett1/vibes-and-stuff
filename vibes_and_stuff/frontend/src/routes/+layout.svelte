<script lang="ts">
	import '../app.css';
	let { children } = $props();
	import { Axios } from "axios";
	import { url } from 'inspector';
	import { text } from 'stream/consumers';
    import { onMount } from "svelte";
	import { blur } from 'svelte/transition';
</script>

<svelte:head>
	<link rel="preconnect" href="https://fonts.googleapis.com">
	<link rel="preconnect" href="https://fonts.gstatic.com">
	<link href="https://fonts.googleapis.com/css2?family=Reenie+Beanie&display=swap" rel="stylesheet">
	<script src="https://cdn.jsdelivr.net/gh/happy358/TornPaper@v0.0.3/tornpaper.min.js"></script>
	<style lang="postcss" scoped>
		:root {
			background: white;
		}
	
	@font-face {
		font-family: 'LCD Dot';
		src: url('/lcddot_tr.ttf') format('truetype');
	}

	.reenie-beanie-regular {
		font-family: "Reenie Beanie", serif;
		font-weight: 400;
		font-style: normal;
		letter-spacing: 0.05em;
    	text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3); 
		background: url(/groovepaper.png);
		background-clip: text;
	}
	</style>
</svelte:head>

{@render children()}
