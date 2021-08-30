///全角空格为12288，半角空格为32 
///其他字符半角(33-126)与全角(65281-65374)的对应关系是：均相差65248 
//半角转换为全角函数 
function ToDBC(input) {
    var output = "";
    for (var i = 0; i < input.length; i++) {
        // 0x20是半角空格符，不进行转换
        if (input.charCodeAt(i) == 0x20) {
            output = output + String.fromCharCode(0x20);
        }
        // 0x30-0x39是从0-9，意思就是数字不转换为全角
        if ((input.charCodeAt(i) <= 0x7E && input.charCodeAt(i) > 0x39) || input.charCodeAt(i) < 0x30) {
            output = output + String.fromCharCode(input.charCodeAt(i) + 0xFEE0);
        }
        else {
            output += input[i];
        }
    }
    return output;
}


result=ToDBC("0123456789０１３４５６７８９,.;:\'\"?!()[]{} ，。；：‘’”“？！（）【】「」《》　");
console.log(result)