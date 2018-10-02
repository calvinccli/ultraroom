var MyFancyObservable=require('./MyFancyObservable1');
var observable=new MyFancyObservable();

observable.on('hello',function(name){
console.log(name);
});

observable.hello('john');
