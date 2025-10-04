 <template>
  <form @submit.prevent="onSubmit" class="card">
    <h2>Inicio de sesión</h2>
    <label>Email</label>
    <input v-model="email" type="email" required />
    <label>Contraseña</label>
    <input v-model="password" type="password" required />
    <button type="submit">Ingresar</button>
    <p class="msg" v-if="msg">{{ msg }}</p>
  </form>
</template>

<script setup>
import { ref } from "vue";
import { login } from "../api";

const email = ref("user@test.com");   // precargado para probar
const password = ref("Test123");
const msg = ref("");

const onSubmit = async () => {
  msg.value = "";
  try {
    const { data } = await login(email.value, password.value);
    msg.value = data.ok ? `Bienvenido ${data.email}` : "Credenciales inválidas";
  } catch (err) {
    msg.value = err?.response?.data?.error || "Error en login";
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


