function convertir() {
  const celsius = document.getElementById("celsius").value;

  fetch("http://localhost:8000", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ celsius })
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("resultado").textContent =
        `Resultado: ${data.fahrenheit} °F`;
    })
    .catch(err => {
      document.getElementById("resultado").textContent =
        "Error al convertir. ¿Está el servidor Python en 8000?";
      console.error(err);
    });
}