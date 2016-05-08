var io = require('socket.io')();
io.on('connection', function(socket)
{
	console.log('client connected')
	socket.on('event', function(data)
	{
		bin = parseInt(data).toString(2)
		bin = "0".repeat(22-bin.length) + bin
		console.log(bin)
	});
	socket.on('disconnect', function() {
		console.log('disconnected')
	});
});
io.listen(3000);