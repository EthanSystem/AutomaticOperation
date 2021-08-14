///全角空格为12288，半角空格为32 
///其他字符半角(33-126)与全角(65281-65374)的对应关系是：均相差65248 
//全角转换为半角函数 
function ToCDB(input) {
    var output = "";
    input=String(input);
    for (var i = 0; i < input.length; i++) {
        // 0xFF10-0xFF19是从0-9，，意思就是将全角数字转换为半角
        // 0xFF21-0xFF3A，意思是将全角的大写字母转换为半角大写字母
        // 0xFF41-0xFF5A，意思是将拳脚的小写字母转换为半角小写字母
        if (input.charCodeAt(i) >= 0xFF10 && input.charCodeAt(i) <= 0xFF19 || input.charCodeAt(i) >= 0xFF21 && input.charCodeAt(i) <= 0xFF3A || input.charCodeAt(i) >= 0xFF41 && input.charCodeAt(i) <= 0xFF5A) {
            output += String.fromCharCode(input.charCodeAt(i) - 0xFEE0);
        }
        else {
            output += String.fromCharCode(input.charCodeAt(i));
        }
    }
    return output
}


result=ToCDB("0123456789０１３４５６７８９ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ,.;:\'\"?!()[]{} ，。；：‘’”“？！（）【】「」《》　");
console.log(result)