const fereastra_afisare = document.querySelector('#fereastra-chat1');
const ButonAfisareChat = document.querySelector('.buton-chat');

ButonAfisareChat.addEventListener('click', () => {
    fereastra_afisare.classList.toggle('show');
})


function raspuns_bot() {
    var prelucrareText = $("#mesaj_utilizator").val();
    var rezultatText = '<p class="mesajutilizator"><span>' + prelucrareText + "</span></p>";
    $("#mesaj_utilizator").val("");
    $("#chatbox").append(rezultatText);
    document
        .getElementById("text-user")
        .scrollIntoView({ block: "start", behavior: "smooth" });
    $.get("/raspuns", { obtine_mesaj: prelucrareText }).done(function (data) {
        var botRaspuns = '<p class="botText"><span>' + data + "</span></p>";
        $("#chatbox").append(botRaspuns);
        document
            .getElementById("text-user")
            .scrollIntoView({ block: "start", behavior: "smooth" });
    });
}
$("#mesaj_utilizator").keypress(function (e) {
    if (e.which == 13) {
        raspuns_bot();
    }
});
$('#buton-trimitere').click(function () {
    raspuns_bot();
});