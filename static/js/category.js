function changeCategory(category) {
    // Get the current city from the page
    const city = document.querySelector('#cityDropdown').textContent.trim();
    
    // Make a fetch request to update the session
    fetch(`/update_category?category=${category}&city=${city}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        }
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Reload the page to show the new category
            window.location.reload();
        } else {
            console.error('Failed to update category');
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
} 