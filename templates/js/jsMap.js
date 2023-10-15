// Initialize and add the map
function initMap() {

    //Posizione di Napoli
    const naples = { lat: 40.8518, lng: 14.2681 };

    //La mappa deve essere centrata a napoli
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 14,
        center: naples,
    });

    // Il marker su Napoli
    const marker = new google.maps.Marker({
        position: naples,
        map: map,
        content: "Dove siamo",
    });

    //I miei parcheggi
    //Vado a inserire le cordinate dei miei parcheggi e le dichiaro costanti:
    const sign = {lat: 40.836633, lng: 14.250964}; //Via Toledo:
    //Aggiungo i marker:
    const marker1 = new google.maps.Marker({
        position: sign,
        map: map,
    });

    //Per la descrizione del Marker (ogni parcheggio)
    const infowindow1 = new google.maps.InfoWindow({
        content: "GigaBarber,\nVia Roma n.57,\n80142 Napoli NA\n" +
            "Italia",
    });

    marker1.addListener("click", () => {
        infowindow1.open(map, marker1);
    });



}

window.initMap = initMap;
