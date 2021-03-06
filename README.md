<h1 align="center">Brahma</h1>
<p align="center"><img src="https://github.com/DevanshRaghav75/Brahma/blob/main/img/Brahma_logo.png">

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![GitHub license](https://img.shields.io/github/license/DevanshRaghav75/Brahma.svg)](https://github.com/DevanshRaghav75/Brahma/blob/master/LICENSE.md)

## What is Brahma?

`Brahma` is a python program that automates the proccess of `xss, sqli, ssrf, nosqli and lfi` with the help of other amazing tools.

## Why Brahma?

Using tools one by one while huntings bugs may be boring so `Brahma` is the solution, `Brahma` automates your favorite tools and saves your time.

## Automates what?

* <a href="https://github.com/tomnomnom/gf">gf by @tomnomnom</a>
* <a href="https://github.com/projectdiscovery/httpx">httpx by @projectdiscovery.io</a>
* <a href="https://github.com/hahwul/dalfox">dalfox by @hahwul</a>
* <a href="https://sqlmap.org/">Sqlmap by @sqlmapproject</a>
* <a href="https://github.com/ffuf/ffuf">ffuf by @ffuf</a>
* <a href="https://github.com/projectdiscovery/subfinder">subfinder by @projectdiscovery.io</a>
* <a href="https://github.com/tomnomnom/waybackurls">waybackurls by @tomnomnom</a>
* <a href="https://github.com/tomnomnom/qsreplace">qsreplace by @tomnomnom</a>
* <a href="https://github.com/1ndianl33t/Gf-Patterns">Gf_Patterns by @1ndianl33t</a>
* <a href="https://github.com/Charlie-belmer/nosqli">Nosqli by @Charlie-belmer</a>

**Thanks to developers for these incredible tools**

## Installation

```
$ git clone https://github.com/DevanshRaghav75/Brahma
$ cd Brahma
$ python3 setup.py install  
$ Brahma -h
```
## Usage and Args
**Args**
  
| Args        |   Discription                        |
|-------------|--------------------------------------|
|-a/--automate| Specify what you want to automate    |
|-d/--domain  | Specify the domain you want to test  |
|-s/--silent  | Skip banner                          |

**Automation arguments**

| Argument   |   Discription                         |
|------------|---------------------------------------|
|-a xss      | Will automate XSS                     |
|-a sqli     | Will automate SQL injection           |
|-a lfi      | Will automate LFI                     |
|-a ssrf     | Will automate SSRF                    |
|-a nosqli   | Will automate NoSQL injection         |
|-a all      | Will automate xss,sqli,lfi,ssrf,nosqli|
