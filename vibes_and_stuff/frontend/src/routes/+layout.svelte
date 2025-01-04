<script lang="ts">
	import '../app.css';
	let { children } = $props();
	import { Axios } from "axios";
    import { onMount } from "svelte";
</script>

{@render children()}
