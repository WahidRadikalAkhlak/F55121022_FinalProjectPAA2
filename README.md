Analysis Algoritma
1. Bubble Sort & Insertion Sort
   Worst Case:
        Bubble Sort: Worst case terjadi ketika elemen-elemen dalam list tidak terurut dan harus dipindahkan secara bertahap ke posisi yang benar. Dalam hal ini, setiap elemen harus membandingkan dengan setiap elemen lainnya dalam iterasi, sehingga menghasilkan jumlah langkah yang tinggi. Untuk list dengan n elemen, jumlah langkah yang diperlukan adalah sekitar n * (n - 1) / 2.
        Insertion Sort: Worst case terjadi ketika elemen-elemen dalam list terurut secara terbalik. Dalam hal ini, setiap elemen harus dipindahkan ke posisi yang benar dengan membandingkannya dengan setiap elemen sebelumnya. Jumlah langkah yang diperlukan adalah sekitar n * (n - 1) / 2, sama seperti bubble sort.
    Best Case:
        Bubble Sort: Best case terjadi ketika list yang diberikan sudah terurut secara membesar. Dalam hal ini, algoritma akan memeriksa bahwa tidak ada pertukaran yang dilakukan, sehingga hanya memerlukan n - 1 langkah untuk memeriksa elemen-elemen. Ini menghasilkan jumlah langkah yang optimal.
        Insertion Sort: Best case terjadi ketika list yang diberikan sudah terurut secara membesar. Dalam hal ini, algoritma hanya perlu memeriksa bahwa tidak ada pemindahan elemen yang diperlukan, sehingga hanya memerlukan n - 1 langkah untuk memeriksa elemen-elemen. Ini juga menghasilkan jumlah langkah yang optimal.
    Average Case:
        Bubble Sort: Average case dalam bubble sort bergantung pada distribusi elemen-elemen dalam list. Secara umum, rata-rata kasus memerlukan sekitar n * (n - 1) / 4 langkah. Namun, bubble sort cenderung lebih lambat dibandingkan dengan algoritma pengurutan lainnya, terutama untuk list yang besar.
        Insertion Sort: Average case dalam insertion sort juga bergantung pada distribusi elemen-elemen dalam list. Secara umum, rata-rata kasus memerlukan sekitar n * (n - 1) / 4 langkah. Insertion sort cenderung lebih cepat dibandingkan dengan bubble sort untuk list yang hampir terurut, tetapi masih memiliki kompleksitas waktu yang tinggi untuk list yang tidak terurut dengan baik.

2. TSP & Djikstra
   Worst Case:
    Algoritma TSP: Dalam algoritma TSP yang digunakan, semua kemungkinan permutasi vertex diuji. Oleh karena itu, jumlah total permutasi yang dihasilkan oleh fungsi itertools.permutations adalah N!, di mana N adalah jumlah vertex dalam graf. Dalam kasus terburuk, algoritma ini harus memeriksa semua permutasi tersebut sebelum menemukan jalur terpendek. Jadi, waktu eksekusi dalam worst case adalah O(N!).
    Algoritma Dijkstra: Dalam algoritma Dijkstra, waktu eksekusi bergantung pada jumlah vertex dan edge dalam graf. Dalam kasus terburuk, ketika semua vertex terhubung satu sama lain, algoritma Dijkstra akan memeriksa semua edge dan vertex sebelum mencapai tujuan. Jadi, waktu eksekusi dalam worst case adalah O(V^2), di mana V adalah jumlah vertex dalam graf.
  Best Case:
    Algoritma TSP: Dalam kasus terbaik, jika jalur terpendek ditemukan pada permutasi pertama yang diperiksa, maka waktu eksekusi adalah konstan. Namun, ini sangat jarang terjadi dan tidak dapat diandalkan dalam praktiknya.
    Algoritma Dijkstra: Dalam kasus terbaik, jika vertex awal adalah vertex tujuan, maka waktu eksekusi adalah konstan, yaitu O(1). Ini terjadi ketika tidak ada perluasan pencarian yang perlu dilakukan.
  Average Case:
    Algoritma TSP: Rata-rata kasus ini sulit untuk ditentukan secara pasti, karena melibatkan perhitungan kompleksitas kombinatorial. Namun, secara umum, waktu eksekusi rata-rata algoritma TSP akan sebanding dengan jumlah vertex dalam graf.
    Algoritma Dijkstra: Dalam kasus rata-rata, algoritma Dijkstra memiliki kompleksitas waktu yang lebih baik daripada worst case, tetapi masih sebanding dengan jumlah vertex dan edge dalam graf. Sebagai aturan praktis, kompleksitas rata-rata algoritma Dijkstra adalah O(V^2), di mana V adalah jumlah vertex dalam graf.
