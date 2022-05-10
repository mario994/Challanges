/*

Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:
createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"

The returned format must be correct in order to complete this challenge.
Don't forget the space after the closing parentheses!

*/

function createPhoneNumber(numbers) {
    let newPhoneNumber = numbers;
    newPhoneNumber.splice(0, 0, '(');
    newPhoneNumber.splice(4, 0, ')');
    newPhoneNumber.splice(5, 0, ' ');
    newPhoneNumber.splice(9, 0, '-');
    return newPhoneNumber.join('').toString();
}

/*

console.log(createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]));

--Expected output--

(123) 456-7890

*/
