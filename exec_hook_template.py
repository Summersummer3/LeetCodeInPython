import frida
import sys

def on_msg(msg, data):
    print('recv...')
    print(msg)
    if msg['type'] == 'send':
        lst = msg['payload'].strip().split('+')
        script.post({'res' : int(lst[0], 16) + int(lst[1], 16) + ctrl})

func = 'add'

js_code = """
var module = Module.load("/data/local/hello");
var syms = module.enumerateSymbols();
var tgt_func;
var res;

for (var idx in syms) {
    if (syms[idx].name == '%s') {
        tgt_func = new NativePointer(syms[idx].address.toString());
        break;
    }    
}

Interceptor.attach(tgt_func, {
    onEnter: function(args) {
        //console.log(args);
        var msg = args[0].toString() + '+' + args[1].toString();
        console.log('rx data: ' + msg);
        send(msg);
        recv(function (rx_msg) {
            res = rx_msg.res;
        }).wait();
        console.log('res : ', res.toString());
        return res;
    },
    onLeave: function(retval) {
        retval.replace(res);
    } 
});
""" % func

ctrl = 0
device = frida.get_usb_device()
pid = device.spawn(['/data/local/hello'])
device.resume(pid)
session = device.attach(pid)
script = session.create_script(js_code)
script.on("message", on_msg)
script.load()
print('script load success...')
while True:
    ctrl = int(sys.stdin.readline())
