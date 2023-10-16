const reportesArray = []

async function getReports() {
    try {
        const response = await fetch(
            'http://localhost:5000/reportes',
            {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                },
            },
        );
        const data = await response.json();
        console.log(data);
    } catch (error) {
        alert(error);
        console.log(error);
    }
}

getReports();