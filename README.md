# Wahid Radikal Akhlak
# F55121022
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
   a. Worst Case:
      TSP (Traveling Salesman Problem):
      Pada worst case, algoritma TSP memerlukan pengecekan semua kemungkinan permutasi jalur yang mungkin.
      Jumlah simpul pada grafik digambarkan sebagai "n".
      Oleh karena itu, jumlah permutasi yang mungkin adalah (n-1)!.
      Dalam kasus ini, waktu eksekusi algoritma akan meningkat secara eksponensial dengan meningkatnya jumlah simpul.
      Jadi, dalam worst case, kompleksitas waktu algoritma TSP adalah O((n-1)!).
      Dijkstra:
      Pada worst case, Dijkstra memeriksa setiap simpul dan setiap sisi dalam grafik.
      Jika kita memiliki "V" simpul dan "E" sisi, maka kompleksitas waktu Dijkstra adalah O((V+E)log(V)) saat menggunakan heap biner sebagai antrian prioritas.
      Jadi, dalam worst case, kompleksitas waktu algoritma Dijkstra adalah O((V+E)log(V)).
b. Best Case:
      TSP (Traveling Salesman Problem):
      Dalam kasus terbaik, algoritma TSP memiliki grafik dengan sedikit simpul.
      Jika kita hanya memiliki 2 simpul (misalnya A dan B), maka jalur terpendek adalah langsung dari A ke B.
      Dalam kasus ini, waktu eksekusi algoritma TSP akan sangat singkat.
      Jadi, dalam best case, kompleksitas waktu algoritma TSP adalah O(1).
      Dijkstra:
      Dalam kasus terbaik, algoritma Dijkstra memiliki grafik dengan simpul awal dan simpul tujuan yang berdekatan.
      Jika kita hanya memiliki 2 simpul yang terhubung langsung (misalnya A dan B), maka jalur terpendek adalah langsung dari A ke B.
      Dalam kasus ini, waktu eksekusi algoritma Dijkstra akan sangat singkat.
      Jadi, dalam best case, kompleksitas waktu algoritma Dijkstra adalah O(1).
c. Average Case:
      TSP (Traveling Salesman Problem):
      Rata-rata kasus TSP sangat tergantung pada struktur grafik dan jumlah simpul.
      Dalam rata-rata kasus, algoritma TSP menggunakan pendekatan heuristik seperti Nearest Neighbor, Dynamic Programming, atau Optimal Substructure untuk mencari solusi           yang memadai.
      Jika jumlah simpul "n" tidak terlalu besar, algoritma TSP dapat memberikan solusi yang cukup efisien dalam waktu yang masuk akal.
      Kompleksitas waktu rata-rata algoritma TSP sangat bervariasi tergantung pada metode heuristik yang digunakan.
      Dijkstra:
      Dalam rata-rata kasus, algoritma Dijkstra memiliki kompleksitas waktu yang efisien.
      Namun, kompleksitas waktu rata-rata masih tergantung pada jumlah simpul dan sisi dalam grafik.
      Jika jumlah simpul dan sisi tidak terlalu besar, algoritma Dijkstra akan memberikan solusi dalam waktu yang masuk akal.
      Kompleksitas waktu rata-rata algoritma Dijkstra adalah O((V+E)log(V)), di mana V adalah jumlah simpul dan E adalah jumlah sisi dalam grafik.
