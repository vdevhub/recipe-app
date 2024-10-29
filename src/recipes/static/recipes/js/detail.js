// JavaScript for delete confirmation and AJAX request
function confirmDelete(event) {
  event.preventDefault(); // Prevents the default link behavior
  const recipeId = event.currentTarget.getAttribute("data-recipe-id");

  if (confirm("Are you sure you want to delete this recipe?")) {
    fetch(`/delete/${recipeId}/`, {
      method: "POST",
      headers: {
        "X-CSRFToken": getCookie("csrftoken") // CSRF token for security
      }
    })
      .then(response => response.json())
      .then(data => {
        if (data.status === "success") {
          alert("Recipe deleted successfully.");
          window.location.href = "/recipes/overview/"; // Redirect after delete
        } else {
          alert("An error occurred while deleting the recipe.");
        }
      })
      .catch(error => console.error("Error:", error));
  }
}

// Function to get CSRF token from cookies
function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    const cookies = document.cookie.split(';');
    for (let i = 0; i < cookies.length; i++) {
      const cookie = cookies[i].trim();
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

// Function to open the Edit Modal and load the form
function openEditModal() {
  document.getElementById("editRecipeModal").style.display = "block";
  loadEditForm();
}

// Function to close the Edit Modal
function closeEditModal() {
  document.getElementById("editRecipeModal").style.display = "none";
}

// Function to load the form HTML via AJAX
function loadEditForm() {
  const editRecipeForm = document.getElementById('editRecipeForm');
  const postUrl = editRecipeForm.getAttribute('data-post-url');
  fetch(postUrl)
    .then(response => response.json())
    .then(data => {
      document.getElementById("editRecipeForm").innerHTML = data.html_form;

      // Dynamically add submit button if it's missing
      const submitButton = document.createElement("button");
      submitButton.type = "submit";
      submitButton.className = "submit-button";
      submitButton.textContent = "Save Changes";
      document.getElementById("editRecipeForm").appendChild(submitButton);
    });
}

// Handle form submission via AJAX
document.getElementById("editRecipeForm").onsubmit = function (event) {
  event.preventDefault();
  const formData = new FormData(this);
  const editRecipeForm = document.getElementById('editRecipeForm');
  const postUrl = editRecipeForm.getAttribute('data-post-url');
  fetch(postUrl, {
    method: "POST",
    body: formData,
    headers: {
      "X-CSRFToken": getCookie("csrftoken"),
    },
  }).then(response => {
    if (response.ok) {
      closeEditModal();
      location.reload(); // Refresh to show updated recipe
    } else {
      response.json().then(data => {
        alert("Error: " + JSON.stringify(data.errors));
      });
    }
  });
};