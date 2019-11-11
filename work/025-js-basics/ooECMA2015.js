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

class Teacher extends Person {
  constructor(name, age, subject) {
    super(name, age);
    this.subject = subject;
  }
}

const teacher1 = new Teacher("Ms. Alice", 32, "Biology");
console.log(teacher1.name);
console.log(teacher1.subject);
console.log(teacher1.farewell());