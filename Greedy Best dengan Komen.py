#Nama Anggota Kelompok :
    #Wardatul Amalia Safitri - 5025211006
    #Melanie Sayyidina Sabrina Refman - 5025211029
    #Yusna Millaturrosyidah - 5025211254

#Set jarak yang berisi list kota-kota yang saling terhubung
jarak = {
    'Magetan': ['Ngawi', 'Madiun', 'Ponorogo'],
    'Ngawi': ['Bojonegoro', 'Madiun'],
    'Madiun': ['Ponorogo', 'Nganjuk'],
    'Bojonegoro': ['Jombang', 'Lamongan', 'Nganjuk'],
    'Nganjuk': ['Jombang'],
    'Lamongan': ['Gresik'],
    'Jombang': ['Surabaya'], 
    'Gresik': ['Surabaya'],
    'Surabaya': ['Sidoarjo', 'Bangkalan'],
    'Sidoarjo': ['Probolinggo'],
    'Bangkalan': ['Sampang'],
    'Probolinggo': ['Situbondo'],
    'Sampang': ['Pamekasan'],
    'Pamekasan': ['Sumenep'],
}


class peta:
    #Inisiasi sesuai set jarak yang sudah ditentukan
    def __init__(kotakab, jarak):
        kotakab.jarak = jarak
    
    #Fungsi untuk memanggil kota-kota yang terhubung
    def cabang(kotakab, val):
        return kotakab.jarak[val]
    
    #Fungsi heuristik dari setiap kota terhadap Surabaya
    def heur(kotakab, val):
        heuristik = {
            'Magetan': 162,
            'Surabaya': 0,
            'Ngawi': 130,
            'Ponorogo': 128, 
            'Madiun': 126,
            'Bojonegoro': 60,
            'Nganjuk': 70, 
            'Jombang': 36, 
            'Lamongan': 36,
            'Gresik': 12, 
            'Sidoarjo': 22,
            'Probolinggo': 70,
            'Situbondo': 146,
            'Bangkalan': 140,
            'Sampang': 90,
            'Pamekasan': 104,
            'Sumenep': 150 
        }
        return heuristik[val]
    
    #Fungsi untuk melakukan searching dengan metode greedy best
    def greedy_best(kotakab, start, finish):
        #Set untuk menyimpan kota yang diexpand. Dimulai dari kota yang menjadi titik start
        rute = set([start])
        #Set untuk menyimpan kota yang dilalui
        past = set([]) 
        parrent = {}
        parrent[start] = start #Inisialisasi parent start dengan dirinya sendiri
        
        while len(rute) > 0:
            #Inisialisasi variabel k sebelum menyimpan kota yang dipilih
            k = None
            
            #Memilih kota mana yang akan dipilih dari kota-kota yang diexpand
            for i in rute:
                #Perbandingannya menggunakan fungsi heuristik tiap kota
                if k == None or kotakab.heur(i) < kotakab.heur(k):
                    k = i;
                    
            #Jika tidak ada kota yang bisa dipilih    
            if k == None:
                print('Rute tidak tersedia')
                return None
            
            #jika k sama dengan kota tujuan
            if k == finish:
                #Membuat list untuk menyimpan final rute
                final_rute = []
                
                #Menabahkan kota yang sudah dilalui ke final rute dengan urutan terbalik
                while parrent[k] != k:
                    final_rute.append(k) 
                    k = parrent[k]
                
                #Menambahkan kota titik awal ke final rute
                final_rute.append(start)
                
                #Membalik urutan kota di final rute agar menjadi urutan yang baik
                final_rute.reverse()
                print('Rute Greedy Best First Search: {}'.format(final_rute))
                return final_rute
            
            #Menentukan kota yang akan diexpand selanjutnya
            for j in kotakab.cabang(k):
                if j not in rute and j not in past:
                    rute.add(j)
                    parrent[j] = k #Inisialisasi parent kota yang diexpand selanjutnya dengan kota yang dipilih
                    
            #Menghapus kota yang dilalui dari kota yang diexpand agar tidak dipilih kembali
            rute.remove(k)
            #Menambahkan kota yang sudah dilalui ke set past
            past.add(k)
        
        #Jika tidak ada rute yang memenuhi
        print('Rute tidak tesedia')
        return None

#Membuat gambaran graph sesuai isi set jarak
graph = peta(jarak)
#Memulai pencarian rute terbaik dari Magetan ke Surabaya dengan metode greedy best
graph.greedy_best('Magetan', 'Surabaya')


