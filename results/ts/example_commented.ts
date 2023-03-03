
/**
 * This class represents a Pizza and has a constructor that initializes its name and toppings.
 * @class
 * 
 */
class Pizza {
    constructor(
        /**
         * A public property that holds the name of the pizza.
         * @type {string}
         * 
         */
        public name: string,
        /**
         * 
         * A public property that holds an array of strings representing the pizza toppings.
         * @type {string[]}
         */
        public toppings: string[]
    ) { };
}
/**
 * This class provides a static method to create a Pizza object.
 * @class
 * 
 */
class PizzaMaker {
    /**
     * Creates a new Pizza object with the given name and toppings.
     * @static
     * @param {Pizza} event - The Pizza object to create.
     * @returns {Pizza} - The newly created Pizza object.
     * 
     */
    static create(event: Pizza) {
        return new Pizza(
            event.name,
            event.toppings
        );
    }
}
/**
 * 
 * Creates a new Pizza object using the PizzaMaker class.
 * @const
 * @type {Pizza}
 */
const pizza = PizzaMaker.create({
    name: 'Inferno',
    toppings: ['cheese', 'peppers']
});