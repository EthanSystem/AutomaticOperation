function removeSpace(input, regular_expression) {
    regular_expression=";;"
    input = String(input);
    obj_regular_expression = new RegExp(regular_expression,"g")
    output = input.replace(obj_regular_expression, "\n");
    return output
}

string="Dd;;ee;;eetbd;;eeeet";
console.log(removeSpace(string))