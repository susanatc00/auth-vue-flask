from flask import Flask, request, jsonify
from flask_cors import CORS
from database import Base, engine, SessionLocal
from models import User

app = Flask(__name__)
# Permite peticiones desde el front en http://localhost:5173
CORS(app, resources={r"/api/*": {"origins": "http://localhost:5173"}}, supports_credentials=True)

# Crea tablas
Base.metadata.create_all(bind=engine)

# Usuario de prueba (user@test.com / Test123) si no existe
def ensure_seed_user():
    db = SessionLocal()
    try:
        email = "user@test.com"
        pwd = "Test123"
        u = db.query(User).filter(User.email == email).first()
        if not u:
            u = User(email=email, password_hash=User.hash_password(pwd))
            db.add(u)
            db.commit()
    finally:
        db.close()

ensure_seed_user()

# ---------- RUTAS ----------

@app.post("/api/register")
def register():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email or not password:
        return jsonify({"ok": False, "error": "email y password son obligatorios"}), 400

    db = SessionLocal()
    try:
        exists = db.query(User).filter(User.email == email).first()
        if exists:
            return jsonify({"ok": False, "error": "El email ya está registrado"}), 409

        u = User(email=email, password_hash=User.hash_password(password))
        db.add(u)
        db.commit()
        return jsonify({"ok": True, "message": "Usuario registrado"})
    finally:
        db.close()

@app.post("/api/login")
def login():
    data = request.get_json(force=True)
    email = (data.get("email") or "").strip().lower()
    password = data.get("password") or ""

    if not email or not password:
        return jsonify({"ok": False, "error": "email y password son obligatorios"}), 400

    db = SessionLocal()
    try:
        u = db.query(User).filter(User.email == email).first()
        if not u or not u.verify_password(password):
            return jsonify({"ok": False, "error": "Credenciales inválidas"}), 401

        # Para el ejercicio NO generamos JWT; devolvemos un "token" simulado
        return jsonify({"ok": True, "token": "fake-token-123", "email": u.email})
    finally:
        db.close()

# CRUD mínimo para demostrar (READ list)
@app.get("/api/users")
def list_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return jsonify([{"id": u.id, "email": u.email, "created_at": u.created_at.isoformat()} for u in users])
    finally:
        db.close()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
 
