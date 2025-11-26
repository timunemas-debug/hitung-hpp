class Iventory:
    """
    Class untuk menghitung hpp.
    """
    def __init__(self, persediaan_awal, pembelian_bersih, persediaan_akhir):
        self.persediaan_awal = persediaan_awal
        self.pembelian_bersih = pembelian_bersih
        self.persediaan_akhir = persediaan_akhir
    def hitung_hpp(self):
        return self.persediaan_awal + self.pembelian_bersih - self.persediaan_akhir

class Transaksi:
    """
    Class untuk menyimpan total penjualan.
    """
    def __init__(self, total_penjualan):
        self.total_penjualan = total_penjualan

class HitungHpp:
    """
    Class untuk menghitung laba untung / laba rugi berdasarkan hpp dan penjualan.
    """
    def __init__(self, iventory: Iventory, transaksi: Transaksi):
        self.iventory = iventory
        self.transaksi = transaksi

    def laba_rugi(self):
        hpp = self.iventory.hitung_hpp()
        return self.transaksi.total_penjualan - hpp
    
if __name__ == "__main__":
    persediaan_awal = int(input("Masukan jumlah persediaan awal anda: "))
    pembelian_bersih = int(input("Masukan jumlah pembelian bersih anda: "))
    persediaan_akhir = int(input("Masukan jumlah persediaan akhir anda: "))
    total_penjualan = int(input("Masukan total penjualan anda: "))

    ivn = Iventory(persediaan_awal, pembelian_bersih, persediaan_akhir)
    trx = Transaksi(total_penjualan)

    hitung = HitungHpp(ivn, trx)

    print("HPP:", hitung.iventory.hitung_hpp())
    print("Laba/Rugi:",hitung.laba_rugi())
