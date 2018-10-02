var fs=require("fs");
var data='Simple Easy Learning';

var writerStream=fs.createWriteStream('output.txt');

writerStream.write(data,'UTF8');

writerStream.end();

writerStream.on('finish',function(){
    console.log('Write Completed');
});

console.log('Program Ended');
