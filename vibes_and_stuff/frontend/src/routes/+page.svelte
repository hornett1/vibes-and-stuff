<script lang="ts">
    import { onMount } from 'svelte';
    import { user } from '../stores/user';
    import axios from 'axios';

    onMount(async () => {
        const csrfToken = document.cookie
            .split('; ')
            .find(row => row.startsWith('csrftoken='))
            ?.split('=')[1];

        try {
            const response = await axios.get('http://127.0.0.1:8000/api/current-user/', {
                withCredentials: true,
                headers: {
                    'X-CSRFToken': csrfToken || '',
                },
            }
            );
            user.set(response.data); // Set the user data in the store
        } catch (error) {
            console.error('Error fetching user:', error);
        }
    });
</script>

<main>
    {#if $user}
        <p>Welcome, {$user.username}!</p>
    {:else}
        <p>Loading...</p>
    {/if}
</main>
