<template>
  <main>
    <h1>Auth Demo (Vue + Flask)</h1>
    <nav>
      <button @click="view='home'">Home</button>
      <button @click="view='users'">Usuarios</button>
    </nav>

    <HomeView v-if="view==='home'" />
    <UsersView v-else />
  </main>
</template>

<script setup>
import { ref } from "vue";
import HomeView from "./views/HomeView.vue";
import UsersView from "./views/UsersView.vue";
const view = ref('home');
</script>

<style>
body { font-family: system-ui, -apple-system, Segoe UI, Roboto, sans-serif; }
main { padding: 24px; max-width: 1000px; margin: auto; }
nav { margin: 12px 0 24px; display:flex; gap:8px; }
button { cursor:pointer; padding:8px 12px; }
</style>

