function fillProductList() {
    fetch('/lab7/rest-api/products/')
    .then(response => response.json())
    .then(products => {
        let productGrid = document.querySelector('.product-grid');
        productGrid.innerHTML = '';

        products.forEach(product => {
            let productItem = document.createElement('div');
            productItem.className = 'product-item';

            let productImage = document.createElement('div');
            productImage.className = 'product-image';

            let img = document.createElement('img');
            img.src = product.img_url;
            img.alt = product.name;
            productImage.appendChild(img);

            let productName = document.createElement('h2');
            productName.className = 'product-name';
            productName.innerText = product.name;

            let productPrice = document.createElement('p');
            productPrice.className = 'product-price';
            productPrice.innerText = `${product.price} руб.`;

            let productDescription = document.createElement('p');
            productDescription.className = 'product-description';
            productDescription.innerText = product.description;

            // Убрали создание и добавление кнопки "Добавить в корзину"

            productItem.appendChild(productImage);
            productItem.appendChild(productName);
            productItem.appendChild(productPrice);
            productItem.appendChild(productDescription);

            productGrid.appendChild(productItem);
        });
    })
    .catch(error => console.error('Error fetching products:', error));
}

function fillProductListOK() {
    fetch('/lab7/rest-api/products/')
    .then(response => response.json())
    .then(products => {
        let productGrid = document.querySelector('.product-grid');
        productGrid.innerHTML = '';

        products.forEach(product => {
            let productItem = document.createElement('div');
            productItem.className = 'product-item';

            let productImage = document.createElement('div');
            productImage.className = 'product-image';

            let img = document.createElement('img');
            img.src = product.img_url;
            img.alt = product.name;
            productImage.appendChild(img);

            let productName = document.createElement('h2');
            productName.className = 'product-name';
            productName.innerText = product.name;

            let productPrice = document.createElement('p');
            productPrice.className = 'product-price';
            productPrice.innerText = `${product.price} руб.`;

            let productDescription = document.createElement('p');
            productDescription.className = 'product-description';
            productDescription.innerText = product.description;

            let addToCartButton = document.createElement('button');
            addToCartButton.className = 'add-to-cart';
            addToCartButton.innerText = 'Добавить в корзину';
            addToCartButton.setAttribute('data-product-id', product.id);

            productItem.appendChild(productImage);
            productItem.appendChild(productName);
            productItem.appendChild(productPrice);
            productItem.appendChild(productDescription);
            productItem.appendChild(addToCartButton);

            productGrid.appendChild(productItem);
        });
    })
    .catch(error => console.error('Error fetching products:', error));
}

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('add-to-cart')) {
        const productId = event.target.getAttribute('data-product-id');
        console.log('Adding product to cart:', productId);

        fetch('/rgz/add_to_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ product_id: productId })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from server:', data);
            alert(data.message);
        })
        .catch(error => console.error('Error:', error));
    }
});

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('remove-from-cart')) {
        const productId = event.target.getAttribute('data-product-id');
        console.log('Removing product from cart:', productId);

        fetch('/rgz/remove_from_cart', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ product_id: productId })
        })
        .then(response => response.json())
        .then(data => {
            console.log('Response from server:', data);
            alert(data.message);
            // Обновляем корзину на странице
            location.reload();
        })
        .catch(error => console.error('Error:', error));
    }
});