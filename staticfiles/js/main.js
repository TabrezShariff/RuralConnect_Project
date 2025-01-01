// static/js/main.js
document.addEventListener('DOMContentLoaded', function() {
    // Fetch data from backend API
    function fetchData(url) {
        return fetch(url)
            .then(response => response.json())
            .catch(error => {
                console.error('Error fetching data:', error);
                return [];
            });
    }

    // Populate product grid
    function populateProductGrid() {
        fetchData('/api/products/').then(products => {
            const productGrid = document.querySelector('.product-grid');
            if (!productGrid) return;

            productGrid.innerHTML = '';
            products.forEach(product => {
                const productCard = document.createElement('div');
                productCard.classList.add('product-card');
                productCard.innerHTML = `
                    <h3>${product.name}</h3>
                    <p>Price: $${product.price.toFixed(2)}</p>
                    <p>Category: ${product.category}</p>
                    <button class="btn btn-primary add-to-cart" data-id="${product.id}">Add to Cart</button>
                `;
                productGrid.appendChild(productCard);
            });

            // Add event listeners for "Add to Cart" buttons
            document.querySelectorAll('.add-to-cart').forEach(button => {
                button.addEventListener('click', function() {
                    const productId = this.getAttribute('data-id');
                    addToCart(productId);
                });
            });
        });
    }

    // Populate price updates table
    function populatePriceUpdates() {
        fetchData('/api/price-updates/').then(priceUpdates => {
            const priceUpdatesTable = document.querySelector('#price-updates tbody');
            if (!priceUpdatesTable) return;

            priceUpdatesTable.innerHTML = '';
            priceUpdates.forEach(update => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${update.product}</td>
                    <td>$${update.price.toFixed(2)}</td>
                    <td class="${update.change >= 0 ? 'positive' : 'negative'}">
                        ${update.change > 0 ? '+' : ''}${update.change.toFixed(2)}
                    </td>
                `;
                priceUpdatesTable.appendChild(row);
            });
        });
    }

    // Populate resource grid
    function populateResourceGrid() {
        fetchData('/api/resources/').then(resources => {
            const resourceGrid = document.querySelector('.resource-grid');
            if (!resourceGrid) return;

            resourceGrid.innerHTML = '';
            resources.forEach(resource => {
                const resourceCard = document.createElement('div');
                resourceCard.classList.add('resource-card');
                resourceCard.innerHTML = `
                    <h3>${resource.title}</h3>
                    <p>${resource.content}</p>
                    <a href="/resources/${resource.id}" class="btn btn-outline">Read More</a>
                `;
                resourceGrid.appendChild(resourceCard);
            });
        });
    }

    // Handle delivery form submission
    function setupDeliveryForm() {
        const deliveryForm = document.querySelector('#delivery-form');
        if (!deliveryForm) return;

        deliveryForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(deliveryForm);
            
            fetch('/api/delivery-requests/', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                alert('Delivery request submitted successfully!');
                deliveryForm.reset();
            })
            .catch(error => {
                console.error('Error submitting delivery request:', error);
                alert('There was an error submitting your request. Please try again.');
            });
        });
    }

    // Add to cart functionality
    function addToCart(productId) {
        fetch(`/api/cart/add/${productId}/`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken')
            }
        })
        .then(response => response.json())
        .then(data => {
            alert('Product added to cart!');
            updateCartCount();
        })
        .catch(error => {
            console.error('Error adding product to cart:', error);
            alert('There was an error adding the product to your cart. Please try again.');
        });
    }

    // Update cart count in the navbar
    function updateCartCount() {
        fetch('/api/cart/count/')
        .then(response => response.json())
        .then(data => {
            const cartCount = document.querySelector('#cart-count');
            if (cartCount) {
                cartCount.textContent = data.count;
            }
        })
        .catch(error => console.error('Error updating cart count:', error));
    }

    // Get CSRF token from cookies
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

    // Initialize all components
    populateProductGrid();
    populatePriceUpdates();
    populateResourceGrid();
    setupDeliveryForm();
    updateCartCount();

    // Auto-hide messages after 5 seconds
    const messages = document.querySelectorAll('.message');
    messages.forEach(message => {
        setTimeout(() => {
            message.style.opacity = '0';
            setTimeout(() => message.remove(), 300);
        }, 5000);
    });
});