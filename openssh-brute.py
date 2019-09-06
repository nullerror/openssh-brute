import subprocess
import sys
import time, datetime

if len(sys.argv) < 2:

    sys.exit("Find password to OpenSSH private key using ssh-keygen\nUsage: %s <OpenSSHKey> <wordlist>" % sys.argv[0])

def cmdline(command):
    proc = subprocess.Popen(str(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (out, err) = proc.communicate()
    return err

def main():
    words = [line.strip() for line in open(sys.argv[2])]
    print("\n")
    count=0
    start_time = time.time()
    print("Started at {}").format(datetime.datetime.now())
    print("Wordist froom {} has {} words...").format(sys.argv[2],len(words))
    for w in words:
        strcmd = "ssh-keygen -e -m 'pem' -f" + sys.argv[1] + " -P " + w + " > /dev/null"
        #print(strcmd)
        res=cmdline(strcmd)
        #print(res)
        if not res:
            end_time = time.time()
            hours, rem = divmod(end_time - start_time, 3600)
            minutes, seconds = divmod(rem, 60)
            print("\nKey Found in {} hours {} minutes {} seconds!\n-------> {}").format(int(hours),int(minutes),seconds, w)
            sys.exit()
        print("Try #: "  +str(count) +": " + str(w))
        count += 1
    print("\n")

if __name__ == '__main__':
    main()
