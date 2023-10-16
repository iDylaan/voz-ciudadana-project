if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition, showError);
} else {
    alert("Geolocalización no es soportada por este navegador.");
}

const reportes = [
    {
        "reporte": "bache",
        "lat": 19.383305,
        "lng": -98.980079,
    },
    {
        "reporte": "iluminacion",
        "lat": 19.381538,
        "lng": -98.978338,
    },
]

const customStyles = [
    {
        featureType: "poi.business",
        elementType: "labels",
        stylers: [{ visibility: "off" }]
    }
];

const showLoader = () => document.querySelector("#map-loader").style.display = "grid";
const hideLoader = () => document.querySelector("#map-loader").style.display = "none";


let map;
let markers = [];

const setLocationMark = (coord, reporte) => {
    const icon = {
        url: `../assets/icon/categoriesIcons/${reporte}.svg`,
        scaledSize: new google.maps.Size(38, 38),
        origin: new google.maps.Point(0, 0),
        anchor: new google.maps.Point(15, 30),
    }
    const marker = new google.maps.Marker({
        position: coord,
        map: map,
        title: reporte,
        icon: icon,
    })
    markers.push(marker);
}

const setReportMarkers = () => {
    reportes.forEach((reporte) => {
        let coord = new google.maps.LatLng(reporte.lat, reporte.lng);
        let reportType = reporte.reporte;
        setLocationMark(coord, reportType);
    })
}

const setFakeReportMarkers = (userCoord) => {
    const numberOfMarkers = 20;
    const markers = [];
    const reportTypes = [
        "bache",
        "iluminacion",
        "basura",
        "coladera",
        "inundacion",
        "mal_olor",
        "obstruccion",
        "poste",
        "semaforo",
        "sin_senial"
    ]

    const maxLatChange = 0.000135 * 15;
    const maxLngChange = 0.000135 * 15;

    reportTypes.forEach((type) => {
        for (let j = 0; j < 2; j++) {
            const deltaLat = (Math.random() - 0.5) * 2 * maxLatChange;
            const deltaLng = (Math.random() - 0.5) * 2 * maxLngChange;

            const newLat = userCoord.lat + deltaLat;
            const newLng = userCoord.lng + deltaLng;
            reportes.push({ lat: newLat, lng: newLng, reporte: type })
        }
    })
    return markers;
}

async function initMap() {
    showLoader();
    const { Map } = await google.maps.importLibrary("maps");
    const centerCoord = { lat: 19.382161, lng: -98.9797574 }
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function (position) {
            centerCoord.lat = position.coords.latitude;
            centerCoord.lng = position.coords.longitude;

            map.setCenter(centerCoord);
            new google.maps.Marker({
                position: { lat: centerCoord.lat, lng: centerCoord.lng },
                map: map,
                title: 'Tu ubicación',
                // icon: {
                //     url: "../imgs/icons/marker.svg",
                //     scaledSize: new google.maps.Size(40, 40),
                //     origin: new google.maps.Point(0, 0),
                //     anchor: new google.maps.Point(15, 30),
                // }
            });

            setFakeReportMarkers(centerCoord);
            setReportMarkers();
            hideLoader();
        }, showError);
    } else {
        alert("Geolocalización no es soportada por este navegador.");
    }

    map = new Map(document.getElementById("map"), {
        center: centerCoord,
        zoom: 17,
        styles: customStyles,
        streetViewControl: false,
        mapTypeControl: false
    });
}

initMap();


function showError(error) {
    switch (error.code) {
        case error.PERMISSION_DENIED:
            alert("El usuario denegó el pedido de geolocalización.");
            break;
        case error.POSITION_UNAVAILABLE:
            alert("Información de la ubicación no disponible.");
            break;
        case error.TIMEOUT:
            alert("El pedido para obtener la ubicación del usuario expiró.");
            break;
        case error.UNKNOWN_ERROR:
            alert("Ocurrió un error desconocido.");
            break;
    }
}


function showPosition(position) {
    const userLocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
    };

    map.setCenter(userLocation);

    new google.maps.Marker({
        position: userLocation,
        map: map,
        title: 'Tu ubicación'
    });
}