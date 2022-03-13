from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime, inverse
from random import getrandbits
import owiener

password = b'password: U3u1lC1hVFLcmQhG'
nbits = 128


def RSA():
    p = int(getPrime(1024))
    q = int(getPrime(1024))
    n = int(p*q)
    phi = int((p-1)*(q-1))
    while True:
        d = int(getPrime(256))
        e = int(inverse(d, phi))
        if e.bit_length() == n.bit_length():
            break
    return n, e, p, q

n, e, p, q = RSA()
c = pow(bytes_to_long(password), e, n)

d = owiener.attack(e, n)

if d is None:
    exit("Failed")

m = pow(c, d, n)

print(long_to_bytes(m))
print(f"n: {n}")
print(f"e: {e}")
print(f"c: {c}")

#n: 25638625885319775965134362575286609665018069876127243141708859563947963506345166000913089539562695408270410537668353164005233052027768210097686073362167298102004921337988369769077943434611654323487631150202171950159041619523201223538635533954006798623676749912382552105532616294540415184166845180342406513231216843960096817132541606787502046463462998420193608208742068530407161665115049317807336433182358850212846045523555740305614515717256157320605225958989195148384827415694919028591028785902238803734527551825108527126474021519415361543504983859110014753294061708531006442296624870723745950476187413041953853799567
#e: 17256810588695599111470182447677557898705177769995297959937780439801976956014227155888547938549879608386503631864465827875010024167091534429401139635502450437619449843986450480739351279372639471516633554619913078968926267806671802782622514997768288685720474487096449642409362724816298930139671366087621687321524727929282122833059682164881625350621252994467137761677731594656792649883523309355002194233164134211211849819622506696387581857506339672595602429295184165770215980087815530856075134691963824793237334185094098645481554938043999365202550960066236681846687069087421484310386085854329653659710717217020879154447
#c: 23576840977636837062476096013917453976212574428676925267390057344522693058641318651919981732808344144451726785132238623390735570347503865501128268996774276055138361725389337013172076517947366549102767573131996421730655667358772907454589453951707773168273816777245167397985816797548342549238480936098306952223425750079637643836563758720657290017901271507347805047918276389516777304011340400265914913367459877478513392772595363611962731215873703047230075925791505139200437933230191758890679737105663798025511413498083166838293303146617526581144898345379293348543866073601449271405995489434762215203021179014217097354626