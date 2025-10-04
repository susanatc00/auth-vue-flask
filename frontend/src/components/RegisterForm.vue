<template>
  <form @submit.prevent="onSubmit" class="card">
    <h2>Registro</h2>
    <label>Email</label>
    <input v-model="email" type="email" required />
    <label>Contraseña</label>
    <input v-model="password" type="password" required />
    <button type="submit">Crear cuenta</button>
    <p class="msg" v-if="msg">{{ msg }}</p>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { register } from "../api";

const email = ref("");
const password = ref("");
const msg = ref("");

const onSubmit = async () => {
  msg.value = "";
  try {
    const { data } = await register(email.value, password.value);
    msg.value = data.message || "Registro exitoso";
  } catch (err) {
    msg.value = err?.response?.data?.error || "Error registrando";
  }
};
</script>

<style scoped>
.card { max-width: 360px; padding: 16px; border: 1px solid #ddd; border-radius: 8px; }
label { display:block; margin-top: 8px; }
input { width:100%; padding:8px; margin-top:4px; }
button { margin-top:12px; width:100%; padding:10px; cursor:pointer; }
.msg { margin-top:10px; }
</style>


