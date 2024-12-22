let savedInput = "";

function saveInput() {
  const inputElement = document.getElementById("textInput");
  savedInput = inputElement.value;
  console.log(savedInput + ' saved successfully');
}

document.getElementById("saveButton").addEventListener("click", saveInput);