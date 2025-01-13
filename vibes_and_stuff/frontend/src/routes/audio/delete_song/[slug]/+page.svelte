<script>
	import { page } from "$app/stores";
    import axios from "axios";


    async function deleteSong(event) {
        event.preventDefault();

        let slug = $page.params.slug;

        const response = await axios.delete(`http://127.0.0.1:8000/api/songs/${slug}/`);

        console.log(response);

        console.log('deleted song' + slug)
    }

</script>

<main>
    <p class='text-yellow-100'>Are you sure?</p>
    <span class='flex flex-row text-yellow-100'>
        <a href='/audio' class='mr-1'>No</a>
        <button type='button' on:click={deleteSong}>Yes</button>
    </span>
</main>

<style>
</style>