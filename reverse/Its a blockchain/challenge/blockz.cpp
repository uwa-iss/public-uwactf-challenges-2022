#include <iostream>
#include <string>

int header() {
    std::cout << ".----------------.  .----------------.  .----------------.  .----------------.  .-----------------. .----------------.  .----------------. " << std::endl;
    std::cout << "| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |" << std::endl;
    std::cout << "| |   _____      | || |     _____    | || |     ______   | || |  _________   | || | ____  _____  | || |     ______   | || |  _________   | |" << std::endl;
    std::cout << "| |  |_   _|     | || |    |_   _|   | || |   .' ___  |  | || | |_   ___  |  | || ||_   \\|_   _| | || |   .' ___  |  | || | |_   ___  |  | |" << std::endl;
    std::cout << "| |    | |       | || |      | |     | || |  / .'   \\_|  | || |   | |_  \\_|  | || |  |   \\ | |   | || |  / .'   \\_|  | || |   | |_  \\_|  | |" << std::endl;
    std::cout << "| |    | |   _   | || |      | |     | || |  | |         | || |   |  _|  _   | || |  | |\\ \\| |   | || |  | |         | || |   |  _|  _   | |" << std::endl;
    std::cout << "| |   _| |__/ |  | || |     _| |_    | || |  \\ `.___.'\\  | || |  _| |___/ |  | || | _| |_\\   |_  | || |  \\ `.___.'\\  | || |  _| |___/ |  | |" << std::endl;
    std::cout << "| |  |________|  | || |    |_____|   | || |   `._____.'  | || | |_________|  | || ||_____|\\____| | || |   `._____.'  | || | |_________|  | |" << std::endl;
    std::cout << "| |              | || |              | || |              | || |              | || |              | || |              | || |              | |" << std::endl;
    std::cout << "| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |" << std::endl;
    std::cout << "'----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' " << std::endl;
    std::cout << "                    .----------------.  .----------------.  .----------------.  .----------------.  .----------------. " << std::endl;
    std::cout << "                    | .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |" << std::endl;
    std::cout << "                    | |     ______   | || |  ____  ____  | || |  _________   | || |     ______   | || |  ___  ____   | |" << std::endl;
    std::cout << "                    | |   .' ___  |  | || | |_   ||   _| | || | |_   ___  |  | || |   .' ___  |  | || | |_  ||_  _|  | |" << std::endl;
    std::cout << "                    | |  / .'   \\_|  | || |   | |__| |   | || |   | |_  \\_|  | || |  / .'   \\_|  | || |   | |_/ /    | |" << std::endl;
    std::cout << "                    | |  | |         | || |   |  __  |   | || |   |  _|  _   | || |  | |         | || |   |  __'.    | |" << std::endl;
    std::cout << "                    | |  \\ `.___.'\\  | || |  _| |  | |_  | || |  _| |___/ |  | || |  \\ `.___.'\\  | || |  _| |  \\ \\_  | |" << std::endl;
    std::cout << "                    | |   `._____.'  | || | |____||____| | || | |_________|  | || |   `._____.'  | || | |____||____| | |" << std::endl;
    std::cout << "                    | |              | || |              | || |              | || |              | || |              | |" << std::endl;
    std::cout << "                    | '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |" << std::endl;
    std::cout << "                    '----------------'  '----------------'  '----------------'  '----------------'  '----------------' " << std::endl;
}

std::string pad(std::string uin, long blocksize) {
    int inlen = uin.length();
    int padno = blocksize - (inlen % blocksize);
    std::string out = uin+std::string(padno, '0')+std::string(blocksize, '0');
    return out;
}

int main(void) {
    header();
    std::string instr;
    std::string uin;
    long blocksize, iv, prev = 0;
    long licence[] = {7393415227443049, 8077192723678156, 4101310444290190, 8090446768978805, 4118192954888783, 2719978387027670, 3869257800022688, 12514449250651222, 13720115820361887, 14458697086363679, 14458697086363679};
    int pass = 1;

    std::cout << "Enter your licence key: ";
    std::cin >> instr;
    for (int i = 0; i < instr.length(); i++) uin += std::to_string(int(instr[i]));
    if (uin.length() < 8) std::cout << "Key is to short ¯\\_( ͡° ͜ʖ ͡°)_/¯" << std::endl;
    else if (uin.length() < 32) {
        blocksize = 4;
        uin = pad(uin, blocksize);
        iv = 1956;
    } else if (uin.length() < 128) {
        blocksize = 8;
        uin = pad(uin, blocksize);
        iv = 4145700;
    } else if (uin.length() < 256) {
        blocksize = 16;
        uin = pad(uin, blocksize);
        iv = 140512244688361;
    }    else if (uin.length() < 1024) {
        blocksize = 32;
        uin = pad(uin, blocksize);
        iv = 19194614834450229370447026415081;
    }
    std::string blocks [(uin.length()/blocksize)];
    for (int i = 0; i < (uin.length()/blocksize); i++) blocks[i] = uin.substr(i * blocksize, blocksize);
    long out [(uin.length()/blocksize)];
    std::string::size_type sz;
    for (int i = 0; i < (uin.length()/blocksize); i++) {
        if (prev == 0) {
            prev = iv^std::stol(blocks[i], &sz);
            out[i] = prev;
        } else {
            prev = prev^std::stol(blocks[i], &sz);
            out[i] = prev;
        }
    }
    for (int i = 0; i < (uin.length()/blocksize); i++) if (out[i] != licence[i]) pass = 0;
    if (pass) std::cout << "Licence Approved!!!" << std::endl << "You can now use your legitimately aqquired" << std::endl << "copy of the RoboBradan quote generator :)" << std::endl << "block chaining is the same as blockchain... right?" << std::endl;
    else std::cout << "No piracy allowed! Buy a licence!" << std::endl;
}