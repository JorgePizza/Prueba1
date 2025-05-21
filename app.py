import streamlit as st

st.set_page_config(page_title="Aprende Python - Condicionales y Bucles", layout="centered")

st.title("🐍 Aprende Python: Condicionales y Bucles")
st.markdown("""
Bienvenido a esta mini plataforma educativa donde aprenderás los conceptos básicos de Python:

- `if` para decisiones.
- `for` para repeticiones con rango o listas.
- `while` para repeticiones hasta que algo ocurra.
""")

# Explicación de conceptos
with st.expander("📘 ¿Cómo funciona `if` en Python?"):
    st.code("""
x = 5
if x > 3:
    print("x es mayor que 3")
""")

with st.expander("🔁 ¿Cómo funciona `for` en Python?"):
    st.code("""
for i in range(3):
    print(i)
""")

with st.expander("🔁 ¿Cómo funciona `while` en Python?"):
    st.code("""
i = 0
while i < 3:
    print(i)
    i += 1
""")

st.divider()

# Preguntas del Quiz
st.subheader("🧠 Quiz: ¿Cuánto sabes sobre Python?")
preguntas = [
    {
        "pregunta": "¿Qué hace un bucle `for` en Python?",
        "opciones": ["Repite una acción mientras una condición sea verdadera", 
                     "Repite una acción un número determinado de veces", 
                     "Solo ejecuta una vez el código"],
        "respuesta": 1
    },
    {
        "pregunta": "¿Qué operador se usa para comparar igualdad?",
        "opciones": ["=", "==", "!="],
        "respuesta": 1
    },
    {
        "pregunta": "¿Cuál es la salida de: `for i in range(2): print(i)`?",
        "opciones": ["0 1", "1 2", "0 1 2"],
        "respuesta"
