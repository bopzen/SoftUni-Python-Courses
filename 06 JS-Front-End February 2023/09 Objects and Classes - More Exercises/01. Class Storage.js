function solve() {
    class Storage {
        constructor(capacity) {
            this.capacity = capacity
            this.storage = []
        }
        product = {};
        get totalCost() {
            let cost = 0;
            for (const product of this.storage) {
                cost += product.price * product.quantity;
            }
            return cost;
        };

        addProduct(product) {
            this.storage.push(product);
            this.capacity -= product.quantity
        }
        getProducts() {
            let result = [];
            for (const product of this.storage) {
                result.push(JSON.stringify(product));
            }
            return result.join("\n");
        }
    }

    let productOne = {name: 'Cucamber', price: 1.50, quantity: 15};
    let productTwo = {name: 'Tomato', price: 0.90, quantity: 25};
    let productThree = {name: 'Bread', price: 1.10, quantity: 8};
    let storage = new Storage(50);
    storage.addProduct(productOne);
    storage.addProduct(productTwo);
    storage.addProduct(productThree);
    console.log(storage.getProducts());
    console.log(storage.capacity);
    console.log(storage.totalCost);

}

solve();