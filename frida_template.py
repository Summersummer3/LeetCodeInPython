import frida
import base64
import time
import sys

def on_message(message, data):
	print(message)
	print(data)
	
	if message['type'] == 'send':
		msg_lst = message['payload'].split('+')
		a, b = int(msg_lst[0].strip()), int(msg_lst[1].strip())
		res = a + b + control
		script.post({'res' : res})


js_code = """
Java.perform(function () {
	var mainActivity = Java.use("com.example.myapplication.MainActivity");
	mainActivity.add.implementation = function (x, y) {
		var string_a = x.toString();
		var string_b = y.toString();
		console.log('rx data: ' + string_a + '+' + string_b);
		var s_m = string_a + "+" + string_b;
		var res;
		send(s_m);
		recv(function (rx_json) {
			res = rx_json.res;
			console.log("hooked data : " + res.toString());
		}).wait();
		return res;
	};
});
"""

control = 0
device = frida.get_usb_device()
pid = device.spawn(["com.example.myapplication"])
device.resume(pid)
time.sleep(1)
session = device.attach(pid)
script = session.create_script(js_code)
script.on("message", on_message)
script.load()
print("Load script ends")
while True:
	control = int(sys.stdin.readline())
