// // Practice 6.10.1
// let userNum = prompt('Введите число');
// alert(`
//     Введённое число - ${userNum}\n
//     Квадрат числа - ${userNum ** 2}\n
//     Куб числа - ${userNum ** 2}\n
// `);

// // Practice 6.10.2
// let userCode = prompt("Введите промокод");
// const promoCode = "скидка";

// if(userCode.toLowerCase() == promoCode) {
//     alert("Промокод применён!");
// } else {
//     alert("Промокод не работает");
// }

// // Practice 6.10.3
// let userName = prompt("Введите имя");
// let userAge = +prompt("Введите год рождения");

// if (userName && userAge && typeof userName == "string" && typeof userAge == "number") {
//     const currentYear = new Date();
//     alert(`${userName}: ${currentYear.getFullYear() - userAge}`);
// } else {
//     alert("Введите корректные данные!");
// }

// // Practice 6.10.4 
// let userName = prompt("Введите имя");
// let userAge = +prompt("Введите год рождения");

// if (userName && userAge && typeof userName == "string" && typeof userAge == "number") {
//     const currentYear = new Date();
//     const remainsAge = (currentYear.getFullYear() - userAge) % 10;

//     if(remainsAge == 1 ){
//         alert(`${userName}: ${currentYear.getFullYear() - userAge} год`);
//     } else if (remainsAge > 1 && remainsAge < 5) {
//         alert(`${userName}: ${currentYear.getFullYear() - userAge} года`);
//     } else {
//         alert(`${userName}: ${currentYear.getFullYear() - userAge} лет`);
//     }
// } else {
//         alert("Введите корректные данные!");
//     }

