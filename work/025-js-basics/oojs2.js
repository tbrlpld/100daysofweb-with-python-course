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


// Defining a derived constructor
function Teacher(name, age, subject) {
  Person.call(this, name, age)

  this.subject = subject
}

const teacher1 = new Teacher("Ms. Alice", 32, "Biology");
console.log(teacher1.name)
console.log(teacher1.subject)
