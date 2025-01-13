<script lang="ts">
    import { goto } from "$app/navigation";

    let username: string = '';
    let password: string = '';

    interface Errors {
        username?: string[];
        password?: string[];
        non_field_errors?: string[];
    }

    let errors: Errors = {};

    let handleLogin = () => {
        const endpoint = 'http://127.0.0.1:8000/api/login/';
        const requestOptions = {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ username: username, password: password })
        };

        fetch(endpoint, requestOptions)
            .then(response => response.json().then(data => ({ status: response.status, body: data })))
            .then(data => {
                if (data.status === 200) {
                    // Успешный логин, перенаправляем пользователя
                    goto('/');
                } else {
                    // Обработка ошибок логина
                    errors = data.body;
                    console.log(data);
                    console.log({ username, password });
                }
            })
            .catch(error => {
                console.log({ username, password });
                console.error('Ошибка:', error);
            });
    }
</script>

<main class="flex items-center justify-center min-h-screen bg-gray-100">
    <form id="loginForm" class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-sm" on:submit|preventDefault={handleLogin}>
        <div class="mb-4">
            <input type="text" id="username" name="username" required bind:value={username} placeholder='Username'
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            {#if errors.username}
                <span id="usernameError" class="text-red-500 text-xs italic">{errors.username.join(', ')}</span>
            {/if}
        </div>
    
        <div class="mb-4">
            <input type="password" id="password" name="password" required bind:value={password} placeholder='Password'
                class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline">
            {#if errors.password}
                <span id="passwordError" class="text-red-500 text-xs italic">{errors.password.join(', ')}</span>
            {/if}
        </div>
    
        {#if errors.non_field_errors}
            <div class="mb-4 text-red-500 text-xs italic">{errors.non_field_errors.join(', ')}</div>
        {/if}
    
        <div class="flex items-center justify-between w-full">
            <button type="submit"
                class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline w-full">
                Login
            </button>
        </div>
    </form>    
</main>
