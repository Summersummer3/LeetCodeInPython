function enumMethods(targetClass)
{
    var hook = Java.use(targetClass);
    var ownMethods = hook.class.getDeclaredMethods();
    hook.$dispose();

    return ownMethods;
}

setTimeout(function (){
	Java.perform(function (){
		var a = enumMethods("com.huawei.nearby.ble.advstack.c")
        	a.forEach(function(s) {
            	console.log(s);
        	});
	});
});
