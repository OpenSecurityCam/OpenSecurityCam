var socket = io.connect('http://localhost:5000');

socket.on('connect', function() {
    socket.send('Connected to Server');
});

function ArmToggleButton()
{
    socket.emit('Toggle_Arm');
}

socket.on('ArmSystem', () => {
    document.getElementById('Arm_Toggle_Button').innerHTML = "Unarm System";
});

socket.on('UnarmSystem', () => {
    document.getElementById('Arm_Toggle_Button').innerHTML = "Arm System";
});