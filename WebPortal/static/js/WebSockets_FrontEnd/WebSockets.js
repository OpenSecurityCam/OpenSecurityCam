var socket = io.connect('http://localhost');

socket.on('connect', function() {
    socket.send('Connected to Server');
});

function ArmToggleButton()
{
    socket.emit('Toggle_Arm');
}

socket.on('ArmSystem', function() {
    document.getElementById('Arm_Toggle_Button').innerHTML = "Unarm System";
});

socket.on('UnarmSystem', function() {
    document.getElementById('Arm_Toggle_Button').innerHTML = "Arm System";
});