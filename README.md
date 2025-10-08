# 🧠 Flask OpenAI API

Este proyecto implementa un servicio **Flask** que permite realizar consultas al modelo **GPT** de OpenAI mediante una API REST.  
Incluye soporte **CORS** para integraciones web y un ejemplo de uso con **cURL**.

---

## 🚀 Características

- API HTTP con Flask (`/ask`)
- Conexión al modelo `gpt-3.5-turbo` de OpenAI
- Manejo de errores HTTP estándar
- Soporte completo para **CORS**
- Ejemplo de uso con `curl`
- Configurable y fácil de integrar en aplicaciones web

---

## 📂 Estructura del proyecto

```
├── main.py        # Script principal con la API Flask
├── requirements.txt (opcional)
└── README.md       # Documentación del proyecto
```

---

## ⚙️ Requisitos

Instalar las dependencias necesarias:

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuración

Antes de ejecutar, define tu clave de OpenAI:

```python
OPENAI_KEY = "tu_clave_aquí"
```

También puedes exportarla como variable de entorno:

```bash
export OPENAI_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

Y luego modificar en el script:

```python
api_key=os.getenv("OPENAI_KEY")
```

---

## ▶️ Ejecución

Inicia el servidor en el puerto **5080**:

```bash
python3 main.py
```

El servicio estará disponible en:

```
http://localhost:5080/ask
```

---

## 🧩 Uso de la API

### Endpoint: `/ask`  
**Método:** `POST`

**Cuerpo del request (JSON):**
```json
{
  "prompt": "¿Cuál es la diferencia entre IA y Machine Learning?"
}
```

### Ejemplo con `curl`:
```bash
curl -X POST http://localhost:5080/ask   -H "Content-Type: application/json"   -d '{"prompt": "¿Cuál es la diferencia entre IA y Machine Learning?"}'
```

### Respuesta (JSON):
```json
{
  "response": "La inteligencia artificial es el campo general..."
}
```

---

## ⚠️ Errores comunes

| Código | Descripción |
|:-------:|-------------|
| 400 | Falta el campo `prompt` |
| 500 | Error en la conexión con OpenAI |

---

## 🧱 Integración web

Puedes integrar este endpoint desde cualquier frontend (HTML, React, Angular, etc.) usando `fetch`:

```javascript
fetch("http://localhost:5080/ask", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ prompt: "Hola GPT 3.5 turbo" })
})
  .then(res => res.json())
  .then(data => console.log(data.response));
```

## Pagina web

Puedes abrir el archivo index.html para probar el chat
