var socket = io.connect('http://79.124.19.242:8081');

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