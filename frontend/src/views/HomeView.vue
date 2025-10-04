<template>
  <div class="grid">
    <RegisterForm />
    <LoginForm />
  </div>
</template>

<script setup>
import RegisterForm from "../components/RegisterForm.vue";
import LoginForm from "../components/LoginForm.vue";
</script>

<style scoped>
.grid { display:flex; gap:24px; flex-wrap:wrap; }
</style>

