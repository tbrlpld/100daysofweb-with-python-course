class Person {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  };

  greeting() {
    return `Hi, I'am ${this.name}`
  };

  farewell() {
    return `${this.name} has left`
  };
}

const person1 = new Person("Alice", 32);
console.log(person1.name);
console.log(person1.greeting());