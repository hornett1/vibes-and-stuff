<script lang="ts">
    export let user: { username: string; email: string } | null;
</script>

<main class="min-h-screen bg-gray-100 flex flex-col">
    <!-- Навигационное меню -->
    <nav class="bg-blue-500 p-4 text-white">
        <ul class="flex space-x-4">
            <li>
                <a href="/audio" class="hover:underline">Songs</a>
            </li>
            <li>
                <a href="/gallery" class="hover:underline">Gallery</a>
            </li>
            <li>
                <a href="/forum" class="hover:underline">Forum</a>
            </li>

            <li>
                <a href="/login" class="hover:underline">Login</a>
            </li>
            <li>
                <a href="/register" class="hover:underline">Register</a>
            </li>

            <!-- Показать имя пользователя, если он авторизован -->
        </ul>
    </nav>
    {#if user}
        <li class="ml-auto">
            <span class="text-white">Welcome, {user.username} ({user.email})</span>
        </li>
    {:else}
        <li>
            <p class='ml-auto'>Ошибка с пользователем</p>
        </li>
    {/if}
</main>
