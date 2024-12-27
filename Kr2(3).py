# «Динамо» — «Зенит»: 2:2
# «Динамо» — «Зенит»: 2:1
# «Спартак» — «Крылья Света»: 3:1
# «Спартак» — «Динамо»: 2:1
# «Крылья Света» — «Зенит»: 1:1
# «Крылья Света» — «Зенит»: 1:0
# Спартак, Динамо, Крылья Света, Зенит

class socer:
    name = None
    vk = None
    nk = None
    pk = None
    gol = None
    prg = None

    def soc_komand(self, name, vk, nk, pk, gol, prg):
        self.name = name
        self.vk = vk
        self.nk = nk
        self.pk = pk
        self.gol = gol
        self.prg = prg

mest_1 = []
mest_2 = []
mest_3 = []
mest_4 = []

d = socer()
d.soc_komand("Динамо", 1, 1, 1, 5, 5)
sumd = d.vk + d.nk - d.pk
noti = [d.name, ":", sumd]
print(noti)

z = socer()
z.soc_komand("Зенит", 0, 2, 2, 4, 6)
sumz = z.vk + z.nk - z.pk

s = socer()
s.soc_komand("Спартак", 2, 0, 0, 5, 2)
sums = s.vk + s.nk - s.pk

k = socer()
k.soc_komand("Крылья Света", 1, 1, 1, 3, 4)
sumk = k.vk + k.nk - k.pk

obsum = [ sumz, sumk, sums, sumd]
obsum.sort(reverse=True)
print(obsum)
