const prices = {};
const customers = {};

function findCustomerSelect() {
    return document.getElementById("id_customer");
}

function findCustomerPhoneElement() {
    return document.getElementById("customer-phone");
}

function findCustomerAddressElement() {
    return document.getElementById("customer-address");
}

function findOrderItemElement(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-row`);
}

function findProductSelect(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-product`);
}

function findQuantityInput(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-quantity`);
}

function findPriceElement(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-price`);
}

function findItemTotalElement(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-total`);
}

function findItemDeleteHiddenInput(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-DELETE`);
}

function findItemDeleteButton(orderItemNumber) {
    return document.getElementById(`id_items-${orderItemNumber}-delete-button`);
}

function findOrderItemsTotalFormsHiddenInput() {
    return document.getElementById("id_items-TOTAL_FORMS");
}

function findSubTotalElement() {
    return document.getElementById("subtotal");
}

function findTaxRateInput() {
    return document.getElementById("id_tax_rate");
}

function findTaxElement() {
    return document.getElementById("tax");
}

function findShippingInput() {
    return document.getElementById("id_shipping");
}

function findDiscountInput() {
    return document.getElementById("id_discount");
}

function findTotalElement() {
    return document.getElementById("total");
}

async function findProductPrice(productId) {
    let productPrice = null;
    if (productId) {
        productPrice = prices[productId];
        if (!productPrice) {
            console.log(`Fetching product price for ${productId}`);
            const response = await fetch(`${window.location.origin}/store/api/products/${productId}`);
            const json = await response.json();
            productPrice = parseFloat(json.price);
            prices[productId] = productPrice;
        }
    }
    return productPrice;
}

async function findCustomerInfo(customerId) {
    let customerInfo = null;
    if (customerId) {
        customerInfo = customers[customerId];
        if (!customerInfo) {
            console.log(`Fetching customer info for ${customerId}`);
            const response = await fetch(`${window.location.origin}/store/api/customers/${customerId}`);
            customerInfo = await response.json();
            customers[customerId] = customerInfo;
        }
    }
    return customerInfo;
}

function updateCustomerInfo() {
    findCustomerInfo(findCustomerSelect().value).then((customerInfo) => {
        const customerPhone = customerInfo ? customerInfo.phone : null;
        const customerPhoneElement = findCustomerPhoneElement();
        
        if (customerPhone) {
            customerPhoneElement.textContent = customerPhone;
            customerPhoneElement.style.display = null;
        } else {
            customerPhoneElement.textContent = "";
            customerPhoneElement.style.display = "none";
        }
        
        const customerAddress = customerInfo ? customerInfo.address : null;
        const customerAddressElement = findCustomerAddressElement();
        
        if (customerAddress) {
            customerAddressElement.textContent = customerAddress;
            customerAddressElement.style.display = null;
        } else {
            customerAddressElement.textContent = "";
            customerAddressElement.style.display = "none";
        }
    });
}

function readIntInput(input) {
    const quantity = parseInt(input.value);
    return isNaN(quantity) ? 0 : quantity;
}

function readFloatInput(input) {
    let result = parseFloat(input.value);
    return isNaN(result) ? 0 : result;
}

async function calculateItemTotal(orderItemNumber) {
    const elProductSelect = findProductSelect(orderItemNumber);
    const productId = elProductSelect.value;
    const price = await findProductPrice(productId);
    return isNaN(price) ? 0 : readIntInput(findQuantityInput(orderItemNumber)) * price;
}

async function calculateSubTotal() {
    var subtotal = 0;
    
    for (const element of document.querySelectorAll('[id^=id_items-][id$=-product]')) {
        const orderItemNumber = element.id.match("[0-9]+")[0];
        const lineItemTotal = await calculateItemTotal(orderItemNumber);
        subtotal += lineItemTotal;
    };
    
    return subtotal;
}

function formatCurrency(amount) {
    const negative = (amount < 0);
    let result = "$" + Math.abs(amount).toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');
    result = negative ? `-${result}` : result;
    return result;
}

function updateOrderItem(orderItemNumber) {
    const elProductSelect = findProductSelect(orderItemNumber);
    const productId = elProductSelect.value;
    
    findProductPrice(productId).then((price) => {
        let priceString = "";
        let totalString = "";
        
        if (!isNaN(price)) {
            const total = readIntInput(findQuantityInput(orderItemNumber)) * price;
            priceString = formatCurrency(price);
            totalString = formatCurrency(total);
        }
            
        findPriceElement(orderItemNumber).innerHTML = priceString;
        findItemTotalElement(orderItemNumber).innerHTML = totalString;
        
        const itemDeleteButton = findItemDeleteButton(orderItemNumber);
        
        if (findProductSelect(orderItemNumber).value == "") {
            itemDeleteButton.style.visibility = "hidden";
        } else {
            itemDeleteButton.style.visibility = null;
        }
        
        updateTally();
    });
}

function updateTally() {
    calculateSubTotal().then((subtotal) => {
        const taxRate = readFloatInput(findTaxRateInput());
        const tax = subtotal * taxRate / 100;
        const shipping = readFloatInput(findShippingInput());
        const discount = readFloatInput(findDiscountInput());
        const total = (subtotal + tax + shipping - discount);

        findSubTotalElement().innerHTML = formatCurrency(subtotal);
        findTaxElement().innerHTML = (tax == 0 ? "" : formatCurrency(tax));
        findTotalElement().innerHTML = formatCurrency(total);
    });
}

function handleProductChange(orderItemNumber) {
    const itemProductSelect = findProductSelect(orderItemNumber);
    const itemQuantityInput = findQuantityInput(orderItemNumber);
    const itemDeleteHiddenInput = findItemDeleteHiddenInput(orderItemNumber);
    
    if (itemProductSelect.value == "") {
        deleteBlankOrderItems();
    } else {
        if (itemQuantityInput.value == "") {
            itemQuantityInput.value = 1;
        }
        if (isLastNonBlankItem(orderItemNumber)) {
            createBlankOrderItem();
        }
    }
    
    updateOrderItem(orderItemNumber);
}

function isLastNonBlankItem(itemNumber) {
    for (let i = itemNumber + 1; findOrderItemElement(i) != null; i++) {
        if (findProductSelect(i).value == "") {
            return false;
        }
    }
    return true;
}

function deleteOrderItem(orderItemNumber) {
    findProductSelect(orderItemNumber).value = "";
    updateOrderItem(orderItemNumber);
    deleteBlankOrderItems();
}

function deleteBlankOrderItems() {
    let itemNumber = 0;
    let itemProductSelect = findProductSelect(itemNumber);
    let lastItemBlank = false;
    
    while (itemProductSelect != null) {
        if (lastItemBlank) {
            const itemNumberLast = itemNumber - 1;
            findOrderItemElement(itemNumberLast).style.display = "none";
            findItemDeleteHiddenInput(itemNumberLast).value = "on";
        }
        lastItemBlank = (itemProductSelect.value == "");
        itemProductSelect = findProductSelect(++itemNumber);
    }
}

function createBlankOrderItem() {

    // Find last item number and the corresponding HTML element
    
    let lastItemNumber = -1;
    let lastItemElement = null;
    let nextItemNumber = 0;
    let nextItemElement = findOrderItemElement(nextItemNumber);
    
    do {
        lastItemNumber = nextItemNumber;
        lastItemElement = nextItemElement;
        nextItemNumber = nextItemNumber + 1;
        nextItemElement = findOrderItemElement(nextItemNumber);
    }
    while (nextItemElement != null);

    // Clone lastItemElement
    
    const newItemNumber = lastItemNumber + 1;
    const newItemElement = lastItemElement.cloneNode(true);
    
    // Update id and name attributes to reference newItemNumber instead of lastItemNumber
    
    replaceInAttributeValues(newItemElement, `-${lastItemNumber}-`, `-${newItemNumber}-`);
    
    // Attach newItemElement to the items table, but keep it invisible for now
    
    lastItemElement.closest("tbody").appendChild(newItemElement);
    newItemElement.style.display = "none"

    // Clear old data from newItemElement
    
    findProductSelect(newItemNumber).value = null;
    findQuantityInput(newItemNumber).value = null;
    findItemDeleteHiddenInput(newItemNumber).value = null;
    
    // Register listeners
    
    registerOrderItemListeners(newItemNumber);

    // Make newItemElement visible
                
    newItemElement.style.display = null;
    
    // Update items-TOTAL_FORMS so that Django knows how many forms to process on submit
    
    findOrderItemsTotalFormsHiddenInput().value = newItemNumber + 1;
}

function replaceInAttributeValues(element, searchValue, replacementValue) {
    if (element.attributes) {
        for (let i = 0; i < element.attributes.length; i++) {
            const attr = element.attributes[i];
            attr.value = attr.value.replace(searchValue, replacementValue);
        }
    }
    if (element.childNodes) {
        for (let i = 0; i < element.childNodes.length; i++) {
            const child = element.childNodes[i];
            replaceInAttributeValues(child, searchValue, replacementValue);
        }
    }
}

function registerOrderItemListeners(orderItemNumber) {
    findProductSelect(orderItemNumber).addEventListener("change", () => {
        handleProductChange(orderItemNumber);
    });

    findQuantityInput(orderItemNumber).addEventListener("input", () => {
        updateOrderItem(orderItemNumber);
    });
    
    findItemDeleteButton(orderItemNumber).addEventListener("click", () => {
        deleteOrderItem(orderItemNumber);
    });
}

function setup() {
    findTaxRateInput().addEventListener("input", updateTally);
    findShippingInput().addEventListener("input", updateTally);
    findDiscountInput().addEventListener("input", updateTally);
    
    findCustomerSelect().addEventListener("change", () => {
        updateCustomerInfo();
    });

    for (let i = 0; findOrderItemElement(i) != null; i++) {
        registerOrderItemListeners(i);
        updateOrderItem(i);
    }

    updateCustomerInfo();
    updateTally();
}
