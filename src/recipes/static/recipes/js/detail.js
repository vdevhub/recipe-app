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