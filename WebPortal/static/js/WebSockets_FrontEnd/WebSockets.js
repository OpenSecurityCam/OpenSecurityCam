$(document).ready(function() {
    var socket = io.connect('http://localhost:80');

    socket.on('connect', function() {
        socket.send('Connected to Server');
    });

    $('#Arm_Toggle_Button').on('click', function() {
        socket.emit('Toggle_Arm');
    });

    socket.on('ArmSystem', function() {
        document.getElementById('Arm_Toggle_Button').innerHTML = "Unarm System";
    });

    socket.on('UnarmSystem', function() {
        document.getElementById('Arm_Toggle_Button').innerHTML = "Arm System";
    });
});