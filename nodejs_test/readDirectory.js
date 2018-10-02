var fs = require("fs");

console.log("Going to read directory /Users/calvinli");
fs.readdir("/Users/calvinli",function(err, files){
   if (err) {
      return console.error(err);
   }
   files.forEach( function (file){
      console.log( file );
   });
   console.log('read directory ended');
});
