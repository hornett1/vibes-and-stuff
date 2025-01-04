<script lang="ts">
	import '../../app.css';
	let { children } = $props();
</script>

<style>
    :root {
        background-color: #592700;
        background-image: url(/dark-wood.png);
    }
</style>

{@render children()}