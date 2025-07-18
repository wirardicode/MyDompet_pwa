const token = 'Z3T4WA1FUKU' // Token 
        function thisTunai() {
            const apiUrl = 'http://127.0.0.1:8000/geting-total'

            fetch(apiUrl, {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token
                }
            })
                .then(res => {
                    if (!res.ok) throw new Error("HTTP error " + res.status)
                    return res.json()
                })
                .then(data => {
                    console.log("Data fetched:", data)
                    if (data.status === 200) {
                        const [row] = data.data
                        const totalMasuk = row[0]
                        const totalKeluar = row[1]

                        const formatIDR = n => (n || 0).toLocaleString('id-ID')

                        document.getElementById('totalMasuk').innerHTML = `: <q>${formatIDR(totalMasuk)}</q>`
                        document.getElementById('totalKeluar').innerHTML = `: <q>${formatIDR(totalKeluar)}</q>`
                        document.getElementById('status').textContent = "Data berhasil dimuat"
                        document.getElementById('status').classList.remove("text-blue-600")
                        document.getElementById('status').classList.add("text-green-600")
                    } else {
                        throw new Error("Status data bukan 200")
                    }
                })
                .catch(err => {
                    console.error("Fetch error:", err)
                    document.getElementById('status').textContent = "Gagal memuat data"
                    document.getElementById('status').classList.remove("text-blue-600")
                    document.getElementById('status').classList.add("text-red-600")
                })
        }

        function getDebit() {
            const apiUrl = 'http://127.0.0.1:8000/get-debit'

            fetch(apiUrl, {
                method: 'GET',
                headers: {
                    'Authorization': 'Bearer ' + token
                }
            })
                .then(res => {
                    if (!res.ok) throw new Error("HTTP error " + res.status)
                    return res.json()
                })
                .then(data => {
                    if (data.status === 200) {
                        const formatIDR = n => (n || 0).toLocaleString('id-ID')
                        document.getElementById('totalDebit').innerHTML = `: <q>${formatIDR(data.message)}</q>`
                        document.getElementById('statusDebit').textContent = "Data debit berhasil dimuat"
                        document.getElementById('statusDebit').classList.replace("text-blue-600", "text-green-600")
                    } else {
                        throw new Error("Status bukan 200")
                    }
                })
                .catch(err => {
                    console.error("Fetch error:", err)
                    document.getElementById('statusDebit').textContent = "Gagal memuat data debit"
                    document.getElementById('statusDebit').classList.replace("text-blue-600", "text-red-600")
                })
        }

        thisTunai()
        getDebit()