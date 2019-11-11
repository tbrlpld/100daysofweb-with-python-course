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