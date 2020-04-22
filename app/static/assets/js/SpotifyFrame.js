
function setSong(URI) {
    var urlName = "https://open.spotify.com/embed/track/" + URI
    document.getElementById("player").src = urlName
}