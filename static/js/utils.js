var greetings = ["cloud Phone Shop",
    "best phone shop",
    "our cloud phone shop",
    "our best phone shop",
];
var greeting_id = Math.floor(Math.random() * greetings.length);
document.getElementById('textme').textContent = greetings[greeting_id];

setInterval(function() {
    var greeting_id = Math.floor(Math.random() * greetings.length);
    document.getElementById('textme').textContent = greetings[greeting_id];
}, 3000);