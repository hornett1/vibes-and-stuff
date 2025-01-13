<script>
	import '../../app.css';
	let { children } = $props();
	import { Axios } from "axios";
    import { onMount } from "svelte";
</script>

{@render children()}

<style>
	@font-face {
		font-family: 'LCD Dot';
	}
</style>