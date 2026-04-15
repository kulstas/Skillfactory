// Practice 7.1
const person = {
  name: 'John',
  age: 23
}

function printInfo(person){
  console.log(`Name: ${this.name}, Age: ${this.age}`);
}

printInfo.call(person);


// Practice 7.2
const task = [2, 3, "+"];

function calculate(a, b, operator){
  if(operator === '+'){
    return a + b;
  } else if (operator === '-'){
    return a - b;
  } else if (operator === '*'){
    return a * b;
  } else if(operator === '/') {
    return a / b;
  } else {
    return "Используется неверный оператор. Можно только: +, -, * или /";
  }
}
              
console.log(calculate.apply(null, task));


// Practice 7.3
const users = [
  {
    name: 'John',
    age: 14
  },
  {
    name: 'Mary',
    age: 26
  },
  {
    name: 'Max',
    age: 18
  },  
  {
    name: 'Vika',
    age: 12
  }
]

users.filter((user, users) => user.age >= 18);
users.map((user) => user['name']);


// Practice 7.4
let person = {
  name: 'John',
  age: 23,
  fullName: ''
}

function setFullName(personObj, fullPersonName){
  this.fullName = fullPersonName;
}

const setPersonFullName = setFullName.bind(person);

setPersonFullName(null, "John Smith");

console.log(person);


// Practice 7.5
const myArray = [1, 8, 3, 10, 3, 7, 55, 2, 11, 10];

function sortingArray(unsortArray){
  let sortArray = Array.from(new Set(unsortArray)).sort((a,b) => a-b);
  console.log(sortArray);
}

sortingArray(myArray);