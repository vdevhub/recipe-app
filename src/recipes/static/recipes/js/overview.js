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