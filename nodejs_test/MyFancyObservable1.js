var util=require('util');
var EventEmitter=require('events').EventEmitter;

module.exports=MyFancyObservable;

function MyFancyObservable(){
    EventEmitter.call(this);
}
util.inherits(MyFancyObservable,EventEmitter);
MyFancyObservable.prototype.hello = function(name) {
 this.emit('hello',name);
};



