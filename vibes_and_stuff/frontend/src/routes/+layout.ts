import type { Load } from '@sveltejs/kit';

export const load: Load = async ({ fetch }) => {
  const response = await fetch('http://127.0.0.1:8000/api/current-user/');

  if (response.ok) {
    const user = await response.json();
    return { props: { user } };
  } else {
    return { props: { user: null } };
  }
};
