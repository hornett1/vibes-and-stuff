<script lang="ts">
    import { goto } from "$app/navigation";

    let username: string = '';
    let password: string = '';
    let email: string = '';

    interface Errors {
        username?: string[]; 
        password?: string[];
    }

    let errors: Errors = {};

    let handleSubmit = () => {
        const endpoint = 'http://127.0.0.1:8000/api/register/';
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json'},
            body: JSON.stringify({username: username, password: password, email: email})
        };

        fetch(endpoint, requestOptions)
            .then(response => response.json().then(data => ({status: response.status, body: data})))
            .then(data => {
                if (data.status === 201) {
                    goto('/register/success/')
                } else {
                    errors = data.body
                    console.log(data)
                }
            })
    }
</script>

<main class="flex items-center justify-center min-h-screen bg-gray-100">
    <form id="registrationForm" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-sm" on:submit|preventDefault={handleSubmit}>
        <div class="mb-4">
            <input type="text" id="username" name="username" required bind:value={username} placeholder='username'
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            {#if errors && errors.username}
                <p class="text-red-600 text-xs italic">{errors.username[0]}</p>
            {/if}

        </div>

        <div class="mb-4">
            <input type="password" id="password" name="password" placeholder="password" required bind:value={password}
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            {#if errors && errors.password}
                <p class="text-red-600 text-xs italic">{errors.password[0]}</p>
            {/if}
        </div>

        <div class="mb-6">
            <input type="email" id="email" name="email" placeholder='email@example.com' bind:value={email}
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
        </div>

        <div class="flex items-center justify-between w-full">
            <button type="submit"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full">
                Register
            </button>
        </div>
    </form>
</main>
