var localtunnel = require('localtunnel'); //you need to install localtunnel on your machine and require it
var subdomain = "galileotoworld"; //subdomain for main domain of localtunnel.me
var tunnel = localtunnel(1337, {subdomain: subdomain},function(err, tunnel) {

    // the assigned public url for your tunnel
    // i.e. https://galileotoworld.localtunnel.me
    console.log(tunnel.url); // write your public url on terminal window
});

tunnel.on('close', function() {
    // tunnels are closed
});
