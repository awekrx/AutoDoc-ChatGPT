
/**
 * This class represents a user with a name property.
 * @class
 * 
 */
class User {
    /**
     * Creates a new User instance with the given name.
     * @constructor
     * @param {string} name - The name of the user.
     * 
     */
    constructor(name) {
        this.name = name;
    }
    /**
     * 
     * Returns the name of the user.
     * @returns {string} - The name of the user.
     */
    getName() {
        return this.name;
    }
}
const user = new User('John');
user.getName();
user instanceof User; 