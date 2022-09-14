# CSAW CTF Qualification Round 2020
## Table of Content
- [Reverse Engineering](./)
    - [DockeRELeakage](./)
- [Web application](./)
    - [World Wild Web](./)
    - [My Little Website](./)
    - [Good Intention](./)
- [Cryptography](./)
    - [Gotta Crack Them All](./)

## Reverse Engineering
### DockeRELeakage

1. download the dockeRELeakage.tar.gz
2. load image: `docker load < dockeRELeakage.tar.gz`
3. look for image's histry `docker images history <IMAGE>` (use `--no-trunc` to see all command)

![history](./images/history.png)

4. found base64 --> crack and found the first half of the falg
5. use dive to reverse engineering and find all file on the container

![dive](./images/dive.png)

6. from the history, I found out that flag.txt likely to have the other half of the flag 
7. all file on the docker present on the /var/lib/docker/overlay2 path
8. find flag
```bash
cd /var/lib/docker/overlay2

find . -name <Keyword>

cat ./c4c2b1111710c840107313a395b2716bb193f4335d173f87984ed7ed8c2fc1c8/diff/chal/flag.txt
```
![flag](./images/find_docker_file.png)

## Web application
### World Wild Web

1. we went to the challenge and find the web page as shown in figure below.

![first](./images/first.png)

2. we clicked the stuff and found the page below.

![stuff](./images/stuff.png)

3. then I disabled css and went thought all links on each webpages and found the flag.

![disable](./images/disable_css.png)

4. You could use the less brute-force appoach by using command `wget -r -l inf http://web.chal.csaw.io:5010/` or write some python script to run thought all links.

