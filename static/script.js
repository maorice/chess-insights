document.getElementById("saveButton").addEventListener("click", () => {
  const input = document.getElementById("textInput");
  player_name = input.value;
  console.log(player_name)

  fetch(`/api/get_stats/${player_name}`)
    .then(response => response.json())
    .then(data => {
      console.log(data)
      document.getElementById("output").innerText = JSON.stringify(data, null, 2)
    })
    .catch(error => console.error(error))
});