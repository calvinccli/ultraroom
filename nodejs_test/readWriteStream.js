var fs=require("fs");
var data='';
var readerStream=fs.createReadStream('input.txt');
var writerStream=fs.createWriteStream('output.txt');


readerStream.setEncoding('UTF8');
readerStream.pipe(writerStream);

readerStream.on('data',function(chunk){
data += chunk;
});

readerStream.on('end',function(){
   console.log(data);
});

readerStream.on('error',function(err){
console.log(err.stack);
});

writerStream.on('finish',function(){
console.log('write completed');
});

writerStream.on('error',function(err){
console.log(wrr.stack);
});

console.log("Program Ended");
