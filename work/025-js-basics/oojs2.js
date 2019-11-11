// Define the properties in the constructor
function Person(name, age) {
  this.name = name;
  this.age = age;
}

// Define methods in the constructors prototype
Person.prototype.greeting = function() {
  return "Hi, I'm " + this.name;
};

const person1 = new Person("Alice", 32);
console.log(person1.greeting())