import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:5000/api",
  withCredentials: false
});

export const register = (email, password) =>
  api.post("/register", { email, password });

export const login = (email, password) =>
  api.post("/login", { email, password });

export const fetchUsers = () => api.get("/users");

export default api;