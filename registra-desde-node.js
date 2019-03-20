#!/usr/bin/env node

var url = 'amqp://platzi:' + process.env.RMQ_PASS + "@localhost:5672/platzi";
var celery = require('node-celery'),
	client = celery.createClient({
		CELERY_BROKER_URL: url,
	});

client.on('error', function(err) {
	console.log(err);
});

client.on('connect', function() {
    var comandos=['uno', 'uno', 'tres', 'uno', 'tres', 'uno', 'dos' ];
    comandos.forEach( function (valor ) {
	client.call('RegistraComandos.registra', [valor], function(result) {
	    console.log(result);
	    client.end();
	});
    });

});
