var observable=require('./MyFancyObservable').MyFancyObservable();

observable.on('hello',function(name){
console.log(name);
});

observable.hello('john');
