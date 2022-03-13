# Challenge

**Name:** Turtles

**Category:** Crypto

**Difficulty:** Hard

**Author:** q3st1on

**Flag:** `ISS{1ts_RSA_4ll_th3_w4y_d0wn}`

**Provided Files:** [crypto-turtles.zip](publish/crypto-turtles.zip) 

## Description
```
If encrypting once is good, then encrypting twice is better.
Your frustration will pass, because RSA is forever!
```
We decided to encrypt our story behind 5 layers of RSA.
No one is getting through our crypto now! Infact, we 
are so confident about our security we will give you
some resources to help :)

[SageMath](https://www.sagemath.org/)

[Twenty Years of Attacks on the RSA Cryptosystem](https://crypto.stanford.edu/~dabo/pubs/papers/RSA-survey.pdf)

(Note: to decrypt files run `gpg -o file --decrypt file.gpg`)

## Solution

### Lvl 1: Small primes
This level doesnt use an attack per say, rather its is exploiting
the fact that in this level` n` is prime. 
#### The Attack
RSA works because of the fact that <img src="http://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;ed\equiv&space;1&space;(mod\text{&space;}\phi&space;(n))" title="http://latex.codecogs.com/png.latex?\inline \dpi{110} ed\equiv 1 (mod\text{ }\phi (n))" />, so that
<img src="http://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;(m^e)^d\equiv&space;m&space;(mod&space;\text{&space;}n)" title="http://latex.codecogs.com/png.latex?\inline \dpi{110} (m^e)^d\equiv m (mod \text{ }n)" />. If <img src="https://render.githubusercontent.com/render/math?math=n"> is prime, then <img src="https://render.githubusercontent.com/render/math?math=\phi (n)=n-1"> so we can
easily compute <img src="https://render.githubusercontent.com/render/math?math=d">.

This is implemented in sage bellow
```python
n = 7612897926387454493341430837467857279730676296553431537405133241990350630072291775121226563164319034893479777163804734430079422292949165270056591769307673
e = 65537
c = 6735329377161533753045510067010928595289070183811762224631644533356638863259468753329942896694117248719244432246176344503968411657701661762113752718311014

phi = n-1

d = inverse(e, phi)

m = long_to_bytes(pow(c, d, n)).decode()

print(m)
```

### Lvl 2: Common Modulus Attack
[This section is from the [Cryptohack Cryptobook page](https://cryptohack.gitbook.io/cryptobook/untitled/common-modulus-attack)]

Imagine Allice sends the same message to bob more than
once using a different public key, but the same private key.
This is the scenario we find our self in for the 2nd level of this
challenge. In such a scenario, a common modulus attack can
be used to recover the plaintext (`m`) of the message without 
knowing the private key given we have the following:
 - `e1` is the first public key
 - `e2` is the second public key
 - `c1` is the first ciphertext
 - `c2` is the second ciphertext
 - `n`  the modulus common to both ciphertexts

The following conditions must also be met to allow us to calculate
the inverses required for this attack.
<img src="https://render.githubusercontent.com/render/math?math=gcd(e_1,e_2)=1">
<img src="https://render.githubusercontent.com/render/math?math=gcd(c_2,n)=1">
#### Maths Behind the attack
We know that rsa goes as follows:
<img src="https://render.githubusercontent.com/render/math?math=c=m^e\space mod\space n">
From the conditions above we know that <img src="https://render.githubusercontent.com/render/math?math=e_1"> and <img src="https://render.githubusercontent.com/render/math?math=e_2"> are coprime. 
Thus using Bezout's Theorem we can get:
<img src="https://render.githubusercontent.com/render/math?math=xe_{1}"> + <img src="https://render.githubusercontent.com/render/math?math=ye_{2}=gcd(e_1,e_2)=1">
Using this , we can derive the original message <img src="https://render.githubusercontent.com/render/math?math=m">:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;\begin{align*}C^x_1&space;\times&space;C^y_2&space;&\equiv&space;(m^{e_1})^x&space;\times&space;(m^{e_2})^y&space;\text{&space;}(&space;mod&space;\text{&space;}&space;n)\\&\equiv&space;m^{e_1&space;x&space;&plus;&space;e_2&space;y}&space;\text{&space;}(&space;mod&space;\text{&space;}&space;n)\\&\equiv&space;m^1&space;\text{&space;}(&space;mod&space;\text{&space;}&space;n)\\&\equiv&space;m&space;\text{&space;}(&space;mod&space;\text{&space;}&space;n)\end{align*}" title="http://latex.codecogs.com/png.latex?\dpi{110} \begin{align*}C^x_1 \times C^y_2 &\equiv (m^{e_1})^x \times (m^{e_2})^y \text{ }( mod \text{ } n)\\&\equiv m^{e_1 x + e_2 y} \text{ }( mod \text{ } n)\\&\equiv m^1 \text{ }( mod \text{ } n)\\&\equiv m \text{ }( mod \text{ } n)\end{align*}" />

In general, Bezout's Theorem gives a pair of positive and negative
numbers.  We just need to adapt this equation a little to make it
work for us. In this case, let's assume <img src="https://render.githubusercontent.com/render/math?math=y"> is the negative number:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;\begin{align*}Let&space;\text{&space;}y&=-a\\C^y_2&=C^{-a}_2\\&=(C^{-1}_2)^a\\&=(C^{-1}_2)^{-y}\end{align*}" title="http://latex.codecogs.com/png.latex?\dpi{110} \begin{align*}Let \text{ }y&=-a\\C^y_2&=C^{-a}_2\\&=(C^{-1}_2)^a\\&=(C^{-1}_2)^{-y}\end{align*}" />

Now to truly recover the plaintext, we are actually doing:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;C^x_1&space;\times&space;(C^{-1}_2)^{-y}&space;\text{&space;}&space;mod&space;\text{&space;}n&space;=&space;m" title="http://latex.codecogs.com/png.latex?\dpi{110} C^x_1 \times (C^{-1}_2)^{-y} \text{ } mod \text{ }n = m" />

This attack implemented in SageMath code is shown bellow:
```python
n = 27390742047211866210026944369743887414566458029516514425033626306774494689864174495801555272383190583160082989655863312205047053183692830244256178957626107376560379967207985126156190858536517205268949994460850754539444809410585157088177071636502330471866361668190182789076443134992817065067251833360182098260126782731885535313311335548973261364561399048355594884908144981171535890330075378020662433636919739225721250388595210241180516033224412865027892600445056035076813797868459879508284740398056781703117842217915374745944665788538529937708042475610187926079841899148576087451377023173071901473591091933937339958843
e1 = 223
e2 = 179
c1 = 26340747778274532766654862748934907641190238831811510416009409348800652359726766791764494117241998650220107492130551055000787536016073648842930661114117853728852033281438609968901796733493973916793475324249548236759154306078379633384886324645602605919981445076258410042190761801406183116358063628177474671044832335760453353873545921040502393107138826827934173828094473127840644522350331873044252353800612552493014143210237904066669883473056610510105777414940005672845193809024250242037882266795778313266209653971406373124342755351866738190064905242404359384377276182001226959012983433085848632602613634696841430256175
c2 = 22519899019163493297221998432752837612694554920681179747605507328287724627960960551384407172088512007451332408885600804890721939370945699733500438976316571609893007875322045832763871141110338906136148425452606887793726153592740012191386168144802034521554966114121888428565319696414617652880234413434888643068344029509749340173265319294969396207282433666543481682857610827618104948921088864616059004881776628539686343477394364143247139128538886076500284836802659205518831799351233904797123120460045480070210088914254770267568405332367121863450478149756863459522399462894899667321110126638386593999683207083396822904703

assert gcd(e1, e2) == 1
assert gcd(c2, n) == 1

x = inverse(e1, e2)
y = (gcd(e1, e2)-e1*x) // e2

temp = inverse(c2, n)

m1 = pow(c1, x, n)
m2 = pow(temp, -y, n)

pt = (m1 * m2) % n

print(long_to_bytes(int(pt)).decode())
```


### lvl 3: Small public exponent
In this level the public exponent (`e`) used is so small that
that ciphertext (`c`) to the power of the public exponent is
smaller than the modulus (`n`):

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;C^e&space;%3C&space;n" title="http://latex.codecogs.com/png.latex?\dpi{110}%20C%5Ee%20%3C%20n" />

this means that the plaintext (`m`) is simply the `e`th 
root of `c` as shown bellow:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;m=\sqrt[e]{c}" title="http://latex.codecogs.com/png.latex?\dpi{110} m=\sqrt[e]{c}" />

Sage code to solve this level shown bellow:
```python
n = 429272348506533423061298506843311422890654431293209941815257350809952454925687209144914412008423605801547009857478099940293024254030120399475743610147821834053600245267463391660289543373645233764610287703860512881518675117273000991170049112692572937109940810437046575663648820732785022618241346986919472626098353940913271081367815091968852126898478862158945570112864445574135104904440373267548424756577351721919007606195646897407900491546480142362538392792167118776607053898641012520060112731914201847429157610882702744186205058919979104384726888861560830711978664898926390553519692869639523152804097992586550735868653253658323216808298455207154341169899081727665188368852407180228642184807348612697577562259351632150800278144695923625732462381691672384728011909616140671495643746805358790888359812931918289053100957424194705741476532486770229590714753588202941615237355763592236238305571085538458253785232118012377084516920059823964490966257074871916944319101456873960008292044139291429157494700926530773889508552032458617164187448640653762915875046825157652548497776548247761947334813252241313853342090469332943999201841600633308739858876319398985598765239947405389720912411778557765727569190077799390963468095042038413471394170779
e = 19
c = 7535708508535600828689737825679727572912929250423280472405392824596219626552190652036251131199448768697481309008030829759531585319043635401505342258560211699487953918733370304959044209432155969600716988883392964611632676060540491460321947655804410767957289396605059848126550283620860062275584452179405797362011643716408910515900336947308830056894874421944819174426107795373924044310864538001663383552488166560015325997093629383787806199805290632599989182599665857824680873154070014685282926577102537702511944806849948370251523064522385239907432090613460069894321420188625059177168121304796601704809881832734623965931285945198411385585774496844632591545159855498066452909241105181018326622622274011690803239326816445287127246084792259646274625318027207046501240677105221234534535418728038963384696588240743111178902077422943351983055091087108794743761363500696972394280937181622496780410622411990209602979186830418790637940123764151278142859107975001006519495420273684746460257772191683421620442532309072598041487521508765502134242280798025187846902973182088643220670736958271740562864588615368706331719983120236163343593263978539555166414649621684701880379665500087516474264789240333

print(long_to_bytes(Integer(c).nth_root(Integer(e))).decode())
```


### Lvl 4: Weiner Attack
[This section is from the [Cryptohack Cryptobook page](https://cryptohack.gitbook.io/cryptobook/untitled/low-private-component-attacks/wieners-attack)]

Wiener's attack is an attack on RSA that uses continued fractions to find
the private exponent <img src="https://render.githubusercontent.com/render/math?math=d"> when it's small (less than <img src="https://render.githubusercontent.com/render/math?math=\frac{1}{3}\sqrt[4]{n}">, where  is the modulus).
We know that when we pick the public exponent <img src="https://render.githubusercontent.com/render/math?math=e"> to be a small number
and calcute its inverse.

#### Weiners Theorem:
Wiener's attack is based on the following theorem:
Let <img src="https://render.githubusercontent.com/render/math?math=n=pq">, with <img src="https://render.githubusercontent.com/render/math?math=q %3C p %3C 2q">. Let <img src="https://render.githubusercontent.com/render/math?math=d %3C \frac{1}{3}\sqrt[4]{n}">. Given <img src="https://render.githubusercontent.com/render/math?math=n"> and <img src="https://render.githubusercontent.com/render/math?math=e"> with <img src="https://render.githubusercontent.com/render/math?math=ed = 1\text{ } mod\text{ } \phi (n)">,
the attacker can efficiently recover <img src="https://render.githubusercontent.com/render/math?math=d">

### The Attack
Suppose we have the public key <img src="https://render.githubusercontent.com/render/math?math=(n,e)">, this attack will determine <img src="https://render.githubusercontent.com/render/math?math=d">
1. Convert the fraction <img src="https://render.githubusercontent.com/render/math?math=\frac{e}{n}"> into a continued fraction <img src="http://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;\[a_0&space;;&space;a_1&space;,...&space;,&space;a_k&space;\]" title="http://latex.codecogs.com/png.latex?\inline \dpi{110} \[a_0 ; a_1 ,... , a_k \]" />
2. Iterate over each convergent in the continued fraction:

	<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;\frac{a_0}{1},a_0&plus;\frac{1}{a_1},a_0&plus;\frac{1}{a_1&plus;\frac{1}{a_2}},...,a_0&plus;\frac{1}{a_1&plus;\frac{^.._.}{a_{k-2}&plus;\frac{1}{a_{k-1}}}}," title="http://latex.codecogs.com/png.latex?\dpi{110} \frac{a_0}{1},a_0+\frac{1}{a_1},a_0+\frac{1}{a_1+\frac{1}{a_2}},...,a_0+\frac{1}{a_1+\frac{^.._.}{a_{k-2}+\frac{1}{a_{k-1}}}}," />
3. Check if the convergent is <img src="https://render.githubusercontent.com/render/math?math=\frac{k}{d}"> by doing the following:
	1. Set the numerator to be <img src="https://render.githubusercontent.com/render/math?math=k"> and the denominator to be <img src="https://render.githubusercontent.com/render/math?math=d">
	2. Check if <img src="https://render.githubusercontent.com/render/math?math=d"> is odd, if not, move on to the next convergent
	3. Check if <img src="https://render.githubusercontent.com/render/math?math=ed \equiv 1 \text{ }mod \text{ } k">, if not, move on to the next convergent
	4. Set <img src="https://render.githubusercontent.com/render/math?math=\phi (n) = \frac{ed-1}{k}"> and find the roots of the polynomial <img src="http://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;x^2-(n-&space;\phi&space;(n)&space;&plus;&space;1)x&space;&plus;&space;n" title="http://latex.codecogs.com/png.latex?\inline \dpi{110} x^2-(n- \phi (n) + 1)x + n" />
	5. If the roots of the polynomial are integers, then we've found <img src="https://render.githubusercontent.com/render/math?math=d">
4. If all convergents have been tried, and none of them work, then the given parameters are not vunerable 

Sage code using this attack to solve lvl 4 shown bellow:
```python
def wiener(n, e):
    """Wiener's attack"""
    n = Integer(n)
    e = Integer(e)
    for f in (e / n).continued_fraction().convergents()[1:]:
        k, d = f.numerator(), f.denominator()
        phi = ((e * d) - 1) / k
        b = -(n - phi + 1)
        dis_sqrt = sqrt(b * b - 4 * n)
        if dis_sqrt.is_integer():
            p = (-b + dis_sqrt) / 2
            q = (-b - dis_sqrt) / 2
            if p < q:
                p, q = q, p
            return (d)

n = 24099095231841740381400590209946532012777586196140747852881794356701209318390096870215877987075261287705771846871655691305082951325277933367577754737809022056950968411825744826856173366221947398162892707628101711509724841434855084014317083692416229331590488628362252707900507565575357825093137229231510422977096804020706676319955448436508559816459424188040699153833030816328807181442313686724854260663971657142025037447939432972686970227439692496138635367283573071982319109698515950069479643818080253015110225515310848235889189051635125929354306015448137582895113579389396427948479618453179863989312618525100346694807
e = 21411373092325257154670070706583215437718698968192728006261271183219160300987798019696486532582850769474663616851282956759773041437755999018329716976972616316767693785040128357989175421881591929340811026984377095130161180932333588246577313020463679272934137317515638812115524684990951109555813209924153468245348946047635758032377807489100078377791208039175536394491204242926598220225780114218277670640608977213542661586439602940402037279269386781963717215502166948103975480005375302318133536513313058964452822067771609909374115669570883249412804918987820907294659235977206567671128608180417481694081670513241313280489
c = 6213108015116372908208911439114751427923187141108124658522770468820840130143170877097207781183814751574055359724921858364828951528535493103323100551334798326743914165258522526599262578310614223679280506688383816027432944393632591209875970480306473625802227743123969882272838474634089740420085036332217543305214455280078425162410069265632840041399148992909042070510070939731881259585709084383516574352644431506982463247009171344545584701308414151786569144442344113936246157175621263501300953409686401144543062337030925209557112228837261937544179181261644555453017859418642817033436703507107107347821769940825733373316

d = wiener(n, e)

if d is None:
    exit("Failed")

 m = pow(c, d, n)
print(long_to_bytes(int(m)).decode())
```
### Lvl5: Franklin-Reiter Related Message Attack (+ Unintended Solution)
Lets say that Bob sends a message (`m`) to Alice encrypted
using the public key `e` and modulus `n`. Alice, having NBN
internet, fails to recieve this message, so Bob resends the
message with a new padding (`r`). In this scenario, the
plaintext `m` can be recovered by anyone who knows the
padding `r`. This is the exact situation we find in the last level
of this challenge.

#### The Attack
[This section is from [this cryptography stack exchange response](https://crypto.stackexchange.com/a/30890)]

We have 2 ciphertexts <img src="https://render.githubusercontent.com/render/math?math=C_1"> and <img src="https://render.githubusercontent.com/render/math?math=C_2"> with a difference <img src="https://render.githubusercontent.com/render/math?math=r"> where:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;\begin{align*}C_1&space;&\equiv&space;m^e&space;\text{&space;}mod&space;\text{&space;}n\\C_2%26space;%26\equiv&space;(m&plus;r)^e&space;\text{&space;}mod&space;\text{&space;}n\end{align*}" title="http://latex.codecogs.com/png.latex?\dpi{110} \begin{align*}C_1 %26\equiv m^e \text{ }mod \text{ }n\\C_2 %26\equiv (m+r)^e \text{ }mod \text{ }n\end{align*}" />

To find <img src="https://render.githubusercontent.com/render/math?math=m">, we must determine:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;gcd(m^e-C_1,(m&plus;r)^e-C_2)" title="http://latex.codecogs.com/png.latex?\dpi{110} gcd(m^e-C_1,(m+r)^e-C_2)" />

After you compute the gcd of the two polynomials you are left
with a polynomial in the form <img src="https://render.githubusercontent.com/render/math?math=X-m">. If:

<img src="http://latex.codecogs.com/png.latex?\dpi{110}&space;\begin{align*}f_1(X)%26=X^e-C_1\\f_2(X)%26=(X&plus;r)^e-C_2\end{align*}" title="http://latex.codecogs.com/png.latex?\dpi{110} \begin{align*}f_1(X)%26=X^e-C_1\\f_2(X)%26=(X+r)^e-C_2\end{align*}" />

have a common root <img src="https://render.githubusercontent.com/render/math?math=m">, then they are of the form <img src="http://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;(X-m)_{g_1}" title="http://latex.codecogs.com/png.latex?\inline \dpi{110} (X-m)_{g_1}" /> and
<img src="http://latex.codecogs.com/png.latex?\inline&space;\dpi{110}&space;(X-m)_{g_2}" title="http://latex.codecogs.com/png.latex?\inline \dpi{110} (X-m)_{g_2}" /> for some arbitrary <img src="https://render.githubusercontent.com/render/math?math=g_1"> and <img src="https://render.githubusercontent.com/render/math?math=g_2">.

Therefore, <img src="https://render.githubusercontent.com/render/math?math=-m"> is the coefficient degree 0 of this common polynomial,
and all that is left to do is extract it.

#### Challenge specifics
For this challenge you dont actually know the difference `r`. However,
a quick reading of the supplied encryption code will tell you that `r` is
a `nbits//(2**7)` bit prime. Given `nbits = 1024`, this tells us that `r` is
an 8 bit prime. 8 bit numbers are between 128 and 255 inclusive. Knowing
this, we can get a list of all the possible values of `r` which is 23 values long.
Given that the computational cost of the Franklin-Reiter attack with `e=3`
is negligable, we can quickly itterate through the possible values of `r` till
we find one that gets us the flag. 

Sage code using this attack to solve lvl 5 shown bellow:
```python
def franklinReiter(n,e,r,c1,c2):
    R.<X> = Zmod(n)[]
    f1 = X^e - c1
    f2 = (X + r)^e - c2
    return Integer(n-(compositeModulusGCD(f1,f2)).coefficients()[0])

def compositeModulusGCD(a, b):
    if(b == 0):
        return a.monic()
    else:
        return compositeModulusGCD(b, a % b)
   
n = 12486223006451013109624622993040038468017944450847242059042600590778771337099229041526439223653365051206369362439076454494705357137428397976689220597119341383834670154238730529513544332737364111809143085650887075389031689066746513309152147670664780381050456872152808174301121733902464207752663343132231212712326245981907275579294311307169030103828573302513774247084021031200550171954434162884645515923090323356442137578629367125406843584740522866129782532939967331435729181702580886180117569118009763357389911955877695060168178063426703125155913124752754045546966207035324873051786059479327044141833747481294867120651
e = 3
c1 = 5889415905357775311780618068204885540404136240189344463554559502670856588635019654289374293853268571082587823207049697706924088786315963049154564064137212322757152477388081823148541559104
c2 = 5889415905357775311780618068204885540404136240189344463554577211151979900678763713504241356533969244055268504815466239919166406436658596998140541196122059004410448829719215695849219149625
primes = [131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251]

for i in primes:
    try:
        out = long_to_bytes(franklinReiter(n, e, i, c1, c2)).decode()
        if out.startswith("password:"):
            print(out)
    except:
        print("",end="")
```
#### Unintended Solution
I accidentaly left this level vunerable to the exact same attack as in level 3 had, this was not at all intentional and should have been picked up prior to the challenge being used in the ctf. However, as it wasnt, finding the cube root of `c1` was an unintended solution to this level. The level could be solved with the following sage code:
```python
n = 12486223006451013109624622993040038468017944450847242059042600590778771337099229041526439223653365051206369362439076454494705357137428397976689220597119341383834670154238730529513544332737364111809143085650887075389031689066746513309152147670664780381050456872152808174301121733902464207752663343132231212712326245981907275579294311307169030103828573302513774247084021031200550171954434162884645515923090323356442137578629367125406843584740522866129782532939967331435729181702580886180117569118009763357389911955877695060168178063426703125155913124752754045546966207035324873051786059479327044141833747481294867120651
e = 3
c1 = 5889415905357775311780618068204885540404136240189344463554559502670856588635019654289374293853268571082587823207049697706924088786315963049154564064137212322757152477388081823148541559104
c2 = 5889415905357775311780618068204885540404136240189344463554577211151979900678763713504241356533969244055268504815466239919166406436658596998140541196122059004410448829719215695849219149625
print(long_to_bytes(Integer(c1).nth_root(Integer(e))).decode())
```
All levels are in the  [solve script](solution/solve.sage).
