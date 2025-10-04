<template>
  <section>
    <h2>Usuarios (demo READ)</h2>
    <button @click="load">Cargar</button>
    <ul>
      <li v-for="u in users" :key="u.id">{{ u.id }} — {{ u.email }} — {{ u.created_at }}</li>
    </ul>
    <p v-if="err" style="color:red">{{ err }}</p>
  </section>
</template>

<script setup>
import { ref } from "vue";
import { fetchUsers } from "../api";
const users = ref([]);
const err = ref("");

const load = async () => {
  err.value = "";
  try {
    const { data } = await fetchUsers();
    users.value = data;
  } catch (e) {
    err.value = "No se pudieron cargar usuarios";
  }
};
</script>
 
