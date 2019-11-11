// const person = {
//   name: {
//     first: "Bob",
//     last: "Smith",
//   },
//   age: 32,
//   gender: "male",
//   interests: ["music", "skiing"],
//   bio: function() {
//     return this.name[0] + " " + this.name[1] + " is " + this.age + " years old. He likes " + this.interests[0] + " and " + this.interests[1] + ".";
//   },
//   greeting: function() {
//     return "Hi, I'm " + this.name[0] + ".";
//   },
// };

function Person(name) {
  this.name = name;
  this.greeting = function () {
    return "Hi, I'm " + this.name + ".";
  };
}

const slava = new Person("Slava");
console.log(slava.name);
console.log(slava.greeting());

// Directly creating Object from `Object()` constructor
const person1 = new Object({
  name: "Chris",
  age: 38,
  greeting: function () {
    return "Hi, I'm " + this.name + ".";
  }
});
console.log(person1.name);
console.log(person1.greeting());

const person2 = Object.create(person1);
console.log(person2.name);
console.log(person2.greeting());

person2.name = "Alice"
console.log(person2.name);
console.log(person1.name);
