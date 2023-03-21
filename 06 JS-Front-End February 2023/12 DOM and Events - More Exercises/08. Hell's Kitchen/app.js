function solve() {
   document.querySelector('#btnSend').addEventListener('click', onClick);

   function onClick () {
      let restaurantsList = []
      let restaurantsInput = JSON.parse(document.getElementsByTagName("textarea")[0].value);
      for (const entry of restaurantsInput) {
         let [restaurantName, workers] = entry.split(" - ");
         let restaurant;
         let exists = false;
         for (const rest of restaurantsList) {
            if (rest.name === restaurantName) {
               restaurant = rest;
               exists = true;
               break;
            }           
         }
         if (!exists) {
            restaurant = {name: restaurantName, workers: [], averageSalary: 0, bestSalary: 0};
            restaurantsList.push(restaurant);
         }
         let workersList = workers.split(", ");
         for (const entry of workersList) {
            let [name, salary] = entry.split(" ");
            if (Number(salary) > restaurant.bestSalary) {
               restaurant.bestSalary = Number(salary);
            }
            let worker = {name, salary: Number(salary)};
            restaurant.workers.push(worker);
         }
         let sumSalaries = 0;
         for (const worker of restaurant.workers) {
            sumSalaries += worker.salary
         }
         restaurant.averageSalary = sumSalaries / restaurant.workers.length;   
      }
      let bestRestaurant;
      let bestAvgSalary = 0;
      for (const restaurant of restaurantsList) {
         if (restaurant.averageSalary > bestAvgSalary) {
            bestRestaurant = restaurant;
            bestAvgSalary = restaurant.averageSalary;
         }
      }
      let bestRestaurantResult = document.querySelector("#bestRestaurant p")
      let bestRestaurantWorkersResult = document.querySelector("#workers p")

      bestRestaurantResult.textContent = `Name: ${bestRestaurant.name} Average Salary: ${bestRestaurant.averageSalary.toFixed(2)} Best Salary: ${bestRestaurant.bestSalary.toFixed(2)}`
      
      for (const worker of bestRestaurant.workers.sort((a, b) => b.salary - a.salary)) {
         bestRestaurantWorkersResult.textContent += `Name: ${worker.name} With Salary: ${worker.salary} `
      }
   }
}