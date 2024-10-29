function clearSearch() {
  // Clears the search term input and submits the form to show all results
  const searchInput = document.querySelector('input[name="search_term"]');
  if (searchInput) searchInput.value = ''; // Clear the input
  document.querySelector('form').submit(); // Submit form with empty input
}

document.getElementById("show-analytics-btn").addEventListener("click", function () {
  const analyticsSection = document.getElementById("analytics-section");
  const button = document.getElementById("show-analytics-btn"); // Get the button element

  // Toggle the visibility of the analytics section
  if (analyticsSection.style.display === "none" || analyticsSection.style.display === "") {
    analyticsSection.style.display = "block"; // Show analytics
    button.textContent = "Hide Analytics"; // Change button text
  } else {
    analyticsSection.style.display = "none"; // Hide analytics
    button.textContent = "Show Analytics"; // Revert button text
  }
});

// Function to open the modal
document.getElementById("add-recipe-btn").onclick = function () {
  document.getElementById("addRecipeModal").style.display = "block";
  loadRecipeForm();
};

// Function to close the modal
function closeModal() {
  document.getElementById("addRecipeModal").style.display = "none";
}

// Function to load the form HTML via AJAX
function loadRecipeForm() {
  fetch("/add-form/")
    .then(response => response.text())
    .then(html => {
      document.getElementById("addRecipeForm").innerHTML = html;
    });
}

// Function to submit the form via AJAX
document.getElementById("addRecipeForm").onsubmit = function (event) {
  event.preventDefault();
  const formData = new FormData(this);
  // Retrieves the URL for posting the form data from a data attribute on the form.
  const addRecipeForm = document.getElementById('addRecipeForm');
  const postUrl = addRecipeForm.getAttribute('data-post-url');
  fetch(postUrl, {
    method: "POST",
    body: formData,
    headers: {
      'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
    }
  }).then(response => {
    if (response.ok) {
      closeModal();
      location.reload();  // Refresh the page to show new recipe
    } else {
      alert("There was an error adding the recipe.");
    }
  });
};

// Close the modal when clicking outside of modal content
window.onclick = function (event) {
  const modal = document.getElementById("addRecipeModal");
  if (event.target === modal) {
    closeModal();
  }
}