// Practice 6.10.1
let userNum = prompt('Введите число');
alert(`
    Введённое число - ${userNum}\n
    Квадрат числа - ${userNum ** 2}\n
    Куб числа - ${userNum ** 2}\n
`);

// Practice 6.10.2
let userCode = prompt("Введите промокод");
const promoCode = "скидка";

if(userCode.toLowerCase() == promoCode) {
    alert("Промокод применён!");
} else {
    alert("Промокод не работает");
}

// Practice 6.10.3
let userName = prompt("Введите имя");
let userAge = +prompt("Введите год рождения");

if (userName && userAge && typeof userName == "string" && typeof userAge == "number") {
    const currentYear = new Date();
    alert(`${userName}: ${currentYear.getFullYear() - userAge}`);
} else {
    alert("Введите корректные данные!");
}

// Practice 6.10.4 
let userName = prompt("Введите имя");
let userAge = +prompt("Введите год рождения");

if (userName && userAge && typeof userName == "string" && typeof userAge == "number") {
    const currentYear = new Date();
    const remainsAge = (currentYear.getFullYear() - userAge) % 10;

    if(remainsAge == 1 ){
        alert(`${userName}: ${currentYear.getFullYear() - userAge} год`);
    } else if (remainsAge > 1 && remainsAge < 5) {
        alert(`${userName}: ${currentYear.getFullYear() - userAge} года`);
    } else {
        alert(`${userName}: ${currentYear.getFullYear() - userAge} лет`);
    }
} else {
        alert("Введите корректные данные!");
    }


// Practice 6.1
let userWord = "Довод";
let clearWord = userWord.replace(/\s+/g, "").toLowerCase();
let paliWord = "";

for (let i = clearWord.length - 1; i >= 0; i -= 1) {
  paliWord += clearWord.at(i);
}

if (clearWord === paliWord) {
  console.log(`Слово «${userWord}» является палиндромом`);
} else {
  console.log(`Слово «${userWord}» НЕ является палиндромом`);
}

// Practice 6.2
const arr = [1, 2, 3, 1, 5, 4, 2, 3, 5, 'they', 'don\'t', 'know', 'that', 'we', 'know', 'that', 'they', 'know' ];

const uniqSet = new Set(arr);
const uniqArr = Array.from(uniqSet);

console.log(uniqArr);


// Practice 6.3
let userNum = prompt("Введите число");
+userNum;
let outArr = [];

if (!isNaN(userNum)) {
  for (let i = 0; i <= userNum; i += 1) {
    outArr.push(i);
  }
} else {
  alert("Введено некорректное значение. Введите число.");
}

console.log(outArr);


// Practice 6.4
for (let i = 1; i <= 3; i += 1) {
  if (i % 2 == 0) {
    console.log("o x o");
  } else {
    console.log("x o x");
  }
}


// Practice 6.5
const obj = {
  some: "some",
  dom: "text",
  arr: [1, 2, 3, 4, 5],
  tom: "there",
};

let arrValues = [];

for (let key in obj) {
  if (Array.isArray(obj[key])) {
    for (let value of obj[key]) {
      arrValues.push(value);
    }
  } else {
    arrValues.push(obj[key]);
  }
}

console.log(arrValues);